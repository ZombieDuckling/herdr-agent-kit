# production agent stack

An agent demo proves a user flow. It does not prove production readiness.

## decomposition rule

Do not review "the agent" as one object. Split the system into inspectable
layers and decide which layer owns each choice, failure, and piece of evidence.

## layers

### objective layer

Name the job before naming the worker:

- user or operating scenario;
- useful output;
- acceptance evidence;
- forbidden outcome;
- owner of final authority.

### model-call layer

Each model call should have a contract:

- prompt or context source;
- expected response shape;
- model/provider class and parameters when relevant;
- one-shot, staged, or loop position;
- cost and latency budget.

The model call is only one layer. If the rest of the stack is invisible, the
system is still a demo.

### orchestration layer

The controller must be explicit:

- human, script, scheduler, event trigger, queue, or model-chosen next step;
- branching rules;
- retry and timeout policy;
- concurrency and rate limits;
- state read and written between steps.

### protocol and connector layer

Every external boundary needs a contract:

- API, CLI, file system, database, browser, webhook, or protocol server;
- request and response schema;
- permission and secret boundary;
- tool allowlist;
- observable failure modes.

Review new protocol servers with
[the protocol boundary checklist](../checklists/protocol-boundary-review.md)
before treating them as agent tools.

### interface layer

The human-facing surface must show what the agent is doing and what it produced:

- file tree;
- current goal;
- tool activity;
- artifacts;
- status;
- errors;
- review actions.

### context layer

The context layer contains curated, source-linked state:

- front desk;
- manifest;
- decisions;
- problem index;
- tool registry;
- current request slip.

### execution layer

Execution can be deterministic code, one-shot model transforms, predictive
models, or bounded agents. Do not use an agent when a script is the right tool.

### parsing and data-processing layer

Unstructured model output cannot flow directly into business logic:

- parse to a schema;
- validate before use;
- store raw and parsed outputs separately when later audit matters;
- preserve source and transformation handles;
- fail closed on malformed output.

### governance layer

Governance defines:

- allowed data classes;
- allowed tools;
- approval boundaries;
- write permissions;
- retention rules;
- escalation paths.

### telemetry layer

Track:

- tool calls;
- tokens or credits;
- runtime;
- retries;
- failures;
- outputs written;
- user overrides.

No telemetry means no operating knowledge.

### validation layer

Validation proves outputs against the job:

- tests;
- lint or schema checks;
- source citations;
- screenshots;
- diff reviews;
- human approval.

Evaluation should include representative inputs, must-include and must-avoid
rules, acceptance thresholds, and regression checks before changing prompts,
models, connectors, or parsers.

### recovery layer

Production systems need recovery before they need more features:

- rollback;
- retry policy;
- circuit breaker;
- backups;
- incident log;
- manual override.

## promotion rule

Do not promote a demo until it can answer:

- who acted;
- what data was used;
- which tools ran;
- what changed;
- what it cost;
- how it was verified;
- how to undo or recover;
- what the system refused to do.
