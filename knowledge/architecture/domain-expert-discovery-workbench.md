# domain-expert discovery workbench

Use this shape when a team asks for an AI product, automation, or advisory
engagement and internal domain experts have already tried to solve pieces of the
job with cheap tools, spreadsheets, scripts, or manual workarounds.

The workbench turns those attempts into requirements and mechanism decisions. It
keeps discovery tied to implementation instead of letting the project become a
slide deck, generic chatbot, or workflow automation that the buyer can replace
with a subscription baseline.

## promotion rule

Start with the cheapest safe baseline: existing process, ordinary chat, office
tools, templates, or a thin script. Build a custom workbench only after the
baseline exposes repeatable gaps in data access, controls, quality, integration,
privacy, scale, or review.

## required surfaces

### front desk

Record the job without tool jargon:

- business outcome;
- user or reviewer role;
- current manual process;
- expected value and failure cost;
- available data and source classes;
- privacy, publication, and authority limits;
- first acceptance evidence.

### source attempts

Preserve rough attempts as evidence, not as polish:

- prompts and outputs;
- spreadsheets, forms, or exports;
- screenshots or redrawn examples;
- manual workaround notes;
- failed automations or scripts;
- domain vocabulary, exceptions, and objections.

Strip or isolate sensitive material before sharing the package. The transferable
record should say what kind of source attempt existed, not who produced it or
what private data it contained.

### questions and decisions

Maintain a Q&A/decision log that converts discovery into build choices:

- what the domain expert tried;
- what worked well enough;
- what failed and why;
- which assumptions remain open;
- which mechanism was selected or rejected;
- who must review or approve the result.

### mechanism map

Classify each step before implementing it:

| step | source evidence | mechanism | why not simpler | review gate |
| --- | --- | --- | --- | --- |
|  |  | manual / checklist / script / software / one-shot model / agent loop / integration |  |  |

The map should make it obvious where ordinary software and deterministic rules
carry the system, and where a model call is genuinely useful for language,
ambiguity, ranking, extraction, synthesis, or bounded tool choice.

### prototype slice

Build the smallest slice that proves the missing layer:

- one workflow stage;
- one representative input set;
- one output shape;
- one review surface;
- one cost/latency/reliability reading.

Do not scale the platform until the slice produces a business receipt.

### evals and truth deck

Keep representative cases separate from implementation code:

- baseline attempts;
- expected output characteristics;
- must-include and must-avoid rules;
- known edge cases;
- cost and latency targets;
- human review thresholds.

### implementation ledger

Record what changed and what remains manual:

- date or change id;
- source attempt or decision that caused it;
- changed files, rules, prompts, or process steps;
- verification evidence;
- remaining risks and manual checkpoints.

## anti-patterns

- Selling generic AI adoption before the job and baseline are known.
- Treating domain-expert attempts as messy anecdotes instead of requirements.
- Building an agent framework before separating manual, deterministic, software,
  model, and integration steps.
- Measuring success by artifact volume instead of time saved, errors reduced,
  adoption, revenue, compliance, or support-cost reduction.
- Hiding rules, source data, and decisions inside prompts that only the model can
  interpret.
