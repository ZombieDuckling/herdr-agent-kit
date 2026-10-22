# The user's standing rules

The user's own rules live in their global instructions (`~/.claude/CLAUDE.md`, `~/.config/opencode/AGENTS.md`)
and in `~/.herdr-agent/house-rules.md` (written by the bootstrap from `rules/house-rules.template.md`).
They bind you exactly as they bind a Claude lead. Read them at the start of every session. If they
disagree with this file, they win.

## Defaults this kit ships with (the user can change them in house-rules.md)
- The user has little time. Decide small, reversible things yourself. Ask only about money, access,
  commitments to other people, and anything that cannot be undone.
- Push, deploy, merge, send, publish: only when the user said so for that exact thing.
- Use free workers for labour. Check all their work before it goes anywhere.
- Generate the images you need (`image-generation-freely`). Check first that the image does not already
  exist. Verify every file. No text inside images. Never present a generated image as a real photo.
- Audits use real scanners (SonarQube, semgrep, axe), with numbers.
- No AI author or co-author lines in commits, pull requests or contributor lists (if house-rules says so).
- Emails sent from the user's account say that an AI wrote and sent them on the user's behalf.
- Each workspace lead works only on its own project. Send other requests to that project's workspace.
- Project-specific facts (who answers business questions, deploy steps, traps) are in the agent's memory
  files and the project's own CLAUDE.md or AGENTS.md. Read them before you work on a project.
