# Adversarial PR merge gate pattern

Use when the user asks for an external coding agent to decide whether a PR may merge, especially after a large corpus, binary/LFS, licensing, CI, or safety-sensitive change.

## Pattern

1. Treat the external agent's verdict as binding.
   - If it returns `DO_NOT_MERGE`, do not merge even if local checks are green.
   - Fix every blocker it lists, push, wait for CI, then rerun the adversarial gate.
   - Only merge after a later review explicitly returns `HAPPY_TO_MERGE` with no blockers.

2. Make the review prompt self-contained and adversarial.
   - Include PR number, repo, current head SHA, base branch, and prior review blockers/fixes.
   - Ask the agent to actively find reasons not to merge.
   - Require a structured verdict with headings: `VERDICT`, `BLOCKERS`, `NON_BLOCKING_ISSUES`, `EVIDENCE_CHECKED`, `REQUIRED_FIXES_IF_ANY`.
   - State: any blocker means `DO_NOT_MERGE`; only `HAPPY_TO_MERGE` can authorize merge.

3. Do not count incomplete agent runs as approval.
   - `error_max_turns`, tool-denial, or missing verdict is not approval.
   - Rerun with enough turns/permissions for read-only inspection.

4. For large LFS/binary PRs, adversarially verify more than green CI.
   - Confirm files are real local content, not just links or unsmudged pointers.
   - Confirm LFS objects are uploaded and CI can fetch/smudge them when validation requires real bytes.
   - Add validators for manifest ↔ file count, checksums, duplicate content, and policy requirements.

5. For third-party corpora, check legal/source class before merge.
   - Avoid unverified boilerplate like "candidate; verify later" for committed binaries.
   - Remove known risky/non-commercial/share-alike documents unless repo licensing explicitly carves them out.
   - Add a third-party notice file when vendoring documents that are not owned by repository contributors.
   - Make the generator/rebuild path enforce the same exclusions as the committed manifest.

6. Keep PR metadata honest.
   - Update PR body after each substantive rebuild so counts/source spread match the actual manifest.
   - Mark draft PRs ready before final gate.
   - Require all required checks green on the current head.

## Merge rule

Only merge after all of the following are true:

- PR is not draft.
- Current head checks are green.
- Hermes has verified the stated artifacts locally or via CI evidence.
- The adversarial agent's latest complete verdict is `HAPPY_TO_MERGE`.
