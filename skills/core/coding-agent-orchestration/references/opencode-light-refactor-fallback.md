# OpenCode Light Refactor Fallback

Use this when the user wants to conserve Claude/Fable tokens, or when a Claude Code fan-out fails and the next best step is a cheap/light hygiene pass.

## When to use

- Claude/Fable session limit or token burn is a concern.
- A full multi-agent launch failed before producing artifacts.
- The user asks for "quick light refactoring" or a preparatory pass before a later Claude review.

## Scope that works well

- README/STATUS/KNOWN_ISSUES cleanup.
- Removing unprofessional placeholder text from root docs.
- Adding CI smoke workflows.
- Fixing very small compile blockers with direct verification.
- Producing a handoff report for a later stronger-model pass.

Avoid:

- Broad architecture refactors.
- Large deletes.
- Vendor-source changes.
- Claims that repos are ship-ready without real build/test/security gates.

## Procedure

1. Smoke test OpenCode:

```bash
opencode --version
opencode auth list
opencode run 'Respond with exactly: OPENCODE_SMOKE_OK' --agent build
```

2. Partition into non-overlapping repo groups.
3. Use bounded `opencode run` prompts, not long TUI sessions, unless iteration is necessary.
4. Tell OpenCode explicitly: no push, no merge, no broad runtime changes.
5. After it finishes, Hermes verifies directly:

```bash
git status --short
git diff --stat
# plus repo-specific build/test commands
find . -maxdepth 4 -name .omc -print
```

6. Remove accidental `.omc/` artifacts unless they are intentionally project-owned.
7. Write a handoff report containing changed files, commands run, pass/fail results, and recommended Claude follow-up.

## Example prompt

```text
You are doing a quick low-risk hygiene pass. Do NOT push, merge, delete content, or refactor architecture. Add/improve README.md, STATUS.md, KNOWN_ISSUES.md. Fix only obvious compile blockers if surgical and verifiable. At the end, print files changed and verification commands run.
```

## Verification standard

A successful OpenCode fallback is not "OpenCode said done". It is:

- Files exist and diffs are sane.
- Canonical test/build command passes where touched code changed.
- No accidental artifacts remain.
- A concise report exists for the next manual/Claude pass.