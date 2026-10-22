# Agent Global Skill Defaults

Use this when the user asks for a behavior or skill to apply across all coding agents by default, not just one project or one session.

## Procedure

1. **Inspect the source skill/repo first.** Read its README and any per-agent manifests so you use the native install path instead of guessing.
2. **Install through each supported agent's plugin mechanism.** Prefer plugin/marketplace install when the repo supports it because it carries manifests, versions, and enablement state:
   - Claude Code: `claude plugin marketplace add <repo-url>` then `claude plugin install <plugin>@<marketplace>`.
   - Codex: `codex plugin marketplace add <owner>/<repo>` then `codex plugin add <plugin>@<marketplace>`.
3. **Also write global context pointers.** Put the always-on rule in the files each agent reads every session:
   - Claude Code: `~/.claude/CLAUDE.md`
   - Codex: `~/.codex/AGENTS.md`
   - OpenCode: `~/.opencode/AGENTS.md` and `~/.config/opencode/AGENTS.md` when both exist or may be used
   - Hermes: active `$HERMES_HOME/AGENTS.md`, not another profile's home
4. **Copy standard skill folders where the agent reads them.** For open Agent Skills repos, copy the relevant `skills/<name>/` directories into:
   - `~/.claude/skills/`
   - `~/.codex/skills/`
   - `~/.opencode/skills/`
   - active `$HERMES_HOME/skills/`
5. **For OpenCode, prefer skill folders unless the repo documents a plugin path.** Its CLI has plugin support, but many Agent Skills repos document OpenCode as folder-based; follow the repo's own support matrix.
6. **Verify activation, not just file writes.** Read back the global context files, confirm the skill folders exist, and run plugin list commands where applicable:
   - `claude plugin list`
   - `codex plugin list`
   - `opencode --help` / `opencode plugin --help` only to confirm the mechanism, then verify the context files/folders actually used
   - `skills_list` for Hermes-visible skills
7. **Record the durable preference in the governing orchestration skill only if it changes how future agent fan-outs should be run.** Use memory only for broad user identity/preferences; workflow belongs in skills.

## Anti-slop default for the user

The user's preferred anti-slop posture is during-work, always-on filtering: every agent output should reject generic AI/vibe-coded slop, placeholder proof, fake stats, weak copy, non-working controls, mobile overflow, purposeless decoration, and unverified claims. Do not pause every task to ask whether it applies; apply it by default and load extra topical anti-slop skills when UI, copy, accessibility, mobile layout, or code comments are involved.

## Pitfalls

- **Do not edit another Hermes profile when installing global defaults.** Resolve the active `$HERMES_HOME`; profiles have isolated skills, memory, and AGENTS files.
- **Do not paste the whole skill into every global context file.** Keep the pointer short and install the skill folders/plugin separately, otherwise context bloat makes every coding-agent invocation more expensive.
- **Do not treat a successful clone as installation.** The repo cache is only a source; the agent must have a plugin entry, skill folder, or global pointer in its own home.
- **Do not overwrite existing global instruction files blindly.** Preserve existing content and replace only the managed block for the shared default.
