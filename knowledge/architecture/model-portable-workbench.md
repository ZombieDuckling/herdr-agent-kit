# model-portable workbench

Use this shape when an AI workflow would be materially harmed if one hosted model,
IDE, chat surface, or provider account became unavailable or changed behavior.

The goal is not provider neutrality as a slogan. The goal is that the workbench's
state, rules, checks, and recovery path outlive any one runtime.

## minimum shape

| layer | artifact | purpose |
| --- | --- | --- |
| State | manifest, current-state ledger, artifacts | lets another runtime or human resume without the original chat |
| Contract | request slip, output schema, acceptance criteria | keeps model calls behind stable task boundaries |
| Deterministic core | scripts, rules, fixtures, validators | removes work the model should not be improvising |
| Runtime adapter | provider/model/tool notes | records the current engine without making it the architecture |
| Truth deck | representative inputs and expected qualities | compares model or prompt changes before adoption |
| Fallbacks | alternate runtime, local/manual path, safe-stop message | avoids outage-driven redesign under pressure |
| Verification | tests, review checklist, source links, receipts | proves the fallback produced acceptable output |

## design rules

1. Store the canonical instructions and current state in files or a database, not
   in a hosted chat.
2. Keep model choice configurable behind a task contract, schema, or routed
   request slip.
3. Move stable transformations into scripts, rules, or validation code before
   tuning prompts.
4. Maintain a small truth deck for repeated workflows before changing models,
   prompts, tools, or adapters.
5. Write down at least one alternate runtime and one local or manual continuation
   path for critical work.
6. Treat provider-specific features as accelerators. If they become required,
   record what equivalent artifact a different runtime would need.
7. Define the safe degraded state: what stops, what can continue, and what the
   operator or user is told.

## readiness questions

- Can a fresh runtime answer what to read, what to run, what to produce, and how
  to verify it without seeing the old chat?
- Which work would still be possible if the preferred provider, model, IDE, or
  chat surface was unavailable today?
- Which parts of the workflow are data, rules, validation, or review rather than
  model judgment?
- What evidence decides that a fallback result is good enough?
- What regression test would catch a model swap that is fluent but wrong?

## anti-patterns

- A runbook that says only "retry later" when the provider is down.
- A prompt that contains business rules no file, schema, or test records.
- A workflow where switching models requires rediscovering source structure.
- A local fallback that cannot access the source files or acceptance criteria.
- A degraded mode that silently lowers quality instead of changing status.
