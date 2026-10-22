# Nightly single-project maintenance cron

Use this pattern when the user asks for an autonomous nightly job to keep one important local project improving over time.

## Prompt shape

Make the cron prompt self-contained because future runs start in a fresh session. Include:

- exact project workdir and any separate state/database paths
- project purpose and architecture constraints
- data-protection rules for databases, RAG folders, secrets, auth tokens, backups, and user files
- “one useful verified improvement per run” scope limit
- required discovery: git status, recent commits, package scripts, README/CLAUDE/AGENTS docs, open issues/PRs if relevant
- rule to avoid overwriting uncommitted user changes
- verification expectations: build/test/lint/smoke, screenshot for UI changes when possible
- commit/push policy and fallback if push is unavailable
- final report fields: target chosen, files changed, commands run, verification result, commit/push status, next target
- explicit invariant: do not create/update/remove cron jobs recursively

## Good recurring target selection

Pick exactly one coherent slice each night:

1. failing build/test/lint or obvious runtime bug
2. small reliability/security hardening
3. minimal regression/smoke test coverage for an important path
4. UI polish only when it can be verified with screenshots
5. docs/runbook update only if no safe code change is available

Avoid broad rewrites, speculative architecture changes, fake metrics, or unverified “improvements.”

## Workdir and delivery

- Set `workdir` to the project root so project context files load automatically.
- Use `attach_to_session=true` when the user may reply to nightly reports.
- Use targeted toolsets such as `terminal`, `file`, `session_search`, `web`, and `delegation`; avoid loading every tool by default.
- Use a finite but long repeat count if the user says “always” but does not specify an end date; this prevents immortal forgotten jobs while still satisfying the request.

## Safety notes

- If the project has a separate data directory/database, name it explicitly and mark it protected.
- If local uncommitted changes exist, either avoid those files or report blocked; do not clean/reset them.
- Commit only verified changes. If verification fails, leave no half-finished commit and report the blocker.
