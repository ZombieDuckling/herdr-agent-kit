# Fabled Five Launcher Hardening

Use this when launching multiple Claude Code panes/sessions from Hermes, especially after a delayed start due to Claude rate limits.

## Durable lessons

- Syntax checks are not enough. A launcher can pass `bash -n` and still fail at runtime if prompt-file expansion or tmux quoting is wrong.
- Always run a **one-pane smoke test with the exact launcher command shape** before arming a five-agent run.
- Prefer a tiny wrapper script per agent over deeply nested `tmux new-session "claude -p \"$(cat %q)\" ..."` command strings.
- Never use Python/printf `%q`-style placeholders unless you verify they are expanded before tmux receives the command. A literal `%q` caused `cat: %q: No such file or directory` and produced zero agent reports.
- Do not count a tmux pane existing as evidence of agent work. Verify output logs and required completion report files.
- If a launch is malformed, kill the tmux session and monitor process immediately to stop token burn.

## Safe pattern

1. Create prompt files under `prompts/`.
2. Create `scripts/run-agent-N.sh` files, one per pane:

```bash
#!/usr/bin/env bash
set -euo pipefail
PROMPT_FILE="/abs/path/prompts/agentN.md"
LOG_FILE="/abs/path/logs/agentN.log"
claude -p "$(cat "$PROMPT_FILE")" \
  --model claude-fable-5 \
  --max-turns 80 \
  --output-format text 2>&1 | tee "$LOG_FILE"
```

3. `bash -n scripts/run-agent-N.sh` for every wrapper.
4. Smoke one wrapper with a harmless prompt requiring a report file:

```bash
claude -p "Read this prompt and write /tmp/agent-smoke-ok.txt containing OK" \
  --model claude-fable-5 \
  --max-turns 3 \
  --output-format text
```

5. Only then start tmux panes:

```bash
tmux new-session -d -s fabled-five -c "$REPOS" "bash /abs/path/scripts/run-agent-1.sh"
tmux split-window -t fabled-five:0 -h -c "$REPOS" "bash /abs/path/scripts/run-agent-2.sh"
```

## Verification before reporting success

- `pgrep -fl 'claude -p'` shows expected commands, not malformed shell fragments.
- Each log file has real model output, not shell errors.
- Each agent writes its required `AGENT*_DONE.md` report.
- Final report count is nonzero and increasing.
- Git status shows expected file changes.

## Recovery pattern

If the launcher fails:

```bash
tmux kill-session -t fabled-five 2>/dev/null || true
process kill <monitor-session-id>
pgrep -fl 'claude -p' # inspect and kill malformed remnants if needed
```

Then switch to a cheaper/light OpenCode pass if the user wants to conserve Claude/Fable tokens.