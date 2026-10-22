# extract a dialogue into a workflow

Use this when a chat, meeting, transcript, or support thread has produced a
repeatable way of working that should survive beyond the conversation.

## trigger

Extract the dialogue when at least one is true:

- the same context has been repeated in multiple sessions,
- a correction or example materially changed the output quality,
- another operator will need to continue the work,
- the conversation caused file, code, data, deployment, or policy changes,
- the transcript is too long to keep feeding into future prompts.

## extraction pass

Create or update durable files for these fields:

| field | capture |
| --- | --- |
| Goal | the actual outcome after corrections, not the first vague request |
| Constraints | security, style, budget, data, timing, interface, and non-goals |
| Assumptions | guesses that were confirmed, rejected, or left open |
| Examples | accepted and rejected outputs, schemas, tests, tone samples, references |
| Decisions | chosen route, rejected alternatives, and why |
| Actions | commands, tool calls, files touched, deployment or data changes |
| Verification | how the group knew the result worked |
| Reusable rule | the compact instruction, skill, script, or checklist future agents should read |

## target artifacts

Pick the smallest set that makes the work reproducible:

- request slip for the next instance of the task,
- workflow routing note or front-desk section,
- markdown skill or prompt asset,
- examples directory with positive and negative cases,
- command/script wrapper for deterministic steps,
- decision log entry,
- action ledger with files/tools touched,
- verification checklist.

Do not publish the raw transcript as the workflow. Keep it as source material only
when retention is allowed and useful.

## live meeting variant

If the dialogue happened in a live call or voice-controlled workspace, require:

- speaker or role attribution for every requested action,
- explicit action scope before writes,
- visible diffs or artifact links before adjournment,
- unresolved follow-ups and rollback/handoff state.

## acceptance test

A fresh operator passes when they can receive a short request, read the workflow
files, reproduce the accepted behavior, and explain which constraints, examples,
and verification rules came from the dialogue.

Related laws: [WB-6](../notes/08-workbench-architecture.md#wb-6-chat-is-not-durable-state),
[WB-10](../notes/08-workbench-architecture.md#wb-10-successful-dialogue-is-source-code-for-the-next-workflow),
and [SDLC-12](../notes/11-agentic-sdlc.md#sdlc-12-prompts-are-software-assets-not-comment-fields).
