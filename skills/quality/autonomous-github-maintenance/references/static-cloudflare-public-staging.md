# Static Cloudflare Pages public staging

Use this pattern during autonomous portfolio maintenance for static HTML/CSS/JS sites deployed to Cloudflare Pages when the workflow currently uploads the repository root.

## When to choose this slice

- The repo is a static site with Cloudflare Pages deployment via GitHub Actions.
- The deploy command uploads `.` or another broad checkout path.
- The repo contains internal non-public files such as `docs/`, planning briefs, dotfiles, obsolete host config (`vercel.json`), agent state, or root Markdown files.
- There are no urgent failing PRs/issues, and a small production-hygiene PR is safer than changing site content.

## What to verify first

1. Inspect repo state before editing:
   - `git status --short --branch`
   - remotes and recent commits
   - open PRs and recent Actions runs
2. Confirm the production exposure if safe:
   - `curl -L -s -o /dev/null -w '%{http_code}\n' https://example.com/docs/internal.md`
   - `curl -L -s -o /dev/null -w '%{http_code}\n' https://example.com/vercel.json`
3. Treat `200` for internal docs/config as a real hygiene issue even if the files are not secret.

## Implementation pattern

Stage a public deploy bundle and deploy that directory instead of the repo root:

```yaml
      - uses: actions/checkout@v4

      - name: Stage public site files
        run: |
          mkdir dist
          rsync -a \
            --exclude '.git*' \
            --exclude '.omc' \
            --exclude 'docs' \
            --exclude 'vercel.json' \
            --exclude '*.md' \
            --exclude 'dist' \
            ./ dist/

      - name: Deploy to Cloudflare Pages
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
        run: npx --yes wrangler@latest pages deploy dist --project-name <project-name> --branch main
```

Notes:
- `--exclude '.git*'` excludes `.git`, `.github`, and `.gitignore`.
- Keep the change cohesive: staging/deploy hygiene only. Deleting obsolete configs or adding cache headers can be separate PRs.
- Do not expose or edit Cloudflare tokens/secrets.

## Local verification

Run a staging smoke check before committing:

```bash
STAGE=/tmp/site-dist-verify
mkdir "$STAGE"
rsync -a \
  --exclude '.git*' \
  --exclude '.omc' \
  --exclude 'docs' \
  --exclude 'vercel.json' \
  --exclude '*.md' \
  --exclude 'dist' \
  ./ "$STAGE"/

test -f "$STAGE/index.html"
test -f "$STAGE/css/site.css"
test -f "$STAGE/js/site.js"
test -d "$STAGE/assets"
test ! -e "$STAGE/docs"
test ! -e "$STAGE/vercel.json"
test ! -e "$STAGE/.github"
test ! -e "$STAGE/.gitignore"

git diff --check
git diff --stat
```

If the repo has a different public asset layout, adapt the `test -f` checks to the actual site files.

## PR report details

Include:
- Current production status codes for public page(s) and internal/config URLs.
- Exact files preserved and excluded by the local staged bundle.
- Whether the repo has PR checks. If the deploy workflow only runs on `main`, say no PR checks are expected instead of implying CI verified the PR.