# domain reference workbench

Use this shape when a plain chat prompt proves that a domain advisory workflow is
valuable, but a real product needs repeatable data access, editable reference
knowledge, scoring, diagnostics, and reviewable evidence.

## promotion rule

Do not build the workbench until a chat baseline has been run with representative
inputs. The baseline report should say what the chat surface already solves and
which product layers are still missing.

## layers

### intake profile

Capture the user's operating profile in a structured file or form:

- goals and constraints;
- capabilities or inventory;
- geography or jurisdiction class when relevant;
- eligibility facts;
- missing-field diagnostics;
- freshness date and owner.

### source feed

Ingest the authoritative opportunity, rule, document, or catalog feed separately
from model prompts:

- source URL or file handle;
- retrieval time;
- source type;
- normalized identifiers;
- attachments or linked documents;
- refresh cadence;
- tombstone/deletion handling.

### editable reference data

Keep codes, categories, rule snippets, synonyms, and eligibility criteria in
reviewable tables or files. A wrong mapping should be corrected in the reference
data before anyone reaches for fine-tuning or prompt accretion.

### matching and scoring

Use deterministic filters and vector or statistical similarity as triage, not as
final authority:

- exact filters for hard constraints;
- similarity scores for ranking large feeds;
- reason fields that explain which profile facts and reference entries matched;
- thresholds that route to review rather than automatic action.

### explanation and coaching

The model layer explains results, suggests profile improvements, drafts next
steps, and translates domain language. It must cite source and reference handles
instead of inventing authority.

### evidence and review surface

Each recommendation should expose:

- source record;
- profile version;
- reference-data version;
- score or route reason;
- missing inputs;
- attachments reviewed;
- human decision and timestamp.

## anti-patterns

- Hiding all domain knowledge in one large prompt.
- Treating similarity rank as eligibility or approval.
- Building an app before the chat baseline shows the repeated job.
- Fixing wrong classifications by adding prose caveats instead of editing the
  reference table.
- Shipping without source handles, review fields, or profile diagnostics.
