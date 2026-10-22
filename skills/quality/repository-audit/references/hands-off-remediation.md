# Hands-Off Remediation Reference

Recipes for the unattended fix pass that follows an audit — the changes an agent can land with
no owner input. Every recipe assumes the audit's read-only clones still exist under
`$BASE/repos/` with working git remotes.

## 1. Decide what is safe to land unattended

Land unattended:

- commit a lockfile that is missing or ignored (makes dependency advisories reportable),
- replace mutable action tags with commit hashes,
- add an explicit `permissions:` scope to every workflow,
- add a CI workflow to a repo that has none, starting with the repo other repos depend on,
- add a drift gate that pins copies which are meant to be identical,
- add ignore files, provenance plumbing (deploy step naming the commit SHA), and checks for
  invariants nobody currently enforces.

Do not land unattended: anything that rewrites shared state or history — renumbering applied
migrations, force-pushing history, deleting files other pages link to, DNS and org settings,
paid-plan features, business semantics in data.

## 2. Which branch is safe

```bash
for f in "$BASE"/*/repos/*/.github/workflows/*.y*ml; do
  [ -f "$f" ] || continue
  printf '%s: ' "${f##*/}"; sed -n '/^on:/,/^[a-z]/p' "$f" | grep -E 'branches:' | head -1
done
```

Committing to a branch no workflow deploys cannot break an environment. Where `main` is trunk
and `staging`/`production` deploy, `main` is the safe target. Confirm nothing triggers on
`main` first:

```bash
grep -rn -A4 '^on:' --include='*.yml' "$BASE"/repos/*/.github/workflows | grep -E 'branches: \[main\]'
```

A guard that runs on `pull_request` only does not fire on a push to trunk — direct commits run
nothing, which is another reason the hands-off pass stays quiet.

## 3. Pin actions to commits

Resolve the current commit behind each tag, then rewrite every `uses:` line:

```bash
for A in actions/checkout:v4 actions/setup-node:v4 cloudflare/wrangler-action:v3 actions/upload-artifact:v4; do
  REPO=${A%%:*}; TAG=${A##*:}
  echo "$REPO@$TAG -> $(gh api "repos/$REPO/commits/$TAG" --jq .sha)"
done
```

Rewrite with the resolved hash and keep the tag as a trailing comment so a human can still see
what the pin means:

```python
text = re.sub(r"uses:\s*" + re.escape(tag) + r"\b", f"uses: {pinned}", text)
```

Collect the distinct action references across the whole org first — orgs typically use a small
set of actions (checkout, setup-node, a deploy action, upload-artifact), so the pinning table
is short.

## 4. Scope workflow permissions

Insert a workflow-level block only when the workflow has none, immediately before `jobs:`:

```yaml
permissions:
  contents: read
```

Read the workflow body before choosing the scope: a step that calls `gh api` for earlier
workflow runs needs `actions: read` as well as `contents: read`. A workflow that already
declares `permissions:` at job level has its scope set — inserting a workflow-level block
without checking duplicates the declaration and silently widens it. When verifying coverage,
count both workflow-level (`^permissions:`) and job-level (`^\s{4}permissions:`) blocks.

## 5. CI scaffolding for a repo that has none

Start with the repo that others read from. Keep the workflow read-only, pinned,
permission-scoped, and honest about the environment:

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<sha> # v4
      - uses: actions/setup-node@<sha> # v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm test
```

For a data or docs repository with no test script, validate what actually exists: parse every
JSON file, syntax-check the scripts, check that page links resolve. Never add a test command the
repository does not have.

## 6. A pipeline that cannot run yet

Cross-repo suites need the sibling repositories. Without a token to read them, skip loudly for
the right reason rather than failing for the wrong one:

```yaml
      - name: Cross-repo checks, when the siblings can be fetched
        env:
          REPOS_TOKEN: ${{ secrets.REPOS_TOKEN }}
        run: |
          if [ -z "$REPOS_TOKEN" ]; then
            echo "REPOS_TOKEN is not set, so the sibling repositories cannot be fetched."
            echo "The suites read them one directory above this checkout; with none present they"
            echo "report 'present in only 0' and fail for a reason that is not about the code."
            exit 0
          fi
          for repo in <siblings>; do
            git clone --depth 1 "https://x-access-token:${REPOS_TOKEN}@github.com/<org>/${repo}.git" "../${repo}"
          done
          npm run test:fast
```

Clone siblings into the workspace's parent directory when the suites resolve paths relative to
their own location — check how an existing suite computes its repo root before choosing the
destination.

## 7. Drift gates

Only pin copies that are byte-identical today. Verify before writing the gate:

```bash
hav() { shasum -a 256 "$1" 2>/dev/null | awk '{print substr($1,1,12)}'; }
for R in <repos>; do printf '%-22s %s\n' "$R" "$(hav "$BASE/repos/$R/scripts/sonar.mjs")"; done
```

Then extend the suite that already carries drift checks: register a new check ID in its style
and keep the same receipt shape (expected, actual, where, repro). Suite-specific IDs must be
fresh — read the suite for the highest number in the family before picking one.

## 8. Gate landing rule

If the invariant is already violated in a repo, land the gate advisory and name the owner-facing
issue in a comment:

```yaml
      # <repo> already holds two files numbered the same, so this step reports a real defect on
      # its first run. It is advisory until the renumbering lands: blocking a pipeline on a
      # pre-existing number would stop every unrelated change. Drop continue-on-error then.
      - name: <check>
        continue-on-error: true
        run: node scripts/<check>.mjs
```

## 9. Commit, push, verify

One reasoned commit per item; the message states the problem the change removes and what the
reader should know (mutable tag, advisory status, what stays deliberately untouched). Set the
identity explicitly in a fresh clone:

```bash
git -C "$R" config user.name "<name>"
git -C "$R" config user.email "<email>"
git -C "$R" add -- <files>
git -C "$R" commit -m "<subject>\n\n<body>"
git -C "$R" push origin "$(git -C "$R" rev-parse --abbrev-ref HEAD)"
```

Then verify from the remote, not from the local tree:

```bash
for R in <repos>; do
  git -C "$BASE/repos/$R" fetch origin --quiet
  test -z "$(git -C "$BASE/repos/$R" log --oneline origin/main..HEAD)" && echo "$R: pushed" || echo "$R: UNPUSHED"
  test -z "$(git -C "$BASE/repos/$R" status --porcelain)" && echo "$R: clean" || echo "$R: DIRTY"
done
```

Evidence that a new gate works is a GitHub run on the remote:

```bash
gh run list -R owner/repo --limit 3 --json workflowName,status,conclusion,headBranch \
  --jq '[.[] | "\(.workflowName)/\(.status)/\(.conclusion // "-") on \(.headBranch)"] | join("  |  ")'
```

## 10. Report the batch

State per item: what landed, in how many repos, and what proves it (remote file, run
conclusion). Then state the things you deliberately left alone and why, so the user knows which
loose ends are theirs. Never claim a repo is clean without the unpushed/dirty check above.
