---
name: fable-verify
description: Load before you say anything is done, fixed, working, safe or ready, and before anything leaves the machine (commit, push, deploy, PR, comment, email). The Fable standard of proof - re-run the done-means check, test the edges, check nothing nearby broke, verify workers' claims yourself, report numbers, name what was not checked.
---

# Verify like Fable

**"Done" is a claim that needs proof.** Fable does not say "should work", "looks good" or "probably
fine". It runs the check, reads the output, and puts the number in the report. What it could not
check, it names.

## Procedure

1. **Re-run the DONE MEANS check** from ORIENT. Read the full output. Write the result with numbers.
2. **Check the edges, not only the main case:**
   - phone width and desktop; slow network; reduced motion
   - empty input, very long input, the error path
   - running the script a second time (is it safe to run again?)
   - a fresh machine or a fake HOME, for setup scripts (`HOME=/tmp/x ./install.sh`)
3. **Check nothing nearby broke:** the full build, the full test suite, the pages next to the one you
   changed, the other users of the function you changed.
4. **Verify claims, not only your own work.** A worker's "done", a README's "supports X", a tool's
   "success" message: confirm with your own check. (A tool once printed success while the file was not
   changed. Reading the file is the proof, not the message.)
5. **Name what is not checked.** "Visual check: not done (no vision)". "Live deploy: not tested,
   not pushed." Never let silence suggest a check happened.

## Checklists

**Code:** `git status`, read `git diff`, build exit 0, tests all pass (count), `gitleaks dir .` no new
leaks, commit messages without AI credit (`git log -5 --format=%B | grep -ciE 'co-authored|generated with'` = 0).

**Websites:** no `gradient(` in styles; served locally with Playwright: console errors 0, 404s 0, axe
serious/critical 0; LCP and CLS on a throttled phone; contact facts identical to live
(`git diff | grep -E '^[-+].*(tel:|mailto:|wa\.me)'`).

**Code audits:** a real scanner, not reading alone: SonarQube (`sonar analyze` or eslint +
sonarjs) and `semgrep --config p/javascript --config p/security-audit`. Numbers in the report.

**Setup or config changes:** the thing actually uses the new setting (read the status line, the
process arguments, a test run) - not only "the file was written". Example: after pinning a model in a
config, start the program with a different "last used" model and confirm the pin wins.

**Before push or deploy** (only with the user's word): all above pass; `git log origin/<branch>..HEAD`
lists exactly the commits you expect; after it, check CI (`gh run list -L 3`) or the live URL.

## Output

```
VERIFIED: <check> -> <result with number>
VERIFIED: ...
NOT CHECKED: <what, and why>
```
