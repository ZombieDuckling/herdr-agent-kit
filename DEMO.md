# DEMO: build this person's teaching site, visibly (for the lead agent)

You are the **lead**. You will build a website that teaches this person how to use everything in this
kit, **personalised to them**, while they watch: workers in visible herdr tabs each write a page, and you
check every page before it is accepted. The site itself is the proof that the setup works.

Load these skills first: `herdr-orchestration`, `fable-method`, `fable-verify`, `web-qa`.
`<kit>` is this repo's folder. `SITE=~/herdr-agent-demo/site`.

## 0. Preconditions (stop and tell them if one fails)

```sh
test "$HERDR_ENV" = 1 && echo "inside herdr: $HERDR_WORKSPACE_ID $HERDR_PANE_ID"
<kit>/scripts/doctor.sh
cat ~/.herdr-agent/profile.json      # missing? run BOOTSTRAP.md step 3 first (or continue with a generic site)
```

Tell them in one line what is about to happen: "I'll build your site with N workers in tabs you can
click; it takes about 15-40 minutes; nothing goes online."

## 1. Prepare the site (you, ~1 minute)

```sh
mkdir -p ~/herdr-agent-demo && cp -R <kit>/demo/starter/. ~/herdr-agent-demo/site/
mkdir -p $SITE/pages $SITE/assets/img
python3 <kit>/demo/tools/build-data.py $SITE        # skills, laws, profile, machine, accent colour
```

Start the build log `$SITE/build-log.md` now and add to it after every step (it becomes the "How this
site was built" page). First lines: who it is for, the date, the plan, which workers you chose and why.

## 2. Images (you; only if an image backend exists)

If `doctor.sh` showed an image backend, generate at most 3 images that fit the person's work (from
profile.json): a home hero and up to two chapter illustrations. Follow `image-generation-freely`:
labelled prompt, no text in the image, no real brands or people, landscape 16:9, then
`verify_image.py` on each file. Convert to WebP (`sips -s format webp` on macOS or `cwebp`) into
`$SITE/assets/img/`. Look at each one if you can see images. No backend: skip; workers use SVG.

## 3. Choose the workers

Pick the cheapest that works on this machine (see `herdr-orchestration`):

| Available | Use |
|---|---|
| OpenCode | OpenCode workers (free). Pin a free model: `OPENCODE_MODEL` in `~/.herdr-agent/env`. |
| Claude Code only | Claude workers on `claude-haiku-5-5` (or the smallest model they have) |
| Codex only | Codex workers |

Concurrency: **3 workers at a time** (2 if the free model is local on one GPU). 15 pages, so they work in
waves. Write the choice and the reason in the build log.

## 4. Brief and launch (the visible part)

```sh
python3 <kit>/demo/tools/make-briefs.py $SITE --images "<list the images you made, with alt text, or omit>"
```

This writes one brief per page into `$SITE/briefs/`. For each page in the plan (home first, then
your-setup, then the chapters in order), start a worker **in its own visible tab** named `pg-<slug>`:

```sh
P=$(herdr tab create --workspace "$HERDR_WORKSPACE_ID" --cwd "$SITE" --label "pg-<slug>" --no-focus \
     | grep -oE '"pane_id":"[^"]*"' | head -1 | cut -d'"' -f4)
# OpenCode:
herdr pane send-text "$P" "opencode run ${OPENCODE_MODEL:+-m $OPENCODE_MODEL} --auto \"\$(cat briefs/<slug>.md)\" 2>&1 | tee briefs/<slug>.log
"
# Claude:   herdr agent start pg-<slug> --kind claude --pane "$P" -- --model claude-haiku-5-5
#           herdr agent prompt pg-<slug> "$(cat $SITE/briefs/<slug>.md)"     (answer a trust prompt with send-keys down enter)
```

Tell the person once: "Click the `pg-…` tabs to watch the workers." Wait for each in the background
(`herdr agent wait` or read its pane every few minutes), never in a tight loop. Start the next page when a
slot frees.

## 5. Check every page yourself (the gate)

When a worker finishes:

```sh
python3 <kit>/demo/tools/check-page.py $SITE <slug> <kit>/<source from the plan>
```

- `ok: true` → read the page quickly for sense and tone; accept; close its tab; log it.
- `ok: false` → send the worker the exact problems (one short message) and let it fix them. Second
  failure → fix it yourself or give it to a stronger worker. Log what happened.

Meanwhile write the three small pages yourself:

```sh
cat > $SITE/pages/catalogue.html <<'EOF'
<!-- title: Skill catalogue | description: Every skill in the kit and every installable pack, searchable. -->
<p class="eyebrow">Reference</p><h1>Skill catalogue</h1>
<p class="lede">Every skill in this kit, and the packs you can add. Search, or filter by group.</p>
<div data-catalogue="data/skills.json"></div>
EOF
cat > $SITE/pages/laws.html <<'EOF'
<!-- title: Law library | description: Hard-won laws for agents and the systems they run, searchable. -->
<p class="eyebrow">Reference</p><h1>Law library</h1>
<p class="lede">Rules learned the hard way, each with the incident behind it. Search by symptom or keyword.</p>
<div data-catalogue="data/laws.json"></div>
EOF
```

## 6. Assemble and test the whole site

```sh
python3 <kit>/demo/tools/assemble.py $SITE           # wraps pages in the shell; builds "How this site was built"
cd ~/herdr-agent-demo && { [ -f package.json ] || npm init -y >/dev/null; } && { [ -d node_modules/playwright ] || npm i -D playwright @axe-core/playwright >/dev/null; } && npx playwright install chromium >/dev/null; cd -
<kit>/demo/tools/serve.sh $SITE 4321                  # run this in its own tab, label "server"
(cd ~/herdr-agent-demo && node <kit>/skills/quality/web-qa/scripts/check-site.mjs http://localhost:4321/ --out $SITE/../qa)
```

Fix until `ok: true`: 0 console errors, 0 failed requests, 0 broken links, 0 serious/critical axe, no
phone overflow. Look at a few screenshots in `~/herdr-agent-demo/qa/` (desktop and phone) if you can see
images; if not, say "visual check: not done". Add the final numbers to the build log and run
`assemble.py` once more so the log page is current.

## 7. Hand it over

Open the site for them (`open http://localhost:4321/` on macOS, `xdg-open` on Linux) and report in the
`fable-report` shape:

```
Your site is ready: http://localhost:4321/  (nothing is online)
Built by <N> <kind> workers in herdr tabs, <M> pages, checked page by page.
QA: <pages> pages · console errors 0 · broken links 0 · axe serious 0 · phone overflow 0
Personal: <2-3 things that are about them>
Not checked: <anything>
Try next: <one task from their goals, phrased as something to say to you>
```

Leave the server tab running. Close the worker tabs. Do not push or publish the site anywhere unless
they ask.
