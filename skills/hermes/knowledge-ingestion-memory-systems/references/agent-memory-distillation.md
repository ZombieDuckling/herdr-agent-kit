# Agent-memory distillation protocol

Use this when a private learning pipeline must also update a strict shared memory repository whose entries are sanitized transferable laws.

## What belongs

- A stable invariant another agent can reuse.
- A sanitized incident shape that teaches detection/fix/generalization.
- Measurements, generic technologies, version numbers, public CLI flags, and generic error strings when they teach.

## What does not belong

- Raw transcripts or private notes.
- Human names, handles, repo owners, project/product names, domains, personal paths, phone/email/account identifiers, wallet/transaction identifiers, cloud/tenant/zone IDs, infrastructure details, or credentials.
- Source-specific fan summaries.
- Claims that cannot be stated as one transferable law.

## Safe workflow

1. Clone/update the target repo and read its `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, and relevant `notes/*.md`.
2. Run the repo's setup hook before editing.
3. Pull/rebase before allocating IDs.
4. Compare new source learnings to existing laws; avoid duplicates.
5. Add one law per entry in the correct note file.
6. Add the matching README index row; in these repos, missing index row means missing entry.
7. Re-read the diff as a stranger: if it identifies who, where, or which private project, remove the detail.
8. Run target repo preflight before commit.
9. Commit with a sanitized message.
10. Pull/rebase again, rerun preflight, then push normally. Never force-push.
11. Report entries added, source lessons generalized, and anything left out for safety.

## Converting private source to a law

Bad:

> In the user's app repo, after watching a tutorial video, update the relevant file to add Argus workspace telemetry.

Good:

> A folder is not a product until it has a manifest and a workbench.

Bad:

> The video's author says the agent app should add more personalities.

Good:

> Do not compensate for weak context with more agents.

## Scheduling pattern

For daily updates, use three jobs:

- source ingestion job writes private notes;
- shared-memory distillation job runs later with `context_from` the ingestion job;
- morning briefing job receives both outputs and reports what was added or intentionally omitted.

Keep the shared-memory job conservative: if the latest material is interesting but not yet a stable law, add nothing and say why.
