# 10 · mechanism selection

These laws prevent agent count, model choice, and tool names from replacing the
actual design question.

---

## MECH-1: name the job before naming the tool

**Law.** A technology choice is meaningless until the job, user, value, data, and
failure mode are explicit.

A request framed as model or agent selection became clearer when rewritten as a
job: what decision must improve, what data exists, what risk matters, and who
reviews the result.

- Detect: the brief asks for a tool before it states the outcome.
- Fix: write the job-to-be-done and acceptance test first.
- Then choose process, script, model, or agent.

---

## MECH-2: deterministic work does not need an agent

**Law.** Use ordinary software for repeated rules, transformations, checks, and
file operations before introducing an autonomous loop.

Agents are expensive where the problem is already known. They are useful when the
system must choose tools, recover from uncertainty, or make bounded decisions.

- Detect: the agent repeats the same steps every run.
- Fix: turn the repeated core into a script or workflow.
- Leave the agent for exception handling, synthesis, and review.

---

## MECH-3: split agents for boundaries, not aesthetics

**Law.** Create another agent only for isolation, permissions, scale, independent
ownership, or adversarial review.

Many-agent designs often hide weak context architecture. A stronger catalog,
manifest, request slip, or tool registry can let one agent do the work more
transparently.

- Detect: personas exist because the prompt feels long or routing feels messy.
- Fix: improve the information architecture first.
- Split only when a boundary would remain useful if the models were humans.

---

## MECH-4: cost telemetry is part of the feature

**Law.** If a system spends model calls, credits, or human review time, the spend
must be visible at the workspace level and compared against the real non-AI
baseline.

Teams hesitate to onboard users when cost is guessed. Invisible spend also hides
bad design: agents doing deterministic work, reprocessing raw corpora, or
retrying ambiguous writes. Token price by itself is also the wrong denominator:
the alternative may be human search, manual review, existing software, local
indexing, cloud storage, latency, privacy exposure, or rework.

- Detect: nobody can say what one task, user, or workspace costs.
- Fix: record model calls, tool calls, runtime, retries, review time, latency,
  privacy exposure, and rework; record the manual or existing-tool baseline the
  system is replacing.
- Use total workflow cost to simplify architecture, not just token price.

---

## MECH-5: impressive metrics can be leakage

**Law.** A predictive signal is not legitimate until domain review and
counterfactual tests show it is not leakage, bias, or source artifact.

The more consequential the system, the less a leaderboard number matters by
itself. Strong validation can still be measuring an illicit shortcut.

- Detect: performance is high but nobody can explain what signal is being used.
- Fix: test perturbations, counterfactuals, and forbidden features.
- Escalate consequential judgments to qualified humans.

---

## MECH-6: model changes need truth decks, not vibes

**Law.** Repeated AI workflows need representative examples with expected
behavior, quality thresholds, latency targets, and cost targets before changing
models, prompts, or providers.

One-off demos made changes feel better than they were. A small truth deck turned
preferences into reviewable cases: inputs, expected output characteristics,
must-include items, must-avoid items, rationale, and acceptable tradeoffs. The
deck let the team compare quality, cost, and latency instead of relying on model
reputation.

- Detect: a model or prompt switch is justified by benchmark rank, anecdote, or a
  single polished answer.
- Fix: run a truth deck of local cases before and after the change.
- Verification: the change report names passed cases, failed cases, cost delta,
  latency delta, and accepted tradeoffs.

---

## MECH-7: automate only after the manual workflow teaches its boundary

**Law.** A workflow should graduate from human execution to markdown, templates,
scripts, model calls, agents, and integrations only when the previous level has
exposed a stable bottleneck.

Teams often reached for agents or integrations before they knew which steps were
judgment, which were copy-paste bridges, and which were deterministic rules. The
cheaper path was to write the workflow down, pressure-test it with a fresh
operator, then automate the smallest repeated bottleneck while keeping review
gates where accountability or taste still mattered.

- Detect: the proposed automation cannot name the manual step it replaces or the
  human decision it preserves.
- Fix: run the workflow from markdown and classify every step as judgment,
  transfer, deterministic helper, one-shot model call, agentic loop, or full
  integration.
- Verification: a second operator can reproduce the result from files, and the
  automation note records which simpler mechanism was rejected and why.

---

## MECH-8: choose the interface by required access

**Law.** Select chat, file workspace, IDE agent, terminal agent, script, or
custom runtime by what the worker must see, edit, run, persist, share, deploy,
and govern.

The same underlying model can be useful or useless depending on its interface.
A chat box may be enough for thinking; a file workspace is needed when the
artifact must become durable; an IDE or terminal agent is needed when the worker
must inspect a repo, edit several files, run checks, or commit; deterministic
scripts belong outside the agent path; custom orchestration earns its cost only
when product boundaries, permissions, scale, audit, or integrations demand it.

- Detect: the proposal names a vendor, model, or "agent" before naming required
  read, write, execution, persistence, collaboration, and governance access.
- Fix: write the access contract first, then choose the smallest layer that can
  complete the job and produce the acceptance proof.
- Verification: the mechanism note records the selected layer, the durable proof
  it can produce, and the simpler layer that was rejected with a concrete reason.

---

## MECH-9: physical parts start at the mating interface

**Law.** For functional 3D-printed parts, model the measured interface and keep
parametric CAD as the source of truth before exporting any mesh.

A plausible replacement part failed because it was generated from the visible
idea rather than the part it had to replace. The mesh preview looked printable,
but it did not encode the removed component's envelope, fastener pattern,
clearances, module cutouts, or build-plate limits. The useful workflow began
only after the job changed from "make a shape" to "replace this interface with
this function," then moved through catalog/part research, measured dimensions,
parametric source, validation, preview, slicer import, and printer-envelope
checks.

- Detect: the artifact is an STL or preview before the mating surface, purchased
  modules, clearances, material, and printer envelope are known.
- Fix: identify the original part family, choose the replacement function,
  measure fit-critical dimensions, expose them as top-level CAD parameters,
  validate the source, export the mesh, and verify the slicer-reported size.
- Generalizes to: adapter plates, delete panels, brackets, enclosures, switch
  panels, cable glands, jigs, fixtures, and any printed part that must mate with
  existing hardware.

---

## MECH-10: let AI translate structured human judgment before replacing it

**Law.** For subjective choices, collect concrete human reactions to artifacts
before asking AI to decide, generate, or optimize.

Ambiguous preference language became useful only after people marked specific
examples, anti-examples, likes, dislikes, and disagreement zones. The model's
best role was translation: summarize patterns, compare segments, surface
contested items, and turn taste into a shared decision language. When the model
generated first, it mostly increased output volume without improving judgment.

- Detect: the prompt says "make it better" but no one has captured what humans
  prefer, reject, tolerate, or find risky.
- Fix: show concrete artifacts, collect structured reactions with the prompt and
  audience segment attached, then ask AI to interpret the signal.
- Verification: the recommendation cites the reaction set, disagreement pattern,
  threshold or risk tolerance, and the human decision still required.

---

## MECH-11: sell the layer above the commoditized output

**Law.** Before building or selling an AI workflow, identify which layer a
vendor or model is likely to make cheap, then move durable value to workflow,
context, data, interaction, governance, or human judgment.

Teams lost leverage when they treated raw AI output or a thin wrapper as the
product. The useful move was to classify the abstraction layer first: raw output
could become acquisition, infrastructure, or a draft, while the protected value
sat in context-specific workflow maps, source data, review criteria, taste,
relationships, permissions, telemetry, and learning loops.

- Detect: the pitch depends on a generic feature that could become a button in a
  model provider, editor, office suite, design tool, or automation platform.
- Fix: run an abstraction-layer risk check; prototype at the cheapest sufficient
  layer, and charge for or protect the layer that contains local context and
  accepted-outcome learning.
- Verification: the project brief states the raw output, likely commoditized
  layer, defensible context, lower-layer validation prototype, and trigger for
  revisiting the bet after vendor changes.
## MECH-12: prove the chat baseline before building the product

**Law.** Before turning a workflow into custom AI software, test the cheapest
plain-chat version and build only the repeatability, data, control, and proof
layers that chat cannot provide.

A domain tool looked like an AI product, but the first useful result came from a
normal chat model plus a well-shaped profile and task prompt. Custom software was
justified only after the missing production layers were visible: source feeds,
editable reference tables, scoring, attachments, audit fields, controlled
runtime, and user-facing diagnostics.

- Detect: a proposed app cannot say what result a one-off chat prompt already
  gets right, or what repeated operation still fails after that baseline.
- Fix: run the chat baseline with representative inputs; record the missing
  data, repeatability, authority, privacy, scoring, editability, and review
  needs; implement the smallest layers that close those gaps.
- Generalizes to: intake assistants, opportunity matching, compliance triage,
  knowledge search, proposal drafting, support workflows, and advisory tools.

---

## MECH-13: source attempts are requirements, not noise

**Law.** When domain experts have already tried cheap tools, treat their rough
prompts, spreadsheets, screenshots, notes, and failed automations as the first
requirements corpus.

Generic AI services collapse when they sell the same answer layer the client can
now prototype alone. The durable design work starts by collecting those partial
attempts, extracting vocabulary and edge cases, and deciding what belongs in
manual process, deterministic rules, ordinary software, one-shot model calls,
agent loops, or governed integrations. The product is the higher layer of
implementation, controls, quality, personalization, telemetry, and adoption, not
the generic first draft.

- Detect: discovery produces slides or interviews but no source attempts,
  examples, mechanism map, or acceptance evidence.
- Fix: build a discovery workbench with source attempts, questions, mechanism
  classification, prototype slices, eval cases, and an implementation ledger.
- Verification: the brief states what the cheap baseline already did, which
  higher layer remains valuable, and how the business outcome will be measured.
## MECH-14: learn or delegate only against a valued bottleneck

**Law.** A tool, course, hire, script, model call, or agent earns attention only
when it removes a named bottleneck from a problem whose value is already clear.

Teams often treated learning a language, adopting an automation platform, or
outsourcing a task as progress by itself. The useful question was smaller: which
constraint blocks a valuable outcome, what is the scarce operator hour worth,
and which mechanism removes the constraint with the least total risk and cost?
Sometimes the answer was study; sometimes it was a checklist, a script, a model
call, a contractor, or doing nothing until a real buyer or user existed.

- Detect: the plan starts with a tool, tutorial, hire, or automation before it
  names the buyer or user, blocked outcome, opportunity cost, and acceptance
  proof.
- Fix: write the problem, value, bottleneck, current manual path, scarce human
  time, and rejected simpler mechanisms before investing in the tool or worker.
- Verification: the first accepted result proves a valued outcome moved, not
  merely that someone learned a stack or completed an outsourced task.

---

## MECH-15: route demand before building supply

**Law.** A marketplace, job board, community workflow, or service platform earns
software only after observed demand can be qualified, matched to capacity, and
accepted as proof.

Teams with attention and capable people often rushed to build the supply side:
roles, channels, automations, agent personas, or platform features. The useful
system started smaller: capture real requests, qualify the pain and acceptance
test, match the work to an operator role or reusable asset, deliver one bounded
artifact, and record whether the requester accepted it. Repetition then shows
which part deserves tooling.

- Detect: the plan starts with a board, marketplace, agent team, or training path
  before any qualified request, capacity match, or accepted artifact exists.
- Fix: create a manual opportunity board with request slips, capacity rows,
  reusable assets, delivery workbenches, and proof rows.
- Verification: the board routes at least one real request from raw demand to an
  accepted or rejected artifact, and the next automation target is the repeated
  bottleneck the board exposed.
## MECH-16: separate capability from permission

**Law.** An AI review must answer capability, permission, system boundary, and
responsibility as separate claims; a model that can do a task has not thereby
earned authority to do it.

Teams lose the thread when they argue whether "AI can" do something while they
mean whether it should be deployed, who is accountable, or whether the system's
inner life matters. The practical subject is the whole boundary: model, tools,
sources, deterministic code, prompts, validators, humans, logs, and rollback.

- Detect: the same discussion mixes "can it work," "is it allowed," "does it
  understand," and "who is responsible" without separate evidence.
- Fix: write four sections: observed capability evidence, ethics/risk judgment,
  model-tool-human boundary, and responsibility chain.
- Generalizes to: education, support, hiring, moderation, operations, creative
  work, and any AI-enabled system where human judgment or harm boundaries remain
  part of the product.
## MECH-17: bounded fuzzy judgments need decision gates

**Law.** Repeated model calls that only return a label, yes/no answer, score,
route, or readiness decision should be written as explicit decision gates with
thresholds, deterministic exclusions, and an override loop.

An expensive language-model step looked agentic because it sat inside a larger
workflow, but its actual job was only to sort an input into one of a few known
outcomes. The durable fix was not another persona or a longer prompt; it was a
folder-local decision file that named the question, allowed outputs, confidence
bands, exact checks that must stay in code, output location, and human review
path.

- Detect: the prompt asks for a category, routing choice, readiness score, or
  done/not-done judgment and then discards the prose around the answer.
- Fix: split exact work into scripts or validators; put the fuzzy bounded
  judgment behind a decision file; persist result records beside the source.
- Verification: low-confidence and overridden cases become review/eval examples,
  while high-confidence automatic action stays inside the authorized scope.
