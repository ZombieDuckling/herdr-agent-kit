# Static Demo Site + Generated Assets + Vercel Pattern

Use this pattern when the user asks for a quick demo website/app with generated imagery and deployment.

## Build sequence

1. Confirm whether the demo should be a new/separate project or an iteration on an existing project. If the user says “separate project,” create a new folder under `~/Projects/<demo-name>` and do not mutate the prior demo.
2. Generate 2–3 text-free images tailored to the domain:
   - landscape hero with negative space for headline copy,
   - square/product/service support image,
   - trust/safety/process illustration when relevant.
3. Copy generated image files out of Hermes cache into stable project paths such as `assets/hero.png`.
4. Build dependency-free `index.html`, `styles.css`, and `script.js` for speed unless the requested demo needs a framework.
5. Include explicit demo-safety copy when the domain has risk or regulated implications. Examples: casino demos should say no real-money gambling, no payments, front-end only, 18+ positioning; appointment demos should say no details are sent.
6. Add minimal `package.json` and `vercel.json` for static deployment and asset caching.

## Verification sequence

- Run `node --check script.js`.
- Run `file assets/*.png`.
- Parse/check HTML references for CSS, JS, images, key sections, and safety copy.
- Serve locally with `terminal(background=true)` / tracked process; do not shell-background with `&` in a foreground terminal command.
- `curl` the page, CSS, JS, and one key image; verify `200` responses and expected content.
- Kill the local server when done.
- Deploy with `vercel deploy --prod --yes`.
- If Vercel prints production/alias URLs but returns nonzero after completion, do not assume failure: verify the live alias directly with `curl` and report the verified URL.

## Reporting

Report the live URL, local project path, generated asset names, verification checks, and any CLI oddity separately from the deployment result.
