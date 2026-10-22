# PR CI restoration for existing Node/Next.js branches

Use this pattern when an open PR has no status checks and the repo already exposes lightweight verification scripts.

## When to use

- Open PR branch already exists and is safe to update.
- `package.json` has scripts such as `lint`, `typecheck`, and `build`.
- Prior CI was removed for token/workflow-scope reasons, or the PR simply has no checks.
- The goal is to make the PR reviewable without changing product behavior.

## Minimal workflow shape

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  verify:
    name: Lint, typecheck, and build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Typecheck
        run: npm run typecheck

      - name: Build
        run: npm run build
```

## Verification sequence

1. Work on the existing PR branch only after confirming `git status --short --branch` is clean.
2. Ask Claude Code for a bounded plan, but keep the actual edit small and inspectable.
3. Run locally: `npm ci`, `npm run lint`, `npm run typecheck`, `npm run build`, and `git diff --check`.
4. Remove generated artifacts before staging (`.next/`, `tsconfig.tsbuildinfo`, agent scratch dirs such as `.omc/`).
5. Commit and push to the PR branch.
6. Poll `gh pr view <n> --json statusCheckRollup,headRefOid` and `gh run list --branch <branch>` until the head commit is green.
7. Add a PR comment with the commit SHA, local verification summary, and Actions run URL.

## Pitfalls

- Do not combine `pull_request` to `main` with `push` to the PR head branch unless duplicate Actions runs are desired. A PR branch update can trigger both.
- Do not add Playwright browser installation by default; it is slower and higher-maintenance. Add it only when the repo already has stable browser tests and the nightly slice explicitly needs them.
- `npm audit` warnings discovered during `npm ci` are worth reporting, but do not broaden a CI-restoration slice into dependency remediation unless that was the selected scope.
