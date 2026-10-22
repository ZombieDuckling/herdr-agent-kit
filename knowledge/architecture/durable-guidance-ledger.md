# durable guidance ledger

Use this architecture when a knowledgebase stores advice across fast-changing tool, model, market, or platform cycles.

A reusable knowledgebase fails in two opposite ways: it trusts old advice because it is well-written, or it discards old advice because the named tool changed. The ledger separates the stable primitive from the volatile surface so future agents know what to promote, refresh, or retire.

## layers

| layer | definition | storage rule |
|---|---|---|
| Durable primitive | A workflow, computing, review, governance, or human-judgment invariant that survives tool churn. | Eligible for laws, skills, and long-lived playbooks after repeated evidence. |
| Current tactic | A model, vendor UI, pricing shape, prompt trick, integration behavior, or release-specific workflow. | Keep in dated notes or decision records with a review trigger. |
| Market observation | A claim about adoption, buyer behavior, competitive baseline, or pricing pressure. | Keep with date, scope, confidence, and expiry/review conditions. |
| Unsupported source-limited claim | A title, metadata note, thin transcript, memory fragment, or unverified anecdote. | Do not promote; keep as source coverage or retry-pending inventory. |

## ledger fields

Each reusable claim needs:

| field | purpose |
|---|---|
| Claim | The shortest statement that might guide future action. |
| Source pointer | Where the claim came from, using a sanitized internal pointer or public source card. |
| Source date / retrieval date | How old the supporting evidence is. |
| Layer | Durable primitive, current tactic, market observation, or unsupported source-limited claim. |
| Still true | The part that survived review. |
| Changed assumptions | What shifted in models, tools, cost, policy, users, or market baseline. |
| Current action | What a future agent should do now. |
| Promotion target | Law, playbook, checklist, template, architecture note, local project note, or no promotion. |
| Next review trigger | Model/provider release, policy change, repeated failure, client evidence, cost change, or scheduled audit. |

## promotion rule

Promote only the primitive. Strip names, private context, and source-specific identifiers. If the useful lesson depends on the identity of a person, platform, buyer, account, company, venue, repository, channel, or private incident, it is not transferable enough for the shared law layer.

## review loop

1. Inventory the old claim and its source pointer.
2. Classify its layer before judging whether it is true.
3. Extract the primitive separately from the dated tactic or market claim.
4. Compare against current evidence or recent failures.
5. Promote, refresh, quarantine, or retire the claim.
6. Record the next review trigger so stale confidence does not become inherited authority.

## verification

A fresh agent can read the ledger and answer:

- what is still safe to reuse;
- what changed and why;
- where the evidence lives;
- which guidance is intentionally not promoted;
- what event should force the next review.
