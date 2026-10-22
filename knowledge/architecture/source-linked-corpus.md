# source-linked corpus architecture

Large corpora are not searched directly. They are turned into compact,
source-linked surrogates first.

## layers

### raw source layer

This is the original material: documents, images, audio, video, emails, exports,
logs, spreadsheets, or folders. It is expensive to process and often unsafe to
publish.

Rules:

- preserve or reference originals;
- do not edit source material during analysis;
- record provenance;
- keep private material out of shareable repos.

### manifest layer

The manifest is the authoritative inventory. Every later artifact points back to
it.

Minimum fields:

- id;
- title;
- source pointer;
- type;
- size or duration if useful;
- collection;
- processing status;
- derived artifacts;
- verification status.

### surrogate layer

The surrogate is compact text or structured metadata generated from the source.
It can include:

- summaries;
- captions;
- frame labels;
- transcript segments;
- extracted tables;
- keywords;
- timestamps;
- source spans;
- confidence notes.

The surrogate is a navigation aid, not the evidence. Every row must point back
to the source span a human can verify.

### index layer

The index lets agents and humans find useful source spans without reprocessing
the entire corpus.

Useful indexes include:

- theme index;
- people or role index;
- problem and solution index;
- artifact index;
- decision index;
- tool and script index;
- unanswered questions index.

### review layer

High-value findings must be reviewed against source. The review layer records:

- claim;
- source pointer;
- exact supporting span or timestamp;
- reviewer role;
- decision;
- confidence;
- follow-up.

## processing loop

1. Inventory first.
2. Sample or extract cheaply.
3. Write surrogate records with source pointers.
4. Build indexes over the surrogate.
5. Search the surrogate.
6. Verify against source before acting.
7. Promote durable lessons into notes, checklists, or skills.

## anti-patterns

- asking a model to reread raw media for every question;
- summarizing without source pointers;
- treating generated captions as evidence;
- letting raw private material leak into shareable output;
- using a vector store as the only catalog;
- losing the original span after compression.
