# workbench components

A folder becomes a useful AI workbench only when a fresh operator can orient,
ask, act, review, and recover without reading the previous chat.

## minimum viable workbench

### front desk

A workbench needs one obvious entry point that answers:

- what this workspace is for;
- what is canonical;
- what is mutable;
- what has been done;
- what to read first;
- what must never be edited or exported.

If a new agent cannot answer “what is here?” from this file, the workbench is not
ready.

### task-room router

The front desk should route the operator to smaller room or workflow context
files. Each room router answers the operational question: for this class of task,
what should the worker load, avoid, produce, and check?

Use a table before building custom orchestration:

| Trigger | Read first | May use | Protect / skip | Output location | Verification |
|---|---|---|---|---|---|
| New brief | brief template, source manifest | approved helper scripts | raw private exports, unrelated rooms | drafts or work items | file exists, links resolve |
| Asset edit | source map, component guide | renderer, design checklist | originals unless explicitly authorized | component or output folder | targeted change renders |
| Source summary | manifest row, source pointer | transcript or extraction helper | full raw source in exportable notes | derived notes | note is linked from manifest |

If the table is too large to scan, split the room. If the table cannot name a
verification path, the workflow is not ready for automation.

### catalog

The catalog lists every important source, artifact, note, script, decision, and
output. It is not decoration. It is the navigation layer that prevents expensive
rediscovery.

The catalog must include:

- stable item id;
- human title;
- source location or source pointer;
- type;
- owner or role, not a personal name;
- status;
- last reviewed time or revision;
- verification path.

### source shelf

The source shelf keeps source material separate from derived work. Derived notes
can be edited; source material is preserved or referenced.

For private or copyrighted material, store derived notes and source pointers in
the shareable workbench. Keep raw material in the private source layer.

### opinion layer

The opinion layer captures the judgment that makes subjective or domain-heavy
work non-generic: principles, examples, anti-examples, hard constraints,
preferences, edge cases, decision logs, and review rubrics.

Do not use one giant taste file for every task. Route only the relevant judgment
files, and keep private source-identifying facts out of any exportable layer.

### request slips

A request slip turns vague intent into bounded work. It records:

- goal;
- inputs;
- allowed tools;
- forbidden actions;
- expected output;
- verification requirement;
- human review owner.

Without a request slip, the agent guesses the job and the reviewer grades a job
that was never agreed.

### work ledger

The work ledger records what changed, not what the agent thought about changing.
It should include:

- files written;
- commands or tools used;
- tests and checks run;
- known limitations;
- follow-up decisions.

### review surface

Every workbench needs an output surface made for review: a rendered document,
spreadsheet, screenshot, diff, source table, report, or dashboard. A hidden file
that only the agent knows exists does not count.

### tool registry

The tool registry describes each available tool by job, input contract, output
contract, side effects, and failure modes. If the agent cannot state the contract,
it must not improvise with the tool.

### state boundary

Separate these states:

- canonical template;
- mutable workbench copy;
- private source layer;
- generated artifact;
- exportable deliverable;
- secret/integration layer.

Most workbench failures come from mixing these states.

## done definition

A workbench is usable when a fresh authorized operator can:

1. read the front desk;
2. find the catalog;
3. ask a grounded question;
4. run or request a bounded task;
5. inspect the output;
6. verify the evidence;
7. hand the work to another operator without sharing a chat transcript.
