---
name: github-cross-repo-triage
description: Use when finding assigned GitHub work across repos.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [GitHub, Issues, Pull-Requests, Triage, Organizations]
---

# GitHub Cross-Repo Triage

## When to use

Use when the user asks what issues, PRs, review requests, or tasks are assigned to them across a GitHub org/account rather than inside the current repository. Also use when GitHub notification emails mention PRs or issues to handle; email is discovery, but GitHub is the source of truth for state and permissions.

## Principles

1. **Do not rely on repo-local commands for org-wide answers.** `gh issue list` and `gh pr list` are repo-scoped unless every target repo is queried explicitly.
2. **Prefer per-repo queries when the org is known.** GitHub search can hit secondary rate limits and exposes different JSON fields than repo-local commands.
3. **Use the real viewer login.** `@me` works in some `gh` contexts but not all search contexts; `gh api user --jq .login` is safer.
4. **Read each item before summarizing work.** Listing titles is not enough; open issue/PR bodies and comments to extract requirements, constraints, and acceptance criteria.

## Workflow

### Living org dashboard requests

When the user asks for a living dashboard over a GitHub org, do not stop at a one-time triage summary. Build a pullable private repo with a deterministic refresh script, static dashboard assets, generated JSON, and a scheduler. Use `references/living-org-dashboard.md` for the full recipe.

### Your own PR backlog

When the question is "how does my PR side look" or "what's left of what I merged", answer with counts and buckets, never a raw list:

```bash
gh search prs --author=@me --state=open --limit 200 \
  --json repository,number,title,isDraft,createdAt
gh search prs --author=@me --merged --limit 100 \
  --json repository,number,title,closedAt    # --merged, NOT --state=merged
```

Group the open set by repo, then for every non-draft PR read the merge state in one pass and bucket it — the bucket is the answer to what needs doing:

```bash
gh pr view <number> -R <owner/repo> \
  --json mergeable,mergeStateStatus,statusCheckRollup,reviewDecision
```

- **Ready** — `CLEAN`/`MERGEABLE` with all checks successful. Safe to merge.
- **Needs a look** — `UNSTABLE` (a check running or failing). Read the failure before touching it.
- **Conflicting** — `DIRTY`/`CONFLICTING`; needs a rebase, and rebase onto the clean sibling PR rather than the other way round.
- **Blocked with no checks at all** — `BLOCKED` and an empty `statusCheckRollup` means branch protection is waiting on a review, not a broken PR. Report it as a decision for the user, not a defect you can fix by pushing.

Also compare against the previous count you reported so the user sees what they cleared, and name the pile that grows on its own (scheduled jobs that open a PR daily) — that one needs a merge-or-stop decision, not routine merging.

### 1. Identify login and repos

If the trigger comes from email, first read the complete notification body and extract canonical GitHub URLs. Then verify each target with explicit repository flags:

```bash
himalaya envelope list -a gmail -s 20 -o json from notifications@github.com
himalaya envelope list -a gmail -s 20 -o json body github.com/OWNER/REPO/pull
himalaya message read -a gmail <message-id>

gh pr view <number> --repo OWNER/REPO \
  --json number,title,url,author,baseRefName,headRefName,isDraft,mergeable,reviewDecision,statusCheckRollup,body,updatedAt
```

Do not trust display names in mail as GitHub usernames. Notification senders may be human display names, bots, or `notifications@github.com`; the PR URL and `gh pr view` author fields are authoritative.

```bash
LOGIN=$(gh api user --jq .login)
ORG=<org-or-user>
gh repo list "$ORG" --limit 200 --json nameWithOwner,description,isPrivate,updatedAt,url
```

### 2. Query each repo explicitly

```bash
for repo in $(gh repo list "$ORG" --limit 200 --json nameWithOwner --jq '.[].nameWithOwner'); do
  echo "=== $repo issues assigned to $LOGIN ==="
  gh issue list --repo "$repo" --state open --assignee "$LOGIN" \
    --limit 100 --json number,title,state,url,updatedAt,author,labels,assignees

  echo "=== $repo PRs assigned to $LOGIN ==="
  gh pr list --repo "$repo" --state open --assignee "$LOGIN" \
    --limit 100 --json number,title,state,url,updatedAt,author,labels,assignees,isDraft,reviewRequests

  echo "=== $repo PRs requesting review from $LOGIN ==="
  gh pr list --repo "$repo" --state open --search "review-requested:$LOGIN" \
    --limit 100 --json number,title,state,url,updatedAt,author,labels,isDraft,reviewRequests
done
```

### 3. Read requirements

For every assigned item:

```bash
gh issue view <number> --repo <owner/repo> \
  --json number,title,state,url,author,assignees,labels,body,comments,updatedAt,createdAt

gh pr view <number> --repo <owner/repo> \
  --json number,title,state,url,author,assignees,labels,body,comments,reviewRequests,files,updatedAt,createdAt
```

Extract:

- concrete required work;
- sequencing/order comments;
- explicit constraints;
- acceptance criteria / definition of done;
- blockers and decisions that must return to the human.

## Pitfalls

- `gh issue list --json repository` is invalid for repo-local issue list. Add the repo name yourself from the loop.
- `gh pr list` and `gh search prs` expose different JSON fields; do not assume `reviewDecision` is available everywhere.
- `gh search prs --state=merged` is invalid — gh fails and the subsequent JSON parse is what surfaces the error. The merged-history flag is `--merged`; open PRs use `--state=open`.
- Secondary rate limits are not a signal that there are no assignments. Fall back to per-repo queries.
- Broad repo search for terms such as `<org keyword> OR <client keyword>` may miss private org repos; enumerate org repos directly when the org is known.
- Treating a GitHub notification as handled after reading email is incomplete; extract the PR/issue URL and handle the GitHub object itself because review state, CI, mergeability, and permissions live on GitHub.
- Omitting `--repo owner/repo` on PR commands after email discovery can target the current checkout instead of the notified repository; pass it on every `gh pr view/checks/diff/review/merge` call.
- If merge fails for permissions after review and checks pass, stop at the highest permitted action such as approval or a comment and report the permission blocker exactly; do not retry through lower-level APIs or imply merge success.
