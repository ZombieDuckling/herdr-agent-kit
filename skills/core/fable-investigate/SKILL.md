---
name: fable-investigate
description: Load when you must find out facts before deciding or acting - which version is live, what a system does, why something is the way it is, whether a tool or repo is safe and worth using. The Fable way to investigate - turn unknowns into checkable questions, pick the cheapest test that separates the possibilities, read the real source.
---

# Investigate like Fable

The goal of investigation is not to read a lot. It is to **remove the unknowns that change your
decision**, with the least work, and to have proof for each answer.

## Procedure

1. **List the unknowns** (from ORIENT). For each, write the question as one sentence.
2. **For each question, list the possible answers** (usually 2 or 3).
3. **Find the cheapest check that tells the answers apart.** Cheap = fast, read-only, small output.
   Ask: "What would I see if answer A is true? And if B is true?" Then look for exactly that.
4. **Run it. Read the output fully.** Write the fact with its proof:
   `FACT: <fact> (proof: <command> -> <key output>)`
5. **Stop when the remaining unknowns no longer change your plan.** More reading after that is waste.

## Where facts come from (best first)

1. The running thing: the live URL (`curl -sI`, download the page), the process (`ps`, `lsof`), the
   service status, the database row, the pane (`herdr pane read`).
2. The source of truth on disk: the file, the config, `git log`, `git status`, the lock file.
3. Tool output you produce now: a build, a test, a dry run.
4. Documentation and READMEs - these can be old. Check a claim before you rely on it.
5. Your memory, notes and worker reports - these are claims. Check them before you repeat them.
   Search memory by the **systems** involved, not only the project name:
   `grep -ril '<machine or service name>' your agent's memory folder (`~/.claude/projects/<project>/memory/`)`. (A test lead read
   only the project's memory file and missed the one that said the service it was debugging was retired.)

## Patterns Fable uses

- **Fingerprint match.** "Which version is live?" Do not read code. Take something unique from the
  live thing (bundle file names with hashes, a version string, a checksum) and compare it with each
  candidate. One match = the answer. Example: build `origin/main` and the old working copy; only the
  working copy's bundle hashes matched the live site, so the live site was NOT main.
- **Read before you run.** For an unknown repo, script, plugin or download: list its files, read the
  entry points, and grep for network calls (`fetch(`, `https://`, `curl`), shell calls
  (`child_process`, `exec`, `spawn`) and file writes. Decide from that, then run it.
- **Ask the system, not the docs.** `<tool> --help`, `<tool> --version`, the actual config file.
  Flags change between versions (OpenCode v2 has no `--model` on the TUI; `opencode run` has `-m`).
- **Look at your own screen.** You can read your own pane: `herdr pane read "$HERDR_PANE_ID"`.
  Things drawn for the human (status lines, model name, usage bars) are visible there.
- **Count, do not estimate.** `wc -l`, `du -sh`, `grep -c`, `git diff --stat`. Put the number in the report.
- **Check what is already running** before you start anything: `herdr agent list`, `ps`, `lsof -i`.

## Judge worth, not only facts

When the task is "should we use X" or "install X": after the facts, judge each part against the user's
setup. Write: useful / not useful / why, in one line each. Recommend the subset worth having.
(Example: of 25 mods, two were worth it; two others were rejected because each made a paid model call
after every turn in every agent.)

## Output

```
QUESTION: <unknown>
FACT: <answer> (proof: <command> -> <output>)
DOES IT CHANGE THE PLAN: yes/no - <how>
```
