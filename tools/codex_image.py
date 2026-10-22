#!/usr/bin/env python3
"""codex-image: generate one image through ChatGPT/Codex sign-in (no API key), via Hermes's
openai-codex provider (gpt-image-2). A no-API-key image backend for every agent on the machine (needs Hermes Agent signed in with `hermes auth codex`); the
image-generation-workflow skill reaches it through IMAGE_BACKEND_CMD.

  codex-image --prompt "<spec>" --out path.png [--size 1024x1024 | --aspect square|landscape|portrait]
              [--ref picture.png ...]        (reference pictures; also IMAGE_REFS=a.png,b.png)
              [--model gpt-image-2-low|medium|high]
  codex-image --find "<words>"     search the shared registry of images any agent already generated
                                   (~/.cache/agent-images/index.jsonl; copies kept next to it)

Prints one JSON line. Exit 0 only when a file was written to --out. Always run verify_image.py
on the result and look at it before using it.
"""
import argparse, hashlib, json, os, shutil, subprocess, sys, time
from importlib.util import spec_from_file_location, module_from_spec

HERMES = os.environ.get('HERMES_AGENT_DIR') or os.path.expanduser('~/.hermes/hermes-agent')
REGISTRY = os.path.expanduser('~/.cache/agent-images')


def register(out, prompt, refs, model):
    """Append one line to the registry and keep a copy by hash. Never fails the generation."""
    try:
        os.makedirs(REGISTRY, exist_ok=True)
        sha = hashlib.sha256(open(out, 'rb').read()).hexdigest()
        copy = os.path.join(REGISTRY, sha[:16] + os.path.splitext(out)[1].lower())
        if not os.path.exists(copy):
            shutil.copyfile(out, copy)
        rec = {'time': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'cwd': os.getcwd(), 'out': out,
               'prompt': prompt, 'refs': refs, 'model': model, 'sha256': sha, 'copy': copy}
        with open(os.path.join(REGISTRY, 'index.jsonl'), 'a') as f:
            f.write(json.dumps(rec) + '\n')
        return sha
    except Exception:
        return None


def find(words):
    idx = os.path.join(REGISTRY, 'index.jsonl')
    terms = [w.lower() for w in words.split()]
    n = 0
    if os.path.isfile(idx):
        for line in open(idx):
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            hay = (str(rec.get('prompt', '')) + ' ' + str(rec.get('out', ''))).lower()
            if all(t in hay for t in terms):
                n += 1
                print(json.dumps({k: rec.get(k) for k in ('time', 'out', 'copy', 'model', 'prompt')}))
    if not n:
        print(json.dumps({'ok': True, 'matches': 0}))
    return 0


def aspect_from_size(size):
    try:
        w, h = (int(x) for x in size.lower().split('x'))
    except ValueError:
        return 'square'
    if abs(w - h) <= max(w, h) * 0.1:
        return 'square'
    return 'landscape' if w > h else 'portrait'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prompt')
    ap.add_argument('--out')
    ap.add_argument('--find')
    ap.add_argument('--size', default='1024x1024')
    ap.add_argument('--aspect', choices=['square', 'landscape', 'portrait'])
    ap.add_argument('--ref', action='append', default=[])
    ap.add_argument('--model')
    a = ap.parse_args()
    if a.find is not None:
        return find(a.find)
    if not (a.prompt and a.out):
        ap.error('--prompt and --out are required (or use --find "<words>")')

    refs = a.ref + [r for r in os.environ.get('IMAGE_REFS', '').split(',') if r.strip()]
    refs = [os.path.abspath(os.path.expanduser(r.strip())) for r in refs]
    missing = [r for r in refs if not os.path.isfile(r)]
    if missing:
        print(json.dumps({'ok': False, 'error': 'reference file not found: ' + ', '.join(missing)}))
        return 1
    if a.model:
        os.environ['OPENAI_IMAGE_MODEL'] = a.model  # read by the provider's _resolve_model

    sys.path.insert(0, HERMES)
    spec = spec_from_file_location('codex_image_provider', HERMES + '/plugins/image_gen/openai-codex/__init__.py')
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    provider = mod.OpenAICodexImageGenProvider()
    if not provider.is_available():
        print(json.dumps({'ok': False, 'error': 'Codex sign-in not available; run: hermes auth codex'}))
        return 1

    r = provider.generate(a.prompt, aspect_ratio=a.aspect or aspect_from_size(a.size),
                          reference_image_urls=refs or None)
    src = r.get('image') if isinstance(r, dict) else None
    if not (isinstance(r, dict) and r.get('success') and src and os.path.isfile(src)):
        err = r.get('error') if isinstance(r, dict) else repr(r)
        print(json.dumps({'ok': False, 'error': str(err)[:500]}))
        return 1

    out = os.path.abspath(os.path.expanduser(a.out))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    ext = os.path.splitext(out)[1].lower()
    if ext in ('.jpg', '.jpeg'):
        subprocess.run(['sips', '-s', 'format', 'jpeg', src, '--out', out], check=True, capture_output=True)
    elif ext in ('', '.png'):
        shutil.copyfile(src, out)
    else:
        print(json.dumps({'ok': False, 'error': f'write .png or .jpg, then convert ({ext} not supported here)', 'png': src}))
        return 1
    sha = register(out, a.prompt, refs, str(r.get('model')))
    print(json.dumps({'ok': True, 'sha256': sha, 'backend': 'codex-auth:' + str(r.get('model')), 'path': out,
                      'size': r.get('size'), 'refs': len(refs),
                      'next': 'verify_image.py, then look at it'}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
