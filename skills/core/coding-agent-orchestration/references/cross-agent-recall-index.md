# Cross-agent recall index (OpenHarness local daemon)

Use when a question about prior work cannot be answered from Hermes' own session
history, or when several coding-agent CLIs have run on the same host.

The gap: Hermes' `session_search` covers Hermes sessions only. Claude Code, Codex,
OpenCode and Cursor keep their own transcript stores on the machine (hundreds of
files each in a busy environment), and none of them is visible to Hermes.

A locally installed OpenHarness daemon indexes every engine's transcripts on the
host. Verified behaviour, measured on a real machine:

- `harness start` runs unsigned-in: status reports `running · this computer only
  (not signed in)`, and the CLI states that `harness login` is what adds other
  machines. Local search, viewers and the tmux backend work without an account.
- `harness search "<words>" --limit=N` returns dated hits across engines,
  including turns from more than seven months earlier, with a quoted excerpt.
- The daemon appends session/turn hooks to `~/.claude/settings.json` (coexisting
  with pre-existing hooks), listens on loopback (e.g. `127.0.0.1:18473`) and keeps
  state under `~/.harness`.
- Only the cross-machine features need `harness login`; the desktop app ships as a
  binary (a local Flutter/Dart toolchain is needed only to build from source).
- `harness dsh check <dir>` validates a domain-harness package offline against
  spec 1 — useful for reusing craft harnesses (CAD, circuits, print) without
  adopting the whole product.

Reversal: `harness stop` (stop the daemon), `harness reset` (clear local state).

Why this is a recall layer and not a fan-out replacement: fan-out (`delegate_task`,
tmux worker pools) executes work; this layer makes the resulting history findable
across engines. Its genuine advantage over Hermes' own tooling is cross-machine
persistence — the daemon dials out, so no host opens a port, which is the correct
shape when peer machines are behind firewalls.
