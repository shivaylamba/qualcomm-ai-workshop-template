"""Check the workshop pages exist, link correctly, and (with --release) have no placeholders left."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

PAGES = ['README.md', 'START-HERE.md', 'HOST.md', 'PRESENTATION.md', 'EXAMPLES.md',
         'setup.md', 'workshop.json', 'starter/README.md', 'solution/README.md',
         'labs/1-run.md', 'labs/2-build.md', 'labs/3-make-it-yours.md']

LABS = ['labs/1-run.md', 'labs/2-build.md', 'labs/3-make-it-yours.md']
LAB_BLOCKS = ['Your turn', 'Done when', 'Go further', 'Stuck?']


def check(release=False):
    errors = []
    for name in PAGES:
        if not (ROOT / name).is_file():
            errors.append(f'Missing page: {name}')

    config_path = ROOT / 'workshop.json'
    if config_path.is_file():
        minutes = json.loads(config_path.read_text(encoding='utf-8'))['minutes']
        if sum(minutes.values()) != 90:
            errors.append(f'Schedule totals {sum(minutes.values())} minutes, not 90')

    for lab in LABS:
        path = ROOT / lab
        if not path.is_file():
            continue
        content = path.read_text(encoding='utf-8')
        for block in LAB_BLOCKS:
            if f'## {block}\n' not in content:
                errors.append(f'{lab}: missing "## {block}" section')

    for path in ROOT.rglob('*.md'):
        if any(part in {'.git', '.venv', 'output'} for part in path.parts):
            continue
        content = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith(('#', 'mailto:')) or '{{' in target:
                continue
            target = target.split('#')[0]
            if target and not (path.parent / target).exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')

    if release:
        # README/PRESENTATION describe the template itself and mention placeholders on purpose.
        for name in [n for n in PAGES if n not in {'README.md', 'PRESENTATION.md'}]:
            path = ROOT / name
            if path.is_file() and re.search(r'\{\{[^}]+\}\}', path.read_text(encoding='utf-8')):
                errors.append(f'Still has {{{{PLACEHOLDERS}}}}: {name}')

    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', action='store_true',
                        help='also fail if any {{PLACEHOLDER}} is unfilled')
    errors = check(parser.parse_args().release)
    print('\n'.join(errors) if errors else 'PASS: pages, lab structure, schedule, and links')
    sys.exit(bool(errors))
