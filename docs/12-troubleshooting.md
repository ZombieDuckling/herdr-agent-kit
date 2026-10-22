# Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `herdr: command not found` after install | `~/.local/bin` not on PATH | `export PATH="$HOME/.local/bin:$PATH"` in your shell profile |
| The lead says it cannot start workers | It is not inside herdr | Start herdr in a terminal (`herdr`), then start the agent inside it |
| "nested herdr launch blocked" | `herdr` was run from inside a herdr pane | Do not; you are already in herdr |
| A worker tab sits at a trust prompt | First Claude run in that folder | `herdr agent send-keys <name> down enter`, or click "Yes" |
| A worker is `working` but nothing changes | Thinking loop | Interrupt it (`escape`), give one smaller step |
| An OpenCode worker "finished" but saved nothing | It wrote the file in its thinking and ran out of reply space | Brief: "plan in 10 lines, then use the write tool"; raise its output token limit |
| OpenCode uses a paid model | It reused the last model | Pin the model in `~/.config/opencode/opencode.json` (`agent.build.model`) |
| Everything is suddenly slow | The laptop slept, or the model server fell back to CPU | `pmset -g log | grep -i sleep`; `caffeinate -i -t 7200`; check the GPU |
| "Context size exceeded" far below the model's limit | The model server's shared cache is full | Fewer parallel slots or fewer workers |
| The agent refuses to install something | A safety system blocked a persistent change | Run the exact command it gives you yourself (in Claude Code: start the line with `!`) |
| The demo site has no generated images | No image backend set up | Expected: it uses SVG and CSS art. Set up a backend (see Images) and ask the lead to add art |
| `check-site.mjs` says "missing playwright" | Not installed in that project | `npm i -D playwright @axe-core/playwright && npx playwright install chromium` |
| A kit skill is not used | You already had a skill with that name | The installer keeps yours; rename one of them |
| You want it all gone | | `./install.sh --uninstall` (keeps your house rules) |

## Asking for help well

Tell your agent the symptom and say "use fable-debug". It will read the whole error, list causes, run
the check that separates them, and tell you what it found, with evidence. For a system that misbehaves,
add "check the law library in the knowledge folder".
