# Skills

A **skill** is a folder with a `SKILL.md`: a name, a one-line description of *when* to use it, and the
instructions. Agents read the descriptions all the time and load a skill's full text only when a task
matches. Skills are how you teach an agent a procedure once and have it followed every time.

## Where they live

| Agent | Skills folder | Global rules file |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `~/.claude/CLAUDE.md` |
| OpenCode | `~/.config/opencode/skills/` | `~/.config/opencode/AGENTS.md` |
| Codex | `~/.codex/skills/` | `~/.codex/AGENTS.md` |
| Hermes | `~/.hermes/skills/` | `~/.hermes/AGENTS.md` |

The kit's installer links its skills into every one of these that exists, and adds a short block to
each rules file. Your own skills with the same name are never overwritten.

## The kit's skills (vendored)

| Group | Skills |
|---|---|
| **core** (how agents work) | herdr-orchestration, herdr-lead-mods, lead-handover, opencode-lead, coding-agent-orchestration, merge-reconciler, agent-resource-hygiene, and the nine fable-* skills |
| **quality** | web-qa, sonarqube, document-to-test-automation, repository-audit, github-issue-to-pr, github-cross-repo-triage, autonomous-github-maintenance |
| **assets** | image-generation-freely, image-generation-workflow, dev-asset-generation |
| **sites** | client-site-design, client-site-polish-qa, static-demo-portfolio-publishing, photography-portfolio-sites, awwwards-site-production |
| **research** | long-form-research-reports, plain-technical-explanation, rubric-driven-assignment-packs |
| **making** | 3d-print, cad-to-print-delivery, fdm-print-production, openscad-parametric-generation |
| **hermes** (Hermes only) | kanban-orchestrator, kanban-worker, session-librarian, hermes-image-generation-routing, knowledge-ingestion-memory-systems, email-outbound-operations |

The full searchable catalogue with every description is on the demo site's Skills page.

## Third-party packs (installed from their source)

```sh
./scripts/install-packs.sh --list
./scripts/install-packs.sh design engineering security
```

| Pack | From |
|---|---|
| design | juliobsz/skills (awwwards, jury), pbakaus/impeccable, ui-ux-pro-max, vercel-labs/agent-skills |
| engineering | obra/superpowers, garrytan/gstack, get-shit-done |
| security | trailofbits/skills |
| cloudflare | cloudflare/skills |
| documents | anthropics/skills (docx, pptx, xlsx, pdf) |
| claude-mods | usage-meter and agent-radar plugins for Claude Code |
| hermes | Hermes Agent itself |

Packs stay with their authors: their licences, their updates (`npx skills update`).

## Write your own

```
~/.claude/skills/my-deploy/SKILL.md
---
name: my-deploy
description: Use when deploying the shop site. Runs the cache-bust script, pushes, checks the live URL.
---
1. Run ./cachebust.sh <tag>. Expected: "stamped N files".
2. ...
```

Good skills: a description that says **when** to load it; numbered steps; exact commands with expected
output; what not to do; how to check it worked. Ask your agent to "turn what we just did into a skill".

Next: [images](06-images.md).
