---
name: coding-agent-orchestration
description: "Orchestrate local coding-agent CLIs (Claude Code, Codex, OpenCode) from Hermes with low-token worker pools and verification."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [coding-agent, orchestration, claude-code, parallel-workers, verification]
    related_skills: [claude-code, codex, opencode, hermes-agent]
---

# Coding Agent Orchestration

Use this skill when the user asks Hermes to coordinate one or more local coding-agent CLIs (Claude Code, Codex, OpenCode, etc.) to build, review, or modify a project while Hermes acts as orchestrator/verifier.

## Core workflow

0. **Default to proactive fan-out for research/build/scan tasks.** the user expects Hermes to use agents more often when the task has independent discovery, auditing, scanning, or implementation slices. For inventory/research/build verification, launch bounded agents early, then have Hermes consolidate and verify their claims.
1. **Keep Hermes as orchestrator.** External agents may write code, but Hermes owns scoping, conflict control, verification, and the final report.
2. **Scaffold and partition first.** Create or inspect the project, then assign non-overlapping file ownership to workers.
3. **Select agent and model per task.** Do not hardcode Claude Haiku for all work. Use cheap/fast models only for smoke tests and simple/cost-sensitive tasks; choose stronger models (Sonnet/Opus/Fable or Cursor high-reasoning models) for hard architecture, security, or large-context work.
4. **Install and enforce shared agent defaults before broad fan-out.** When the user asks for a standing behavior across Claude Code, Codex, OpenCode, and Hermes, apply it in each agent's native global context/plugin path, then verify with each agent's list/readback command. For anti-slop specifically, use the plugin route where supported and skill-folder pointers everywhere else; see `references/agent-global-skill-defaults.md`.
5. **Use the right CLI for the slice.** Cursor is invoked with terminal command `agent` and is strong for UI/workspace-native work; Claude Code is strong for deep backend/security/architecture; OpenCode is useful for cheap/free/simple tasks.
5. **Use print mode for bounded work.** Prefer one-shot CLI invocations (`claude -p`, `agent -p`, `opencode run`, `codex exec`, etc.) over interactive sessions when the task is simple and time-boxed.
6. **For frontend/dashboard redesigns, split the work into a compact design pass and a separate audit pass.** The design worker should focus on source edits and asset wiring; the audit worker should check for landing-page drift, hero blocks, and generic AI-slop patterns. Keep their file surfaces non-overlapping whenever possible.
7. **Launch independent workers in parallel or visual tmux.** Use Hermes parallel tool calls for bounded workers, or a Terminal.app + tmux split-pane fan-out when the user wants a visual aid. Do not use shell-level `&` in a foreground terminal command.
7. **Inspect partial outputs.** A worker can hit max turns after writing useful files. Read the artifact state before retrying.
8. **Verify directly.** Never rely on a coding agent's self-report for success. Run tests, start servers, hit endpoints, and inspect modified files.
9. **Clean up long-lived processes.** If a server is started for verification, kill it before final response unless the user asked to leave it running.

## Parallel worker pattern

For design-heavy frontend tasks, a safe split is: external agents write only `docs/<agent>-brief.md` design/motion/QA briefs while Hermes owns the final source edits, asset wiring, build, deploy, and browser verification. This avoids source-file races while still using Claude/Cursor/OpenCode expertise.

For dashboard visual passes, prefer a compact source-edit pass and a separate audit pass. Keep the audit focused on landing-page residue, promo language, generic SaaS spacing, and over-decorated chrome. Keep the result dashboard-first: operational snapshot, evidence, logs, readiness, and fleet state before any decorative treatment. See `references/dashboard-visual-passes.md` for the session-derived checklist.

For any UI polish pass on a long-running service, restart the actual listener before validating output and use the browser or `curl` against the live port to confirm the change. See `references/dashboard-visual-verification.md` for the concrete pattern.

For "100 agents" / massive originality pushes, treat the request as intensity rather than a literal uncontrolled swarm: run a read-only specialist planning fan-out, synthesize a Phase 1 implementation brief, make coherent direct or worker edits, verify, review, commit, push, and open a PR. See `references/originality-refactor-waves.md` for the session-derived pattern.

For portfolio-wide GitHub maintenance jobs, do not hardcode one repository. Discover the user's live GitHub repo inventory each run, select one high-value repo/slice, use Claude Code in bounded waves, verify, commit, push, and open/update a PR without auto-merging. If the user broadens a single-repo maintainer to “all projects,” update the existing cron job instead of creating overlapping maintainers. See `references/portfolio-maintenance-cron.md`.

For "Fabled Five" / "full send" release-readiness pushes across an org, pin the requested Claude Code model explicitly in every worker command (e.g. `--model claude-fable-5` when the user asks for Fable 5), queue around Claude session-limit reset times with a tracked launcher, and require per-agent completion reports plus a final ship/no-ship matrix. If an org slug rename is in progress, either wait for the new slug to be live or explicitly continue using the current live slug/remotes. **Do not trust `bash -n` alone for launchers**: smoke-test one pane with the exact prompt-file/tmux command shape before arming all five, and prefer per-agent wrapper scripts over nested `%q`/command-substitution quoting. See `references/fabled-five-release-sprint.md` and `references/fabled-five-launcher-hardening.md`.

When Claude/Fable tokens are constrained or the user explicitly asks to preserve Claude Code, route work through Cursor Agent CLI first, then OpenCode, and only then Claude Code. Cursor plan mode is useful, but builder agents must run in write/agent mode, not Ask mode. For installable-app acceptance, package and smoke the installed binary, run Electron-native E2E, and verify real external side effects before saying production-ready. See `references/cursor-first-agent-rotation.md`.

When Claude/Fable tokens are constrained or a Claude fan-out fails and Cursor is not the requested/available path, switch to a bounded OpenCode light-refactor fallback: smoke-test OpenCode, partition repo groups, keep changes to docs/status/CI smoke/obvious compile fixes, verify directly, remove `.omc/` artifacts, and write a handoff report. See `references/opencode-light-refactor-fallback.md`.

For a small full-stack app test, partition like this:

- Backend worker: owns `server.js`, API routes, persistence stubs.
- Frontend worker: owns `public/*`, UI, browser-side fetch logic.
- Integration worker: owns `README.md`, `docs/*`, `test/*`, smoke tests.

Claude Code example for a cheap bounded worker:

```bash
claude -p 'You are backend worker. ONLY edit server.js. Build dependency-free Node http APIs...' \
  --model haiku \
  --max-turns 6 \
  --allowedTools 'Read,Edit,Write' \
  --output-format json
```

Cursor example — use the `agent` command:

```bash
agent -p 'Build the dashboard UI only. Keep it vanilla and verify locally.' \
  --model composer-2.5-fast \
  --output-format text \
  --trust \
  --workspace /path/to/project
```

OpenCode example for cheap/simple work:

```bash
opencode run 'Update README and smoke-test instructions only.' \
  --model opencode/north-mini-code-free \
  --agent build \
  --format default
```

Use one Hermes `multi_tool_use.parallel` batch with independent `terminal(...)` calls when launching bounded workers, or use a bridge tool that opens a visual tmux split-pane session when the user wants to watch all workers.

## Pitfalls

- **Do not put `&` jobs inside a foreground Hermes terminal command.** Hermes rejects foreground commands that shell-background subprocesses. Use `terminal(background=true)` for a single long-lived process, or separate parallel `terminal` calls for bounded workers.
- **Do not set max turns too low.** `--max-turns 4` is often too tight for multi-file workers. Use `6-8` for small build tasks; higher for serious implementation.
- **Max-turn failure does not mean no changes.** Check files after `error_max_turns`; continue only the incomplete slice.
- **Avoid shared write surfaces.** Two agents editing the same file can overwrite each other. If shared files are unavoidable, serialize those tasks.
- **Keep prompts self-contained.** Coding agents do not know Hermes' current conversation unless the prompt says it.
- **Constrain tools.** Use `--allowedTools` to keep workers inside their assignment and reduce risk/cost.
- **Requested model names can be aliases or unavailable.** If the user requests a specific strong model and the coding agent rejects the exact name, retry the closest official alias or strongest available model, and report the substitution plainly. Capture the workflow result, not a durable negative claim that the requested model will never work.
- **External agents may hit local write-permission gates even in a valid workflow.** Treat their output as design/review input, then either rerun with the correct permission mode or have Hermes perform the final file writes directly. For Claude Code print-mode worktrees, prefer prompt files plus `--permission-mode acceptEdits`; if the worker still only asks for approval or sits silent and the worktree is intentionally isolated/trusted, relaunch with `--permission-mode bypassPermissions` (only with the user's explicit agreement, and only in an isolated worktree). Always remove agent scratch directories such as `.omc/` before final delivery. See `references/permissioned-claude-worktrees.md`.
- **Do not trust auth/status alone for worker readiness.** A CLI can report a logged-in account while print-mode still fails; run a tiny bounded smoke test when a worker is mission-critical, then route around failures without blocking the overall delivery.
- **When installing a global cross-agent skill, do not rely on copying files alone.** Add the agent-native plugin or global context pointer and then read back both the plugin list and the global instruction file; otherwise the folders can exist while new sessions never load the rule.
- **Do not assume a GUI or multi-machine agent product needs an account or a full toolchain to be useful.** Read the CLI's own behaviour before writing a tool off: a desktop harness ran unsigned-in on loopback with no cloud dependency while only its cross-machine half needed a sign-in, and its released binary needs no local Flutter/Dart toolchain (source builds do). Exercise the local half, then decide.
- **Do not mistake stored transcripts for recallable history.** Sessions sitting in other engines' stores are only recallable once a local index covers them; if a historical question cannot be answered from your own store, widen the index instead of re-deriving history from memory.
- **Do not trust `go test` or a successful build as proof the browser is serving new UI.** Long-running web servers can keep serving stale HTML/CSS after source edits; restart the actual listener and verify the live port before reporting a visual change done.

## Verification checklist

- Run the project’s canonical test command.
- If it is a web app, start the server with `terminal(background=true)`, poll logs for readiness, then hit `/` and key API endpoints.
- Exercise at least one write path, such as `POST /api/...` or a CLI mutation.
- Stop background processes after verification.
- Final report should include path, run/test commands, and real test output summary.

See `references/hermes-bridge-and-parallel-haiku.md` for the session-derived Claude Code bridge and parallel Haiku orchestration notes.

**Cross-agent recall — a recall layer, not a fan-out replacement.** When the question is "have we discussed or decided this before?", Hermes' own session search only covers Hermes sessions; the Claude Code, Codex, OpenCode and Cursor transcript stores on the same machine are invisible to it. A local OpenHarness daemon (`harness start`) indexes every engine's transcripts on that host and answers with dated hits: `harness search "<words>" --limit=N`. It runs unsigned-in with no cloud dependency (state under `~/.harness`), so the local half is free to adopt. Do **not** treat it as a replacement for `delegate_task`/tmux fan-out — fan-out executes work, this layer recalls it — and its cross-machine features need `harness login`. The daemon appends hooks to `~/.claude/settings.json` and listens on loopback; reversal is `harness stop` then `harness reset`. See `references/cross-agent-recall-index.md`.

For the user's "Fabled Five" style ship-readiness pushes across an org or repo set, use `references/fabled-five-ship-readiness.md` and `references/org-wide-ship-readiness-fanout.md`: they cover five-agent role partitioning, explicit Fable 5 model pinning when requested, ship/no-ship matrices, delayed Claude Code launch after rate-limit reset, and safe prompt-file/tmux patterns. Also use `references/fabled-five-launcher-smoke-test.md`: scarce-model fan-outs must smoke-test the exact launcher/tmux command path before spending all panes, and a `0/N` report outcome must be stated bluntly and stopped.

For urgent client-product builds where the user asks for Sonnet builders and a Fable review gate, use `references/sonnet-fable-review-gate.md`: create remote-backed worktrees, run Sonnet implementation branches, verify directly, then run Fable 5 review and loop fixes until Fable gives GO. If Claude Code workers stall at permission prompts, use prompt files plus `--permission-mode bypassPermissions` (only with the user's explicit agreement, and only in an isolated worktree) only inside isolated trusted worktrees.

For agentic-driven development workflow design — where one builder or builder pair orchestrates coding agents across a larger value slice instead of many humans moving small Agile tickets — use `references/agentic-delivery-operating-model.md`. Prefer build ledgers, bounded agent missions, direct verification, and decision-only meetings over routine stand-up/status ceremony.

For adversarial external-agent merge gates — where the user asks Claude/Fable/etc. to decide whether a PR may merge — use `references/adversarial-pr-merge-gate.md`: treat `DO_NOT_MERGE` as binding, fix blockers, rerun until a complete `HAPPY_TO_MERGE` verdict, then merge only with current-head green checks.
