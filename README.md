# herdr-agent-bootstrap

**Give your AI agent this link, and it sets you up with a team of agents you can watch, then proves it
by building you a personal website that teaches you how to use everything.**

```
Set me up from <the link to this repo>
```

Say that to Claude Code, Codex or OpenCode. It will:

1. **Check your machine** and install [herdr](https://herdr.dev) (a terminal workspace for AI agents),
   asking before anything big.
2. **Ask you a few questions**: your name, what you do, what you want agents for, your projects, a colour.
3. **Install the skills**: how to lead workers, how to work like a top model, how to check websites and
   code, how to generate images, how to survive usage limits, plus a law library of hard-won lessons.
4. **Write your house rules**: what agents must never do, how to report to you, what to ask you.
5. **Run the demo** inside herdr: a lead agent starts workers in visible tabs, each writes a page of your
   site, and the lead checks every page before accepting it. You get a local site, addressed to you,
   that explains your new setup using your own goals and projects as the examples.

Nothing is pushed, published or sent anywhere without your yes.

## What is inside

| Folder | What |
|---|---|
| `skills/` | 44 skills, grouped: **core** (orchestration, the Fable method, handover, OpenCode lead), **quality**, **assets**, **sites**, **research**, **making**, **hermes** |
| `packs.json` | Third-party packs installed from their source: design, engineering, security, cloudflare, documents, claude-mods, hermes |
| `knowledge/` | 80 laws, playbooks and checklists, and 35 operating lessons for running agents in herdr |
| `rules/` | The house-rules template and the small block added to each agent's global instructions |
| `docs/` | The guide, 13 chapters: also the source of the demo site |
| `demo/` | The demo: starter site (design system, page shell), worker brief template, tools that assemble and check it |
| `tools/` | `start-opencode-lead` (a free lead when you hit a usage limit), `codex-image` (no-key images via Hermes) |
| `install.sh` | The installer: `--dry-run`, `--yes`, `--no-herdr`, `--packs a,b`, `--uninstall` |

## By hand

```sh
git clone <the link to this repo> ~/herdr-agent-bootstrap
cd ~/herdr-agent-bootstrap
./scripts/doctor.sh          # what you have
./install.sh                 # install (asks before installing herdr)
herdr                        # then start your agent inside herdr and say: "Run the herdr-agent-bootstrap demo"
```

Remove it all with `./install.sh --uninstall` (your house rules are kept).

## Requirements

macOS or Linux, git, Python 3, Node.js 20+, and at least one agent: Claude Code, OpenCode or Codex.
OpenCode is recommended as a free worker. Image generation is optional (Hermes with a Codex sign-in, or
an OpenAI-compatible key); without it the demo uses SVG art.

## Credits and licences

The kit is MIT licensed. `knowledge/laws/` and its playbooks come from the agent-memory library (MIT).
`skills/assets/image-generation-workflow` is MIT. Skills marked `author: Hermes Agent` are MIT. Packs in
`packs.json` are installed from their own repositories under their own licences and are not
redistributed here.
