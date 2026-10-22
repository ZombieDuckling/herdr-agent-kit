#!/usr/bin/env python3
"""The lead's gate for one worker page (run it yourself; do not trust the worker's report).
Usage: check-page.py <site-dir> <slug> [<source.md>]
Checks: file exists; starts with the title comment, eyebrow, h1, lede; no gradient/script/style/<link>;
every command line from the source's code blocks appears on the page; mentions the person if a profile exists.
Exit 0 = pass. Prints one JSON line."""
import html, json, os, re, sys

KIT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
site, slug = sys.argv[1], sys.argv[2]
src = sys.argv[3] if len(sys.argv) > 3 else None
p = os.path.join(site, 'pages', f'{slug}.html')
r = {'page': slug, 'ok': False, 'problems': []}
if not os.path.exists(p):
    r['problems'].append('missing file'); print(json.dumps(r)); sys.exit(1)
t = open(p).read()
low = t.lower()
if not re.match(r'\s*<!--\s*title:.*\|\s*description:.*-->', t): r['problems'].append('no title/description comment on line 1')
for need, label in [('class="eyebrow"', 'eyebrow'), ('<h1', 'h1'), ('class="lede"', 'lede')]:
    if need not in t: r['problems'].append(f'no {label}')
for bad, label in [('gradient', 'gradient'), ('<script', 'script tag'), (' style=', 'inline style'), ('<style', 'style block'), ('<link', 'link tag')]:
    if bad in low: r['problems'].append(f'contains {label}')
if src:
    s = open(src).read()
    cmds = []
    for block in re.findall(r'```[a-z]*\n(.*?)```', s, re.S):
        for line in block.splitlines():
            line = line.split('#')[0].strip() if not line.strip().startswith('{') else line.strip()
            if len(line) > 6 and not line.startswith(('---', '|', '<', '//')): cmds.append(line)
    text = html.unescape(re.sub(r'<[^>]+>', '', t))
    norm = lambda x: re.sub(r'\s+', ' ', x)
    missing = [c for c in cmds if norm(c) not in norm(text)]
    r['source_commands'] = len(cmds); r['commands_kept'] = len(cmds) - len(missing)
    if missing: r['problems'].append(f'{len(missing)} source commands missing, e.g.: ' + ' || '.join(missing[:3]))
pp = os.path.join(site, 'data', 'profile.json')
if os.path.exists(pp):
    name = (json.load(open(pp)).get('name') or '').split(' ')[0]
    if name and slug in ('index', 'your-setup', 'recipes') and name.lower() not in low:
        r['problems'].append(f'does not mention {name}')
r['ok'] = not r['problems']
print(json.dumps(r)); sys.exit(0 if r['ok'] else 1)
