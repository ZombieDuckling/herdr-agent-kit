---
name: repository-audit
description: "Use when auditing a repo or org for tech debt, then landing the fixes."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Repository-Audit, Codebase, Documentation, Refactor, Quality, Security]
    related_skills: [github-repo-management, github-code-review, codebase-inspection, requesting-code-review]
---

# Repository / Organization Audit

Run a read-only audit across one repo or an entire GitHub org/account. This skill is for inherited or messy codebases where the user wants to know what is broken, unprofessional, incomplete, dead, or unsafe before refactoring.

## When to Use

- User asks for a “full audit” of a repo/org/codebase.
- User says a developer left messy work, many features are unfinished, READMEs are unprofessional, or repos need refactoring.
- User asks what should be removed/refactored but has not explicitly approved code changes yet.
- User wants repo-by-repo status, broken builds/tests, dead-code signals, TODOs, placeholder inventory, README rewrite needs, or professionalization plan.

## Default Safety Rule

**Audit first, do not change runtime code.**

Unless the user explicitly asks for implementation/refactor changes, clone locally, inspect, run safe read-only/build checks, and write reports. Do not push branches, open PRs, delete code, or “clean up” files during the audit phase.

The audit phase ends when the user gives a go-ahead (often phrased as "what can you handle
without me"). From that point Step 6b governs: land the reversible items unattended, and keep
anything that rewrites shared state or history for the owner to authorise.

## Step 1 — Inventory Scope

For a GitHub org:

```bash
ORG=<org>
BASE="$HOME/Documents/GitHub-org-audits/$ORG-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BASE/repos" "$BASE/reports"
gh repo list "$ORG" --limit 200 --json name,nameWithOwner,description,isPrivate,isArchived,isFork,updatedAt,defaultBranchRef,url,primaryLanguage,visibility > "$BASE/repos.json"
```

For a local repo, set:

```bash
BASE="$PWD/.audit-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BASE/reports"
```

Record repo count, default branches, language, archived/fork status, and descriptions.

## Step 2 — Clone / Snapshot Read-Only

Clone repos into `$BASE/repos/`:

```bash
cd "$BASE/repos"
gh repo clone owner/repo repo -- --quiet
```

Keep all generated artifacts under `$BASE/reports/`. Avoid modifying source files. If a command writes build artifacts, note it; prefer discovery commands first.

## Step 3 — Static Hygiene Audit

Check each repo for:

- Root README presence and professionalism.
- README sections: purpose, status, architecture, setup, env/config, usage, development, test, deploy/release, directory map, known issues.
- TODO/FIXME/HACK/WIP/STUB/PLACEHOLDER/COMING SOON markers.
- Debug leftovers: `console.log`, `debugger`, `print`, `println`, `fmt.Printf`, `std::print`, noisy emoji logs in production paths.
- Secret-looking patterns, but **do not reproduce secret values in final reports**.
- Tests and CI presence.
- Manifests/build systems: `package.json`, `go.mod`, `Cargo.toml`, `build.gradle`, `Package.swift`, `Makefile`, `CMakeLists.txt`, etc.
- Duplicate, empty, large, generated, vendored, or unclear files.
- Active vs experimental vs generated vs vendor code boundaries.

## Step 4 — Lightweight Build/Test Probes

Run safe, minimal checks to establish baseline. Capture logs under `$BASE/reports/`.

Suggested probes:

```bash
# Go
go test ./...

# Node — inspect scripts first; install only if in scope
npm run typecheck
npm run lint
npm run test -- --run
npm run build

# Gradle/Android — tooling baseline before expensive build
./gradlew tasks --all --stacktrace

# Rust
cargo check
cargo test --no-run

# C/C++
cmake -S . -B build && cmake --build build --target help
# or inspect Makefile targets only if build would be expensive

# Swift/iOS
xcodebuild -list
```

If a build fails because local tooling is not pinned or compatible, report the exact failure and the fix direction (for example: pin a supported JDK), not a permanent claim that the repo is unbuildable.

## Step 4b — Verify the measurement before trusting it

A metric that counts the wrong population is worse than no metric, because it
ends up quoted in the executive summary. Before writing any finding from a
scan, spot-check that scan against two or three repos by hand and confirm the
hits are real.

- **Read committed state from git, never the working tree — once the probes
  have run, `npm install` has written a lockfile that is not committed.** Ask
  `git ls-files` for lockfiles and for any file list that must reflect the
  repository, and re-run disk-based counts after installs with `node_modules`,
  `dist`, `build`, `out` and coverage excluded. Scanning the working tree after
  a probe inflated total size roughly fivefold and invented lockfiles in repos
  that have none — that is wrong in the direction that flatters the org.
- **Marker scans match attribute names and substrings unless anchored.**
  `placeholder=` in HTML, and the word "related" (which contains the marker
  `later`), both register as TODO markers. Match uppercase word-boundary tokens
  and sample the flagged lines before reporting the count.
- **"Missing README section" is a claim about the repo, so match the headings
  the repos actually use.** Searching for "Installation" when a repo titles the
  same content "Run it locally" or "Deploying" reports nine absent sections per
  repo that are all present. Read three READMEs first and build the pattern from
  their real headings.
- **Duplicate-file detection across repos is the highest-leverage structural
  finding.** Hash every code file of non-trivial size across the clones and
  group by digest. Identical copies of one library or one workflow in four repos
  mean every fix must be applied four times, and drift between the copies is
  silent.
- **Separate environment-caused probe failures from real defects.** A suite
  failing on an unset variable or a 401 without a bearer token is an environment
  caveat, not a code fault. Group failures by cause, say which are environmental,
  and state plainly that a laptop run is not a CI run.
- **The org's own open issues are the debt inventory — collect them.** Pull
  issues, labels and CI conclusions per repo with `gh api`. A decision-needed
  label tells you which findings are blocked on the owner rather than on
  engineering, which is what the user needs to act on.
- **On private repos a free plan returns 403 for branch protection.** Do not
  read that as "no protection exists"; report it as unavailable and check what
  is actually enforceable — org-level 2FA via the org API, and workflow contents
  for `permissions:` blocks and action pinning.

## Step 5 — Classify Findings

Use practical priorities:

- **P0 / Critical:** unprofessional client-visible README; real or possible secrets in repo/docs; build/test command fails; release/debug auth enabled; destructive operations; missing root README for active production repo.
- **P1 / High:** no CI; user-facing placeholders/coming-soon pages; raw debug logs in production paths; undocumented env/deploy; active vs experimental code unclear.
- **P2 / Medium:** duplicate docs, generated artifact policy, repo splitting, style cleanup, stale notes.

## Step 6b — Hands-off remediation pass

When the user says "handle what you can without me", the deliverable is *landed
changes*, not a proposal. A branch and a pull request left open is work the user
still has to do, which is the opposite of hands-off.

Answer first with the split they asked for, in two short lists:

1. **What you can land unattended** — lockfiles, action pinning, workflow
   `permissions:`, CI for repos that have none, drift gates, ignore files,
   deploy-provenance plumbing. Each item carries a risk label and no question.
2. **What needs one decision, not work** — org 2FA, DNS records, paying for
   branch protection, splitting staging data, choosing a licence, business
   semantics in the data. State the decision, not the implementation behind it.

Then land list 1. Sequence per item: check the deploy triggers, edit, validate
locally, commit with a reasoned message, verify on the remote, report which new
pipelines ran and what their conclusion was.

Before pushing anything, read `on:` in every workflow to learn which branches
deploy. Committing to a branch that deploys nothing means the change cannot break
a live environment — that is what makes the pass safe to run unattended. Where
`main` is the trunk and `staging`/`production` deploy, commit to `main`.

Validate every gate you generate before it is committed:

- Run the new check locally against the clones and confirm it exits 0 on the
  current tree — a gate that goes red on day one is a gate the user will disable.
- Never land a blocking gate on a pre-existing violation. Land it advisory
  (`continue-on-error: true`) with a comment naming the tracked issue and the
  condition for removing the flag; blocking unrelated work on an old defect is
  worse than the defect.
- Parse every edited workflow to prove the YAML still loads and still declares a
  trigger and jobs. A YAML 1.1 parser reads an unquoted `on:` as the boolean
  `true`, so accept `doc[True] or doc["on"]` before reporting a missing trigger.
- Prefer extending a check suite the repo already runs over adding a parallel
  one: read its manifest and its check IDs, then add new numbered IDs in the same
  style. Duplication is a repo-wide problem, so a second scanner for it is the
  same mistake one level up.

## Step 7 — Recommend Safe Refactor Sequence

Default sequence:

1. **Phase 1 — Documentation/professionalization only**
   - Rewrite root READMEs.
   - Redact secrets/examples.
   - Add `.env.example`, `STATUS.md`, `KNOWN_ISSUES.md`.
   - Move scratch notes to `docs/archive/` if worth keeping.

2. **Phase 2 — Build/test baseline**
   - Fix minimal build/test blockers.
   - Pin tool versions.
   - Add CI smoke workflows.

3. **Phase 3 — Safe cleanup/refactor**
   - Remove or quarantine confirmed dead code.
   - Replace debug prints with structured logging.
   - Convert TODOs to tracked issues.
   - Hide/remove production placeholders.

4. **Phase 4 — Feature completion planning**
   - Prioritize unfinished features only after repo hygiene is measurable.

Committed reality beats any claim about intent. After pushing, verify the remote
rather than trusting the push:

```bash
git -C "$R" show origin/main:<path>          # the file as the remote has it
git -C "$R" log --oneline origin/main..HEAD   # anything unpushed
git -C "$R" status --porcelain                # anything uncommitted
gh run list -R owner/repo --limit 3 --json workflowName,status,conclusion
```

Report the pipelines your change triggered and their conclusions — a new CI
workflow that ran and passed on the remote is the strongest evidence a gate
works. Where a pipeline cannot run yet (missing cross-repo token, a suite that
needs browsers), make it skip with an explanatory message instead of failing for
a reason that is not about the code, and say so in the report.

Leave alone, and name as left alone: anything that rewrites shared state or
history. Renumbering migrations that are already applied, force-pushing to purge
binaries from history, and deleting files other documents link to are all
changes the owner should authorise, not changes to slip into a hands-off batch.

## Report Artifacts

Produce at minimum:

- `reports/automated_audit.json` — machine-readable findings.
- `reports/automated_audit.md` — repo-by-repo automated summary.
- `reports/FULL_AUDIT_SUMMARY.md` — executive report with priorities, exact failures, and next-step plan.
- Build/test logs for failed probes: `reports/<repo>-<check>.log`.

## the user Reporting Style

The user prefers blunt, practical assessment. Lead with the broken things and what should happen next. Avoid fluff. If the written audit is long, also provide a concise voice-note style summary when practical.

## References

- `references/org-wide-repo-audit.md` — condensed workflow and command checklist from a multi-repo GitHub org audit.
- `references/hands-off-remediation.md` — recipes for the unattended fix pass: action pinning, permission scoping, CI scaffolding, drift gates, safe commit and remote verification.

## Pitfalls

- Do not start deleting code before a build/test baseline exists.
- Do not reproduce secret values in reports; say “secret-pattern warning” and point to file/line.
- Do not treat third-party/vendor mirrors like application code; add fork/vendor notes instead.
- Do not let an unprofessional README become the final source of truth; rewrite it as a first-class deliverable.
- Do not confuse local tool mismatch with repo failure; record exact environment/tooling issue and recommended pin/version.
- **Do not report a count you have not spot-checked.** Recount the largest number in the report by hand on one repo before it reaches the summary. Audits fail the same way check suites do: several separate auto-counts, each quietly measuring the wrong population.
- **Do not present corrected figures as if they were the first ones.** Name which checks you corrected and that the numbers changed. A reader who already quoted the first table should not be silently contradicted.
- **Do not let the probes dirty the diagnosis.** Install and test runs write lockfiles, build output and vendored trees; judge the repository by its committed contents and say which findings came from a probe instead.
- **Do not hash-claim a duplicate without hashing it.** Before pinning a drift gate, confirm the copies are byte-identical with `shasum -a 256`; near-identical files (deploy workflows deliberately differ per repo) must not be pinned together or the gate fails on a difference that was intended.
- **Do not write a checker that asserts a repo invariant before reading how the repo documents that invariant.** A publish script that resolves `img/<name>` from a separate pictures directory, or a sidebar file that deliberately carries no heading, turns a naive validator into dozens of false failures.
- **Do not assume an existing gate covers what its name implies.** A "numbering is continuous" check finds gaps and passes happily on a duplicated number; read the check body before claiming coverage either way.
- **Do not leave a batch of commits half-applied because files were already staged in an earlier commit of the same batch.** Group each item's files deliberately, and if a later item has nothing left to commit, fold its reasoning into the earlier commit rather than shipping a silent no-op.
