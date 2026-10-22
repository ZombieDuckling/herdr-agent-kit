# 08 · workbench architecture

The repeated failure pattern is not a weak model. It is an environment that gives
the model no map, no source boundary, no request contract, and no review surface.

---

## WB-1: a front desk is part of the product

**Law.** Every agent-readable workspace needs one entry point that explains what
is here, what is canonical, what is mutable, and what to read first.

A folder of valuable material still failed onboarding because a fresh session had
to infer the workspace from filenames and stale chat. The fix was not another
agent. It was a front desk, catalog, and current-state ledger.

- Detect: the first question in every session is "what is this repo?"
- Fix: write a front desk file with purpose, entry points, status, and rules.
- Generalizes to corpora, client folders, research repos, and agent workbenches.

---

## WB-2: preserve the template and work in a copy

**Law.** Separate canonical context from mutable workbench state.

A reusable knowledge package becomes fragile when experiments, client-specific
edits, generated files, and source material all live in the same layer. Treat the
source package as a template and create mutable workbench copies for execution.

- Detect: edits needed for one task would pollute the baseline for the next.
- Fix: define template, workbench, generated artifact, and export layers.
- Verification: a disposable workbench can be deleted without losing the source.

---

## WB-3: multiplayer means shared artifacts, not shared vibes

**Law.** Collaboration requires shared files, visible state, identity,
permissions, and handoff; a chat room beside an agent is not multiplayer.

The useful product shape was a shared workspace where people and agents could see
the same files, continue each other's work, review outputs, and hand off without
sharing credentials or raw chat history.

- Detect: a second operator cannot answer what changed or where the output is.
- Fix: expose file tree, active requests, artifacts, decisions, and review state.
- Do not call it multiplayer until takeover works.

---

## WB-4: request slips beat vague prompts

**Law.** A task becomes operable when the goal, inputs, allowed tools, forbidden
actions, output, and verification are written before execution.

Vague prompts made agents optimize for plausible completion instead of the actual
job. Request slips turned intent into a contract that both the agent and reviewer
could check.

- Detect: the reviewer asks for a different thing than the agent built.
- Fix: write the request slip first, then execute against it.
- The slip is also the handoff object for the next operator.

---

## WB-5: the tool registry is the agent's API manual

**Law.** Tools need explicit contracts: input, output, side effects, failure
modes, and verification path.

An agent with many tools but no registry is forced to discover behavior by
experimentation. That is acceptable in a sandbox and dangerous in production.

- Detect: the agent chooses tools by name similarity or guesswork.
- Fix: write a tool registry before expanding tool access.
- Verification: the agent can state what a tool may change before using it.

---

## WB-6: chat is not durable state

**Law.** Decisions, current status, and artifacts must be written back to files or
a database; a chat transcript is not a workbench memory layer.

Long sessions felt productive until a fresh session had to reconstruct state from
conversation history. Durable ledgers made the work resumable and reviewable.

- Detect: pausing work requires summarizing a chat by hand.
- Fix: keep current state, decisions, artifacts, and blockers in the workspace.
- Fresh-session recovery is the test.

---

## WB-7: secrets are integrations, not files

**Law.** Credentials and provider access belong in a governed integration layer,
never in the editable or exportable workspace.

Agent-readable folders are copied, summarized, exported, zipped, and sent. A
secret placed there becomes source material. The safer design is a tool boundary:
the agent can request an action without reading the credential.

- Detect: a workspace export could include a key, token, cookie, or private URL.
- Fix: store secrets outside the workspace and expose only governed tool calls.
- Verification: export and search the workspace for secret-shaped material.

---

## WB-8: the review surface is a first-class component

**Law.** If a human must judge the work, the system must produce a reviewable
artifact, not just hidden files and a confident summary.

The useful outputs were the visible ones: source tables, rendered documents,
spreadsheets, screenshots, diffs, and ledgers. If the reviewer cannot inspect it,
it is not done.

- Detect: success is reported, but the human has no artifact to inspect.
- Fix: define the review surface in the request slip.
- Verification: the artifact opens, renders, and points to its evidence.

---

## WB-9: build context layers around workflows, not around everything

**Law.** A useful second brain is a workflow-specific context layer, not a
general note dump.

A broad knowledge folder became more useful only after it was narrowed around one
high-value operation and split into source material, derived signal,
instructions, decisions, outputs, and protected boundaries. The structure made
the important paths obvious enough that a fresh operator did not need to reread
all raw material or infer the workflow from chat.

- Detect: the agent must scan raw notes repeatedly before knowing what matters.
- Fix: create a front desk and workflow folder that separates sources, derived
  notes, instructions, decisions, outputs, and non-exportable integrations.
- Verification: a fresh session can answer what to read, what to run, and what
  not to touch for that workflow without opening the whole archive.

---

## WB-10: successful dialogue is source code for the next workflow

**Law.** When a chat, meeting, or transcript repeatedly produces useful work,
extract its goal, constraints, examples, decisions, commands, and verification
into durable workflow files instead of preserving the conversation as the tool.

The working method was hidden in the back-and-forth: a correction narrowed the
real goal, examples established taste, a permission boundary changed the action,
and the accepted output revealed the test. Future sessions did not need the whole
dialogue; they needed the compact procedure and artifacts the dialogue exposed.

- Detect: a fresh operator must replay an old conversation to reproduce an
  accepted result.
- Fix: mine the dialogue into a request slip, routing note, skill, examples,
  action log, and verification checklist.
- Verification: a fresh session can perform the same class of work from a short
  request plus the files, while naming which constraints and examples it used.

---

## WB-11: try position-addressed memory before semantic memory

**Law.** When a workflow has known stages and human-editable artifacts, encode
memory first in folders, filenames, manifests, local routers, and templates; add
semantic retrieval only after that map fails.

A useful operating memory did not require a new vector store before it had a
stable path structure. The path itself carried the client, stage, source class,
derived note, output, and review expectation. Once those positions existed, a
fresh operator could continue the work from the front desk and manifest without
replaying the chat or searching every raw source.

- Detect: the proposed memory layer cannot explain what a path, manifest row, or
  local routing file will not already provide.
- Fix: create the front desk, canonical manifest, staged folders, templates, and
  source/derived/output separation first.
- Escalate: use explicit links for maintained relationships and semantic search
  for large or irregular corpora, but keep provenance and review handles.

---

## WB-12: export the workbench, not the hosted session

**Law.** The durable value of an AI-assisted asset workflow is the reusable file
package: source map, routed instructions, examples, components, helpers, and
review outputs.

Hosted design or content tools can spend many credits discovering the same asset
library again and again. The transferable system records what was learned into a
portable workbench so another capable file-reading runtime can continue without
depending on the original chat, UI, or provider-specific import.

- Detect: recreating the same deck, page, document, or visual output requires
  re-uploading and reinterpreting the same sources.
- Fix: export a package with a front desk, manifest, source shelf, examples,
  anti-examples, reusable components, deterministic helpers, and review surface.
- Verification: a fresh runtime can produce a new artifact from the package and
  identify the source assets it used.

---

## WB-13: route context in three layers before building agents

**Law.** Start file-aware AI workflows with a compact front desk, task-room
routers, and active workspace files before adding personas, custom apps, or
agent swarms.

A team kept reaching for more specialized agents because each task needed a
different prompt bundle. The simpler fix was a three-layer folder router: the
root file explained the workspace, each workflow folder named what to read and
skip, and active files held briefs, assets, drafts, outputs, logs, and checks.
The same capable worker could then enter the right room instead of loading the
whole house.

- Detect: the same session repeatedly pastes giant context, or new agents exist
  only because the folder cannot say where the task belongs.
- Fix: write a routing table with columns for trigger, read-first files, allowed
  helpers, protected paths, output location, and verification.
- Escalate: add scripts, databases, custom UIs, or separate agents only after the
  routed folder fails on a repeated, named bottleneck.

---

## WB-14: make the spec the control surface for generated artifacts

**Law.** For generated media, pages, decks, reports, and code-backed visuals,
separate source, human-readable spec, generated source, rendered output, and
review notes before accepting the artifact.

An impressive first generation became hard to edit because the prompt, intent,
implementation, timing, and output were collapsed into one step. The durable
control surface was the plain-language spec: it stated the audience, beats,
meaning, timing, assets, acceptance criteria, and review gates while leaving
implementation freedom until the first build existed.

- Detect: a small requested edit causes the system to regenerate the whole
  artifact or forces the reviewer to spelunk generated code.
- Fix: create a staged workbench: source brief, spec or PRD, generated source or
  components, render/export, and review ledger.
- Verification: a fresh worker can change one named beat, section, scene, or
  component by reading the spec rather than replaying the original chat.

---

## WB-15: build control surfaces over workflows, not over vibes

**Law.** A useful AI interface exposes the workflow map, files, active requests,
review artifacts, and human/agent handoff state; it is not just a prettier chat
wrapped around a runtime.

A custom interface was tempting because the existing runtime was powerful but
hard to navigate. The safer design was not to duplicate authentication,
provider calls, or execution infrastructure. It was a local control surface over
the real workspace: folders, specs, editors, chats, commands, outputs, and a
clear indicator of who is driving each stage.

- Detect: the proposed UI adds another agent/runtime but cannot name which file,
  stage, handoff, or review action it makes clearer.
- Fix: map the real pipeline first, then add panels and controls for opening,
  editing, running, reviewing, taking over, and handing back work.
- Verification: another operator can enter the interface, see current stage and
  artifacts, decide whether human or agent is driving, and resume without hidden
  chat context.
## WB-16: shallow feedback is not governance

**Law.** Consequential AI work needs an affected-user route from informed
deliberation to decisions, prototypes, implementation evidence, and outcome
checks; a survey or advisory chat is not enough.

A product team treated user feedback as legitimacy while the real decisions still
flowed from builders and sponsors. The transferable fix was a governance
workbench: representative roles, onboarding material, facilitated discussion,
proposal drafting, lightweight prototypes, explicit tradeoff ranking, and a
decision ledger that shows what changed and why.

- Detect: the team can show comments but cannot link them to accepted, rejected,
  or deferred product decisions.
- Fix: create a participatory workbench with participant roles, source material,
  proposals, ranked tradeoffs, decision records, and eval cases.
- Verification: shipped specs, issues, commits, or roadmap items cite the
  governance input, and later checks measure whether participation altered the
  system.

---

## WB-17: domain AI literacy teaches boundaries, not buttons

**Law.** When adoption depends on expert judgment, teach the domain's use and
non-use boundaries before teaching tool operation.

Generic AI training made people faster at prompting while leaving the hard
questions unanswered: which tasks should remain human-only, which outputs require
review, which fundamentals must still be practiced manually, and which examples
define acceptable local work. The transferable shape is a community workbench
with role-covered practitioners, examples and anti-examples, a boundary map,
assistant roles tied to artifacts, and an evidence loop showing what changed.

- Detect: learners can operate the tool but cannot say where AI is forbidden,
  assist-only, review-required, or safe to automate.
- Fix: build a domain literacy workbench with a use-boundary map, preserved
  fundamentals, workflow rooms, artifact ledger, and learning loop.
- Verification: a fresh practitioner can defend an accepted artifact and point to
  the boundary, reviewer role, examples, and implementation evidence behind it.
## WB-18: branch discussions from artifacts, not from vibes

**Law.** A collaborative AI branch must name its parent artifact, target section,
edit contract, diff, and merge decision; otherwise it is only another chat.

Document-centered collaboration failed when agents and humans discussed changes
without preserving which part of the artifact they were changing or how the
result would return to the source. The useful shape treated a branch like a
small reviewable workspace: it inherited context from a source discussion,
targeted a bounded section, produced a diff or proposal, and waited for an
accept/reject/merge decision before mutating the canonical artifact.

- Detect: a participant cannot say which document section a side discussion is
  editing, what changed, or whether the output has been merged.
- Fix: create branch records with parent artifact, source section, role/output
  contract, changed sections, reviewer, decision, and merge receipt.
- Verification: a fresh operator can trace every branch back to a source
  section and inspect the accepted diff before the source artifact changes.
## WB-19: every consequential workbench has a governance surface

**Law.** When a workspace can shape identity, access, money, reputation, safety,
infrastructure, public decisions, or sensitive data, map its governance surface
before treating it as a product.

A shared AI system looked like a collaboration layer, but the important boundary
was power: who could enter, read, edit, execute, export, delete, approve, or
override; which sources and providers could influence outcomes; and which humans
were accountable when the system affected other people. The fix was a short
governance-surface section in the brief plus explicit role, data, source,
provider, audit, and rollback ledgers.

- Detect: the project is described as "just a chat" or "just a workspace" while
  it changes decisions, access, commitments, or sensitive records.
- Fix: add actors, data classes, tool/action rights, source rules, provider
  dependencies, audit logs, affected-user representation, abuse paths, and
  rollback owners to the workbench design.
- Generalizes to agent products, collaborative document systems, customer-facing
  automations, cyber-adjacent workflows, and AI-assisted governance processes.
## WB-20: model relationships as files before adding retrieval

**Law.** A second brain becomes operational when its nouns and verbs are
addressable: teams, roles, workflows, inputs, outputs, and the relationships
between them.

One note pile could not answer basic workflow questions because it stored prose
about work but not the work's structure. The useful map named the entities first,
then the verbs between them: consumes, produces, reviews, blocks, hands off to,
and approves. Only after those files existed did heavier graph or retrieval tools
have something reliable to index.

- Detect: the agent can quote notes but cannot say who owns a workflow, what it
  consumes, or where the output goes.
- Fix: create entity, workflow, relationship, evidence, and open-question files
  with confidence and freshness fields.
- Verification: a fresh operator can trace one workflow from trigger to accepted
  output without scanning the whole archive or inferring relationships from
  prose.
## WB-21: encode opinion as portable context

**Law.** Defensible judgment must leave the expert's head as principles,
examples, anti-examples, decision rules, and review criteria that any approved
runtime can inspect.

As generic agent harnesses became easier to copy, the valuable layer was not the
wrapper around the model. It was the situated taste, standards, vocabulary,
references, and refusal boundaries that made the output non-generic. Capturing
that layer in plain files made it portable across chat, file workspaces, coding
agents, local models, and future tools.

- Detect: the operator must join every run to restate taste, priorities, or what
  "good" and "bad" mean.
- Fix: create an opinion layer with principles, examples, anti-examples,
  hard constraints, edge cases, decision logs, and acceptance rubrics.
- Verification: a fresh worker using the folder can produce or review aligned
  work and cite the judgment files it used.
## WB-22: make the workbench portable before the runtime fails

**Law.** Critical AI workflows need portable state, alternate runtimes, and a
manual or deterministic continuation path before the preferred model or provider
goes down.

The fragile pattern was not using one strong hosted model. It was letting the
hosted chat, IDE, or provider feature become the only place where instructions,
state, and acceptance criteria existed. When the runtime changed or disappeared,
the workflow stopped because there was no independent workbench to resume from.
The durable unit is the file package: sources, request slips, rules, artifacts,
truth deck, verification, and fallback runbook.

- Detect: an outage, rate limit, model swap, or UI change would leave only a chat
  transcript and a hope that the same tool comes back.
- Fix: keep state and rules in files or a database, put model calls behind stable
  contracts, and name the hosted, local, scripted, and manual fallback paths.
- Verification: a different capable runtime or a human can continue the task
  from the workbench and pass the same acceptance checks.
## WB-23: verify the boundary between layers

**Law.** A layered AI/software workflow is trustworthy only when each boundary
states what crosses it, who validates it, and which independent check catches a
bad transfer.

Useful systems expose simple menus: an API call, a prompt, a file path, a button,
or a public method. Failures hide in the edges between those menus and their
lower layers. A model may sound confident because a phrase is statistically
familiar, an API may accept a write that later fails, a prompt may mix
instructions with untrusted source text, and the runtime beneath all of it may
drop, stale, or corrupt state. Treat each layer boundary as a contract instead
of assuming the layer below is correct.

- Detect: a review asks whether “the AI” is right without naming the source,
  tool, state, parser, runtime, or human boundary that would catch a failure.
- Fix: map interface, context, instruction, deterministic, model, tool/API,
  state, substrate, and human-review layers; label what crosses each edge as
  instruction, data, evidence, state, authority, or secret; add the cheapest
  independent check for exact/current/stateful/side-effecting claims.
- Verification: the workbench can show which boundary checked the claim and
  where the artifact, read-back, test, checksum, source handle, or human
  acceptance receipt lives.
## WB-24: creative artifacts need source lanes, not just final renders

**Law.** For AI-assisted creative work, preserve the source/spec, asset
provenance, generated takes, deterministic finishing steps, and review notes
beside the final artifact.

A generated image, animation, deck, or short video can look persuasive while the
important questions live elsewhere: which sources were used, what was generated,
what was edited deterministically, what use is allowed, and which claims were only
visible-quality judgments. A blind comparison can test whether viewers can tell
outputs apart, but it cannot approve authorship, licensing, consent, originality,
or deployment context.

- Detect: the only durable output is a rendered file, screenshot, or hosted
  session link.
- Fix: keep a programmable media workbench with brief, source assets, scene/spec
  or prompt chain, components, render/export command, generated takes, review
  notes, and allowed-use status.
- Verification: a fresh operator can distinguish perceptual quality,
  provenance, transformation, allowed use, and final execution proof without
  reopening the original tool session.
## WB-25: connectors are the sync plane, not the workbench

**Law.** A connector protocol is useful only after the workspace has a template,
mutable copy, permission boundary, import/export manifest, secret boundary, and
review surface.

An access layer can make a folder reachable from several clients, but reachability
is not collaboration. Without a defined source template and active copy, clients
edit unclear state. Without an org or workspace boundary, context crosses scopes.
Without export and review surfaces, the handoff is still trapped in a hosted
session. Without secret isolation, the shared folder becomes a credential leak.

- Detect: the design says it is connector-enabled before it can name canonical
  source, active workbench, scoped actors, export contents, and review artifacts.
- Fix: build the workbench first, then expose a scoped sync/auth endpoint around
  it.
- Verification: a second approved client can read the same current files, make a
  permitted edit, export the package, and fail to access another workspace or
  any credential material.
## WB-26: action requests need prerequisite gates

**Law.** Before an assistant performs operational work, the workbench must expose
the procedure, role context, source access, permission boundary, and read-back
verification path.

A clear command like "check the inbox" or "update the record" is not one task.
It hides at least five prerequisites: how the work should be done, whose
priorities apply, which current source is authoritative, what writes are allowed,
and how the result will be proven. Without those layers the assistant either
guesses, stalls on clarifying questions, fabricates access, or returns generic
advice while sounding useful.

- Detect: the agent asks the same priority/access questions repeatedly or claims
  it can act without a live source and permission boundary.
- Fix: add an action-prerequisite gate with procedure, context, source,
  permission, and verification fields before execution.
- Verification: the workflow can declare `ready`, `read-only`, `offline`, or
  `blocked` before acting, then read back the target state after any write.
## WB-27: follow-up is an architecture review, not a satisfaction survey

**Law.** After a workbench, training, pilot, or agent workflow reaches real use,
inspect the changed system and its evidence before claiming value.

A passive "how did it go?" follow-up misses the durable lesson. The useful
review walks the current workflow, compares it to the original promise, records
direct and follow-on outcomes, names blockers and failure modes, and routes the
learning into templates, checks, scripts, archives, or backlog items.

- Detect: reports mention meetings, usage, or enthusiasm but cannot name what
  workflow changed, what artifact proves it, or what reusable asset improved.
- Fix: run an outcome review with an architecture map, evidence table,
  failure-mode ledger, owner, and next verification target.
- Verification: a second operator can explain what changed, what failed, what
  evidence supports the value claim, and which reusable component was updated or
  queued.
