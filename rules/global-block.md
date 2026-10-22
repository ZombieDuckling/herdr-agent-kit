## herdr-agent-bootstrap (shared agent setup)
- **House rules first:** read `~/.herdr-agent/house-rules.md` at the start of work. It wins over every skill.
- **Work like Fable 5.1:** unless you are Claude Fable 5.1 itself, load `fable-method` at the start of
  every task and follow its loop (orient → facts → plan → small steps → prove → report), loading the
  other `fable-*` skills at their step. For a one-line question, just answer.
- **Inside herdr** (`HERDR_ENV=1`) with work of more than one part: load `herdr-orchestration`. You are the
  lead; workers run in visible tabs. Leads also load `herdr-lead-mods` (plan usage) and, near a weekly
  limit, hand over to an OpenCode lead (`opencode-lead`, `~/.herdr-agent/kit/HANDOVER.md`).
- **Visual assets:** generate what you need (`image-generation-freely`), after checking it does not exist.
- **Audits and websites:** real scanners and a running-page check (`web-qa`, `sonarqube`), with numbers.
- **Stuck on a system that misbehaves:** search `~/.herdr-agent/kit/knowledge/laws/` for the symptom
  and `~/.herdr-agent/kit/knowledge/operating-lessons.md`.
