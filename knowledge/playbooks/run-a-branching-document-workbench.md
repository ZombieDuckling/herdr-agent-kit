# run a branching document workbench

Use this when collaboration around a document, spec, policy, plan, or lesson set
starts producing side discussions, role-agent edits, or conflicting revisions.

## 1. declare the canonical artifact

- Name the artifact that may change.
- Add or confirm stable headings, anchors, chunk ids, or numbered sections.
- State which parts are canonical, draft, generated, or locked.

## 2. open branches deliberately

Create a branch only for a bounded question, disagreement, defect, or delegated
section edit. Record:

- parent artifact;
- source section;
- trigger;
- participant roles;
- role/output contract;
- allowed inputs and forbidden actions;
- expected proposal or diff;
- reviewer or merge policy.

Use [the branch ledger template](../templates/branch-ledger.md) when no project-
specific ledger exists.

## 3. constrain the agent work

- Prefer one section, one issue, one output contract.
- Ask for patch/proposal form when possible.
- Require rationale tied to the source section and branch inputs.
- Forbid whole-document rewrites unless the request explicitly authorizes them.

## 4. review before merge

Before changing the canonical artifact, verify:

- the branch points to the right source section;
- the diff is inspectable;
- acceptance criteria are satisfied;
- conflicts with other branches are named;
- sensitive or source-specific material has been stripped when the workbench is
  shareable;
- the decision is recorded as accepted, rejected, deferred, or superseded.

## 5. record the receipt

After merge or rejection, update the ledger with the artifact version, diff,
commit, review record, or artifact registry row that proves the decision.

Close the branch. Do not leave stale side discussions as implicit state.

## quick checks

- Can a new participant identify the source artifact and target section without
  replaying chat?
- Does every role have a distinct output contract?
- Is there a visible diff or proposal?
- Is the canonical artifact unchanged until the merge decision?
- Can rejected ideas be found later without being mistaken for active state?