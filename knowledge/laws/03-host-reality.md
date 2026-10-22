# 03 · the box is not what the documentation says it is

Vendor docs describe the machine the vendor tested on. On anything ARM64, recent,
or shared, the gap between documented and actual is where the week goes.

---

## HOST-1: architecture mismatch is the default failure, not the exception

**Law.** On ARM64, assume every artifact is x86-64 until proven otherwise, and
check before installing, not after.

Four separate instances of one root cause:

- A vendor's `.deb` download page advertised x64 only and its "linux" URL 404'd
  for arm64. An **ARM64 AppImage existed** at a URL the public page never linked.
  The build was there; the documentation was not.
- A CUDA build script hardcoded a GPU architecture flag for an older consumer
  card. The installed GPU was a newer compute capability entirely, so the binary
  built happily and then refused to run. Building against the *detected*
  architecture rather than a pinned one fixed it.
- The upstream `make` all-target referenced sources that did not exist. The
  actual working recipe was two compiler invocations inside the build script.
  When a build system is broken, read what it *executes*, not what it *declares*.
- A required container image was published for x86-64 only. Under emulation its
  runtime crash-looped immediately. No native build existed, so that path was
  simply closed — the correct outcome was to stop and say so, not to keep
  fighting the emulator.

Order of operations: `uname -m`, then check the vendor's actual artifact list
(not the download page), then confirm the toolchain targets the *installed* GPU.
Note also that CUDA's `nvcc` is frequently not on `PATH` by default.

---

## HOST-2: accelerators fail open to the slow path

**Law.** When a GPU disappears, well-built software does not crash. It gets slow,
which is far harder to diagnose.

An unattended kernel upgrade booted a new kernel. The GPU driver on this
distribution ships as **prebuilt per-kernel modules, not DKMS**, and the modules
metapackage stayed pinned to the *old* kernel. Result: no driver module, no
device nodes, `nvidia-smi` failing — and both model servers silently falling back
to CPU. Generation dropped from ~90 tok/s to ~3.

The reported symptom was **"the agent is down / not responding."** It was never
down. It was ~30× too slow to answer inside a client timeout. Days of agent-layer
debugging pointed at a kernel package.

- When anything GPU-backed gets mysteriously slow, check `nvidia-smi` and the
  loaded kernel module **first**, before touching the application.
- `dkms status` being empty is not evidence of a problem on prebuilt-module
  distributions — it is the design.
- Fix the class, not the instance: upgrade the HWE modules *metapackage* so
  future kernel bumps pull the matching module in the same transaction. Then
  `modprobe`; no reboot needed.
- The general law: any fallback path that is correct-but-slower will eventually
  be mistaken for an outage. Log loudly when you take one.

---

## HOST-3: pkill over SSH can kill the SSH session

**Law.** `pkill -f <pattern>` matches your own remote command line, which
contains that pattern.

Run `ssh host 'pkill -f llama-server'` and the remote shell's own argv contains
the string `llama-server`. `pkill` matches it and kills the session executing it.
You get exit 255, no output, and a redirected logfile that never gets created —
an exact impersonation of a dropped network link. Hit twice in these notes, on
two different processes, because the failure looks like the network and not like
you.

- Use `pkill -x <exact-process-name>` (matches the name, not the full argv), or
  resolve the PID and kill that.
- Corollary for agents: a command that appears to drop your connection may have
  been a suicide. Reconnect and check whether the target actually died before
  concluding anything about the network.

---

## HOST-4: a service whose port is taken may disable itself silently

**Law.** Check port ownership before installing, and verify the daemon is
*enabled* after.

A remote-desktop server was installed onto a host where a container already
published its default port. The daemon quietly disabled itself rather than
failing loudly — clients could then neither discover nor connect, with no error
at either end pointing at the port.

- Before install: `ss -tulpn` for the default port, and remember that container
  port publishing binds on the host and is easy to miss.
- After install: confirm the daemon reports itself enabled *and* is listening on
  the port you think it is. Moving it to a free port is a config change, not a
  fight worth having with the container.

---

## HOST-5: LISTEN does not mean reachable

**Law.** Reachability is a property of the socket **and** the filter in front of
it, including on loopback.

An owner-uid `nftables` rule restricted a loopback model-server port to two
specific uids. A third user on the same host, in the same network namespace, got
`connection refused` in ~0ms — while `ss` plainly showed the port `LISTEN`. Every
instinct says "the service is down." The service was perfectly healthy and
serving the two permitted uids.

- `connection refused` that returns *instantly* on loopback is a filter, not a
  dead process. A dead process also refuses instantly, so confirm with `ss` and
  then check `nft list ruleset` for `meta skuid` / owner matches.
- The sane resolution was a **sanctioned shared entry point**: a transparent
  forwarder on a second port, reachable by everyone, proxying the whole API
  surface including streaming. Do not hand out the restricted port; publish the
  supported one and document which identity uses which.

---

## HOST-6: shared installs must be self-contained

**Law.** A multi-user install cannot depend on any path inside one user's home.

Making a per-user agent available to everyone on a host required copying it to
`/opt` **and** dereferencing its version-managed Python interpreter into the same
tree — because home directories were mode `0750` and unreadable to other users.
A symlink back into the original home would have worked for exactly one user.

- Copy or vendor the interpreter/runtime; repoint the venv (`pyvenv.cfg` home
  plus the `bin/python` link). Verify as a *different* user, not as the owner.
- Seed `/etc/skel` so future accounts inherit the config.
- Deliberately do **not** propagate the original user's `.env` — secrets are
  per-identity. Everyone gets an empty one.
- Backends stay single and shared (one model server on loopback); only the
  clients are per-user.

---

## HOST-7: prove it is hardware before you touch a working config

**Law.** Eliminate configuration as a cause by *comparison*, then stop — do not
reset your way toward a diagnosis.

One device of a pair would not work. Authenticated inspection showed its
configuration was byte-for-byte equivalent to its healthy twin: same endpoint,
same credentials, same algorithm. It had a plausible-looking `active: false`
flag, which was a symptom of not working, not a cause. Both a power cycle and a
software restart failed to bring up its engine; the local control port never
opened. Conclusion: hardware — a seated board or power delivery — not remotely
fixable.

The factory reset was explicitly **not** run. It would have wiped the network
configuration and made the device unreachable, converting a hands-on repair into
a hands-on repair that first requires physically re-provisioning the device.

- A known-good peer is the best diagnostic instrument you have. Diff against it.
- Never take an irreversible action to test a hypothesis you can test reversibly.
- Know which "repair" operations destroy the access path you are using.
