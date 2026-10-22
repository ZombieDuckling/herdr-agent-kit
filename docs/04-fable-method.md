# The Fable method

Claude Fable 5.1 is the strongest agent this kit was built with. What makes it good is not magic; it is
**how it works**: it finds out before it acts, plans with the risky part first, changes little at a
time, proves every claim and reports plainly. Nine skills write that way of working down as procedures,
so **any model** (a small Claude, Codex, a free local model) can follow it step by step.

Every agent loads `fable-method` at the start of a task (the kit's rules block says so). Fable itself
skips it.

## The loop

```
ORIENT -> FACTS -> PLAN -> ACT (one small step) -> PROVE -> ... -> REPORT
              ^                                      |
              +-------- facts changed: re-plan ------+
```

Before touching anything the agent writes:

```
GOAL:        what you want, in your words and meaning
DONE MEANS:  the check that proves it (a command, a number, a URL)
CONSTRAINTS: what must not happen
UNKNOWNS:    what it does not know yet that would change what it does
```

## The nine skills

| Skill | Loaded when | The habit it teaches |
|---|---|---|
| `fable-method` | Every task | The loop above, and which skill to use at each step |
| `fable-investigate` | It needs facts | Turn unknowns into questions a command can answer; the cheapest check that separates the possibilities |
| `fable-plan` | Bigger jobs | Work back from the goal; risky first; who does each step; a check per step; your decisions asked early, together |
| `fable-change-code` | Before editing | Read first; match the surrounding code; smallest diff; no extras; look before deleting |
| `fable-debug` | Anything fails | Read the whole error; reproduce; 2-3 causes; test that tells them apart; fix the cause; change approach after two failures |
| `fable-verify` | Before "done" | Proof with numbers; edge cases; nothing nearby broken; never trust a "success" message |
| `fable-decide` | A choice | Decide small reversible things; bring you money, access, commitments, irreversible and taste questions, with a recommendation |
| `fable-report` | Before reporting | Result first; numbers; failures stated; one question at most |
| `fable-self-check` | All the time | Red flags: "should work", retrying a failure, scope creep, a long report hiding the result |

## A worked example

You say: "Why do I get a failure email from my server every morning?" A worker following the method:

1. **Orient:** goal = find the cause and the fix; done = cause with evidence + exact fix; constraint =
   read only.
2. **Facts:** finds the script that sends the email, reads its list of watched services, compares with
   what is installed: three of four services no longer exist.
3. **Debug:** possible causes were (a) a real crash, (b) a stale list, (c) a mail bug. One check (are
   the services installed?) separates them: (b).
4. **Report:** "The watchdog checks three services that were removed. Fix: delete these three lines.
   Evidence: ... Not applied (read-only)."

This was a real test: a free local model, given only these skills, found the right cause with eleven
proven facts and changed nothing.

Next: [skills](05-skills.md).
