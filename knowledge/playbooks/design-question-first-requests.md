# design question-first requests

Use this when a reusable prompt, skill, intake form, or agent workflow keeps producing plausible outputs that miss the real constraint.

## 1. Start from failures, not clever prompts

Collect three to ten real cases where the first answer was wrong, generic, or had to be corrected. For each case, record:

- the user's original request,
- the missing context,
- the question that would have exposed it,
- the source or file path needed,
- the acceptance signal that proved the final answer was useful.

If no real failures exist yet, keep the prompt local and provisional.

## 2. Separate intake from generation

Do not hide discovery questions inside a generation prompt. Write an explicit intake block with:

| field | purpose |
|---|---|
| goal | what outcome the user actually wants |
| audience or operator | who will use or judge the output |
| source set | which files, records, or examples are authoritative |
| constraints | budget, policy, style, interface, timing, or risk limits |
| unknowns | questions that must be answered before building |
| non-goals | what the workflow must not solve or touch |
| acceptance evidence | how the result will be reviewed |

## 3. Route before reading everything

Ask for or generate a compact file tree/source map before broad search. The request should say which paths to read first, which are background only, and which are forbidden or stale.

## 4. Gate output on intake quality

Before generation, the operator or agent must choose one:

- **ready** — enough context exists to execute;
- **ask** — a missing answer changes the mechanism or output;
- **assume** — proceed with a labeled assumption because the risk is low;
- **stop** — sources, authority, or acceptance criteria are insufficient.

## 5. Promote repeated questions into reusable structure

When the same intake question appears repeatedly, turn it into a request-slip field, template field, router entry, checklist item, or validation rule. Do not leave it as chat folklore.

## Verification

A question-first request works when:

- it changes the input quality before output generation;
- a fresh operator can explain why each question exists;
- irrelevant questions have been removed or moved to a narrower workflow;
- the final output cites the sources and acceptance criteria gathered during intake.

## Related laws

- [WB-1](../notes/08-workbench-architecture.md#wb-1-a-front-desk-is-part-of-the-product)
- [WB-4](../notes/08-workbench-architecture.md#wb-4-request-slips-beat-vague-prompts)
- [WB-6](../notes/08-workbench-architecture.md#wb-6-chat-is-not-durable-state)
- [SDLC-12](../notes/11-agentic-sdlc.md#sdlc-12-prompts-are-software-assets-not-comment-fields)
- [SDLC-13](../notes/11-agentic-sdlc.md#sdlc-13-turn-user-intent-into-a-traceable-outcome-contract)
