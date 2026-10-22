---
name: sonarqube
description: Run a SonarQube static analysis over code with the sonar CLI — quality, security and secrets findings, the same rules the SonarQube for IDE panel shows. Use when asked to audit code, review code quality, scan for vulnerabilities or secrets, check a diff before committing, or when the user mentions SonarQube, SonarLint, Sonar findings, or a code audit. Also covers the offline eslint + eslint-plugin-sonarjs fallback for when the CLI is not authenticated.
---

# SonarQube

Two ways to get Sonar's findings. Reach for the CLI first; fall back to the local scanner when
there is no connection to a SonarQube server.

## 1. The `sonar` CLI (needs a connection)

Installed at `/opt/homebrew/bin/sonar` (`brew install sonarqube-cli`).

**It does nothing without authentication — every subcommand, including `analyze secrets`,
answers "Not authenticated".** Authentication is a browser login the user must do themselves:

```
sonar auth login          # opens a browser; needs a SonarQube Cloud account or a Server ≥ 25.1
sonar auth status         # "No saved connection" means nothing below will work
```

In CI or a headless session, export `SONARQUBE_CLI_TOKEN` plus `SONARQUBE_CLI_ORG` (Cloud) or
`SONARQUBE_CLI_SERVER` (self-hosted) instead.

Once connected:

```
sonar analyze --file src/thing.js            # quality and security issues in one file
sonar analyze secrets <file>                 # hardcoded credentials; also reads stdin
sonar analyze dependency-risks               # known-vulnerable and badly-licensed dependencies
sonar list issues --project <key> --severities BLOCKER,CRITICAL --format json
sonar quality-gate status --project <key>
sonar api GET /api/…                         # anything the CLI does not wrap
```

`sonar integrate claude --global` installs SonarSource's own Claude Code integration —
secrets-scanning hooks and an MCP server in `~/.claude`. **Ask before running it:** it adds
hooks that run on every session, not just this one.

## 2. No connection? Use eslint + eslint-plugin-sonarjs

The same SonarJS rules the CLI applies to JavaScript and TypeScript, run locally with no
account and no network:

```
npm i --no-save --prefix /tmp/sonar eslint@9 eslint-plugin-sonarjs
SONAR_DIR=/tmp/sonar/node_modules node scripts/sonar.mjs
```

`scripts/sonar.mjs` is worth committing in every repository you audit. It scans everything `git
ls-files` lists, compares against `sonar-baseline.json` — the count of each rule in each file
today — and **fails only on a new finding**, so a codebase with hundreds of stylistic findings
can still gate its deploys on not getting worse. `--update` banks an improvement or accepts a
new finding deliberately. If a repository has no such script, copy one from another repo that has it.

## Reading the findings

- **Most of what SonarJS reports in a dense codebase is house style** — nested template
  literals, nested conditionals, cognitive complexity. Do not mass-rewrite them; baseline them.
- **The ones worth acting on** are `no-dead-store`, `no-unused-vars`, `unused-import`,
  `no-all-duplicated-branches`, `no-identical-expressions`, `no-element-overwrite`,
  `no-empty-collection`, `misplaced-loop-counter` and the hotspot rules `super-linear-regex`
  (S8786) and `pseudo-random` (S2245). Check each one is really dead before deleting it: a
  variable assigned and never read is sometimes a value that *should* have been used.
- **HTML rules** (`Web:S6853`, `Web:InputWithoutLabelCheck`) come from the SonarQube for IDE
  panel rather than the JS rules, and are usually real: a `<label>` with no `for=` that does
  not wrap its control is an unlabelled field for a screen reader. A runtime accessibility
  check (axe) will not see it if the form lives in a hidden modal — read the markup instead.
