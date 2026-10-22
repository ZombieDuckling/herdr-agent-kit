#!/usr/bin/env node
// Check a running website the way a careful reviewer would: crawl every same-origin page, then report
// console errors, failed requests (404s and others), broken links, buttons with no action, axe
// accessibility violations, and horizontal overflow at phone width. Saves desktop and phone screenshots.
//
// Usage:  node check-site.mjs <base-url> [--out <dir>] [--max-pages 50]
// Needs:  npm i -D playwright @axe-core/playwright   (and `npx playwright install chromium` once)
// Exit:   0 when there are no console errors, no failed requests, no broken links and no serious or
//         critical axe violations; 1 otherwise. Prints one JSON summary line last.

import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

// Load Playwright and axe from the project being checked (the current folder), not from this script's folder.
const req = createRequire(path.join(process.cwd(), 'package.json'));
const load = async name => {
  try { return await import(pathToFileURL(req.resolve(name)).href); }
  catch { console.error(`missing ${name}: run  npm i -D playwright @axe-core/playwright && npx playwright install chromium  in ${process.cwd()}`); process.exit(2); }
};
const pw = await load('playwright');
const axeMod = await load('@axe-core/playwright');
const chromium = pw.chromium ?? pw.default?.chromium;
const AxeBuilder = axeMod.AxeBuilder ?? axeMod.default?.AxeBuilder ?? axeMod.default;

const args = process.argv.slice(2);
const base = args.find(a => !a.startsWith('--'));
if (!base) { console.error('usage: node check-site.mjs <base-url> [--out dir] [--max-pages N]'); process.exit(2); }
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const outDir = opt('--out', '.qa');
const maxPages = Number(opt('--max-pages', 50));
const origin = new URL(base).origin;
fs.mkdirSync(path.join(outDir, 'desktop'), { recursive: true });
fs.mkdirSync(path.join(outDir, 'phone'), { recursive: true });

const browser = await chromium.launch();
const viewports = { desktop: { width: 1440, height: 900 }, phone: { width: 390, height: 844 } };
const queue = [new URL(base).href];
const seen = new Set();
const report = { pages: [], consoleErrors: [], failedRequests: [], brokenLinks: [], deadButtons: [], axe: [], overflow: [] };
const slug = u => (new URL(u).pathname.replace(/\/$/, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '') || 'home');

while (queue.length && seen.size < maxPages) {
  const url = queue.shift();
  if (seen.has(url)) continue;
  seen.add(url);
  for (const [vp, size] of Object.entries(viewports)) {
    const context = await browser.newContext({ viewport: size });
    const page = await context.newPage();
    page.on('console', m => { if (m.type() === 'error') report.consoleErrors.push({ url, vp, text: m.text().slice(0, 300) }); });
    page.on('pageerror', e => report.consoleErrors.push({ url, vp, text: String(e).slice(0, 300) }));
    page.on('response', r => { if (r.status() >= 400) report.failedRequests.push({ url, vp, request: r.url(), status: r.status() }); });
    page.on('requestfailed', r => report.failedRequests.push({ url, vp, request: r.url(), status: r.failure()?.errorText || 'failed' }));
    const res = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 }).catch(e => ({ status: () => String(e) }));
    if (vp === 'desktop') report.pages.push({ url, status: res?.status?.() });
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(outDir, vp, `${slug(url)}.png`), fullPage: true });
    if (vp === 'phone') {
      const over = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      if (over > 1) report.overflow.push({ url, pixels: over });
    }
    if (vp === 'desktop') {
      const axe = await new AxeBuilder({ page }).analyze();
      for (const v of axe.violations) report.axe.push({ url, id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.help });
      const links = await page.$$eval('a[href]', as => as.map(a => a.href));
      for (const l of links) {
        const u = new URL(l, url); u.hash = '';
        if (u.origin === origin && !seen.has(u.href) && !queue.includes(u.href) && !/\.(png|jpe?g|webp|svg|pdf|zip)$/i.test(u.pathname)) queue.push(u.href);
        if (u.origin === origin) {
          const r = await page.request.get(u.href).catch(() => null);
          if (!r || r.status() >= 400) report.brokenLinks.push({ from: url, to: u.href, status: r ? r.status() : 'failed' });
        }
      }
      const dead = await page.$$eval('button', bs => bs.filter(b => !b.disabled && !b.onclick && !b.closest('form') && !b.hasAttribute('aria-controls') && !b.hasAttribute('aria-expanded') && !b.dataset.action && !b.getAttribute('type')?.match(/submit|reset/)).map(b => (b.innerText || b.getAttribute('aria-label') || '').trim().slice(0, 60)));
      for (const d of dead) report.deadButtons.push({ url, button: d, note: 'no inline handler, form, aria-controls or data-action: confirm a listener exists' });
    }
    await context.close();
  }
}
await browser.close();

const dedupe = a => [...new Map(a.map(x => [JSON.stringify(x), x])).values()];
for (const k of Object.keys(report)) report[k] = dedupe(report[k]);
const serious = report.axe.filter(v => v.impact === 'serious' || v.impact === 'critical');
fs.writeFileSync(path.join(outDir, 'report.json'), JSON.stringify(report, null, 2));
const summary = {
  pages: report.pages.length,
  consoleErrors: report.consoleErrors.length,
  failedRequests: report.failedRequests.length,
  brokenLinks: report.brokenLinks.length,
  axeSeriousOrCritical: serious.length,
  axeOther: report.axe.length - serious.length,
  phoneOverflowPages: report.overflow.length,
  buttonsToConfirm: report.deadButtons.length,
  screenshots: path.resolve(outDir),
  report: path.resolve(outDir, 'report.json'),
};
summary.ok = !summary.consoleErrors && !summary.failedRequests && !summary.brokenLinks && !summary.axeSeriousOrCritical;
console.log(JSON.stringify(summary));
process.exit(summary.ok ? 0 : 1);
