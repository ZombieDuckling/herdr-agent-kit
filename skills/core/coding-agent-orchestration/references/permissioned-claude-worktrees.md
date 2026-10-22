# Permissioned Claude Code worktrees

Session-derived pattern for fast multi-agent desktop/app builds.

## Problem

Claude Code print-mode workers can self-report that changes are “ready” but stop at permission/write gates, especially when launched through wrappers. Visual tmux fan-outs can also mangle multiline prompts into shell `quote>` mode if the prompt is embedded directly in the command string.

## Working pattern

1. Create isolated git worktrees per branch/surface.
2. Write each worker prompt to a prompt file in the main repo, e.g. `prompts/core-workflow-sonnet.md`.
3. Launch Claude Code from the target worktree with the prompt file substituted by the shell and an explicit permission mode:

```bash
claude -p "$(cat /path/to/prompts/core-workflow-sonnet.md)" \
  --model claude-sonnet-4-5 \
  --permission-mode acceptEdits \
  --max-turns 30 \
  --output-format text
```

4. If a worker still only asks for write approval or sits silent, kill it and relaunch in the isolated worktree with:

```bash
--permission-mode acceptEdits
```

Use bypass only when the worktree is intentionally isolated and the prompt is constrained to the repo/surface.

5. Always verify the branch yourself:

```bash
npm run lint
npm test
npm run build
```

6. Remove agent scratch directories before final merge when present, e.g. `.omc/`.

## Review gate pattern

For high-pressure builds:

- Sonnet implements in worktrees.
- Hermes verifies locally.
- Fable/strong reviewer reviews the integrated branch.
- Sonnet fixes reviewer feedback.
- Repeat until reviewer gives a clear GO.

Do not rely on worker self-reports for success; use committed code + direct verification output.