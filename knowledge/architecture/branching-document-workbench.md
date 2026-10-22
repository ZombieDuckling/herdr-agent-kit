# branching document workbench

Use this shape when several humans or agents are working on one document, spec,
plan, policy, lesson set, or other long-lived artifact.

The goal is not “more agents in chat.” The goal is controlled collaborative
editing: discussion stays connected to a source artifact, changes are scoped to
sections, and merge decisions are reviewable.

## minimum shape

1. **Source discussion** — the parent conversation or issue that states the goal,
   constraints, disagreements, and current decision state.
2. **Canonical artifact** — the document or spec that branch outputs may propose
   changes to but may not silently overwrite.
3. **Section map** — stable headings, anchors, chunk ids, or numbered regions so
   branches can name what they affect.
4. **Branch record** — one focused sub-workspace per disputed or delegated change.
5. **Role/output contract** — the agent or participant role, allowed inputs,
   allowed edits, expected output, and forbidden actions.
6. **Diff or proposal** — a reviewable change set, not just a prose summary.
7. **Merge ledger** — accepted, rejected, superseded, and deferred decisions with
   reviewer role and receipt.

## branch record fields

Each branch should be small enough that a reviewer can understand it without
replaying the whole parent discussion.

| field | purpose |
|---|---|
| Branch id | stable identifier for references and merge ledger rows |
| Parent artifact | canonical file, document, or object being changed |
| Source section | heading, anchor, chunk id, or region under discussion |
| Trigger | the question, disagreement, defect, or delegated task that created the branch |
| Participants | roles, not personal identifiers |
| Role/output contract | what each agent or participant is allowed to produce |
| Inputs | source material and branch-local context |
| Proposed change | patch, replacement text, decision note, or artifact link |
| Acceptance criteria | tests, review questions, or policy gates |
| Decision | accepted, rejected, deferred, superseded, or needs more evidence |
| Merge receipt | diff, commit, artifact registry row, or review record proving what landed |

## operating rules

- Branch from a named artifact section, not from a vague feeling in chat.
- Keep whole-document rewrites exceptional; default to bounded section edits.
- Treat agent personas as edit contracts. If two personas have the same inputs,
  powers, and outputs, they are not separate roles.
- Keep semantic search auxiliary. It may find relevant sections, but it does not
  replace explicit parent/section/merge links.
- Do not mutate the canonical artifact until review has accepted a diff or
  proposal.
- Close stale branches explicitly as rejected, deferred, or superseded; do not
  let them become orphaned context.

## failure patterns

- **Orphan branch:** useful side discussion with no parent artifact or merge path.
- **Persona theater:** many named roles, no distinct output contracts.
- **Whole-document churn:** a small disagreement causes a full rewrite and large
  review debt.
- **Decorative vectoring:** chunks are embedded but not used for provenance,
  section targeting, or review.
- **Silent merge:** the source artifact changes without a decision or receipt.

## done definition

A branching document workbench is ready when a fresh operator can answer:

- What is the canonical artifact?
- Which branch am I in?
- Which section does this branch affect?
- What role/output contract applies?
- What change is proposed?
- Who or what decides merge eligibility?
- Where is the accepted diff or rejection recorded?

See [WB-18](../notes/08-workbench-architecture.md#wb-18-branch-discussions-from-artifacts-not-from-vibes) and the [branch ledger template](../templates/branch-ledger.md).