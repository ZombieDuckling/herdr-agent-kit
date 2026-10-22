# House rules

Your preferences, written down once, binding every agent. They live in `~/.herdr-agent/house-rules.md`,
and every agent's global rules say to read them first. They win over any skill.

## What goes in

- **About you:** your name, how you like reports, how much the agents should ask you.
- **Safety:** nothing pushed, deployed or sent without your yes; no secrets printed; refusals are not
  worked around.
- **Credit and disclosure:** for example no AI co-author lines in commits; an AI disclosure on emails
  sent from your accounts.
- **Taste:** for example no gradients; real photos first; honest copy; reduced motion respected.
- **Workers and cost:** cheapest capable worker first; workers visible; everything checked.
- **Your projects:** one line each: folder, who answers business questions, how it deploys, its traps.

The bootstrap agent fills it in with you in a few questions. Edit it any time; agents read it fresh at
the start of each task.

## How the rules reach every agent

```
~/.claude/CLAUDE.md                 <!-- herdr-agent-bootstrap:start --> ... <!-- ...:end -->
~/.config/opencode/AGENTS.md        same block
~/.codex/AGENTS.md                  same block
~/.hermes/AGENTS.md                 same block
            |
            v
~/.herdr-agent/house-rules.md       your rules (the block says: read this first)
```

The block is small and marked, so `./install.sh --uninstall` removes it cleanly and your own text in
those files is never touched.

## Memory

Claude Code also keeps per-project **memory** files (facts it learned: where things are, what broke
before, what you prefer). House rules are for preferences that apply everywhere; memory is for facts
about one project. Tell your agent "remember that ..." for memory, "add to my house rules that ..." for
rules.

Next: [knowledge](10-knowledge.md).
