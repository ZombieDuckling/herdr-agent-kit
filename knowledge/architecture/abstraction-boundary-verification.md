# abstraction boundary verification

Use this shape when a system combines public methods, prompts, tools, APIs,
models, hardware, data stores, and human review. The goal is not to explain every
layer in depth; it is to know which boundary can fail and how the next boundary
catches it.

## layer map

For the workflow under review, write one row per active layer:

- User-visible job: what the user thinks the system does.
- Interface: chat, UI, CLI, API, webhook, file drop, or scheduler.
- Context package: files, manifests, retrieved sources, examples, memories, or
  prompt assets loaded into the run.
- Instruction layer: system prompts, skills, routing files, policies, schemas,
  and tool-use rules.
- Deterministic layer: scripts, database queries, validators, parsers, build
  steps, and other rule-bound machinery.
- Model layer: model calls, sampling parameters, output contracts, confidence
  limits, and retry policy.
- Tool/API layer: external or side-effecting calls with permissions, inputs,
  outputs, and read-back checks.
- State layer: files, databases, queues, ledgers, caches, and durable receipts.
- Substrate layer: runtime, network, storage, hardware, clocks, process limits,
  and lower-level error correction.
- Human/accountability layer: owner, reviewer, approval boundary, acceptance
  criteria, and incident path.

Omit layers that truly do not participate, but do not omit a layer merely because
it is managed by a provider.

## boundary questions

For each edge between layers, answer:

- What object crosses this boundary?
- Is it instruction, data, evidence, state, authority, or a secret?
- What can corrupt it, stale it, truncate it, bias it, or reinterpret it?
- Which side owns validation?
- What is the cheapest independent check?
- What is the failure mode if the check is skipped?
- Where is the receipt stored?

## design rules

- Public methods may be auditable; secrets must stay outside the editable or
  exportable workbench.
- Model confidence is not a truth signal. Route exact, current, or stateful
  claims through sources, tools, tests, checksums, or read-backs.
- A prompt is an entry point into architecture, not the architecture. If the
  prompt carries state, policy, examples, and output rules by itself, split it.
- APIs are contracts. Record accepted inputs, outputs, permissions, errors,
  idempotency, and post-write readback before relying on them.
- Lower layers fail too. Clocks drift, storage corrupts, networks partition,
  caches stale, and hardware flips bits; boundary checks must assume substrate
  fallibility.
- Human review must inspect artifacts, diffs, source handles, or run receipts,
  not only the model's explanation of its own work.

## minimum artifact

Create a short boundary review with:

- Layer table.
- Boundary table.
- Secret/data/authority separation note.
- Verification path for every exact, current, stateful, or side-effecting claim.
- Open assumptions and the layer that owns each one.
- Acceptance statement naming which boundary checks passed.

Link the result from the workbench front desk or request slip so future sessions
reuse the same map instead of rediscovering the stack.
