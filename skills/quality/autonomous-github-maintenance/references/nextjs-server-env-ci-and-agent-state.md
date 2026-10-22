# Next.js PR CI with server-only env placeholders + agent-state cleanup

Use this pattern for small Next.js repos where builds depend on server-only environment variables and the repo has accumulated local agent runtime state.

## When it applies

- Next.js App Router / TypeScript project.
- No existing PR verification workflow, or PRs rely only on deployment previews.
- `next build` needs server-only env vars for API routes/integrations, but real secrets must not be exposed in CI.
- Tracked local agent/runtime directories exist, especially `.omc/state/*`.

## Safe slice

1. Inspect live repo state first: `git status --short --branch`, remotes, recent commits, open PRs, and recent runs.
2. Create a clean branch from the default branch.
3. Add a PR-only workflow that runs the repo's existing local verification commands, usually:
   - `npm ci`
   - `npm run lint`
   - `npm run build`
4. For server-only env vars required only to compile/build, set explicit placeholder values in the workflow step, e.g.:
   ```yaml
   env:
     APPS_SCRIPT_URL: https://script.google.com/macros/s/example/exec
     APPS_SCRIPT_SECRET: ci-placeholder-secret
   run: npm run build
   ```
   Do not use real secrets unless the project already has GitHub Actions secrets configured and the PR trust model is understood.
5. Document the exact local verification commands in the README so the CI contract is reproducible.
6. If `.omc/` or similar agent state is tracked, remove tracked files with `git rm -r .omc`, add `.omc/` to `.gitignore`, and verify only intended deletions are staged.
7. Run local verification plus `git diff --check`; inspect `git diff --stat` before committing.
8. Push a feature branch and open a PR; watch checks until the new workflow and any deployment previews finish.

## Pitfalls

- Do not stage ignored deletions by re-adding the ignored path after adding it to `.gitignore`; once `git rm` has staged deletions, just review `git diff --cached --name-status` and commit.
- If lint initially passes with warnings, consider cleaning obvious unused imports/dead locals as part of the same CI slice so future CI output is actually signal.
- `npm audit` findings from `npm ci` are worth reporting, but do not fold dependency upgrades into a CI-hygiene PR unless the fix is clearly safe and verified.
- In unattended cron, avoid broad shell constructs likely to trip approvals when a simpler direct command works. For example, query individual PRs with `gh pr view` rather than piping GitHub JSON into interpreters inside a large loop.
