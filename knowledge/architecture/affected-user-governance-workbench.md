# affected-user governance workbench

Use this architecture when an AI system affects a group whose trust, rights,
work, learning, safety, or access can be changed by the system. Do not use it as
ceremony for low-risk personal scripts.

The purpose is not to collect opinions. The purpose is to create a visible route
from informed participation to product decisions and outcome checks.

## minimum components

```text
governance-workbench/
  README.md                    # purpose, scope, decision rights, risk level
  participant-roles.md          # roles and representation gaps, not identities
  source-material.md            # material participants must see before judging
  deliberation-themes.md        # themes, disagreements, open questions
  proposals.md                  # concrete recommendations and eval cases
  prototype-log.md              # prototypes, demos, hackathon outputs, limits
  tradeoff-ranking.md           # feasibility, impact, ethics/risk, adoption, cost
  decision-ledger.md            # accepted/rejected/deferred with rationale
  outcome-checks.md             # post-change measures and review dates
```

Keep raw discussion records and participant identities outside the publishable
workbench unless every participant has explicitly approved the disclosure. The
shareable artifact is the decision trail, not the private room.

## flow

1. **Name the affected groups.** Include domain experts, frontline operators,
   edge-case users, support roles, and risk/ethics voices where relevant.
2. **Declare decision rights.** State who decides, who advises, who can block,
   and what is out of scope.
3. **Onboard participants.** Give enough context about the goal, limits, data,
   model behavior, expected failures, and participation norms for informed input.
4. **Deliberate against source material.** Use concrete examples, scenarios,
   failure cases, and existing workflow evidence instead of generic preference
   questions.
5. **Draft proposals.** Convert themes into specific requirements, policies,
   prompts, UI changes, eval cases, or operating rules.
6. **Prototype where useful.** Lightweight prototypes let non-builders react to
   artifacts instead of abstractions.
7. **Rank tradeoffs explicitly.** Score proposals by feasibility, user impact,
   ethics/risk, adoption cost, maintenance cost, and reversibility.
8. **Record decisions.** Accept, reject, or defer each proposal with rationale
   and a link to the implementing artifact or backlog item.
9. **Check outcomes.** Later, measure whether participation changed the system
   and whether the affected groups saw the promised effect.

## interfaces

- A **front desk** explains scope, roles, and the current decision state.
- A **source shelf** stores only consent-safe material needed for review.
- A **proposal table** turns discussion into implementation-ready work.
- A **decision ledger** prevents participation from becoming theater.
- A **review surface** shows prototypes, diffs, specs, eval results, and open
  risks.

## failure modes

- Feedback is limited to surveys, sentiment summaries, or informal interviews.
- Participants are asked for values but never shown constraints or prototypes.
- The loudest or most technical voices dominate without facilitation.
- Participation barriers make the sample unrepresentative.
- Recommendations disappear into a backlog with no accepted/rejected/deferred
  state.
- Outcome checks measure attendance or satisfaction but not whether the system
  changed.

## done

The governance workbench is usable when a fresh reviewer can answer:

- who was affected, by role;
- what they were shown before judging;
- what proposals were made;
- how each proposal was ranked;
- what decisions were accepted, rejected, or deferred;
- which specs, issues, commits, policies, prompts, or evals changed; and
- when the outcome will be checked again.
