# Task: write one page of {{PERSON}}'s teaching site: {{SLUG}}.html

You are a worker. The lead gave you this brief. Follow it exactly. Plan in 10 lines or fewer, then use
your tools. Do not write the page inside your thinking: create the file with a tool, in parts if it is long.

## Facts (already checked; do not check again)
- The site folder is `{{SITE}}`. You write ONE file: `{{SITE}}/pages/{{SLUG}}.html`.
- Your source text is `{{SOURCE}}`. It is the truth: every command, path, number and rule in it must
  appear on your page, unchanged.
- The person this site is for is described in `{{SITE}}/data/profile.json` (name, what they do, their
  goals, their projects). Their machine is in `{{SITE}}/data/machine.json`.
- The allowed HTML pieces are in `{{KIT}}/demo/COMPONENTS.md`. Read it before you write.
- Images you may use: {{IMAGES}}

## Steps
1. Read `{{KIT}}/demo/COMPONENTS.md`, `{{SOURCE}}`, `{{SITE}}/data/profile.json` and `{{SITE}}/data/machine.json`.
2. Write `{{SITE}}/pages/{{SLUG}}.html`. It starts with the page-start block from COMPONENTS.md:
   the comment line `<!-- title: ... | description: ... -->`, then `<p class="eyebrow">{{EYEBROW}}</p>`, an `<h1>`, a `<p class="lede">`.
3. Turn the source into a page that teaches. Keep all its facts. Use the components: steps for
   procedures, tables for comparisons, `<pre><code>` for commands, callouts for rules and tips.
4. **Make it personal.** Where the source gives a generic example, use this person instead: their name,
   what they do, their goals, their projects (from profile.json). Example: a bakery owner gets
   "build the order page for Crumb & Co", not "build a site for my bakery". Where their machine is
   missing something the page talks about (machine.json), add a short callout saying so and how to add it.
   Do not invent facts about them; use only what profile.json and machine.json say.
   Write facts from machine.json in plain words: "the usage meter is not installed yet", never
   "usage mods: false" or other raw values.
5. Add **one** visual that helps understanding: an inline SVG diagram (rules in COMPONENTS.md), a herdr
   window, or a terminal block. Not decoration. Keep SVG diagrams simple: at most 6 boxes, one short label per box, labels inside
   their box with room to spare (estimate 9 px per character at font-size 14), nothing overlapping.
6. Check your file: `grep -c 'gradient' {{SITE}}/pages/{{SLUG}}.html` must print `0`;
   `grep -c '<script' {{SITE}}/pages/{{SLUG}}.html` must print `0`; `grep -c 'style=' {{SITE}}/pages/{{SLUG}}.html` must print `0`.
   For each command in the source (the lines inside its ``` blocks), confirm it appears on your page.

## Must not
- Change any file other than `{{SITE}}/pages/{{SLUG}}.html`.
- Add CSS, scripts, inline styles, gradients, external fonts or images not listed above.
- Invent features, numbers, testimonials or facts about the person.
- Run git, deploy commands, or `herdr` commands.

## Report (write exactly this at the end)
PAGE: {{SLUG}}.html
SOURCE FACTS KEPT: <number of commands from the source found on the page> of <number in the source>
PERSONAL TOUCHES: <one line each>
VISUAL: <what you added>
CHECKS: gradient=<n> script=<n> style=<n>
PROBLEMS: <none, or the exact problem>
