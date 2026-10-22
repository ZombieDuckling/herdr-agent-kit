# Sonnet build teams + Fable review gate

Use this pattern when the user asks for a high-speed client-product build with Claude teams, worktrees, and a hard reviewer gate.

## Pattern

1. Create/push a baseline repo first so every worker has a remote-backed foundation.
2. Split into non-overlapping git worktrees/branches by responsibility, for example:
   - `feature/core-workflow`
   - `feature/publisher-automation`
   - `feature/packaging`
   - `feature/design-assets`
3. Use Sonnet for implementation workers unless the user explicitly asks otherwise.
4. Hermes verifies every worker branch directly: `npm run lint`, tests, build, packaging/smoke as applicable.
5. Run Fable 5 as a reviewer after implementation/integration.
6. Feed Fable's review findings back to Sonnet implementers or fix directly if small.
7. Repeat: Sonnet fixes → Hermes verifies → Fable reviews → until Fable returns a clear GO.

## Claude Code permission handling

Claude Code print-mode workers can stop with permission questions even when the prompt says permission is granted. For trusted isolated worktrees, launch with explicit permission mode:

```bash
claude -p "$(cat prompts/task.md)" \
  --model claude-sonnet-4-5 \
  --permission-mode acceptEdits \
  --max-turns 40 \
  --output-format text
```

Use `acceptEdits` first when safety matters more than speed, but if it still stalls at permission prompts, use `bypassPermissions` only when the user has explicitly agreed, and only in an isolated repo/worktree with tight branch ownership.

## Tmux caveat

Multi-line prompts passed through tmux launchers can get shell-quote mangled and leave panes stuck at `quote>`. If that happens:

1. Kill the tmux session.
2. Write each worker prompt to `prompts/<worker>.md`.
3. Launch direct background `claude -p "$(cat prompts/<worker>.md)" ...` commands.
4. Track with Hermes background process IDs.

## Asset requests

When workers request images/assets, prefer deterministic assets for product UI (SVG/PNG/icon generation scripts) over decorative image-model output unless the prompt truly requires generative imagery. Commit generated assets and re-run build/tests before review.

## Reporting

Report branch names, process IDs, verification commands, and whether a worker was killed/relaunched. Do not claim a branch is ready until Hermes has verified it directly.