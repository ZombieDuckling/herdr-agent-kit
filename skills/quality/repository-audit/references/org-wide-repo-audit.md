# Org-Wide Repo Audit Reference

This reference captures a reusable pattern for auditing a messy GitHub organization before refactoring.

## Workspace shape

```bash
ORG=<org>
BASE="$HOME/Documents/GitHub-org-audits/$ORG-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BASE/repos" "$BASE/reports"
```

Keep all outputs in `reports/` and clone sources under `repos/`.

## Inventory command

```bash
gh repo list "$ORG" --limit 200 \
  --json name,nameWithOwner,description,isPrivate,isArchived,isFork,updatedAt,defaultBranchRef,url,primaryLanguage,visibility \
  > "$BASE/repos.json"
```

## Read-only clone loop

```bash
python3 - <<'PY' > "$BASE/clone-commands.sh"
import json, os, shlex
base=os.environ['BASE']
repos=json.load(open(f'{base}/repos.json'))
print('set -euo pipefail')
print('cd '+shlex.quote(f'{base}/repos'))
for r in repos:
    print(f'if [ ! -d {shlex.quote(r["name"])}/.git ]; then gh repo clone {shlex.quote(r["nameWithOwner"])} {shlex.quote(r["name"])} -- --quiet; fi')
PY
bash "$BASE/clone-commands.sh" 2>&1 | tee "$BASE/reports/clone.log"
```

## Static checks to collect

For each repo, collect:

- file/source counts and primary languages,
- manifests/build systems,
- root README and nested READMEs,
- tests and CI,
- TODO/FIXME/HACK/WIP/STUB/PLACEHOLDER/COMING SOON markers,
- debug logs/prints,
- profanity/unprofessional language in docs/comments,
- secret-pattern warnings, with values redacted,
- duplicate/empty/large/generated files,
- safe build/test probe results.

## Useful regexes

```text
TODO/FIXME:       \b(TODO|FIXME|HACK|XXX|BUG|WIP|TEMP|STUB|PLACEHOLDER|NOT IMPLEMENTED|COMING SOON)\b
Debug leftovers: console\.log|debugger;|print\(|println\(|fmt\.Print|std::print
Secrets:         (api[_-]?key|secret|token|password|passwd|private[_-]?key)\s*[:=]\s*['"]?[A-Za-z0-9_./+\-=]{12,}
```

Two rules make these usable:

- **Anchor the marker pattern to a standalone uppercase token.** Unanchored, `placeholder=` in HTML and the letters `later` inside "related" count as markers and inflate the headline number.
- **Exclude generated and vendored trees from every count.** Skip `node_modules`, `dist`, `build`, `out`, `.next`, `coverage`; otherwise size, file and test counts are all reporting the probe's effects rather than the repo.

## Committed state versus working tree

Never read repository facts from disk once probes have run. Installing dependencies writes lockfiles, build trees and vendored sources that are not part of the repo.

```bash
# lockfiles must be COMMITTED, not merely present
for R in "$BASE"/repos/*/; do
  [ -d "$R/.git" ] || continue
  git -C "$R" ls-files | grep -E '(^|/)(package-lock\.json|pnpm-lock\.yaml|yarn\.lock|bun\.lockb)$' \
    && echo "  ^ committed lockfile in $(basename "$R")" || true
done
```

Record also whether `.gitignore` and `.env.example`/`.dev.vars` are tracked, and flag lockfiles that exist on disk only because a probe ran.

## Cross-repo duplication sweep

Duplicate libraries and workflows across repos are the highest-leverage structural finding in an org audit: every fix must be applied once per copy and drift is silent.

```bash
python3 - <<'PY'
import hashlib, collections, pathlib
CODE={'.js','.ts','.mjs','.cjs','.tsx','.jsx','.py','.sh','.yml','.yaml','.sql'}
SKIP={'node_modules','.git','dist','build','coverage','.next','out'}
h=collections.defaultdict(list)
for repo in pathlib.Path('repos').iterdir():
    if not (repo/'.git').exists(): continue
    for f in repo.rglob('*'):
        if not f.is_file() or any(s in f.parts for s in SKIP): continue
        if f.suffix not in CODE or f.stat().st_size < 400: continue
        h[hashlib.sha256(f.read_bytes()).hexdigest()].append(f'{repo.name}/{f.relative_to(repo)}')
for v in h.values():
    if len({p.split('/')[0] for p in v}) > 1:
        print(' == '.join(v))
PY
```

## Org-level settings checks

Branch protection may be unavailable on private repos without a paid plan — GitHub returns 403. Report it as unavailable rather than as "no protection"; check what is enforceable instead.

```bash
gh api "orgs/$ORG" --jq '{two_factor_requirement_enabled, plan: .plan.name}'
for R in "$BASE"/repos/*/.github/workflows/*.y*ml; do
  [ -f "$R" ] || continue
  echo "$R"
  grep -cE 'uses: [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@' "$R"   # total action uses
  grep -cE 'uses: [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@v' "$R"  # tag-pinned, not SHA-pinned
  grep -cE '^permissions:' "$R"                              # explicit permissions block
done
```

Collect per repo: CI presence, latest run conclusions (`gh run list --json conclusion,workflowName`), open issues with labels (`gh issue list --json number,title,labels`), and PRs. A decision-needed label marks findings blocked on the owner rather than on engineering — surface those separately, because they are what the user can actually action.

## Build/test probes

Run probes only when safe and record logs:

```bash
# Go
go test ./... > "$BASE/reports/<repo>-go-test.log" 2>&1 || true

# Gradle/Android
./gradlew tasks --all --stacktrace > "$BASE/reports/<repo>-gradle-tasks.log" 2>&1 || true

# Node
npm run typecheck > "$BASE/reports/<repo>-typecheck.log" 2>&1 || true
npm run lint > "$BASE/reports/<repo>-lint.log" 2>&1 || true
npm run test -- --run > "$BASE/reports/<repo>-test.log" 2>&1 || true
npm run build > "$BASE/reports/<repo>-build.log" 2>&1 || true

# Rust
cargo check > "$BASE/reports/<repo>-cargo-check.log" 2>&1 || true
```

Record the exit code and the pass/fail tally in each log, and classify every failure by cause before it reaches the report:

- **real defect** — code-level, reproducible, names a file or assertion;
- **environment** — unset variable, missing token, unreachable local endpoint, absent runtime. Report as a caveat, not a code fault, and say a laptop run is not a CI run;
- **tracked waiver** — the suite may carry its own baseline of accepted failures with reasons, expiry dates and linked issues. Read that baseline file; a red suite may be mostly documented debt, and conflating the two misrepresents the org in both directions.

## Report structure

Use:

```markdown
# <org> Organization Audit

## Executive Summary
- Blunt current state.
- Highest-risk repos.
- Exact build/test failures.
- Recommended next phase.

## Repository Inventory

## Top Risks by Repo

## Repo-by-Repo Audit
### <repo> — <priority>
- What it appears to be
- Evidence
- Serious issues
- What is probably broken/incomplete
- Refactor/professionalization needed

## Cross-Repo Problems

## Recommended Refactor Plan
Phase 1 docs/professionalization only → Phase 2 build/test baseline → Phase 3 safe cleanup/refactor → Phase 4 feature completion.

## Corrections Made to the Measurement
Name any scan whose rule was fixed during the audit and state that the figures changed.

## Artifacts Produced
```

Lead the executive summary with the finding that is quietly dangerous rather than the one that is loudest — shared production/staging resources and spoofable email outrank an untidy README even though neither fails a build.

## Important judgment calls

- If a repo is a third-party/vendor mirror, do not refactor upstream code by default. Add `FORK_NOTES.md` / vendor status docs.
- If README content is profane or scratchpad-like, replacing it is P0 even if code works.
- Secret-looking values in docs are P0 until reviewed/rotated/redacted.
- A local toolchain failure should become "pin/document supported toolchain," not a blanket claim that the repo is broken.
- Do not start dead-code removal until the repo has a build/test baseline; otherwise deletion risk is high.
- Do not present a corrected count as though it were the original; state the correction so nobody quotes a number you have since replaced.
