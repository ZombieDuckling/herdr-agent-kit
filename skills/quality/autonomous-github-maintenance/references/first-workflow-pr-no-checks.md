# First workflow PR reports no checks

When a repository has no existing GitHub Actions workflow on the default branch and a maintenance PR introduces `.github/workflows/*.yml` for the first time, GitHub may show no PR checks/runs even if:

- Actions are enabled for the repository (`gh api repos/OWNER/REPO/actions/permissions`).
- The workflow includes `pull_request`.
- The workflow also includes `push` for the maintenance branch.
- The branch was pushed after the workflow file was added.

This is not a local verification failure. GitHub often does not execute a newly introduced workflow until it exists on the default branch / is trusted by repository policy.

## What to do in a nightly maintainer run

1. Verify locally with the exact commands the workflow will run.
2. Check repo Actions permissions and existing runs:
   ```bash
   gh api repos/OWNER/REPO/actions/permissions
   gh run list --repo OWNER/REPO --limit 5 --json databaseId,headBranch,displayTitle,status,conclusion,url
   gh pr checks PR_NUMBER --repo OWNER/REPO || true
   ```
3. If no checks are reported, do **not** claim CI is green.
4. Leave a PR comment stating:
   - local verification commands and real output summary,
   - Actions permissions status if checked,
   - that no GitHub checks/runs were reported because the PR introduces the first workflow.
5. Report this as a GitHub Actions bootstrap caveat, not a blocker to opening the PR.

## Avoid

- Do not keep pushing harmless trigger-only commits in a loop trying to force a run.
- Do not merge automatically just to seed the workflow.
- Do not fabricate a GitHub Actions result from local verification.
