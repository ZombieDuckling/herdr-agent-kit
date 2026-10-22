#!/usr/bin/env python3
"""Build the site's data files from the kit and from the person's own machine, so every page is true
and personal. Usage: build-data.py <site-dir>
Writes <site-dir>/data/{skills.json,laws.json,profile.json,machine.json} and assets/personal.css."""
import json, os, re, shutil, subprocess, sys

KIT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
site = sys.argv[1] if len(sys.argv) > 1 else 'site'
os.makedirs(os.path.join(site, 'data'), exist_ok=True)

def front(path):
    t = open(path, errors='ignore').read()
    m = re.match(r'^---\n(.*?)\n---', t, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line and not line.startswith(' '):
                k, v = line.split(':', 1); meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta

skills = []
for group in sorted(os.listdir(os.path.join(KIT, 'skills'))):
    gdir = os.path.join(KIT, 'skills', group)
    if not os.path.isdir(gdir): continue
    for name in sorted(os.listdir(gdir)):
        p = os.path.join(gdir, name, 'SKILL.md')
        if not os.path.isfile(p): continue
        m = front(p)
        desc = m.get('description', '')
        if desc in ('|', '>', '>-'): desc = ''
        skills.append({'name': m.get('name', name), 'group': group, 'description': desc[:400], 'source': 'in this kit'})
packs = json.load(open(os.path.join(KIT, 'packs.json')))['packs']
for pack, v in packs.items():
    for item in v['items']:
        skills.append({'name': item['name'], 'group': 'pack: ' + pack, 'description': v['why'], 'source': 'install: scripts/install-packs.sh ' + pack, 'license': item['license']})
json.dump(skills, open(os.path.join(site, 'data', 'skills.json'), 'w'), indent=1)

laws = []
ldir = os.path.join(KIT, 'knowledge', 'laws')
for f in sorted(os.listdir(ldir)):
    if not re.match(r'^\d\d-.*\.md$', f): continue
    chapter = re.sub(r'^\d\d-', '', f[:-3]).replace('-', ' ')
    t = open(os.path.join(ldir, f)).read()
    for m in re.finditer(r'^#{2,3}\s+([A-Z]+-\d+)[^\n]*?[·:-]?\s*(.*)$', t, re.M):
        body = t[m.end():].split('\n#', 1)[0].strip()
        first = re.sub(r'\s+', ' ', re.sub(r'[*_`>#]', '', body.split('\n\n', 1)[0]))[:320]
        laws.append({'name': m.group(1) + ' · ' + m.group(2).strip(' ·-'), 'group': chapter, 'description': first})
json.dump(laws, open(os.path.join(site, 'data', 'laws.json'), 'w'), indent=1)
print(json.dumps({'skills_in_kit': sum(1 for s in skills if s['source'] == 'in this kit'), 'pack_items': sum(1 for s in skills if s['source'] != 'in this kit'), 'laws': len(laws)}))

# ---------------------------------------------------------------- the person and their machine
H = os.path.expanduser('~')
profile = {}
pp = os.path.join(H, '.herdr-agent', 'profile.json')
if os.path.exists(pp):
    profile = json.load(open(pp))
json.dump(profile, open(os.path.join(site, 'data', 'profile.json'), 'w'), indent=1)

def ver(cmd):
    if not shutil.which(cmd[0]): return None
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=20).stdout.strip().splitlines()[0][:80]
    except Exception: return 'installed'
def count(d):
    d = os.path.join(H, d)
    return len([x for x in os.listdir(d) if not x.startswith('.')]) if os.path.isdir(d) else None
oc_model = ''
try: oc_model = json.load(open(os.path.join(H, '.config/opencode/opencode.json'))).get('model', '')
except Exception: pass
img = 'none (SVG and CSS art instead)'
if os.environ.get('OPENAI_API_KEY') or os.environ.get('IMAGE_API_KEY'): img = 'OpenAI-compatible key'
if os.path.exists(os.path.join(H, '.hermes/hermes-agent/venv/bin/python')): img = 'Hermes + Codex sign-in (codex-image)'
plugins = ''
if shutil.which('claude'):
    try: plugins = subprocess.run(['claude', 'plugin', 'list'], capture_output=True, text=True, timeout=30).stdout
    except Exception: pass
machine = {
    'os': ' '.join(os.uname()[i] for i in (0, 4)),
    'herdr': ver(['herdr', '--version']),
    'agents': {k: v for k, v in {
        'claude': ver(['claude', '--version']), 'opencode': ver(['opencode', '--version']),
        'codex': ver(['codex', '--version']), 'hermes': 'installed' if shutil.which('hermes') else None}.items() if v},
    'free_worker_model': oc_model or None,
    'skills_installed': {k: v for k, v in {'claude': count('.claude/skills'), 'opencode': count('.config/opencode/skills'),
        'codex': count('.codex/skills'), 'hermes': count('.hermes/skills')}.items() if v is not None},
    'image_backend': img,
    'usage_mods': ('usage-meter' in plugins and 'agent-radar' in plugins),
    'node': ver(['node', '-v']), 'gh': ver(['gh', '--version']), 'semgrep': ver(['semgrep', '--version']),
}
json.dump(machine, open(os.path.join(site, 'data', 'machine.json'), 'w'), indent=1)

# the person's accent colour (a CSS colour name or #hex), applied on top of the design tokens
accent = str(profile.get('accent', '')).strip()
css = ''
NAMED = {'red': '#dc2626', 'orange': '#ea580c', 'amber': '#d97706', 'yellow': '#ca8a04', 'green': '#16a34a', 'teal': '#0d9488',
         'blue': '#2563eb', 'navy': '#1e3a8a', 'indigo': '#4f46e5', 'purple': '#9333ea', 'violet': '#7c3aed', 'pink': '#db2777',
         'brown': '#92400e', 'black': '#111111', 'grey': '#4b5563', 'gray': '#4b5563', 'gold': '#b45309', 'maroon': '#7f1d1d'}
def rgb(h):
    h = h.lstrip('#'); h = ''.join(c * 2 for c in h) if len(h) == 3 else h[:6]
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]
def lum(c):
    c = [x / 255 for x in c]; c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + 0.05) / (lb + 0.05)
def fit(c, bg, darker):  # move the colour toward black (light theme) or white (dark theme) until text contrast >= 4.5
    c = list(c)
    for _ in range(40):
        if ratio(c, bg) >= 4.6: break
        c = [max(0, int(x * 0.92)) for x in c] if darker else [min(255, int(x + (255 - x) * 0.1)) for x in c]
    return '#%02x%02x%02x' % tuple(c)
hexv = NAMED.get(accent.lower(), accent) if accent else ''
if re.match(r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', hexv):
    light, dark = fit(rgb(hexv), rgb('#f6f3ec'), True), fit(rgb(hexv), rgb('#12110e'), False)
    css = (f':root {{ --accent: {light}; }}\n'
           f'@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --accent: {dark}; }} }}\n'
           f':root[data-theme="dark"] {{ --accent: {dark}; }}\n')
os.makedirs(os.path.join(site, 'assets'), exist_ok=True)
open(os.path.join(site, 'assets', 'personal.css'), 'w').write(css)
print(json.dumps({'profile': bool(profile), 'name': profile.get('name'), 'agents': list(machine['agents']), 'image_backend': img}))
