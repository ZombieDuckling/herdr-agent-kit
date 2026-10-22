# Fabled Five Release Sprint Pattern

Use this when the user asks to "spin up Fabled Five" / "full send" a multi-repo or portfolio cleanup using Claude Code.

## Durable lessons

- Pin the requested model explicitly in every worker command. If the user says Fable 5, use `claude ... --model claude-fable-5`; do not rely on Claude Code defaults.
- Smoke-test Claude Code availability before launching. If print mode reports a session limit/reset time, queue a delayed launcher rather than repeatedly retrying.
- For delayed launches, write a reviewed shell script, run `bash -n`, and start it with a tracked Hermes background process using `notify_on_complete=true`.
- If a queued launcher must be changed, kill the old background process before re-arming the new one. Report the new process id/session id and explain that killed-process notifications for the old launcher are expected cleanup noise.
- For org/repo rename work, do not launch workers against URLs that do not exist yet. Add a preflight loop that waits for `gh api orgs/<new-slug>` to succeed, then rewrites local remotes before starting workers.
- Keep local audit/workspace folder names stable even if the public org slug changes; tell workers that old local path segments may be historical only.

## Worker split that worked well

1. Backend/security: backend docs/security cleanup + Go compile/CI baseline.
2. Mobile: Android JDK/tooling/release flags + SwiftUI build/debug placeholder pass.
3. Frontend/product UX: README, build/typecheck, placeholder route triage, Playwright smoke.
4. Docs/ops/vendor hygiene: ops docs, documents/notes status, vendor fork notes.
5. Release manager/QA: final ship/no-ship matrix and read-only verification.

## Guardrails

Allow workers to create branches, edit files, run tests, commit, and push PR branches. Forbid merging default branches, deleting large/vendor trees, exposing secrets, and claiming ship-ready without concrete verification output.

## Completion artifact

Require each worker to write a report under the audit workspace plus a final matrix with:

```text
Repo:
Status: Ship / Conditional Ship / No Ship / Archive / Vendor Mirror
Branch:
PR:
Build command:
Test command:
Security scan:
Docs status:
Known blockers:
Next owner action:
```
