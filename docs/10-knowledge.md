# Knowledge

Skills say *how* to do a job. Knowledge says *what goes wrong* and why. The kit ships two libraries.

## The law library (`knowledge/laws/`)

80 laws, each a transferable rule plus the sanitised incident that produced it, in six chapters:

| Chapter | About |
|---|---|
| 02 control loops | Deadlocks, watchdogs, restart loops, circuit breakers |
| 03 host reality | The machine is not what the docs say: architectures, drivers, ports |
| 06 shipping | Getting work to users |
| 08 workbench architecture | Structuring an agent's working folders |
| 09 corpus and review | Big documents, review debt |
| 10 mechanism selection | Choose the mechanism before the agent |

`knowledge/laws/INDEX.md` lists every law; the demo site's Law library page makes them searchable.
Playbooks and checklists sit next to it in `knowledge/`.

A few laws, to give the flavour:

- **LOOP-3 · A restart loop is not a crash loop.** Read the signal and the period.
- **LOOP-5 · Every self-healing loop needs a circuit breaker.** And a hard stop.
- **LOOP-6 · A timed-out write is ambiguous.** It may have landed: re-read, never blind-retry.
- **MECH-2 · Deterministic work does not need an agent.** Use a script.

## Operating lessons (`knowledge/operating-lessons.md`)

35 rules from running a lead with many workers in herdr every day: briefing literal models, pinning
free models, why workers stall, waiting without polling, checking CI after a push, Mac sleep making
everything look slow, refusals being boundaries. Read it once; your agents read it when stuck.

Next: [recipes](11-recipes.md).
