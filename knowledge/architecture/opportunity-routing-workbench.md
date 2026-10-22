# opportunity routing workbench

Use this system shape when a community, agency, internal team, or service shop has attention and capable operators, but paid or high-priority requests disappear into chat, meetings, or inboxes.

The goal is not to build a marketplace first. The goal is to make demand, capacity, reusable assets, fulfillment status, and proof-of-work visible enough that the next smallest mechanism is obvious.

## components

| component | purpose | minimum file/table |
| --- | --- | --- |
| Demand intake | Capture the buyer/user, pain, current cost, urgency, and acceptance test. | request slip or opportunity row |
| Capacity ledger | Show which operator role can fulfill which class of work and at what review boundary. | operator/capability table by role, not identity |
| Asset catalog | List reusable templates, examples, prompts, components, scripts, or prior artifacts. | asset registry with source and reuse limits |
| Routing board | Track new, qualified, claimed, blocked, delivered, accepted, and archived requests. | kanban/table with state and owner role |
| Fulfillment workbench | Hold source inputs, working notes, generated outputs, checks, and handoff artifacts. | per-request folder or linked workbench |
| Proof ledger | Preserve accepted outputs, review notes, results, and follow-up value. | outcome/proof rows linked to artifacts |
| Escalation log | Record why a heavier mechanism is justified: template, script, agent, integration, or product. | mechanism decision note |

## routing states

1. **Raw demand** — a request, complaint, lead, or recurring pain exists, but value and acceptance are not yet clear.
2. **Qualified pain** — user/buyer role, current cost, expected output, data/source inputs, deadline, and review owner are explicit.
3. **Matched capacity** — at least one operator role or reusable asset can plausibly fulfill it within the authority boundary.
4. **Claimed experiment** — one bounded attempt is authorized with a delivery surface and done definition.
5. **Delivered artifact** — output exists in a workbench with source links and checks.
6. **Accepted proof** — the buyer/user or review owner accepts, rejects, or asks for a scoped revision.
7. **Reusable pattern** — repeated accepted proofs are compressed into a template, checklist, script, model call, agent, or product feature.

## design rules

- Start with a board and request slips before building a platform.
- Route by problem class, data boundary, operator capacity, and proof requirements; do not route by enthusiasm alone.
- Treat reusable assets as inventory. A deck, prompt, component, checklist, or script should be discoverable before new work begins.
- Keep buyer/user demand separate from learning goals. Learning is justified only when it unlocks a qualified request or repeated bottleneck.
- Keep claims role-based and sanitized in shared notes. Private identities, channels, customers, amounts, and deal details stay outside reusable architecture.
- Graduate only the bottleneck that repeated accepted work exposes. A job board may need better intake long before it needs autonomous agents.

## acceptance tests

- A fresh operator can see what requests exist, which are qualified, which are claimed, and what proof is due.
- A reviewer can trace each delivered artifact back to its request slip, source inputs, capacity match, and acceptance decision.
- A builder can name which repeated bottleneck justifies the next mechanism escalation.
- The board can produce a useful manual result before any custom marketplace, integration, or agent runtime is built.

Related laws: [MECH-1](../notes/10-mechanism-selection.md#mech-1-name-the-job-before-naming-the-tool), [MECH-7](../notes/10-mechanism-selection.md#mech-7-automate-only-after-the-manual-workflow-teaches-its-boundary), [MECH-14](../notes/10-mechanism-selection.md#mech-14-learn-or-delegate-only-against-a-valued-bottleneck), and [MECH-15](../notes/10-mechanism-selection.md#mech-15-route-demand-before-building-supply).
