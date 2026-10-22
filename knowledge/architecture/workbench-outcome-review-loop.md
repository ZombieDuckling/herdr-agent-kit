# workbench outcome review loop

A workbench is not finished when the first artifact is delivered. It is finished when later use shows whether the artifact changed behavior, where it failed, and which reusable component should improve.

## system shape

```text
original promise
  -> delivered workbench or workflow
  -> elapsed real use
  -> architecture walkthrough
  -> outcome evidence
  -> blocker/failure-mode ledger
  -> reusable asset update
  -> next verification
```

## components

| component | purpose |
|---|---|
| Original promise | Preserves what the work was meant to make possible before hindsight changes the story. |
| Current architecture map | Shows inputs, stages, tools, model calls, human checks, outputs, and owners as they now exist. |
| Outcome evidence | Separates direct value, follow-on value, adoption, cost, risk, and negative evidence. |
| Failure-mode ledger | Keeps blockers and support issues visible instead of hiding them in follow-up chats. |
| Reusable asset router | Decides whether a finding updates a template, checklist, script, mutable workbench, archive, backlog, or stop decision. |
| Next verification | Converts the review into one owned change with a proof target. |

## boundaries

- Do not count activity as outcome unless it changed a workflow, artifact, decision, cost, risk, or user behavior.
- Do not treat follow-up support as cleanup only; it is source material for product, training, and template improvement.
- Do not let one expert remain the only carrier of definitions, concept relationships, or teaching order.
- Do not turn every blocker into software. Some blockers need a human service, a simpler folder, a clearer template, or a stop decision.

## review surfaces

The loop should produce at least one visible artifact:

- outcome review record,
- updated workbench map,
- blocker/failure-mode ledger,
- updated template/checklist/script,
- backlog item with evidence,
- or archive/stop decision with reason.

## fit with other architecture

- Uses [workbench components](workbench-components.md) for the inspected system surface.
- Uses front-desk files, manifests, request slips, and local workflow maps when a repeated job should become a portable package.
- Uses [product outcome assurance](product-outcome-assurance.md) when the reviewed work affects shipped software or rollout acceptance.
