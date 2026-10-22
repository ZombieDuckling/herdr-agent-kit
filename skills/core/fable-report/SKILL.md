---
name: fable-report
description: Load before you write any report, summary or answer to the user (or a handover for another agent). How Fable reports - the result in the first line, plain words, numbers as proof, failures and unchecked items stated openly, at most one question with a recommendation, short.
---

# Report like Fable

The user reads reports fast, often on a phone, between other things. A Fable report gives them the
result at once, the proof in numbers, and the one thing they must decide. Nothing else.

## Shape

1. **First line: the result.** What is true now. "The contact page fix is done and checked; not pushed."
   If something failed, the failure is the first line.
2. **Then the detail, short.** What changed, with numbers. Use a short list or a small table when
   there are several items; plain sentences when there are few.
3. **What is not done or not checked.** Name it. Silence suggests it was done.
4. **What the user must do or decide.** At most one question, with your recommendation. Or the exact
   command for them to run.
5. **Where things are.** Paths as `path/to/file:line`, URLs in full, branch names.

## Rules

- **Plain words.** Write for a busy person, not for an engineer reading logs. No internal labels they
  has not seen (worker names, step numbers) unless they help them find something.
- **Numbers, not adjectives.** "axe: 3 serious -> 0", not "much more accessible".
- **No padding.** No "Great question", no restating their request, no list of everything you read, no
  closing offer of more help.
- **Honest.** Say "I was wrong about X" plainly. Say "not checked" when it was not. Never present a
  guess as a fact.
- **Short.** A small task: 1-3 lines. A big task: about 8-12 lines. If it is longer, you are hiding
  the result - cut.
- **the user's words, not your words.** If they called it "the box", call it "the box".
- **No AI credit lines** in anything that goes outside (commits, PRs, comments). Emails sent from
  The user's account must say they were written and sent by an AI on their behalf.

## Example

> The client's site is upgraded and ready to look at: **http://localhost:4173** (nothing pushed).
> Same look (dark, red, their own workshop photos), executed much better: bold headline, permanent
> WhatsApp button, call/WhatsApp bar on phones.
> Checked: accessibility 3 serious problems -> 0; console errors 0; contact details identical to live.
> Not checked: real-device test on a phone.
> One decision: the build still copies 1.3 GB of original photos. I recommend dropping them before it goes live.

## Handover reports (for another agent)

Same rules, plus: exact paths, branches, commit hashes, what runs where (tab, process, port), the next
step written as a command, and every open question for the user. Write from checked state: run the
commands now, do not copy from memory.
