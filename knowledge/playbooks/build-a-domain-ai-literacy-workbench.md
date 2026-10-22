# build a domain AI literacy workbench

Use this when AI adoption depends on practitioners learning judgment and shared
standards, not merely a new tool interface.

## 1. qualify the need

Run this playbook when at least one condition is true:

- practitioners are overwhelmed by AI tool churn;
- adoption requires trust from domain experts or reviewers;
- the domain has fundamentals that AI could hide or erode;
- misuse would change learning, quality, safety, eligibility, service, or
  professional accountability;
- useful examples and anti-examples differ by local workflow.

Do not run a full community workbench for a one-person reversible task. Use a
request slip, mechanism review, or small workflow context file instead.

## 2. create the folder

Start from the architecture in
[`domain-ai-literacy-workbench.md`](../architecture/domain-ai-literacy-workbench.md).
At minimum create:

- `README.md`
- `use-boundary-map.md`
- `examples.md`
- `fundamentals.md`
- `assistant-roles.md`
- `artifact-ledger.md`
- `implementation-evidence.md`
- `learning-loop.md`

Use the [boundary map template](../templates/domain-ai-boundary-map.md) for the
highest-authority artifact.

## 3. teach primitives before products

Explain the stable primitives in local language:

- source material and context;
- generation, transformation, classification, retrieval, and tool use;
- hallucination and review;
- privacy and consent;
- deterministic automation versus model judgment.

Treat vendor names and current features as examples, not the curriculum.

## 4. build the use-boundary map

For each recurring task, classify it as:

- human-only;
- AI-assisted drafting or exploration;
- AI output allowed only after expert review;
- deterministic automation preferred;
- agentic loop allowed under supervision;
- prohibited.

Record rationale, reviewer role, evidence needed, and failure risk. If a task is
controversial, keep the disagreement visible instead of averaging it away.

## 5. collect examples and anti-examples

Use concrete artifacts, not abstract opinions. Capture:

- a task where AI improves quality or speed;
- a task where AI damages learning, trust, safety, or review;
- an output a practitioner can defend;
- an output that looks good but fails domain standards;
- a source or privacy boundary violation;
- an example that should become an eval or training case.

Strip private identities and sensitive source data before sharing outside the
workspace.

## 6. create workflow rooms

Create a room only for a repeated workflow. Each room needs:

- local purpose and non-goals;
- sources or examples allowed in that room;
- assistant roles available there;
- expected artifacts;
- review rules;
- current open questions.

Rooms prevent one giant handbook from becoming context bloat.

## 7. tie assistant roles to artifacts

Every assistant role must answer:

- what artifact it creates or reviews;
- what sources it may use;
- what it may not decide;
- what human role accepts or rejects the output;
- what evidence appears in the artifact ledger.

Delete roles that only produce commentary or persona flavor.

## 8. run the first evidence loop

Pick one real workflow and record:

1. baseline human process or current pain;
2. AI-assisted attempt;
3. review notes;
4. accepted, rejected, and revised parts;
5. final artifact or decision;
6. outcome check.

No evidence loop means the program is still training material, not a workbench.

## 9. update the learning loop

After each cohort, sprint, or review cycle, update:

- boundary map changes;
- new examples and anti-examples;
- assistant role changes;
- recurring objections;
- incidents and near misses;
- eval cases and acceptance criteria.

## stop conditions

Stop and redesign if:

- the sponsor wants adoption metrics but no use/non-use boundaries;
- practitioners cannot influence examples, review rules, or artifacts;
- private conversation data would have to be exposed to prove value;
- AI outputs are accepted without a named reviewer role;
- the workbench cannot show a changed artifact, policy, workflow, or decision.
