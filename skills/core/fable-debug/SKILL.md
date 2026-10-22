---
name: fable-debug
description: Load the moment anything fails or behaves unexpectedly - an error, a failed test, a command that does nothing, a wrong result, a tool that is refused. The Fable way to work through problems - read the whole error, reproduce, list 2-3 causes, run the cheapest test that separates them, fix the cause not the symptom, change approach after two failures.
---

# Work through problems like Fable

Fable does not retry blindly and does not give up early. It **reads, narrows down, proves, then fixes
the cause**. Follow these steps in order. Write each one in your notes.

## Procedure

1. **STOP and read the whole output.** Not only the last line. The real cause is often the first
   error, a "caused by", or a warning above. Copy the exact error text into your notes.
2. **Reproduce it.** Find the smallest command that shows the failure. If you cannot reproduce it,
   write that down - do not "fix" something you cannot see.
3. **List 2 or 3 possible causes.** Never only one; one cause is a guess. For each cause write:
   "If this is the cause, I would also see ___."
4. **Run the cheapest check that separates the causes.** Prefer read-only checks. One good check can
   rule out two causes at once.
5. **Name the cause, with its proof.** `CAUSE: <cause> (proof: <check> -> <output>)`
6. **Fix the cause, not the symptom.** These hide a problem and are NOT fixes: a retry loop, a longer
   sleep, `|| true`, `2>/dev/null`, a skipped test, a disabled check, a looser rule. If you must work
   around something, say so in the report and say why.
7. **Prove the fix** with the reproduce command from step 2. Then check that nothing near it broke.
8. **Write one line for the future** in your notes: what caused it and how to avoid it.

## The two-failure rule

- The same approach failed twice? **Do not run it a third time.** Change the approach: another tool,
  another angle, a smaller step, or a worker with different abilities.
- Three different approaches failed? Stop. Tell the user exactly: what you tried, the exact errors, what
  you think the cause is, and what you need from them.

## Special cases

- **A permission or safety refusal** ("denied by classifier", "permission denied", "blocked"): do not
  look for a way around it. Read the reason. Finish everything else. Then give the user the exact command
  to run themselves (in Claude Code: a line starting with `!`), and say why it is needed.
- **Nothing happened** (no output, no change): check whether it ran at all before you debug what it
  did. Was the command sent as text instead of being run? Did it run in another folder, another
  machine, another branch? Is a process already holding the port or the lock?
- **It worked yesterday:** find what changed - `git log`, `brew list --versions`, tool `--version`,
  config files' modification times, `pmset -g log` (the Mac slept?).
- **Flaky (sometimes fails):** run it 5 times and count. Look for timing, shared state, network.
- **You made the mistake:** say so plainly, fix it, and add the "avoid it" line. Example: a wrong
  session ID typed from memory. Fix: copy IDs from the system (`herdr agent list`), never from memory.

## Worked examples

**"The command did nothing."** the user pasted an install command into chat. Causes: (a) it failed,
(b) it never ran, (c) it ran but changed nothing. Check: `claude plugin list` (plugins absent) and no
shell output in the chat. Cause: (b), it was sent as a chat message. Fix: run it with `!` first.

**"Host key verification failed"** on SSH to a new machine. Causes: (a) wrong host, (b) host key not
known yet, (c) host key changed (danger). The full error says the key is unknown, not changed: (b).
Fix the cause: accept the key once for that host (`StrictHostKeyChecking=accept-new`). Do NOT turn
off host key checks for all hosts.

**"Daily FAIL email from a watchdog."** Causes: (a) a service really is down, (b) the watchdog checks
services that no longer exist, (c) the mail step is broken. Check: read the watchdog's list of
services and compare with what is installed (`launchctl list | grep <label>`). Two listed services
were retired months ago: (b). Fix: remove them from the list (with the user's OK if it is shared state).
