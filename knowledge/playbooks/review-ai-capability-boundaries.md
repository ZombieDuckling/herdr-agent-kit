# review AI capability boundaries

Use this playbook before adopting, shipping, teaching, or blaming an AI-enabled
workflow when the discussion has collapsed capability, permission, metaphysics,
or responsibility into one argument.

## 1. state the claim narrowly

Write the smallest claim under review:

- Task:
- User/context:
- Output or action:
- Data/tools available:
- Failure cost:
- Current decision needed:

Do not review broad claims such as "AI can replace this role" or "AI cannot do
this work." Rewrite them as observable task claims under a named boundary.

## 2. draw the system boundary

List every component that contributes to the outcome:

- Model or models.
- Prompts, skills, policies, and routing files.
- Retrieved sources or uploaded documents.
- Deterministic code, schemas, parsers, filters, and validators.
- Tools, permissions, and side-effecting actions.
- Human reviewers, approvers, operators, and escalation paths.
- Logs, monitoring, and rollback controls.

The claim applies to this whole system, not to the model label alone.

## 3. split four questions

Answer these in separate sections:

1. Capability: what evidence shows the system can or cannot perform the task?
2. Permission: should this use be allowed under the risk, consent, data, and
   stakeholder constraints?
3. Boundary: which parts are automated, which are deterministic, which are
   human-reviewed, and which are forbidden?
4. Responsibility: who chose the data, prompts, tools, validation, deployment,
   monitoring, and remediation path?

If one section is unknown, label it unknown. Do not fill it with a confident
answer from another section.

## 4. inspect harms without scapegoating the model

For a harmful or low-quality outcome, trace the responsibility chain:

- Source quality and provenance.
- Instruction and policy design.
- Tool and permission scopes.
- Validation and review gates.
- Release or message approval.
- Monitoring, incident response, and correction.
- Incentives that rewarded speed, volume, or deflection over judgment.

The phrase "the AI did it" is not an incident analysis.

## 5. add human-boundary gates

If the workflow touches grief, crisis, identity, care, education, access,
reputation, money, safety, or high-stakes support:

- Define the non-automation boundary.
- Add escalation and opt-out routes.
- Keep a human accountable for final decisions where harm is plausible.
- Require review evidence before increasing autonomy.

## 6. produce the decision note

The final note must include:

- The narrow claim and evaluated boundary.
- Evidence used and evidence missing.
- Allowed, forbidden, and review-only uses.
- Human responsibility chain.
- Deployment controls and rollback path.
- Open questions and the next review trigger.

Route the decision through
[`checklists/ai-capability-boundary-review.md`](../checklists/ai-capability-boundary-review.md)
before treating it as accepted.
