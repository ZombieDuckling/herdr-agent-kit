# gate an action workflow

Use this before letting an assistant perform operational work against live or
current systems.

## 1. name the action class

Write the action as a concrete verb and object:

- triage messages;
- schedule a meeting;
- update a record;
- edit a repository;
- monitor an alert;
- publish an artifact.

Reject labels like "agent," "assistant," or "automation" as the action class.
Those are implementation choices, not the job.

## 2. fill the prerequisite gate

| layer | question | evidence |
| --- | --- | --- |
| procedure | What steps define correct work? | workflow note, checklist, runbook, examples |
| role/context | Whose priorities govern edge cases? | role file, policy, examples, rubric |
| source/access | What current source is authoritative? | connector, file manifest, API read, source map |
| permission | What may be changed without approval? | request slip, allowlist, approval record |
| verification | How will success be read back? | target read, diff, receipt, screenshot, log |

If a layer is missing, set the state to `blocked`, `offline`, or `read-only`
instead of asking the model to improvise.

## 3. classify the safe execution mode

- `blocked`: stop; record the missing prerequisite.
- `offline`: prepare a draft, plan, template, or source map only.
- `read-only`: inspect and summarize current state; do not write.
- `ready`: execute only the approved action scope.

## 4. choose the simplest mechanism

- Use a checklist or human step when judgment is still tacit.
- Use deterministic code for exact routing, validation, and formatting.
- Use a one-shot model call for bounded transformation or drafting.
- Use an agentic loop only when tool choice, retries, or multi-step state reading
  are necessary and gated.

Do not split into multiple named agents unless the split creates a real boundary:
permission isolation, ownership, scale, runtime separation, or user legibility.

## 5. execute with a receipt

For a ready workflow, record:

- request slip;
- sources read;
- tools used;
- writes attempted;
- target read-back;
- cost or quota when relevant;
- unresolved items.

A successful API/tool response is not sufficient. The workflow is complete only
when the target state or review artifact confirms the result.

## 6. convert misses into structure

If the assistant asked repeated clarification questions, guessed priorities, or
returned generic advice, update the missing layer instead of adding prompt prose.

Common repairs:

- add a role/context file;
- add examples and anti-examples;
- add a connector health check;
- narrow the request slip;
- add a read-back step;
- split a permission boundary out of the worker.
