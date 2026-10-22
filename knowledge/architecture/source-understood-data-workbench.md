# source-understood data workbench

A data workbench is not source-grounded because it can produce charts or tables. It is source-grounded when a reviewer can trace every interpretation back to field meanings, source provenance, transformations, and caveats.

## components

| component | purpose | minimum contents |
|---|---|---|
| Source inventory | Names the inputs before analysis | dataset id, origin class, collection date or version, owner/authority class, allowed use, known gaps |
| Data dictionary | Prevents column-name hallucination | field name, meaning, unit, allowed values, null meaning, join key status, caveats |
| Transformation log | Separates source from derived signal | step id, input, operation, output, script/query pointer, row/count checks, reviewer |
| Analysis contract | States what questions may be answered | question, supported fields, forbidden inferences, confidence threshold, required visual/table outputs |
| Interpretation notes | Keeps judgment outside the generated artifact | claims, supporting rows/fields, assumptions, alternative explanations, human review notes |
| Review packet | Makes the output checkable | source sample, chart/table provenance, validation output, caveats, unresolved questions |

## flow

1. Inventory the source objects before loading them into a model.
2. Write or generate the data dictionary, then have a reviewer correct it.
3. Record every transformation as a separate step; never overwrite raw source.
4. Ask the model for structure, candidate charts, anomaly discovery, or prose only inside the analysis contract.
5. Attach review handles to outputs: source rows, field names, transformation step ids, checks, and caveats.
6. Publish conclusions only after a reviewer can explain the fields and transformations without relying on the model's prose.

## failure modes

- A polished chart has no source-row or transformation pointer.
- A model infers field meaning from a column name that the source does not define.
- Derived fields are mixed back into raw inputs without labels.
- The output reports correlations or rankings without caveats about missing data, sampling, or measurement limits.
- A conclusion survives because it looks plausible, not because the data supports it.

## acceptance test

A fresh reviewer can answer: what each input field means, which transformations created each derived field, which claims are supported, which claims are forbidden, and where uncertainty remains.
