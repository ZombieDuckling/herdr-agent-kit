# Cursor-first / OpenCode / Claude rotation with real-app acceptance gates

Use this when the user explicitly asks to preserve Claude Code budget, or to rotate through agents until exhausted.

## Routing rule

1. **Cursor Agent CLI first** (`agent`, via Hermes `coding_agent(agent='cursor')` or direct tmux if needed).
2. If Cursor is exhausted/blocked, switch to **OpenCode**.
3. If OpenCode is exhausted/blocked, then use **Claude Code**.
4. State substitutions plainly. Do not silently call Claude Code when the user asked to preserve it.

## Cursor invocation notes

- Cursor CLI command is `agent`; verify with `which agent && agent --version` when challenged.
- In Hermes `coding_agent`, do not set Cursor `mode='ask'` for builders. Ask mode returns plans and blocks edits. Use agent/write mode (`force: true`, no `mode='ask'`) for implementation.
- Plan mode is useful first when the user asks for Cursor's planning, but immediately relaunch implementation agents in write mode.
- Use different Cursor models for parallel workstreams when available: runtime/install, publisher/auth/session, E2E/acceptance, hard review.

## Worktree fan-out pattern

- Commit or stash current integration state first.
- Create remote-backed or local worktrees per slice to avoid write races.
- Assign non-overlapping goals:
  - runtime/install packaging and native-module ABI
  - publishing/session adapter
  - onboarding/E2E acceptance
  - review gate
- Merge back serially; resolve package/main/preload/test conflicts by preserving the union of scripts/IPC/tests, not one branch wholesale.
- Hermes must rerun canonical verification after every merge; never trust worker self-report alone.

## Real-app acceptance gate pattern

For installable desktop apps with external-account side effects, use a gate stronger than unit tests:

1. Build/package the app.
2. Run installed-app smoke from the packaged binary, not just `electron .`.
3. Add an Electron-native E2E harness for onboarding and fake API publish/log assertions.
4. For real external publish, require either:
   - approved API token + author/account identifier, or
   - dedicated authenticated browser target (e.g. Chrome CDP) with challenge detection.
5. Stop on password/passkey/2FA/CAPTCHA/security prompts; ask the user to complete those manually.
6. After a claimed real publish, verify the returned/public URL or account-visible evidence before saying done.

## Pitfalls surfaced

- Cursor Ask mode can look successful but make no edits; relaunch in Agent/write mode.
- A normal logged-in Chrome window cannot be attached by CDP unless launched with remote debugging. Use a dedicated profile, never Default.
- Package-time native modules can pass tests but fail installed runtime. Separate Node ABI rebuild from Electron ABI rebuild and smoke the packaged app.
- Documentation can become stale after agents implement a once-gated path; search for old blocker strings like `dry_run`, `gated`, or stale API versions before final report.
