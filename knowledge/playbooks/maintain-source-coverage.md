# maintain source coverage during corpus ingestion

Use this when a corpus contains mixed evidence quality: full sources, partial
extracts, metadata-only records, failed fetches, OCR/transcript gaps, or rejected
items.

## output

Produce or update a manifest with a `source coverage` field and, when the corpus
is large enough, a short coverage index grouping source-backed, partial-source,
metadata-only, retry-pending, and rejected-too-thin items.

## procedure

1. **Classify before summarizing.** For each item, record whether the source was
   read, partially read, unavailable, or too thin to use.
2. **Separate progress from confidence.** A processed count may include every
   completed record, but the report must also show how many are source-backed
   versus source-limited.
3. **Constrain derived notes.** Metadata-only notes may describe only title,
   description, declared type, date, or other observed metadata. Do not infer
   unseen content.
4. **Keep retry state visible.** Failed fetches stay retry-pending until a new
   fallback, manual review, or explicit rejection changes their state.
5. **Promote patterns only from adequate evidence.** A theme, law, checklist, or
   reusable procedure needs source-backed or otherwise independently verified
   support. Metadata-only items can motivate a queue, not a doctrine.
6. **Verify links and counts.** Every processed item links to an existing note or
   artifact, every retry-pending item remains queued, and coverage totals match
   the manifest.

## stop conditions

Stop and label the item `rejected-too-thin` when the only available evidence is a
decorative title, a missing transcript, or an unverifiable generated artifact and
no safe transferable lesson can be derived.

Stop and repair the ingestion pipeline when coverage status is stored only in
prose summaries or reports, because the next agent cannot query it reliably.