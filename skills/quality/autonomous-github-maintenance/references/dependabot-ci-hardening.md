# Dependabot CI hardening example: npm ECONNRESET

Session pattern from a portfolio maintenance run on a Node/Electron repo.

## Situation

- A Dependabot PR updated a native npm dependency.
- CI failed during `npm ci` with `ECONNRESET` / network aborted before tests ran.
- Another Dependabot PR already updated `actions/setup-node` and was green, so duplicating that change in a manual PR would have mixed scopes.
- Dependabot PRs reported `maintainerCanModify: false`, so editing those branches was not appropriate.

## Safe maintenance slice

Create a separate CI hardening PR from `main` that adds npm retry/timeout settings before install:

```yaml
- name: Harden npm network retries
  run: |
    npm config set fetch-retries 5
    npm config set fetch-retry-mintimeout 20000
    npm config set fetch-retry-maxtimeout 120000
    npm config set fetch-timeout 60000
```

## Verification checklist

- Confirm workflow contains the new step, e.g. with a simple Python/string sanity check.
- Run `npm ci` locally.
- Run the repo's full verification, e.g. `npm run verify`.
- Run `git diff --check`.
- Push a CI branch and open a PR.
- Watch PR checks and report real GitHub check status.

## Reporting nuance

If `npm ci` reveals pre-existing audit findings, report them as existing dependency-tree findings and do not silently run `npm audit fix` unless dependency changes are the chosen slice.