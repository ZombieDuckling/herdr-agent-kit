# Org-Wide Ship-Readiness Fan-Out

Use this reference when the user asks to “full send” a whole GitHub org/repo portfolio with Fabled Five / Claude Code and expects the result to be ready to ship, not merely audited.

## Preconditions

1. Inventory repos and clone/update a local workspace.
2. Write a repo-by-repo audit report before editing.
3. Convert the audit into a ship-readiness brief with explicit gates:
   - professional docs,
   - build/test baseline,
   - security/static scan where relevant,
   - CI smoke checks,
   - product/placeholder review,
   - final ship/no-ship matrix.
4. If Claude Code is rate-limited, queue a delayed launcher rather than pretending work started.
5. When the user requests Fabled Five specifically, pin Claude Code to Fable 5 explicitly:

```bash
claude -p "$(cat prompt.md)" --model claude-fable-5 --max-turns 80 --output-format text
```

## Five-agent split

- Agent 1 — Backend/security: active backend repos, docs redaction, compile fixes, Semgrep/static-analysis, CI smoke.
- Agent 2 — Mobile: Android/iOS build baselines, toolchain pins, release flags, Swift/Gradle verification.
- Agent 3 — Frontend/product UX: README reset, build/typecheck/test, placeholder route triage, Playwright smoke.
- Agent 4 — Docs/ops/vendor hygiene: ops safety docs, archive/status docs, vendor fork notes; no destructive cloud/vendor edits.
- Agent 5 — Release manager/QA: final matrix, verifies reports, checks branches/PRs, catches overreach, never merges default branches.

## Guardrails

Agents may create branches, edit files, test, commit, and push PR branches if authorized. They must not:

- merge default branches,
- delete large code/vendor trees,
- rewrite architecture speculatively,
- expose secrets in docs/logs/PRs,
- claim ship-ready without real commands passing.

## Shell safety for queued launchers

When generating large prompts for tmux/Claude panes, do not execute markdown prompt content through shell expansion. Prefer:

```bash
claude -p "$(cat /path/to/prompt.md)" --model claude-fable-5 ...
```

Generate prompt files with quoted heredocs or simple file writes. Syntax-check launchers with `bash -n` before arming them.

## Final matrix format

Each repo must end with:

```text
Repo:
Status: Ship / Conditional Ship / No Ship / Archive / Vendor Mirror
Branch:
PR:
Build command:
Test command:
Security scan:
Docs status:
Known blockers:
Next owner action:
```

## Reporting preference

For client-facing/user-facing PDFs or reports, use the user’s preferred public brand rather than raw technical org slugs. Keep technical slugs only where they are necessary for URLs, remotes, or commands.