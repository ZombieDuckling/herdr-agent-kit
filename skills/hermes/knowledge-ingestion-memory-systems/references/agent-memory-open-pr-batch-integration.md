# Agent-memory open PR batch integration

Use this when a sanitized memory repository has multiple open PRs and the user asks to "handle them all" rather than review one PR.

## Working pattern

1. Start by reading the repo-local contribution rules (`AGENTS.md`, `CONTRIBUTING.md`) and listing every open PR with head branch, draft state, merge state, and check rollup.
2. Process PRs oldest-first unless there is a dependency order visible in titles or diffs. After every merge, refresh `origin/main` before touching the next PR.
3. For each PR:
   - checkout the PR branch;
   - merge current `origin/main` into it instead of assuming the old guard result is still meaningful;
   - resolve conflicts additively when entries are independent laws/playbooks/index rows;
   - if law IDs collide, keep the already-merged main ID stable and renumber the incoming law to the next free ID, then update all index anchors;
   - run the repository's full preflight locally before pushing;
   - push integration commits and wait for the branch guard to pass;
   - mark draft PRs ready only after local and remote gates pass;
   - squash-merge and delete the branch.
4. After the last merge, verify: open PR list is empty, local main fast-forwards to origin, full local preflight passes, and post-merge main guard succeeds.

## Timeout recovery

Long `gh pr checks` / merge loops can time out after pushing or merging. Treat timeout as ambiguous side effect:

- inspect `git status --short --branch`, recent local commits, `gh pr list`, `gh pr view <n>`, and recent `gh run list` before retrying;
- never re-run a side-effecting merge/push blindly;
- if the PR branch has a new merge commit and checks are running or passed, continue from that state.

## Sanitized memory repo conflict rule

When conflicts are index/list collisions, prefer additive resolution:

- keep both entries if both are transferable and sanitized;
- renumber the incoming entry rather than rewriting history already on `main`;
- update README / MANIFEST / architecture / playbook indexes consistently;
- run link/index validation after resolution.

## Reporting

Final report should name merged PR numbers/titles, any integration fix made, local gate status, remote guard status, remaining open PR count, and final main head. Do not over-narrate every polling attempt.
