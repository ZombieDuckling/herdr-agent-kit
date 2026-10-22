---
name: fable-change-code
description: Load before you edit, create or delete files in a project. How Fable changes code - read the surrounding code first, match its style, make the smallest diff that does the job, no unasked extras, one change then check, look before you delete, commit cleanly without AI credit.
---

# Change code like Fable

Good changes look like the person who wrote the surrounding code made them. They are small, they do
exactly what was asked, and each one is checked before the next.

## Before the first edit

1. `git status --short` and `git branch --show-current`. Know where you are. Do not work on a branch
   or folder the task did not name.
2. **Read the file you will change, and the code that calls it.** Find how the project already does
   the same kind of thing (naming, error handling, comments, file layout). Do it the same way.
3. Find the project's own rules: `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, lint config, tests.
   Project rules win over your habits.
4. Find the check you will run after the change (build, test, lint, a curl, a page load).

## While editing

- **Smallest diff that does the job.** Do not reformat, rename or reorder code you were not asked to touch.
- **Match the surroundings:** same comment density, same naming, same idiom. Do not add comments that
  explain obvious code. Do not add new dependencies when the project already has a way.
- **No extras.** No "while I was here" features, refactors or cleanups. Write them in the notes as
  suggestions.
- **One logical change, then check it.** Build or test after each, not at the end of ten.
- **Big files:** create in parts. Never compose a whole long file in your thinking.
- **Exact edits.** Find the exact text, replace it. Re-read the result of a tricky edit.
- **Keep business facts unchanged** unless asked: phone numbers, addresses, prices, legal text, emails.
- **the user's design rules:** no CSS gradients or gradient overlays, ever. Respect `prefers-reduced-motion`.
  Real client photos before generated images; never present a generated image as a real photo.

## Deleting or overwriting

1. **Look at the target first** (`ls -la`, `cat`, `git log -- <path>`). Is it what you think it is?
2. Is it someone else's work, or shared? Then stop and ask.
3. Make a backup and write where it is, unless it is in git and committed.
4. Then delete, and say what you deleted.

## Committing

1. `git diff` - read every line. No debug code, no secrets, no unrelated changes, no stray files
   (briefs, logs, screenshots) unless they belong in the repo.
2. Run the project checks (`fable-verify`).
3. A clear message: what changed and why, in plain words.
4. **Never** add `Co-Authored-By`, "Generated with", or any AI credit. This is the user's hard rule.
5. **Never push, force-push, merge or deploy** without the user's word for that exact action.
