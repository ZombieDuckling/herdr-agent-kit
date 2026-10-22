# Operating lessons: running agents in herdr

Lessons from months of running a lead agent with many workers in herdr, every day, on real client and
personal work. Each one cost real time once. They are written as rules with the reason, so your agents
do not pay for them again. The law library in `knowledge/laws/` is the deeper, more general version.

## Orchestration

1. **One lead per project, workers in visible tabs.** The lead plans, briefs, verifies and reports.
   Workers do the labour, each in its own herdr tab so the human can watch. Headless workers that the
   human cannot see feel like nothing is happening, and nobody notices when one hangs.
2. **Cheapest capable worker first.** Free or local model (OpenCode) for mechanical work, a small paid
   model (Haiku or Sonnet) next, a strong model (Codex or Opus) only for real reasoning or vision. Ask
   "does this need judgement or eyes?" before spending.
3. **Many micro-tasks beat a few big ones** for literal models. "Convert these 40 images", "apply this
   exact edit to this one file", "run this script and fill this table". Big vague tasks stall.
4. **Concurrency is limited by the model server, not by herdr.** A local model on one GPU box serves
   one or two conversations well. Five workers on it is slower than two. Measure before you fan out.
5. **Brief from a file, never inline.** The shell expands backticks and `$` in inline text. Write the
   brief to a file and pass `"$(cat brief.md)"`.
6. **Agent names are lowercase** letters, digits, `-` and `_`. An uppercase name fails silently later.
7. **Answer the folder-trust prompt** when a new Claude tab starts in a new folder
   (`herdr agent send-keys <name> down enter`), or the worker waits forever.
8. **Wait without polling.** Run `herdr agent wait <name>` in a background job that prints the pane
   tail when it ends. Polling every few seconds wastes the lead's context and money.
9. **A "working" worker with no new tool call for about 20 minutes is looping.** Interrupt it and give
   it one smaller step.
10. **Close tabs when the result is in.** Twenty idle tabs hide the two that matter.

## Briefing literal (local) models

11. **Simplified Technical English:** numbered steps, one instruction per sentence, exact paths and
    commands, the expected output of each, what to do when it differs, what not to touch, a fixed
    report layout. "Do not guess causes; do not recommend."
12. **"Plan in 10 lines, then use your tools."** Local models often write the whole file inside their
    thinking, run out of reply space and save nothing. Say it in every brief. A one-line nudge
    ("stop planning, use the write tool now") usually rescues a stuck one.
13. **Raise the reply-token limit** for local models that write files (32k instead of 8k) if the server
    allows it. Many "it never saved the file" failures are this.
14. **Pin the model.** Some agent UIs reuse whichever model was used last. Pin the free model in the
    agent's config so a worker does not drift to a paid cloud model.
15. **Two failures, then switch.** One nudge is fine. A second failure or a 15-minute stall without
    writing: give the same brief to a stronger worker.

## Verification

16. **A worker's "done" is a claim.** Read the diff. Re-run its checks. Count things yourself.
17. **Check the running thing, not only the source:** console errors, links that 404, buttons with no
    listener, axe accessibility, phone width. A static scanner and a live page each miss what the
    other catches.
18. **Run real scanners for audits** (SonarQube or eslint with sonarjs; semgrep) and report numbers.
    Baseline what is house style; fix what is a defect.
19. **Check CI after a push,** not only the local gate. Local green and CI red happens often.
20. **"Which version is live?" is a fingerprint question.** Compare bundle hashes or version strings
    of the live site with each candidate build. The newest commit is often not what is deployed.
21. **Vision is scarce; use it once, well.** One strong visual review at the end beats many weak ones.

## Hosts and tools

22. **Before blaming the model server for slowness, check whether the laptop slept**
    (`pmset -g log | grep -i sleep` on macOS). Closed lids and sleep make every agent look slow.
    `caffeinate -i -t 7200` keeps a Mac awake during long runs.
23. **zsh does not word-split `$var`.** Use `${=var}` in zsh, or run loops under bash.
24. **Never use `/model` inside a Claude session** to change a worker's model: it rewrites the global
    default for every new session. Pass `--model` when you start the worker.
25. **GPU servers fail open to CPU.** A kernel update can silently break the GPU driver; the model
    still answers, just 20 times slower. "Slow" is often "on CPU".
26. **Context errors far below the model's limit** usually mean the server's shared KV cache is full
    (too many parallel slots), not that the prompt is too long. Lower the parallel slot count.
27. **A refused action is a boundary, not a puzzle.** When a safety system blocks an action (installing
    persistent jobs, editing credentials, merging your own pull request), do not route around it. Give
    the human the exact command to run themselves (in Claude Code, a line starting with `!`) and why.
28. **DNS and some account settings can only be changed in the provider's dashboard** with the tokens
    most people have. Say so early instead of trying five API calls.
29. **Codex quirks:** it sometimes self-updates and exits on launch (start it again), and "model at
    capacity" leaves work uncommitted (start a new Codex on the same folder with another model and a
    brief naming the uncommitted files).

## Working with the human

30. **Decide small reversible things yourself.** Ask only about money, access, commitments to other
    people, irreversible actions and taste questions the house rules do not answer. Ask once, all
    questions together, with a recommendation.
31. **Never push, deploy, merge or send without a "yes" for that exact action.** An earlier yes for
    something else does not count.
32. **Report the result in the first line**, then numbers, then what is not done, then one question.
33. **Route questions to the person who owns the answer.** A client's business questions go to the
    client (by email, with the AI disclosure), not to the developer.
34. **Long-lived leads degrade.** Give the lead tripwires (context size, compactions, mistakes) and let
    it hand over to a fresh session before quality drops (`lead-handover` skill).
35. **Watch the plan usage, not only the work** (`herdr-lead-mods`). Near the weekly limit, hand the
    workspace to a free OpenCode lead (`opencode-lead`) instead of stopping.
