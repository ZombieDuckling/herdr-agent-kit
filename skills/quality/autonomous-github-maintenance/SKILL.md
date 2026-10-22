---
name: autonomous-github-maintenance
description: "Autonomous recurring maintenance of a GitHub portfolio: inventory, rank repos/PRs, make one safe verified improvement, and open PRs without merging."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [GitHub, Maintenance, Portfolio, CI, Dependabot, Cron]
    related_skills: [github-pr-workflow, claude-code]
---

# Autonomous GitHub Maintenance

Use this skill for scheduled or autonomous portfolio-maintenance runs where the goal is to keep many GitHub repos alive with small safe improvements.

## Core policy

- Discover live repo inventory every run; do not rely on stale memory.
- Touch normally **one repo and one coherent slice** per run.
- Never merge to `main` automatically.
- Never force-push, delete branches, expose secrets, or overwrite user changes.
- Before editing, inspect repo state: `git status --short --branch`, branch, remotes, recent commits, open PRs, and CI status.
- Prefer clean temporary clones/worktrees when local repos may contain user work.
- Use Claude Code as the primary coding worker when available, but verify and own the final result yourself.

## Discovery workflow

1. Check GitHub auth and list repos:
   ```bash
   gh repo list "$GH_OWNER" --limit 200 --json nameWithOwner,name,description,isPrivate,isFork,isArchived,primaryLanguage,updatedAt,pushedAt,url,defaultBranchRef
   ```
2. Search open PRs and issues across the owner:
   ```bash
   gh search prs --owner "$GH_OWNER" --state open --json repository,number,title,url,updatedAt,author --limit 50
   gh search issues --owner "$GH_OWNER" --state open --json repository,number,title,url,updatedAt,labels --limit 50
   ```
3. Inspect CI for candidate repos:
   ```bash
   gh pr list --repo OWNER/REPO --state open --json number,title,headRefName,baseRefName,isDraft,updatedAt,url,statusCheckRollup --limit 20
   gh run list --repo OWNER/REPO --limit 10 --json databaseId,headBranch,displayTitle,status,conclusion,createdAt,updatedAt,url
   ```

## Candidate ranking

Prioritize:

1. Open PRs with failing CI or stale failures.
2. Green dependency/CI PRs that need a safe enabling or sequencing step.
3. Recently relevant, non-archived, non-fork repos.
4. Strategic public portfolio projects.
5. Low-risk documentation, CI, test, smoke, or dependency-health improvements.

Do not over-focus on a single flagship repo every run if other repos have active work.

## Dependabot CI hardening pattern

When a Dependabot PR fails due to infrastructure/transient install problems rather than a clear code incompatibility:

1. Inspect the PR and failed logs:
   ```bash
   gh pr view <n> --json number,title,headRefName,baseRefName,url,maintainerCanModify,statusCheckRollup,mergeStateStatus,body
   gh run view <run-id> --log-failed
   ```
2. If `maintainerCanModify` is false or the fix is workflow policy, do **not** edit the Dependabot branch.
3. Create a separate small CI hardening branch from `main`.
4. Avoid duplicating another open green Dependabot PR's exact scope; reference it instead.
5. Verify locally and in GitHub Actions, then report the new PR and next sequencing step.

See `references/dependabot-ci-hardening.md` for a concrete npm retry example.

## Implementation workflow

1. Clone or use a clean worktree.
2. Confirm clean state.
3. Ask Claude Code for a bounded plan grounded in current files.
4. If Claude Code is unavailable due a transient automation/session limit, do **not** abandon the run: proceed directly with a smaller, obviously safe slice, and report the Claude blocker factually.
5. If Claude Code only proposes edits due permission constraints, apply the small change directly with Hermes file tools and keep Claude's plan as advisory.
6. If a bounded Claude/coding-agent run exits with `Reached max turns` and no useful diff, do not keep increasing turns blindly. Inspect `git status`/diff for incidental metadata, remove helper artifacts such as `.omc/`, then execute a smaller obviously-safe slice directly.
7. Run the repo's normal verification. If unknown, infer minimal safe checks: install, syntax/lint, tests, build/smoke.
8. Run `git diff --check` and inspect `git diff --stat`.
9. Commit with a clear conventional message.
10. Push a feature branch and open/update a PR.
11. Watch PR checks when feasible and include real check status in the report.

## Good nightly slices

- For an active PR with no CI coverage, add a minimal workflow plus focused tests that verify the PR's stated safety/product claims. Example pattern for small Python/macOS projects: `macos-latest`, Python matrix, dependency install, `python -m py_compile` on core modules, and `python -m unittest discover -s tests -v`.
- For a Node/Next.js PR with no checks but existing `lint`, `typecheck`, and `build` scripts, restore or add a lightweight GitHub Actions workflow before making feature changes. Prefer `npm ci` + `npm run lint` + `npm run typecheck` + `npm run build`; skip browser-heavy Playwright jobs unless the repo already maintains them reliably. Trigger PR verification on `pull_request` to the base branch; avoid also triggering `push` on the PR head branch unless there is a specific need, because that creates duplicate Actions runs on every PR update. See `references/pr-ci-restoration.md`.
- For small Next.js repos where `npm run lint` still uses deprecated `next lint` and prompts interactively, a high-value CI slice is to migrate lint to a non-interactive ESLint CLI config, add a PR workflow for `npm ci` + lint + build, and document the commands. Match `eslint-config-next` to the repo's Next major/minor instead of pulling the newest major by accident. See `references/nextjs-pr-verification-eslint.md`.
- For small Next.js repos where `next build` needs server-only integration env vars, add PR CI with explicit placeholder env values rather than real secrets, document the local verification command, and clean tracked local agent state such as `.omc/` in the same hygiene slice when present. See `references/nextjs-server-env-ci-and-agent-state.md`.
- After pushing to an existing PR branch, add a concise PR comment summarizing the new commit, local verification, and GitHub Actions run status. This avoids duplicate PRs and leaves reviewer context attached to the live work.
- If a helper/coding agent creates incidental local metadata (for example hidden session folders), remove it before staging and explicitly review `git status --short` so only intended project files are committed.
- For security/recon/agentic-tool projects, a high-value small slice is to enforce existing authorization/scope guardrails at every AI-to-tool dispatch boundary, not only at the interactive CLI entrypoint. Add focused tests that mock subprocess execution and prove out-of-scope public targets are blocked before any command runs while local or explicitly authorized targets still pass.
- For static GitHub Pages / HTML portfolio repos with no existing PR failures, add a tiny no-dependency smoke validator and PR workflow before adding more visual content. Validate every local HTML file has basic metadata (`<html lang>`, viewport, non-empty title), local `href`/`src` targets resolve inside the repo, and index pages still link to required demos. See `references/static-portfolio-smoke-validation.md` for the pattern.
- For static Cloudflare Pages sites whose workflow deploys the whole repository root, stage a public-only `dist/` bundle before deploy so internal docs, dotfiles, obsolete host config, and agent state are not published. Verify current production exposure with status-code checks and smoke-test the staged bundle locally. See `references/static-cloudflare-public-staging.md`.
- For open static-site PRs that add public-only deploy staging but have no PR checks because the deploy workflow only runs on `push` to `main`, update the same PR branch with a `pull_request` trigger, gate the actual deploy step with `if: github.event_name != 'pull_request'`, and add staged-bundle verification for private-file leaks plus broken local HTML refs. See `references/pr-deploy-staging-verification.md`.
- For first-workflow PRs where Actions initially does not report checks, it can be useful to temporarily allow push checks on the maintenance branch to bootstrap visibility. Once PR checks are reporting, narrow the workflow back to `pull_request` plus `push` on the default branch only; do not leave `push` triggers on feature/test branches that cause duplicate check suites for every PR update.
- For tiny hand-written Node static-server repos with no `package.json`, tests, or CI, add a zero-dependency `node:test` smoke suite plus a PR workflow before touching product/UI behavior. Pair it with small static-serving hardening: `PORT` env override for tests, `path.relative(...)` traversal guard, and sanitized `404` handling. See `references/tiny-node-static-server-smoke-ci.md` for the raw encoded-traversal testing pitfall.
- For Electron / desktop app repos that already have local `lint`, `test`, `smoke`, and `build` scripts but no pull-request checks, a high-value small slice is to add a minimal PR GitHub Actions workflow that runs those exact scripts, then document the commands and CI badge in the README. If the local working tree has untracked user planning/screenshots/prompts, use a clean temp clone instead of touching it. See `references/electron-desktop-pr-ci.md` for the pattern.
- For small public Python cybersecurity portfolio repos with no tests or CI, add a pytest characterization suite plus a two-version GitHub Actions workflow before changing detector logic. Cover documented examples, boundary thresholds, one test per signal, and CLI/file-loading edge cases; update the README test command and roadmap. See `references/python-cyber-portfolio-ci.md` for the pattern.

## Cron approval-safe patterns

Scheduled maintainers often run without a user available to approve risky shell shapes. Keep commands approval-safe so the job can finish autonomously.

For single-project nightly jobs (for example a flagship local app rather than the whole GitHub portfolio), use the self-contained prompt pattern in `references/nightly-single-project-maintenance-cron.md`: pin `workdir`, protect state/database paths, require one verified improvement per run, and forbid recursive cron changes.

- Avoid `rm -rf` cleanup in shell when a fresh temp path or a short Python `shutil.rmtree(..., ignore_errors=True)` cleanup is enough.
- Avoid piping live `gh`/network output directly into interpreters (`gh ... | python3 ...`) in cron; use `gh` built-ins such as `gh pr checks --watch`, plain JSON output for inspection, or a separate inspected file if parsing is truly needed.
- If local verification needs pytest or another dev dependency, prefer an external temp venv (`/tmp/<repo>-verify-*`) or remove any repo-local `.venv/` before staging.
- Re-run `git status --short --branch` immediately before staging and again after commit; remove `.omc/`, `.venv/`, and other agent/runtime metadata before `git add`.
- If `git push` succeeds but later `gh` API calls fail due DNS/network (`Could not resolve host: api.github.com`), do not keep retrying indefinitely in cron. Verify the pushed branch locally (`git status --short --branch`, `git rev-parse HEAD`), include the compare/PR-create URL, and report PR creation as a blocker instead of claiming a PR exists.
- If a PR introduces a repository's first GitHub Actions workflow and `gh pr checks` / `gh run list` report no checks, do not fabricate CI status and do not push trigger-only commits in a loop. Verify locally, check Actions permissions, leave a PR comment explaining the bootstrap caveat, and report GitHub checks as "not reported yet." See `references/first-workflow-pr-no-checks.md`.

## Final report format

Include:

- Selected repo and why it was chosen.
- Branch, PR URL, commit SHA.
- What changed.
- Real verification output summary, both local and GitHub Actions if available.
- Skipped/blockers.
- Next recommended repo/slice.

If genuinely nothing changed and there is nothing new to report for a scheduled silent job, return the configured silence token exactly as requested by the job.