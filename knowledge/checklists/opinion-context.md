# opinion context checklist

Use this before a subjective, domain-heavy, brand, product, or advisory workflow
asks a model to produce or judge output. The goal is portable judgment, not a
larger prompt.

## minimum gate

- [ ] The opinion layer names the workflow or decision it governs.
- [ ] Principles are written as action-guiding rules, not slogans.
- [ ] Examples show accepted work, with why it was accepted.
- [ ] Anti-examples show rejected work, with why it fails.
- [ ] Hard constraints are separated from preferences.
- [ ] Review criteria say what a human or agent must inspect before acceptance.
- [ ] Source references point to sanitized, shareable files or public sources.
- [ ] Private names, accounts, domains, customer details, and live operational
      facts have been removed before sharing.
- [ ] The layer is small enough that a worker can load only the relevant section
      for the task.
- [ ] A fresh worker can cite which principle, example, or constraint drove its
      output or review.

## warning signs

- The expert must restate the same taste or domain rule in every session.
- The file contains only adjectives: premium, clean, bold, trustworthy, modern.
- The model is asked to infer forbidden topics, audience needs, or risk tolerance
  from a single prompt.
- One giant voice or brand file is loaded for every task, including small edits.
- Accepted and rejected examples are mixed without labels.
- The layer includes private operational facts that would identify the source.

## acceptance test

Give a fresh worker one request, the opinion layer, and the relevant source
artifact. It should produce or review the work, cite the rule/example it used,
and leave a review handle that a human can inspect.
