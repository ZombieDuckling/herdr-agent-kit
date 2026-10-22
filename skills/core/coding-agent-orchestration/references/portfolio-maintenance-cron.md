# Portfolio-Wide GitHub Maintenance Cron Pattern

Use this when the user asks to “keep all projects active/maintained,” not just one named repo.

## Trigger

- User asks for ongoing maintenance across all GitHub projects.
- User broadens a single-repo maintainer job to all repos.
- User wants Claude/agent automation to keep repos alive with PRs.

## Durable pattern

Create or update one recurring maintainer job whose workdir is the user’s home directory, not a single repo. The job must discover live repo state each run instead of relying on memory.

Core live discovery:

```bash
gh repo list "$GH_OWNER" --limit 200 \
  --json nameWithOwner,name,description,isPrivate,isFork,isArchived,primaryLanguage,updatedAt,pushedAt,url,defaultBranchRef
```

Also inspect local repos under likely roots only when they have GitHub remotes clearly belonging to the user:

- `~/Projects`
- `~/Documents`
- `~/Desktop`

## Operating rules for the cron prompt

- Use Claude Code as the primary coding worker where available.
- Do not spawn uncontrolled swarms; use focused inspect → plan → implement → verify → PR waves.
- Never auto-merge, force-push, delete branches, or expose/modify secrets.
- Before editing a repo, inspect `git status --short --branch`, current branch, remotes, recent commits, open PRs, and CI state.
- If there are uncommitted user changes, skip/report or use a separate clean worktree/clone; never overwrite.
- Normally touch one repo and one coherent slice per run.
- Prioritize open failures, stale but strategic projects, CI/test fixes, README accuracy, dependency health, smoke tests, and small original/product improvements.
- Commit, push, and open/update a PR for meaningful changes; update an existing matching PR instead of creating duplicates.

## Required final report from each cron run

- Selected repo and why it was chosen.
- Branch name.
- PR URL if created/updated.
- Commit SHA if any.
- What changed.
- Real verification output summary.
- Blockers/skips.
- Next recommended repo or slice.

## Pitfall

If the user first asks for a maintainer on one repo and later says “actually all projects,” update the existing cron job rather than creating a second overlapping job. Overlapping night jobs can compete for the same GitHub/auth/local resources and create duplicate PRs.