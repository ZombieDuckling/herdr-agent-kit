# Agent-memory auxiliary textbook/PDF corpus pattern

Use when building a broad software-engineering / IT learning corpus inside a sanitized memory repository.

## User correction captured

If the user asks for “200 PDFs” or “actual textbooks,” do not satisfy it with mixed HTML links, course links, or general resource pages. They mean actual direct PDF resources. If a broader mixed-resource repertoire is useful, keep it separate and clearly label it as mixed-format.

## Legal/source boundary

- Do not scrape pirated textbook mirrors, shadow libraries, paywalled scans, or copied textbook chapters.
- Prefer public-domain, open-license/OER, author/publisher-provided free PDFs, official standards PDFs, and official course PDFs.
- Track source URL and license note; tell the user when redistribution rights are unclear.
- Keep binary PDFs out of Git by default unless the repository explicitly permits large binaries and the license clearly permits redistribution.

## Repository shape

Recommended structure:

```text
auxiliary-reports/
  README.md
  textbooks/
    README.md
    manifest.json                  # small seed of known-good PDFs
    pdf-manifest-200.json           # direct-PDF-only catalog when user asks for 200 PDFs
    pdf-catalog-200.md              # readable index with local pdfs/<file>.pdf paths
    download-textbooks.sh           # seed downloader
    download-200-pdfs.py            # large corpus downloader
    download-200-pdfs-parallel.py   # gap-fill downloader for large corpora
    pdf-download-report.tsv         # present/downloaded/failed status for every manifest item
    pdf-checksums-200.sha256        # one checksum per manifest PDF
    pdfs/                           # actual PDF knowledge base
```

Default to a reproducible manifest/cache for exploratory work, but if the user explicitly says the repo is a knowledge base, not a link tracker, commit the actual PDFs. Use Git LFS rather than normal Git blobs for large PDF corpora:

```sh
git lfs install --local
git lfs track 'auxiliary-reports/textbooks/pdfs/*.pdf'
git add .gitattributes auxiliary-reports/textbooks/pdfs/*.pdf
```

If hidden filenames exist, stage them explicitly; shell globs may miss names such as `.net-*.pdf`.

## Sanitized repo gotchas

A shared memory repo may reject otherwise-public URLs when they resemble private paths or identifiers. Filter direct PDF URLs before committing manifests:

- reject `/users/` or `~user` path components if the repo treats personal paths as sensitive;
- reject long opaque hex path components that trip secret/account/transaction scanners;
- reject known pirate domains even if the URL is a direct PDF.

If the repo gate fails, remove the offending URL entirely; do not mask it.

## Verification

Before pushing a PR:

1. Generate the direct-PDF manifest and assert `count == requested_count`.
2. Download the PDFs and verify the manifest maps to actual local files, not just URLs.
3. Check for duplicate cache filenames; `200` manifest entries can collapse into fewer distinct files if titles normalize to the same filename. Rewrite duplicate filenames or fill replacements until `manifest_count == distinct_pdf_file_count == checksum_count`.
4. Rebuild `pdf-download-report.tsv` and `pdf-checksums-*.sha256` from the final manifest.
5. Verify checksums against the files and verify every manifest item has a present PDF file over a minimum size threshold.
6. Verify LFS applies to every PDF path with `git check-attr filter -- <path>` or `git lfs ls-files` after staging.
7. Run the repo preflight after staging so new files are scanned.
8. Report the true local file count, checksum count, approximate corpus size, LFS status, and CI status.

## GitHub Actions + LFS pitfall

If a repo workflow creates `git worktree` checkouts for guard self-tests, newly committed LFS PDFs can break CI because Actions may try to smudge/download LFS objects without credentials. The redaction/index guards usually do not need PDF contents. Patch the workflow to skip LFS smudge for checkout/worktree, for example:

```yaml
- uses: actions/checkout@<pinned-sha>
  env:
    GIT_LFS_SKIP_SMUDGE: "1"
  with:
    fetch-depth: 0
    persist-credentials: false
    lfs: false
```

and for worktree creation:

```sh
GIT_LFS_SKIP_SMUDGE=1 git worktree add -q "$tmp/wt" HEAD
```

`git lfs install --local` may generate hook files under the repo's configured hook path. If they appear as untracked repo files and are not intended project policy, remove them before commit.

## Wording for PRs

Be explicit:

- “200 direct-PDF resources in the manifest” is not the same as “200 PDFs downloaded locally.”
- If the user says “knowledge base, not link tracker,” commit actual PDFs through Git LFS and say so.
- “This excludes pirated mirrors and mixed HTML/course links.”
