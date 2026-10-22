# PR verification for static deploy-staging branches

Use this when a static site has an open PR that hardens deployment by staging a public-only bundle (for example Cloudflare Pages `dist/`), but the workflow only runs on `push` to the default branch so the PR has no useful checks.

## Reliable slice

1. Work on the existing PR branch instead of creating a duplicate PR.
2. Add a `pull_request` trigger for the default branch.
3. Keep the deploy job in one workflow if that is the smallest diff, but gate the actual deploy step:
   ```yaml
   if: github.event_name != 'pull_request'
   ```
   This lets PRs verify without requiring deployment secrets or publishing preview artifacts.
4. After the staging step, add a verifier that asserts:
   - internal/private paths are absent from the staged bundle (`docs`, host config such as `vercel.json`, agent state like `.omc`, `.github`, `.gitignore`)
   - leaked files are absent (`*.md`, `.git*`, `.DS_Store`)
   - required public entrypoints/assets exist
   - local HTML `href` and `src` targets resolve inside the staged bundle
5. Run the same staging and verification script locally, then `git diff --check` and a YAML parse/lint before pushing.
6. After pushing, watch the PR check with `gh pr checks <number> --watch --interval 10` and comment on the PR with the commit, local verification, and Actions result.

## Minimal verifier skeleton

```yaml
- name: Verify staged dist
  run: |
    set -euo pipefail

    for path in docs vercel.json .omc .github .gitignore; do
      if [ -e "dist/$path" ]; then
        echo "::error::private path staged: $path"
        exit 1
      fi
    done

    leaked_files=$(find dist \( -name '*.md' -o -name '.git*' -o -name '.DS_Store' \) -print)
    if [ -n "$leaked_files" ]; then
      echo "::error::leaked files in staged output:"
      echo "$leaked_files"
      exit 1
    fi

    failed=0
    while IFS= read -r html_file; do
      while IFS= read -r ref; do
        [ -z "$ref" ] && continue
        if [ ! -e "dist/$ref" ]; then
          echo "::error::$html_file -> broken local asset/link: $ref"
          failed=1
        fi
      done < <(
        grep -oE '(href|src)="[^"]+"' "$html_file" \
          | sed -E 's/^(href|src)="//; s/"$//' \
          | grep -vE '^(https?:|mailto:|tel:|#|//)' \
          | sed -E 's/[?#].*$//' \
          | sort -u
      )
    done < <(find dist -maxdepth 1 -name '*.html' -print | sort)
    exit "$failed"
```

Adapt the required-file list to the repo's actual public pages and assets. Do not include deploy-secret validation in PR checks; PR verification should be safe without secrets.