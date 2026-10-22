# BOOTSTRAP: set this person up (for the agent)

You are an AI agent. A person gave you the link to this repo and wants the setup it describes. Follow
these steps in order. Talk to them in plain words; they may not be technical. Keep each message short.

**Ground rules for the whole bootstrap**
- Ask before anything that changes their machine in a big way (installing herdr, installing packs).
  Small, reversible steps (cloning this repo, linking skills, writing files under `~/.herdr-agent`) are
  covered by their request; say what you did.
- Never print, store or send their passwords, tokens or keys.
- If a safety system refuses a command, do not work around it. Show them the exact command to run
  themselves (in Claude Code they can type it after a `!`) and say why it is needed.
- Nothing is pushed, published or sent anywhere.

## Step 1. Get the kit

If you are not already inside a clone of this repo:

```sh
git clone <the link to this repo> ~/herdr-agent-bootstrap
cd ~/herdr-agent-bootstrap
```

(Use the link they gave you.) From here on, `<kit>` means this folder.

## Step 2. Check the machine

```sh
<kit>/scripts/doctor.sh
```

Read the output. Tell them in 3-5 lines what is ready and what is missing. If **git, python3 or node 20+**
is missing, help them install it first (Homebrew on macOS: `brew install git python node`). They need at
least one agent: Claude Code, OpenCode or Codex (you are probably one of them). Recommend OpenCode as a
free worker if it is missing (<https://opencode.ai>), but do not insist.

## Step 3. A short interview (2 minutes)

Ask these together in one message, with examples, and say every answer is optional:

1. **Your name** (what the agents should call you).
2. **What you do** - your work or business, in a sentence ("I run a bakery in Cape Town", "I'm a
   backend developer at a fintech", "I'm a student who builds games").
3. **Three things you'd like agents to do for you** ("keep my shop site up to date", "review my pull
   requests", "turn my notes into reports").
4. **Projects** - any folders or repos you work on (paths or GitHub names), and for each, who answers
   business questions and how it goes live, if they know.
5. **A colour you like** (for your demo site).
6. **House rules** - for each, yes/no (recommend the default in brackets):
   - No AI co-author/credit lines in commits and pull requests [yes]
   - Emails sent from your accounts say an AI wrote them on your behalf [yes]
   - No gradients in designs [their taste; no default]
   - Never push, deploy or send anything without your yes for that exact thing [always on]

Write their answers to `~/.herdr-agent/profile.json` (create `~/.herdr-agent` if needed):

```json
{ "name": "Sam", "work": "runs a bakery in Cape Town (Crumb & Co)",
  "goals": ["keep the shop site fresh", "post weekly specials", "track orders"],
  "projects": [{"name": "Crumb & Co site", "path": "~/Projects/crumb", "business_questions": "Sam", "deploy": "Netlify, push to main"}],
  "accent": "#b45309", "site_name": "Sam's agent team" }
```

`accent` is a CSS colour (`#hex` or a name like `teal`). If they skipped it, leave it out.

## Step 4. Install

Tell them what will happen, in one short list: herdr (if missing), the kit's skills linked into each
agent they have, a small marked block in each agent's global rules, `~/.herdr-agent/` files, and two
tools in `~/.local/bin`. Everything is undone by `./install.sh --uninstall`. Then:

```sh
<kit>/install.sh            # add --yes if they agreed to install herdr; --no-herdr if they declined
```

Then fill in `~/.herdr-agent/house-rules.md` from their interview answers: replace each `{{...}}`
(`{{NAME}}`, and `[x]`/`[ ]` for the yes/no rules), and add their projects under "My projects".

**Packs (optional).** Show `<kit>/scripts/install-packs.sh --list` in a few lines and suggest the packs
that fit their goals (design for websites, engineering for code, security for audits, documents for
office files, claude-mods if they use Claude Code). Install only the ones they pick:
`<kit>/scripts/install-packs.sh <pack> ...`.

**Images (optional).** If `doctor.sh` showed no image backend, explain the two options in
`docs/06-images.md` (Hermes + Codex sign-in, or an API key) and that the demo works without one.

## Step 5. Move into herdr

The demo must run inside herdr, because the lead starts workers in herdr tabs.

- If `HERDR_ENV=1` is set, you are already inside herdr: go to Step 6.
- Otherwise tell them exactly:
  1. Open a new terminal window.
  2. Run: `cd <kit> && herdr`
  3. In the herdr pane, start their agent (for example `claude`, `opencode` or `codex`).
  4. Say to it: **"Run the herdr-agent-bootstrap demo: read DEMO.md."**

  Restarting the agent inside herdr also loads the newly installed skills and rules. Stop here.

## Step 6. Run the demo

Read `DEMO.md` and follow it.
