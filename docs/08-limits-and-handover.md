# Limits and handover

Two things quietly ruin long agent sessions: **running out of plan usage**, and **a lead that has been
running so long it starts to slip**. The kit handles both.

## Watch the plan usage (`herdr-lead-mods`)

Install the Claude Code mods (`./scripts/install-packs.sh claude-mods`). Two lines appear above the
prompt: **usage-meter** (5-hour and 7-day plan usage, reset time, session cost) and **agent-radar** (one
line per running subagent or background command). The lead reads them from its own pane:

```sh
herdr pane read "$HERDR_PANE_ID" --source visible | grep -E '5h|7d|session'
```

| 5-hour usage | The lead |
|---|---|
| under 75% | works normally |
| 75-90% | starts no new paid workers; free workers only |
| 90%+ | lets running work finish, notes where it stopped, tells you the reset time |

And it ends every report with `Usage: 5h 42% (resets 16:00) · 7d 30% · session $3.10 · running: 2`.

## Near the weekly limit: an OpenCode lead takes over (`opencode-lead`)

At 90% of the **weekly** limit, the Claude lead writes a handover file and starts a free OpenCode lead in
the same workspace:

```sh
start-opencode-lead <workspace-id> <project-folder> ~/.herdr-agent/handover/<workspace-id>-handover.md
```

The OpenCode lead follows the Fable method, keeps notes as its memory, runs at most one or two workers,
uses Codex for anything visual, and never pushes without you. When Claude is back, the Claude lead reads
its notes, checks its work, and takes over. Details: `HANDOVER.md`.

## A tired lead replaces itself (`lead-handover`)

Opt a workspace in (`echo $HERDR_WORKSPACE_ID >> ~/.claude/handover/workspaces`) and register the
`canary.sh` hook (see the skill). The lead then has **tripwires**:

| Canary | Warn | Trip |
|---|---|---|
| Live context size | 350k tokens | 500k tokens |
| Context compactions | | 1 |
| Its own recorded mistakes ("strikes") | 2 | 3 |

When one trips, the lead finishes the step, writes a handover document from checked state, starts its
successor in a new tab, waits for it to confirm, and retires. The same tripwires bind every successor.

Next: [house rules](09-house-rules.md).
