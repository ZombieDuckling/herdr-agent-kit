# turn a corpus into a surrogate index

Use this when the source is too large, visual, noisy, or expensive to analyze on
every question.

## steps

1. Create a manifest with stable ids.
2. Decide the cheapest adequate extraction path per source type.
3. Generate compact descriptions, captions, summaries, or extracted rows.
4. Store every surrogate record with a source pointer.
5. Build indexes over themes, entities, decisions, and problems.
6. Search the surrogate first.
7. Verify important findings against the original source span.
8. Promote durable lessons into notes, checklists, or playbooks.

## acceptance test

A user can search the text layer, jump to the original source span, and verify the
claim without reprocessing the whole corpus.
