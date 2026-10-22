# AI capability boundary review

Use this when a discussion mixes technical capability, ethical permission,
consciousness claims, deployment safety, or responsibility for an AI-enabled
failure.

## capability evidence

- [ ] State the exact task being claimed, not a broad model ability.
- [ ] Name the evaluated system boundary: model, tools, retrieved sources,
      prompts, deterministic code, human operators, validation, and interface.
- [ ] Record the evidence: representative inputs, outputs, tool traces, tests,
      source citations, and failed/unknown cases.
- [ ] Separate current observed capability from speculation about future models
      or hidden internal states.

## permission and risk

- [ ] State whether the system can do the task separately from whether it should
      be allowed to do the task.
- [ ] List affected people, data classes, failure cost, abuse paths, and review
      requirements.
- [ ] Define allowed, forbidden, and review-only uses.
- [ ] Preserve opt-out, appeal, escalation, and human override routes where the
      workflow affects identity, money, reputation, safety, education, care, or
      access.

## deployment boundary

- [ ] Identify who supplies source data and who is accountable for its quality.
- [ ] Identify who authored or approved prompts, policies, tools, and permission
      scopes.
- [ ] Identify who monitors outputs, handles incidents, and can disable or roll
      back the system.
- [ ] Confirm logs and review artifacts can reconstruct the chain from input to
      action.

## emotional and support boundary

- [ ] Mark workflows involving grief, crisis, suffering, vulnerable users,
      personal identity, or high-stakes support.
- [ ] State when the system must defer to a human or support resource.
- [ ] Do not optimize emotionally loaded workflows only for speed, volume, or
      deflection.
- [ ] Avoid presenting an AI response as sufficient support for serious harm or
      crisis-adjacent situations.

## review output

A passing review produces a decision note with four separate answers:

1. What can this system do, under the observed boundary?
2. What is it allowed or not allowed to do, and why?
3. Who is responsible for source data, instructions, tool access, validation,
   deployment, monitoring, and remediation?
4. Where does the workflow preserve human judgment, escalation, or refusal?
