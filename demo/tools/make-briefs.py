#!/usr/bin/env python3
"""Write one worker brief per page into <site>/briefs/, from demo/page-brief.template.md.
Usage: make-briefs.py <site-dir> [--images "assets/img/hero.webp (alt: ...), ..."]
Prints the page plan as JSON: slug, source, brief path."""
import json, os, sys

KIT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
site = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else 'site')
images = 'none. Use SVG, herdr windows and terminal blocks only.'
if '--images' in sys.argv: images = sys.argv[sys.argv.index('--images') + 1]
prof = {}
pp = os.path.join(site, 'data', 'profile.json')
if os.path.exists(pp): prof = json.load(open(pp))
person = prof.get('name') or 'the reader'

PAGES = [  # slug, source, eyebrow
    ('index', 'docs/00-start-here.md', 'Your agent team'),
    ('your-setup', 'docs/00-start-here.md', 'Your setup'),
    ('start-here', 'docs/00-start-here.md', 'Chapter 00'),
    ('herdr', 'docs/01-herdr.md', 'Chapter 01'),
    ('lead-and-workers', 'docs/02-lead-and-workers.md', 'Chapter 02'),
    ('orchestrating', 'docs/03-orchestrating.md', 'Chapter 03'),
    ('fable-method', 'docs/04-fable-method.md', 'Chapter 04'),
    ('skills', 'docs/05-skills.md', 'Chapter 05'),
    ('images', 'docs/06-images.md', 'Chapter 06'),
    ('quality', 'docs/07-quality.md', 'Chapter 07'),
    ('limits-and-handover', 'docs/08-limits-and-handover.md', 'Chapter 08'),
    ('house-rules', 'docs/09-house-rules.md', 'Chapter 09'),
    ('knowledge', 'docs/10-knowledge.md', 'Chapter 10'),
    ('recipes', 'docs/11-recipes.md', 'Chapter 11'),
    ('troubleshooting', 'docs/12-troubleshooting.md', 'Chapter 12'),
]
EXTRA = {
    'index': 'This is the HOME page. Use the "Home page hero" block from COMPONENTS.md. Greet the person by name and say, in their terms, what their agent team will do for their goals (profile.json). Then cards linking to the chapters most useful for their goals, and a short "what happens next" steps block. Keep it to one screen and a half.',
    'your-setup': 'This is the YOUR SETUP page. Put `<div data-machine></div>` near the top (it renders their machine). Then, from machine.json and profile.json: what is ready, what is missing and the exact command to add each missing piece (from docs/05-skills.md, docs/06-images.md and docs/08-limits-and-handover.md), and three first tasks to give the lead, written for their goals and projects.',
    'recipes': 'Rewrite every recipe group around this person: their business, their projects, their goals. Keep one generic example per group too.',
}
os.makedirs(os.path.join(site, 'briefs'), exist_ok=True)
tpl = open(os.path.join(KIT, 'demo', 'page-brief.template.md')).read()
plan = []
for slug, src, eyebrow in PAGES:
    b = (tpl.replace('{{PERSON}}', person).replace('{{SLUG}}', slug).replace('{{SITE}}', site).replace('{{KIT}}', KIT)
            .replace('{{SOURCE}}', os.path.join(KIT, src)).replace('{{EYEBROW}}', eyebrow).replace('{{IMAGES}}', images))
    if slug in EXTRA: b = b.replace('## Steps', '## This page\n' + EXTRA[slug] + '\n\n## Steps', 1)
    p = os.path.join(site, 'briefs', f'{slug}.md'); open(p, 'w').write(b)
    plan.append({'slug': slug, 'source': src, 'brief': p})
print(json.dumps(plan, indent=1))
