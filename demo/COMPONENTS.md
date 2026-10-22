# Page components

Every page body is plain HTML built only from these pieces. The styles already exist
(`assets/styles.css`); do not add CSS files, `<style>` blocks, inline `style=""` or gradients. Do not
add `<script>`; `assets/app.js` already handles navigation, copy buttons, the catalogue and the machine table.

## Page start (always first)

```html
<!-- title: Orchestrating in practice | description: How the lead starts, briefs, watches and closes workers in herdr. -->
<p class="eyebrow">Chapter 03</p>
<h1>Orchestrating in practice</h1>
<p class="lede">One or two sentences that say what the reader will be able to do after this page.</p>
```

## Headings and text
`<h2>` for sections, `<h3>` inside them. Paragraphs `<p>`, lists `<ul>`/`<ol>`, `<strong>`, `<code>`, links `<a href="...">`.
Links between pages use the file names: `start-here.html`, `herdr.html`, `lead-and-workers.html`,
`orchestrating.html`, `fable-method.html`, `skills.html`, `images.html`, `quality.html`,
`limits-and-handover.html`, `house-rules.html`, `knowledge.html`, `recipes.html`, `troubleshooting.html`,
`catalogue.html`, `laws.html`, `your-setup.html`, `how-this-was-built.html`.

## Code (gets a copy button automatically)
```html
<pre><code>herdr agent list</code></pre>
```
Escape `<`, `>` and `&` inside code as `&lt;`, `&gt;`, `&amp;`.

## Callouts
```html
<div class="callout"><span class="label">Note</span><p>Text.</p></div>
<div class="callout tip"><span class="label">Tip</span><p>Text.</p></div>
<div class="callout rule"><span class="label">Rule</span><p>Text.</p></div>
```

## Numbered steps
```html
<ol class="steps">
  <li><strong>Give your agent the link.</strong> It checks your machine and installs what is missing.</li>
  <li><strong>Open herdr.</strong> Run <code>herdr</code> in a terminal.</li>
</ol>
```

## Cards (a grid of short items; can be links)
```html
<div class="cards">
  <a class="card" href="quality.html"><span class="tag">quality</span><h3>web-qa</h3><p>Checks the running site.</p></a>
  <div class="card"><h3>Free workers</h3><p>OpenCode on a free model.</p></div>
</div>
```

## Tables
Normal `<table><thead><tr><th>…</th></tr></thead><tbody><tr><td>…</td></tr></tbody></table>`.

## Agent states
```html
<span class="state working">working</span> <span class="state blocked">blocked</span>
<span class="state done">done</span> <span class="state idle">idle</span>
```

## A herdr window (a picture of herdr made of HTML, for explaining it)
```html
<div class="herdr" role="img" aria-label="herdr with a lead and two workers">
  <div class="ws"><div class="on"><span>my-project</span><span class="state working">2</span></div><div><span>other</span><span class="state idle">0</span></div></div>
  <div><div class="tabs"><span class="on">lead</span><span>worker-home</span><span>worker-gallery</span></div>
  <div class="pane"><span class="prompt">❯</span> build the gallery page<br><span class="dim">starting worker-gallery (opencode)…</span></div></div>
</div>
```

## Terminal output (not copyable)
```html
<div class="term"><span class="prompt">$</span> herdr agent list<br><span class="dim">gallery  working  w1:p2</span></div>
```

## Figure with an inline SVG diagram
```html
<figure class="figure">
  <svg viewBox="0 0 640 160" role="img" aria-labelledby="d1"><title id="d1">The Fable loop</title>
    <!-- simple shapes and text only; use currentColor and var(--accent) via fill="currentColor" -->
  </svg>
  <figcaption>What the diagram shows, in one sentence.</figcaption>
</figure>
```
SVG rules: solid fills only (no `<linearGradient>`/`<radialGradient>`), `fill="currentColor"` or
`stroke="currentColor"` so it works in dark mode, real `<text>` labels, a `<title>`.

## Images (only files the lead lists in your brief)
```html
<figure class="figure"><img src="assets/img/hero.webp" alt="What the image shows" width="1200" height="675" loading="lazy"><figcaption>Generated illustration.</figcaption></figure>
```

## Special blocks
- Skill catalogue: `<div data-catalogue="data/skills.json"></div>`
- Law library: `<div data-catalogue="data/laws.json"></div>`
- This person's machine: `<div data-machine></div>`
- Home page hero: `<section class="hero"><div>…heading, lede, <div class="cta"><a class="btn primary" href="start-here.html">Start here</a><a class="btn secondary" href="your-setup.html">Your setup</a></div></div><div>…a herdr window or figure…</div></section>`
