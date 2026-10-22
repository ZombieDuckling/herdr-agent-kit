# domain AI literacy workbench

Use this architecture when a profession, department, or community needs to adopt
AI without losing domain judgment, learning, trust, or accountability. The goal is
not to teach prompt tricks. The goal is to create a shared practice that knows
when AI helps, when it harms, and how changed work will be reviewed.

## minimum components

```text
domain-ai-literacy-workbench/
  README.md                    # domain, purpose, participants by role, scope
  use-boundary-map.md           # no-AI, assist-only, automate, and review zones
  examples.md                   # approved examples and anti-examples
  fundamentals.md               # skills practitioners must still learn manually
  rooms/                        # workflow/topic rooms with local routing notes
  assistant-roles.md            # assistant roles tied to outputs and review jobs
  artifact-ledger.md            # generated artifacts, source pointers, review state
  implementation-evidence.md    # before/after examples, decisions, outcome checks
  learning-loop.md              # failures, objections, updated rules and examples
```

Keep raw conversations, private participant identities, and sensitive source
material outside the shareable workbench unless explicitly approved for that
workspace. Publish the boundary map, examples, and decision trail; protect the
private room.

## flow

1. **Name the domain outcome.** State what practice should improve: review
   quality, onboarding, drafting, analysis, learning, service delivery, or another
   concrete workflow.
2. **Recruit practitioners by role.** Include experienced experts, novices,
   reviewers, support roles, and affected downstream users where their judgment
   changes the boundary.
3. **Reduce overwhelm.** Start with plain-language primitives and local examples,
   not vendor feature tours.
4. **Map use and non-use boundaries.** Classify tasks as human-only, AI-assisted,
   review-required, automatable, or prohibited. Record why each boundary exists.
5. **Preserve fundamentals.** Identify which skills must still be learned or
   practiced manually because they support judgment, safety, taste, or review.
6. **Create conversation rooms.** Organize discussion by real workflows. Each room
   should have local sources, open questions, assistant roles, and expected
   artifacts.
7. **Attach assistant roles to outputs.** Use roles such as drafter, critic,
   source finder, simulator, rubric checker, or data formatter only when they own
   a concrete output or review function.
8. **Ledger artifacts and decisions.** Capture generated drafts, accepted edits,
   rejected suggestions, implementation pointers, and review notes.
9. **Close the learning loop.** Turn recurring failures, objections, and strong
   examples into updated boundaries, examples, eval cases, or training modules.

## interfaces

- A **front desk** explains the domain, role coverage, current boundaries, and
  what a fresh participant should read first.
- A **boundary map** is the highest-authority artifact: it says where AI is not
  allowed, where it assists, and where human review is mandatory.
- **Rooms** hold workflow-specific context so the whole community does not need a
  single bloated prompt or handbook.
- **Assistant roles** are tools inside rooms, not theatrical personas.
- An **artifact ledger** proves whether conversation changed a document, policy,
  workflow, lesson, or product decision.
- An **implementation-evidence file** records before/after examples and outcome
  checks.

## failure modes

- Training teaches generic tool operation while practitioners still cannot name
  use, non-use, or review boundaries.
- Resistance is dismissed as ignorance instead of mined for valid workflow,
  assessment, privacy, safety, or trust constraints.
- AI produces polished artifacts that practitioners cannot explain or defend.
- Group chat turns into persona theater with no files, decisions, or reviewable
  outputs.
- Human conversation is mined for model or product improvement without explicit
  consent, retention, and disclosure rules.
- The boundary map is written once and never updated from real failures.

## done

The workbench is usable when a fresh reviewer can answer:

- which roles participated and which gaps remain;
- which domain tasks are human-only, assist-only, review-required, automatable,
  or prohibited;
- which fundamentals must still be practiced without AI;
- which examples and anti-examples define the local standard;
- which assistant roles produce or review which artifacts;
- what changed in real work because of the program; and
- which failures or objections changed the boundary map.
