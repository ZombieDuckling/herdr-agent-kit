# The lead and its workers

You talk to **one** agent per project: the **lead**. The lead does what a good engineering manager does
and nothing else:

1. **Understands** what you actually want (and asks only what it cannot find out).
2. **Plans** the work, with the riskiest step first and a check for every step.
3. **Delegates** the labour to **workers**, each in its own visible herdr tab, with a precise written brief.
4. **Verifies** every result itself: reads the diff, re-runs the checks, looks at the output.
5. **Reports** to you: the result first, the numbers, what is not done, at most one question.

## Choosing the worker

The lead picks the cheapest worker that can do the job well.

| Worker | Good for | Cost |
|---|---|---|
| **OpenCode** on a free or local model | Mechanical, literal work: apply an exact edit, convert files, run a script and fill a table, run tests | Free |
| **Claude Haiku / Sonnet** | Contained coding with some judgement; writing; reviews | Low |
| **Codex** | Hard reasoning, vision (looking at screenshots), stubborn bugs | Medium; use one tight pass |
| **Claude Opus / Fable** | Design, judgement, the lead itself | High |
| **The lead, directly** | Anything irreversible or shared (push, deploy, database, email); short command chains | |

Rules of thumb:
- **Does it need judgement or eyes?** If not, a free worker does it.
- **Many small tasks beat a few big ones** for literal models.
- **Concurrency is limited by the model server.** A local model on one GPU serves one or two workers
  well. Cloud models take more. Start with 2 or 3 workers and watch.
- **Two failures, then switch** to a stronger worker with the same brief.

## What the lead never does without you

- Push, deploy, merge, publish, or send email.
- Spend money or use your accounts in a new way.
- Work around a safety refusal. It gives you the exact command and the reason instead.

## Why this works better than one agent

- **Context stays clean.** The lead keeps the plan and the conclusions, not thousands of lines of output.
- **Cost drops.** The expensive model thinks; free models type.
- **You can see it.** Every worker is a tab you can click into. Nothing is hidden.
- **Quality rises.** Every result is checked by someone who did not produce it.

Next: [orchestrating in practice](03-orchestrating.md).
