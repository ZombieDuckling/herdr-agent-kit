# raise the baseline after AI

Use this playbook when a task, class of work, or product workflow becomes easy to
produce with AI assistance. The goal is to convert the capability gain into a
better acceptance contract, not merely faster generic output.

## 1. freeze the old task

Record the old accepted output and why it used to be valuable.

```md
Old task:
Old accepted output:
Old evidence:
Why this used to test or deliver value:
```

## 2. identify the commoditized layer

Mark which pieces are now cheap enough to treat as baseline.

- drafting or rewriting
- grammar and tone smoothing
- boilerplate code or document structure
- simple search or summary
- formatting or conversion
- comparison, extraction, or calculation
- procedural compliance

If nothing has actually become cheaper or more reliable, stop; this is not a
baseline-ratchet event.

## 3. choose the higher layer

Pick the smallest stronger requirement that preserves the real value of the
work.

| old value | raised acceptance layer |
| --- | --- |
| writing fluency | source fit, argument quality, tone, specificity |
| code generation | tests, diffs, maintainability, security review |
| research summary | triangulation, contradictions, decision impact |
| classroom exercise | critique, defense, originality, source judgment |
| operations procedure | rollback, observability, audit trail, handoff proof |
| product demo | usable outcome, governance, support, cost controls |

## 4. assign the saved time

Write where the saved time must go. Examples: verification, polishing, deeper
source review, better examples, adversarial review, user-fit testing,
documentation, or implementation evidence.

Do not count “more pages,” “more tickets,” or “more drafts” as a quality gain
unless the outcome contract says why that volume matters.

## 5. update the request or rubric

Add a side-by-side section to the request slip, rubric, or workflow file:

```md
Pre-AI baseline:
AI-assisted baseline:
Raised-bar output:
Evidence required:
Human judgment retained:
Tool-use disclosure or audit requirement:
Rejected easy output:
```

## 6. verify before adoption

Run representative examples through the new contract.

- Does the old output now fail for the right reason?
- Does a generic generated output fail even if fluent?
- Does an excellent tool-assisted output pass with evidence?
- Can a reviewer see where human judgment was applied?
- Did accepted-outcome quality improve without hidden review debt?

If the answer is no, revise the acceptance contract before changing the default
workflow.

## related laws and gates

- `SDLC-1` — measure accepted outcomes, not activity.
- `SDLC-21` — turn capability gains into raised acceptance criteria.
- `MECH-1` — name the job before naming the tool.
- `WB-8` — make the review surface first-class.
- `checklists/ai-baseline-ratchet.md` — gate the update.
- `templates/baseline-ratchet-record.md` — record the decision.
