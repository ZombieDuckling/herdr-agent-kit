# run an abstraction-layer risk check

Use this before investing in an AI feature, workflow product, internal platform, or agency/service offer.

The check asks whether the proposed value sits at a layer that a model vendor, platform, or ordinary software feature is likely to commoditize, and whether the project should move up to a more context-heavy layer before building.

## procedure

1. **Name the raw output.** State the visible thing the user receives: page, report, answer, animation, classification, summary, extraction, routing decision, or automation.
2. **Name the buyer outcome.** Write the business or human result the output is meant to improve.
3. **Classify the layer.** Use the ladder below.
4. **Check commoditization risk.** Ask whether a general model, host platform, design tool, office suite, IDE, or automation tool could plausibly make the raw output a button.
5. **Find the defensible context.** Identify workflow nuance, private data, review criteria, relationships, taste, governance, integrations, compliance, or learning loops that cannot be supplied by a generic button.
6. **Choose the cheapest validation layer.** Test demand with a manual process, folder workbench, markdown spec, simple script, or one-shot model call before building a full application.
7. **Move value capture upward.** Decide what should become free/cheap infrastructure and what should be protected, sold, or governed.
8. **Record the bet.** Put the layer, rejected lower-layer prototype, risk, and acceptance proof in the project brief.

## layer ladder

| layer | value shape | typical risk | better bet |
|---|---|---|---|
| Raw output | text, image, page, extraction, generic answer | vendor feature or commodity model | use as acquisition, draft, or internal helper |
| Produced workflow | sequenced process, source map, edits, review, delivery | copied by better workflow tooling | encode domain-specific criteria and handoffs |
| Interactive workbench | user participates, edits, routes, resumes, reviews | UI wrapper if context is shallow | shared state, permissions, artifacts, and control surfaces |
| Learning system | captures preferences, failures, telemetry, decisions | bad data or weak governance | feedback loops tied to accepted outcomes |
| Human/domain layer | trust, relationships, taste, accountability, expertise | not scalable if undocumented | codify examples, boundaries, and review gates |

## red flags

- The proposal sells a generic prompt output.
- The moat is only a wrapper around another runtime.
- The customer outcome can be tested by a markdown/manual prototype, but the plan starts with a platform build.
- No one can name what private context or human judgment makes the workflow better than a commodity feature.
- The system does not record preferences, corrections, bottlenecks, or accepted outcomes.

## acceptance proof

A completed check should produce a short note with:

- raw output;
- buyer outcome;
- selected layer;
- likely commoditized layer;
- defensible context;
- cheapest validation prototype;
- what is intentionally free/cheap;
- what is protected or charged for;
- trigger for revisiting the decision after vendor/model changes.
