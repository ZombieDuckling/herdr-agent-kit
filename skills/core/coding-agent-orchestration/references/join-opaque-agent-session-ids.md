# Joining opaque coding-agent session IDs

Session lesson from a short “Join <id>” request where the opaque ID was not a Codex saved session but Cursor Agent accepted it with `--resume`.

## Pattern

When the user says “Join <opaque-id>” without naming the tool, treat it as a request to attach/resume a coding-agent session, not as a new build task.

## Safe join ladder

1. Check obvious session managers if available:
   - `codex resume <id> --no-alt-screen` for Codex saved sessions.
   - `agent --resume <id> --workspace <path> --trust` for Cursor Agent sessions.
   - `opencode session list` / `opencode run --session <id>` patterns for OpenCode when relevant.
2. Use a PTY/background process for interactive resumes so the agent stays attached rather than exiting immediately.
3. Poll/read the process log once to confirm whether the session was actually found.
4. Report the joined process/session handle and which tool accepted the ID.
5. If one tool rejects the ID, do not turn that into a durable “session missing” conclusion; try the next likely agent before asking the user.

## Notes

- Codex short IDs may fail with “No saved session found” or Codex Cloud may return “Invalid task ID” for local/chat IDs. That only rules out that Codex namespace.
- Cursor Agent can resume short chat IDs with `agent --resume <id>` and may open an interactive prompt without producing much output; treat the running PTY as the joined session.
