# 02 · deadlocks, watchdogs, and the machinery that was supposed to save you

The recurring shape: a system had automatic recovery, the recovery was healthy,
and the outage lasted two days anyway. Self-healing machinery is itself a system
that fails, and it tends to fail quietly, because its whole purpose is to make
noise unnecessary.

---

## LOOP-1: never gate a consumer on state only the consumer can produce

**Law.** If A creates a resource lazily when B asks for it, B's supervisor must
not require the resource to exist before starting B.

A node built its work template on demand — the first time the pool polled for it.
The pool's start gate refused to launch the pool until a template already
existed. So: no pool, therefore no poll, therefore no template, therefore no
pool. A liveness watchdog then bounced the node every ~15 minutes trying to shake
the template loose, which reset everything and guaranteed the next iteration was
identical. Roughly 48 hours of a fully healthy, fully synced node mining nothing.

The fix was one line of intent: **start the consumer once its upstream is ready.**

- Gate on *upstream readiness* (is the node synced and serving?), never on a
  derived signal that is downstream of the thing you are gating.
- Smell test: if the precondition can only become true after the gated action
  runs, it is not a precondition, it is a deadlock with good manners.
- The replacement supervisor deliberately gates on the upstream's own readiness
  endpoint, not on the derived "is work flowing" flag, precisely to avoid
  recreating this.

---

## LOOP-2: automation behind an allowlist fails silently

**Law.** Alarm on "wanted to act, was not permitted." Never let a permission gate
be indistinguishable from nothing being wrong.

Every repair action in the stack was wrapped in a "are mutations permitted?"
predicate, backed by a config allowlist. During an earlier manual recovery an
operator set the mode flag back to normal but left that allowlist **empty**. The
watchdog then ran perfectly, decided to repair 234 consecutive times, and was
denied 234 consecutive times. Its "last repaired at" timestamp was still zero —
it had never once repaired anything in its life. Nothing logged at a level anyone
watched, because from the gate's perspective refusing is normal operation.

- Emit a distinct, loud event for *blocked* actions, separate from both success
  and failure. `repair_blocked_total` is a metric; make it page after N.
- Any "maintenance mode" / "safe mode" flag needs an expiry or a standing
  reminder. Modes entered during an incident outlive the incident.
- Audit question for any recovery system: when did it last actually do something?
  If the answer is "never," it is decoration.

---

## LOOP-3: a restart loop is not a crash loop

**Law.** Read the signal and the period before you debug the process.

A service restarted 70+ times. The instinct is OOM, panic, segfault — go read the
crash. There was no crash. Every termination was a graceful `SIGTERM` arriving on
a near-exact ~16 minute cadence, which is the signature of a *timer*, not a
fault. Something outside the process was killing it on schedule. Debugging the
process would have found nothing, forever.

- `SIGTERM` + suspiciously round period = supervisor, cron, or health-check
  killer. `SIGKILL` from the kernel = OOM. `SIGSEGV`/panic = the process.
- Check `journalctl` for *who* initiated the stop before reading what the process
  said as it died.
- Restart counts are a symptom with at least two very different diseases; the
  distinction is free to make and expensive to skip.

---

## LOOP-4: counters reset, progress watchdogs must survive it

**Law.** A watchdog comparing a live counter to a stored baseline must handle the
counter going backwards.

A supervisor tracked "shares accepted" to decide whether work was progressing,
persisting the last value to a file. The counter lived in a container that resets
it to 0 on every fresh start. So after any legitimate restart, the watchdog read
`0 < last_progress`, concluded the system had stalled, and restarted it — which
reset the counter to 0 again. The stale baseline file had to be deleted by hand
as part of the fix, or the recovery re-entered the loop it was fixing.

- Treat `current < baseline` as **reset**, not as stall. Re-baseline and wait one
  full interval before judging.
- Better: track a monotonic timestamp of last observed work, or pair the counter
  with a process/boot epoch so a reset is detectable rather than inferred.
- This bug is endemic to anything reading Prometheus-style counters across
  restarts; `rate()` exists exactly because of it.

---

## LOOP-5: every self-healing loop needs a circuit breaker

**Law.** Bounded retries, a ledger, and a hard stop that pages a human.

The supervisor that replaced the broken machinery is worth copying wholesale:

- Restart the dependent service only when its **upstream is ready** (LOOP-1).
- **Ledger every restart** with a timestamp, so rate is computable.
- **Trip** on >3 service starts or >5 upstream re-inits in 30 minutes: pause the
  sibling automation timers, write an `ALERT` state file, and *stop*. Do not keep
  trying.
- Never auto-remediate the class of thing that needs hands. Physical devices were
  alert-only — an agent cannot reseat a cable, and pretending otherwise just
  burns the device's power cycles.

The trip condition matters more than the repair logic. An unbounded repair loop
does not fix outages, it converts them into thrash that hides the original cause.

---

## LOOP-6: a timed-out write is ambiguous

**Law.** On timeout you know your request failed to *return*. You know nothing
about whether it was *applied*.

Order placements that timed out may still have landed on the exchange. Blind
retry doubles the position; assuming failure loses track of it. Either guess is
a real, unrecoverable error.

- Re-read authoritative state before deciding what happened. The server knows;
  you do not.
- Prefer idempotency keys / client-supplied IDs so a retry is provably the same
  operation rather than a second one.
- This is at-least-once delivery wearing a disguise, and it applies to every
  non-idempotent POST you have ever written.
