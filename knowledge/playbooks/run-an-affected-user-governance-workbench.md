# run an affected-user governance workbench

Use this when a consequential AI workflow needs legitimacy, adoption, or domain
judgment from people affected by it. The playbook converts participation into
traceable system changes.

## 1. decide whether governance is required

Run this when at least one condition is true:

- the workflow changes access, evaluation, learning, safety, eligibility, or work
  conditions for a group;
- domain expertise sits outside the build team;
- quality depends on local practice, culture, taste, or values;
- failure would be hard for affected users to detect or contest;
- the sponsor needs visible accountability, not only a working demo.

Do not run a full governance workbench for reversible internal scripts owned by a
single accountable operator. Use a lightweight review instead.

## 2. create the folder

Start from the architecture in
[`affected-user-governance-workbench.md`](../architecture/affected-user-governance-workbench.md).
At minimum create:

- `README.md`
- `participant-roles.md`
- `source-material.md`
- `proposals.md`
- `tradeoff-ranking.md`
- `decision-ledger.md`
- `outcome-checks.md`

Use the [governance decision ledger template](../templates/governance-decision-ledger.md)
for decisions.

## 3. recruit roles, not token witnesses

Record the role coverage required for legitimacy. Include representative users,
edge cases, frontline operators, domain experts, maintainers, support staff, and
risk reviewers as needed. Also record gaps honestly.

Do not publish names, private contact details, raw demographic data, or raw
deliberation unless explicit disclosure approval exists.

## 4. onboard before asking for judgment

Provide participants with:

- the purpose and non-goals;
- what the system can and cannot do;
- examples of normal and failure behavior;
- data and privacy boundaries;
- what decisions participants can influence;
- compensation, access, and support arrangements where applicable.

A person cannot govern a system they have only seen as a sales pitch.

## 5. deliberate from concrete artifacts

Use scenarios, source examples, prototypes, anti-examples, draft policies, or
workflow traces. Capture:

- recurring needs;
- disagreements;
- unacceptable failure modes;
- suggested rules or UI changes;
- examples that should become eval cases.

Summarize themes into the workbench. Keep raw records protected.

## 6. convert discussion into implementation units

For every recurring theme, write a proposal with:

- problem statement;
- affected role;
- recommendation;
- acceptance test or eval case;
- likely implementation surface;
- risk if ignored;
- dependencies or unknowns.

If a proposal cannot be implemented, say why instead of leaving it as vague
feedback.

## 7. rank tradeoffs

Score each proposal on:

- feasibility;
- affected-user impact;
- ethics/risk reduction;
- adoption burden;
- maintenance/cost;
- reversibility.

Avoid simple majority voting when a minority group carries disproportionate risk.
The ranking is evidence for a decision, not an automatic decision.

## 8. record decisions and implementation evidence

For every proposal, mark one status:

- accepted;
- rejected;
- deferred;
- needs more evidence.

Each row must include rationale, decision owner role, date, and a link or pointer
to the spec, issue, policy, prompt, eval, commit, or roadmap item. No link means
no implementation evidence.

## 9. evaluate outcomes

Schedule a later check that asks:

- did the system change;
- did the affected group experience the intended change;
- did new risks appear;
- which proposals need to be reopened;
- what evidence should be added to the eval set.

## stop conditions

Stop and redesign the process if:

- participation cannot influence any decision;
- the sponsor refuses to record rejected recommendations;
- participants lack enough context to judge;
- private participant data would have to be published to prove the work;
- the proposed system risk exceeds the team's ability to monitor and reverse.
