# Fabled Five launcher smoke-test pattern

Use this when a delayed Claude Code / tmux fan-out launcher will spend scarce model quota such as Fable 5.

## Lesson

A launcher can pass `bash -n` but still fail at runtime because the prompt-file expansion, quoting, or tmux command construction is wrong. In one session, a five-pane Fable 5 launcher passed syntax checks but launched malformed commands that emitted `cat: %q: No such file or directory`, creating panes without useful agent work.

## Required pattern

1. Write each worker prompt to a real prompt file.
2. Build the exact command that tmux will execute using robust shell quoting.
3. Before arming the five-agent run, execute one cheap smoke pane or one direct command with the same command-construction path.
4. Require the smoke worker to create a tiny completion artifact, for example `logs/smoke/SMOKE_OK.md`.
5. Verify the artifact from Hermes before launching the remaining panes.
6. Only then arm or start the full fan-out.

## Safe command construction

Prefer explicit prompt-file arguments or command substitution inside a quoted shell script over ad-hoc `printf %q` strings embedded in another templating layer.

Example shape:

```bash
prompt_file="$LOGDIR/prompts/worker-1.md"
log_file="$LOGDIR/worker-1.log"
claude -p "$(cat "$prompt_file")" --model claude-fable-5 --max-turns 12 \
  --output-format text >"$log_file" 2>&1
```

If using tmux, test the exact tmux send/new-window command on a smoke prompt first.

## Verification gate

Do not report a multi-agent run as productive unless at least one of these is true:

- per-agent report files exist and contain substantive summaries;
- git diffs/commits exist in the expected repos;
- test/build logs exist from the workers;
- tmux/log output shows successful command execution.

If reports are `0/N`, say so bluntly and stop the run rather than allowing token burn.
