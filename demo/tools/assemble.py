#!/usr/bin/env python3
"""Wrap page bodies in the shared shell.
Usage: assemble.py <site-dir>
For each <site-dir>/pages/<slug>.html (a body fragment whose first line is
<!-- title: ... | description: ... -->), writes <site-dir>/<slug>.html.
Also converts <site-dir>/build-log.md (the lead's log) into the "how this was built" page."""
import html, os, re, sys

KIT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
site = sys.argv[1] if len(sys.argv) > 1 else 'site'
shell = open(os.path.join(KIT, 'demo', 'starter', '_page.html')).read()
import json
prof = {}
pp = os.path.join(site, 'data', 'profile.json')
if os.path.exists(pp): prof = json.load(open(pp))
person = prof.get('name') or 'you'
site_name = prof.get('site_name') or (f"{prof['name']}'s agent team" if prof.get('name') else 'herdr agent kit')
shell = shell.replace('{{SITE_NAME}}', html.escape(site_name)).replace('{{PERSON}}', html.escape(person))

def md(t):
    """Small Markdown subset: headings, lists, code fences, tables, paragraphs, inline code/bold/links."""
    out, lines, i = [], t.split('\n'), 0
    inline = lambda s: re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', re.sub(r'`([^`]+)`', lambda m: '<code>' + m.group(1) + '</code>', html.escape(s, quote=False))))
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            j = i + 1; buf = []
            while j < len(lines) and not lines[j].startswith('```'): buf.append(lines[j]); j += 1
            out.append('<pre><code>' + html.escape('\n'.join(buf)) + '</code></pre>'); i = j + 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)', l)
        if m: n = len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'): rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip('|').split('|')] for r in rows if not re.match(r'^\|[\s:|-]+\|$', r)]
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in cells[0]) + '</tr></thead><tbody>' +
                       ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in cells[1:]) + '</tbody></table>'); continue
        if re.match(r'^\s*([-*]|\d+\.)\s', l):
            tag = 'ol' if re.match(r'^\s*\d+\.', l) else 'ul'; buf = []
            while i < len(lines) and re.match(r'^\s*([-*]|\d+\.)\s', lines[i]): buf.append(re.sub(r'^\s*([-*]|\d+\.)\s', '', lines[i])); i += 1
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(b)}</li>' for b in buf) + f'</{tag}>'); continue
        if l.strip():
            buf = []
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#|```|\||\s*([-*]|\d+\.)\s)', lines[i]): buf.append(lines[i]); i += 1
            out.append('<p>' + inline(' '.join(buf)) + '</p>'); continue
        i += 1
    return '\n'.join(out)

pages = os.path.join(site, 'pages')
log = os.path.join(site, 'build-log.md')
if os.path.exists(log):
    os.makedirs(pages, exist_ok=True)
    open(os.path.join(pages, 'how-this-was-built.html'), 'w').write(
        '<!-- title: How this site was built | description: The real log of the lead agent and its workers building this site in herdr. -->\n'
        '<p class="eyebrow">Reference</p>\n' + md(open(log).read()))
made = []
for f in sorted(os.listdir(pages)):
    if not f.endswith('.html'): continue
    body = open(os.path.join(pages, f)).read()
    m = re.match(r'\s*<!--\s*title:\s*(.*?)\s*\|\s*description:\s*(.*?)\s*-->', body)
    title, desc = (m.group(1), m.group(2)) if m else (f[:-5].replace('-', ' ').title(), '')
    page = shell.replace('{{TITLE}}', html.escape(title)).replace('{{DESCRIPTION}}', html.escape(desc)).replace('{{CONTENT}}', body[m.end():] if m else body)
    page = page.replace('<!-- CONTENT: replace this comment with the page. Use only the components in demo/COMPONENTS.md. -->\n', '')
    if 'class="content wide"' not in page and ('data-catalogue' in body or 'class="hero"' in body):
        page = page.replace('<article class="content">', '<article class="content wide">')
    open(os.path.join(site, f), 'w').write(page); made.append(f)
print(f'assembled {len(made)} pages: ' + ' '.join(made))
