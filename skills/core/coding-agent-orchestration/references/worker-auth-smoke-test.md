# Worker auth smoke-test lesson

Session-derived orchestration note for local coding-agent CLIs.

## Lesson

A worker can report as logged in or healthy, but still fail immediately in print mode with an auth error when asked to do real work. Before assigning a real slice, run a tiny one-shot smoke test that exercises the same invocation path you plan to use.

## Practical pattern

1. Check the CLI version and auth state.
2. Run a minimal print-mode or one-shot command that does almost nothing.
3. Confirm the worker returns a successful result, not just a healthy status code.
4. Only then assign the actual task.

## Why this matters

- Prevents fan-out sessions from stalling on a single broken worker.
- Catches credential drift early.
- Gives Hermes a clean fallback path: reroute the task to another worker or complete it directly.

## Example failure mode

- `auth status` looks fine.
- The first real `-p` invocation returns a 401 / invalid authentication error.
- The worker is not reliable for this session even though the status check looked healthy.

## Recommendation

Treat the smoke test as mandatory for any mission-critical fan-out, especially when the task is time-sensitive or the worker is expected to own files.
