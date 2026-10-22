# Orchestrating in practice

The `herdr-orchestration` skill teaches the lead all of this. This page shows you what it does, so you
can read along in the tabs (or do it yourself).

## Start a worker in a visible tab

```sh
# a new tab in this workspace, in the project folder, without stealing focus
P=$(herdr tab create --workspace "$HERDR_WORKSPACE_ID" --cwd ~/Projects/bakery --label gallery --no-focus \
     | grep -oE '"pane_id":"[^"]*"' | head -1 | cut -d'"' -f4)

# a Claude worker on a cheaper model
herdr agent start gallery --kind claude --pane "$P" -- --model claude-haiku-5-5
herdr agent prompt gallery "$(cat .briefs/gallery.md)"

# or a free OpenCode worker: run it in the pane with its brief
herdr pane send-text "$P" "opencode run --auto \"\$(cat .briefs/gallery.md)\" 2>&1 | tee .briefs/gallery.log
"
```

## Watch without polling

```sh
herdr agent wait gallery --timeout 3600000; herdr pane read "$P" --source recent | tail -30
herdr agent read gallery --source visible      # a peek while it works
herdr agent list                               # every agent and its state
```

The lead runs the `wait` in the background and is woken when the worker finishes, so it does not burn
its own context checking every few seconds.

## Unstick a worker

| You see | Do |
|---|---|
| `blocked` | It is asking something. Read the pane, answer it (`herdr agent send-keys <name> enter`). |
| A folder-trust prompt in a new Claude tab | `herdr agent send-keys <name> down enter` |
| `working` but no new step for ~20 minutes | It is looping. `herdr agent send-keys <name> escape`, then a smaller brief. |
| A shell prompt instead of the agent | It exited. Read the error; start it again. |

## Write the brief

The brief is the only context a worker has. For literal models write it in Simplified Technical
English: numbered steps, one instruction per sentence, exact paths and commands, the expected output
of each, what not to touch, and a fixed report layout.

```
# Task: build the gallery page
## Facts (checked, do not re-check)
- Repo ~/Projects/bakery, branch site-v2. Photos are in public/photos (24 files).
## Rules
- Plan in 10 lines or fewer, then use your tools. Change only gallery.html and css/gallery.css.
- Do not run git push, any deploy command or rm -rf.
## Steps
1. ...   Expected: ...
## Report
CHANGED FILES / CHECKS (command -> result) / PROBLEMS
```

The full template is in `skills/core/herdr-orchestration/brief-template.md`.

## Close up

```sh
herdr tab close <tab-id>       # as soon as the result is verified
```

A tidy workspace shows you the two tabs that matter instead of twenty idle ones.

Next: [the Fable method](04-fable-method.md).
