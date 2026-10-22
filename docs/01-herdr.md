# herdr basics

[herdr](https://herdr.dev) is a terminal workspace manager for AI coding agents. Like tmux, a background
server owns real terminals, so they keep running when you close the window. Unlike tmux, it is
mouse-first and it *knows* which panes hold agents and what state each one is in.

## Install

```sh
curl -fsSL https://herdr.dev/install.sh | sh     # macOS and Linux
herdr --version
```

Windows, Homebrew and other options: <https://herdr.dev/docs/install/>. The kit's `install.sh` offers
to do this for you.

## The parts

| Part | Think of it as | Example |
|---|---|---|
| **Session** | The background server. You usually have one. | `herdr` attaches to it |
| **Workspace** | One project. Shown in the left sidebar with a roll-up of its agents' states. | "bakery-site" |
| **Tab** | A view inside a workspace. The kit uses one tab per agent. | "lead", "worker-gallery" |
| **Pane** | A real terminal inside a tab. Tabs can be split. | the lead's terminal |
| **Agent** | A coding agent herdr recognises in a pane: Claude Code, Codex, OpenCode and more. | state: working / blocked / done / idle |

## Everyday use

- **Start:** `cd` into a project and run `herdr`. It creates a workspace for that folder.
- **Start your agent in the pane:** `claude`, `opencode` or `codex`. herdr detects it.
- **Click everything.** Panes, tabs, workspaces and split borders are all clickable; right-click for menus.
- **Keys (optional):** prefix is `ctrl+b`, then `c` new tab, `v` split right, `-` split down.
- **Detach and come back:** close the window; the agents keep running. Run `herdr` again to return.
- **Agent states in the sidebar** tell you where to look: *blocked* means an agent is waiting for you.

## Integrations

```sh
herdr integration install claude      # also: codex, opencode, and others
herdr integration status
```

Integrations give herdr lifecycle state and native session restore for that agent.

## How agents drive herdr

Inside a herdr pane, `HERDR_ENV=1` is set and agents can control herdr with its CLI: create tabs, start
other agents, send them prompts, read their screens and wait for them to finish. That is what makes
the lead pattern possible. See [orchestrating](03-orchestrating.md) for the commands.

One rule: **never run `herdr` from inside a herdr pane** (nested launches are blocked) and never run
`herdr server stop` from an agent, because it would kill every agent at once.

Next: [the lead and its workers](02-lead-and-workers.md).
