---
name: agent-resource-hygiene
description: Use when agent/browser processes overheat a Mac.
version: 1.0.0
created_by: agent
---

# Agent Resource Hygiene

Use this skill when the user reports that the Mac is hot, fans are loud, agents feel runaway, browser automation has piled up, or long-lived local agent services are consuming too much CPU/disk/memory.

The goal is to cool the machine without breaking the healthy core services the user still needs.

## Core principles

- Separate **measurement** from **destructive cleanup**. Inventory first; kill/delete/disable only after scope is clear.
- Treat high `fseventsd` CPU as a symptom of filesystem churn, not necessarily the root cause.
- Look for disposable browser automation profiles under `/tmp` and agent-launched Chrome profiles with `--user-data-dir`.
- If a process respawns after being killed, find the `launchd` label or supervisor before repeated `pkill` loops.
- Preserve core Hermes/WhatsApp gateway unless the user explicitly wants it stopped.
- Prefer stopping optional surfaces or stale automation processes over parking all agent infrastructure.
- For scheduled daily cleanup reviews, produce one concise morning digest that includes cleanup actions, broken/stale surfaces, and ranked suggested tasks for the day; do not send separate voice notes or repeated routine pings unless the user asks.

## Diagnostic workflow

1. Snapshot load and hot processes:

```bash
uptime
ps -Ao pid,ppid,%cpu,%mem,state,etime,command | sort -k3 -nr | head -25
ps -Ao pid,ppid,%cpu,%mem,state,etime,command | sort -k4 -nr | head -25
```

2. Check system churn and thermal hints:

```bash
pmset -g ps 2>/dev/null || true
pmset -g thermlog 2>/dev/null || true
```

If thermal commands hang or are unavailable, do not dwell; process and disk churn are usually enough to act.

3. Identify disposable browser automation profiles:

```bash
ps -Ao pid,ppid,%cpu,%mem,etime,command | grep -- '--user-data-dir=' | grep -v grep
```

4. Size likely temp profiles and recent churn:

```bash
du -sh /tmp/hermes-* /tmp/*chrome* 2>/dev/null | sort -hr | head -30
find /tmp -maxdepth 2 -type f -mmin -30 2>/dev/null | head
```

5. If a hot process respawns, inspect launchd:

```bash
launchctl list 2>/dev/null | grep -Ei 'hermes|openclaw|claude|codex|chrome|agent'
find "$HOME/Library/LaunchAgents" /Library/LaunchAgents /Library/LaunchDaemons -maxdepth 1 -type f 2>/dev/null | grep -Ei 'hermes|openclaw|claw|agent'
```

## Cleanup workflow

Only after diagnosis and user approval:

1. Stop the smallest respawning service/surface, not everything.
2. Kill stale child/browser processes tied to the disposable profile.
3. Delete only disposable temp profiles after their owning processes have stopped.
4. Quarantine or disable broken optional jobs/surfaces when safe; never delete repositories, deliverables, credentials, skills, memories, or user data as part of a routine cleanup.
5. Re-check load and process table after 15-30 seconds.
6. Report what was stopped, what remains running, whether load dropped, and which broken items need approval before destructive action.

## Approval-safe sequencing

Avoid bundling too many destructive actions into one opaque command when approval guards are likely. Prefer:

1. non-destructive inventory command;
2. explicit user-facing summary of exact PIDs/paths/LaunchAgents;
3. one cleanup command with only the approved PIDs/paths;
4. separate verification command.

If a cleanup command is blocked by an approval timeout, stop and ask for renewed approval. Do not try the same destructive outcome through a different tool in the same turn.

## Prevention ideas

- Close or kill browser automation profiles after publishing/posting tasks complete.
- Do not leave temporary Chrome profiles running overnight unless needed for an authenticated session.
- For recurring checks, use a script-only cron watchdog that reports only when thresholds are exceeded.
- Keep long-lived agent gateways explicit and supervised; runaway respawn loops usually mean the LaunchAgent is the real control point.

## References

- `references/macos-agent-heat-triage-2026-07.md` — session-derived example: OpenClaw gateway CPU spike, Chrome temp-profile churn, and `fseventsd` as a write-storm symptom.
