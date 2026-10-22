# Electron desktop PR CI restoration pattern

Use this during autonomous GitHub maintenance when a small Electron or Vite desktop app has useful local verification scripts but no pull-request GitHub Actions coverage.

## When to use

- Repo is active/recently relevant and has no higher-priority failing PR.
- `package.json` already exposes lightweight scripts such as `lint`, `test`, `smoke`, `build`, or `build:renderer`.
- There is no existing `.github/workflows/*.yml` PR verifier, or existing checks do not cover the local scripts.
- Local user checkout is dirty with planning docs, screenshots, prompts, or other untracked work: use a clean temp clone rather than touching the user's tree.

## Slice

1. Create a feature branch from clean `main`, e.g. `ci/add-pr-verification`.
2. Add `.github/workflows/ci.yml`:
   - trigger on `pull_request` to `main`
   - optional `workflow_dispatch`
   - `permissions: contents: read`
   - Node 22 via `actions/setup-node`
   - `cache: npm`
   - run `npm ci`
   - run the repo's existing verification scripts in the same order a maintainer would: lint, tests, smoke, build
3. If the lint script syntax-checks source files manually, include existing test files too so tests cannot contain syntax errors unnoticed.
4. Add a README CI badge and list the verification commands under Commands/Test Plan.
5. Do not change dependencies in the same PR unless the task is specifically dependency maintenance.
6. Run local verification and `git diff --check` before commit.
7. Open a PR and watch the first GitHub Actions run; report both local and remote results.

## Template workflow

```yaml
name: CI

on:
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  verify:
    name: Lint, test, smoke, and build
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v6
        with:
          node-version: 22
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Lint JavaScript
        run: npm run lint

      - name: Run tests
        run: npm test

      - name: Run smoke check
        run: npm run smoke

      - name: Build renderer
        run: npm run build
```

## Reporting notes

- If `npm ci` reports audit vulnerabilities but succeeds, mention the audit count in the final report without running `npm audit fix --force` as part of this CI slice.
- If `gh pr view --repo OWNER/REPO` errors with `argument required`, rerun it with the PR number or branch, e.g. `gh pr view 1 --repo OWNER/REPO --json ...`.
- If a coding helper creates incidental metadata such as `.omc/`, remove it before staging and verify `git status --short` contains only intended project files.
