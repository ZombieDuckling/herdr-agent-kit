# Source-backed knowledge-base artifact delivery: session note

This note captures a correction from a repository knowledge-base task where the
user asked for "full textbooks" and later challenged that the result looked like
thin Markdown/link tracking. Use it to avoid repeating that failure mode.

## Durable lesson

When the user asks for a knowledge base with downloadable source artifacts, do
not satisfy the request with catalogs, manifests, summaries, or standards bulk
unless the user explicitly accepts that scope. The deliverable must contain the
artifact class they asked for and must be easy to find in the remote repository.

## Practical rules

- Treat "knowledge base, not a link tracker" as requiring local artifact bytes,
  not only URLs or generated notes.
- Treat "full textbooks" as meaning actual book-length educational PDFs, not a
  mostly RFC/NIST standards corpus.
- Do not pad a target count with marginally related standards to hit a numeric
  goal. If licensing blocks full textbooks, report the trade-off before merging
  a diluted corpus.
- Verify both local and remote presence:
  - local file count and size;
  - Git LFS tracking count when binaries use LFS;
  - GitHub contents API or web path count;
  - sample remote file metadata that shows real LFS object size;
  - clone/LFS retrieval instructions.
- Make the artifact path visible from the repository root, agent instructions,
  manifest, and directory map.
- If Git LFS is used, explain that GitHub raw/tree views may show pointer files
  and that `git lfs pull` is required for real bytes.

## Review gate nuance

Adversarial review is useful, but it can optimize for legal safety at the cost of
user intent. If review forces removal of desired artifacts, loop back to a
better source list rather than replacing the requested artifact class with a
technically safe but semantically weak substitute.
