// Shared behaviour for every page: navigation, theme, mobile menu, copy buttons, catalogues.
const NAV = [
  ['index.html', '', 'Home'],
  ['your-setup.html', '', 'Your setup'],
  ['start-here.html', '00', 'Start here'],
  ['herdr.html', '01', 'herdr basics'],
  ['lead-and-workers.html', '02', 'The lead and its workers'],
  ['orchestrating.html', '03', 'Orchestrating in practice'],
  ['fable-method.html', '04', 'The Fable method'],
  ['skills.html', '05', 'Skills'],
  ['images.html', '06', 'Images'],
  ['quality.html', '07', 'Quality'],
  ['limits-and-handover.html', '08', 'Limits and handover'],
  ['house-rules.html', '09', 'House rules'],
  ['knowledge.html', '10', 'Knowledge'],
  ['recipes.html', '11', 'Recipes'],
  ['troubleshooting.html', '12', 'Troubleshooting'],
  ['catalogue.html', '', 'Skill catalogue'],
  ['laws.html', '', 'Law library'],
  ['how-this-was-built.html', '', 'How this site was built'],
];

const here = location.pathname.split('/').pop() || 'index.html';

function buildNav() {
  const nav = document.querySelector('[data-nav]');
  if (!nav) return;
  const groups = [['Guide', NAV.slice(0, 15)], ['Reference', NAV.slice(15)]];
  nav.innerHTML = groups.map(([title, items]) => `<h2>${title}</h2>` + items.map(([href, n, label]) =>
    `<a href="${href}"${href === here ? ' aria-current="page"' : ''}><span class="n">${n}</span><span>${label}</span></a>`).join('')).join('');
  const i = NAV.findIndex(([href]) => href === here);
  const pager = document.querySelector('[data-pager]');
  if (pager && i >= 0) {
    const prev = NAV[i - 1], next = NAV[i + 1];
    pager.innerHTML = (prev ? `<a href="${prev[0]}">← ${prev[2]}</a>` : '<span></span>') + (next ? `<a href="${next[0]}">${next[2]} →</a>` : '<span></span>');
  }
}

function theme() {
  const btn = document.querySelector('[data-theme-toggle]');
  let saved = null;
  try { saved = localStorage.getItem('theme'); } catch {}
  if (saved) document.documentElement.dataset.theme = saved;
  btn?.addEventListener('click', () => {
    const dark = document.documentElement.dataset.theme === 'dark' ||
      (!document.documentElement.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
    const next = dark ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch {}
  });
}

function menu() {
  const btn = document.querySelector('[data-menu]'), nav = document.querySelector('[data-nav]');
  btn?.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
  });
}

function copyButtons() {
  document.querySelectorAll('pre').forEach(pre => {
    const b = document.createElement('button');
    b.className = 'copy'; b.type = 'button'; b.textContent = 'copy';
    b.setAttribute('aria-label', 'Copy this code');
    b.addEventListener('click', async () => {
      const text = (pre.querySelector('code') || pre).innerText.replace(/\ncopy$/, '');
      try { await navigator.clipboard.writeText(text); b.textContent = 'copied'; } catch { b.textContent = 'select + copy'; }
      setTimeout(() => (b.textContent = 'copy'), 1500);
    });
    pre.appendChild(b);
  });
}

// Catalogue: <div data-catalogue="data/skills.json" data-group-key="group"></div>
async function catalogues() {
  for (const el of document.querySelectorAll('[data-catalogue]')) {
    const items = await fetch(el.dataset.catalogue).then(r => r.json());
    const key = el.dataset.groupKey || 'group';
    const groups = [...new Set(items.map(x => x[key]))];
    el.innerHTML = `<div class="filters"><label class="count" for="q-${key}">Search</label>
      <input type="search" id="q-${key}" placeholder="Search names and descriptions">
      ${groups.map(g => `<button type="button" class="chip" aria-pressed="false" data-g="${g}">${g}</button>`).join('')}
      <span class="count" aria-live="polite"></span></div><div class="list"></div>`;
    const q = el.querySelector('input'), list = el.querySelector('.list'), count = el.querySelector('.count[aria-live]');
    const chips = [...el.querySelectorAll('.chip')];
    const render = () => {
      const on = chips.filter(c => c.getAttribute('aria-pressed') === 'true').map(c => c.dataset.g);
      const s = q.value.trim().toLowerCase();
      const shown = items.filter(x => (!on.length || on.includes(x[key])) && (!s || JSON.stringify(x).toLowerCase().includes(s)));
      count.textContent = `${shown.length} of ${items.length}`;
      list.innerHTML = shown.map(x => `<article class="item"><h3>${x.name}</h3><p>${x.description}</p>
        <div class="meta">${[x[key], x.source, x.license].filter(Boolean).join(' · ')}</div></article>`).join('');
    };
    chips.forEach(c => c.addEventListener('click', () => { c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); render(); }));
    q.addEventListener('input', render);
    render();
  }
}

// <div data-machine></div>: a table of what is installed on this person's machine (data/machine.json)
async function machine() {
  const el = document.querySelector('[data-machine]');
  if (!el) return;
  const m = await fetch('data/machine.json').then(r => r.json()).catch(() => null);
  if (!m) { el.textContent = 'Machine data not built yet (run demo/tools/build-data.py).'; return; }
  const row = (k, v, ok) => `<tr><th scope="row">${k}</th><td>${v ?? 'not installed'}</td><td><span class="state ${ok ? 'done' : 'idle'}">${ok ? 'ready' : 'missing'}</span></td></tr>`;
  const agents = ['claude', 'opencode', 'codex', 'hermes'].map(a => row(a, m.agents[a], !!m.agents[a])).join('');
  const skills = Object.entries(m.skills_installed || {}).map(([a, n]) => `${a} ${n}`).join(' · ');
  el.innerHTML = `<table><thead><tr><th>Piece</th><th>On this machine</th><th>State</th></tr></thead><tbody>
    ${row('system', m.os, true)}${row('herdr', m.herdr, !!m.herdr)}${agents}
    ${row('free worker model', m.free_worker_model, !!m.free_worker_model)}
    ${row('skills installed', skills, !!skills)}${row('image backend', m.image_backend, !m.image_backend.startsWith('none'))}
    ${row('usage mods', m.usage_mods ? 'usage-meter + agent-radar' : null, m.usage_mods)}
    ${row('node', m.node, !!m.node)}${row('gh', m.gh, !!m.gh)}${row('semgrep', m.semgrep, !!m.semgrep)}</tbody></table>`;
}

theme(); buildNav(); menu(); copyButtons(); catalogues(); machine();
