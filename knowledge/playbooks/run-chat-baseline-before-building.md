# run a chat baseline before building

Use this before proposing custom AI software for an advisory, classification,
matching, drafting, or triage workflow.

## steps

1. Name the repeated job and the decision the system should improve.
2. Collect 3-5 representative inputs that are safe to use in the test context.
3. Write the smallest domain prompt that includes the task, constraints, output
   shape, and review expectations.
4. Run the prompt in an ordinary chat surface with the representative inputs.
5. Record what the baseline gets right, what it gets wrong, and what it cannot
   access.
6. Classify every gap:
   - source-feed access;
   - editable reference data;
   - deterministic validation;
   - matching or scoring;
   - attachment or document handling;
   - persistence and audit;
   - permissions, secrets, or privacy;
   - review workflow;
   - scale, scheduling, or cost control.
7. Build only the smallest layers that close the classified gaps.
8. Keep the chat prompt as a regression case or fallback until the product layer
   clearly outperforms it.

## output

The build brief should include:

- baseline prompt and input class;
- observed baseline quality;
- missing layers;
- simpler mechanisms rejected;
- proposed architecture;
- acceptance evidence for the first product slice.

If the baseline already solves the job and no repeatable gap remains, do not
build a product; package the prompt, checklist, or template instead.
