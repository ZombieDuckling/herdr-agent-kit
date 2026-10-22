# source-understood data analysis checklist

Use before accepting AI-assisted research, tables, charts, rankings, or conclusions.

- [ ] Source inventory lists every input object and its provenance class.
- [ ] Raw source is preserved separately from derived outputs.
- [ ] Data dictionary defines every field used in the analysis.
- [ ] Units, null values, categorical values, and join keys are documented.
- [ ] Transformation log records each cleaning, filter, aggregation, join, labeling, or sampling step.
- [ ] Row counts, checksums, or equivalent sanity checks exist before and after material transformations.
- [ ] The analysis contract states the questions being answered and the inferences that are out of scope.
- [ ] Generated charts/tables include source pointers and transformation step ids.
- [ ] Claims cite the fields/rows/aggregates that support them.
- [ ] Caveats name missing data, sampling limits, measurement limits, and plausible alternative explanations.
- [ ] A human reviewer can explain the source meaning and transformation path without relying on the generated prose.
- [ ] Outputs that fail review are turned into dictionary fixes, transformation fixes, or explicit non-claims.
