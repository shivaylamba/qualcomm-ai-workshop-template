"""Validate the teaching scaffold; --release also rejects unresolved placeholders."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(release=False):
    errors = []
    required = ['README.md', 'START-HERE.md', 'AUTHORING.md', 'PRESENTATION.md',
                'WORKSHEET.md', 'VERIFICATION.md', 'workshop.json', 'setup/README.md',
                'instructor/README.md', 'instructor/RELEASE-CHECKLIST.md',
                'resources/EXAMPLE-TOPICS.md', 'resources/TEACHING-PATTERN.md']
    labs = ['01-understand-and-run', '02-build', '03-test-and-improve', '04-personalize']
    required += [f'labs/{lab}/README.md' for lab in labs]
    required += [f'{folder}/README.md' for folder in ['starter', 'solution', 'data', 'tests']]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f'Missing: {name}')
    config = json.loads((ROOT / 'workshop.json').read_text(encoding='utf-8'))
    for duration, segments in config['formats'].items():
        if len(segments) != 7 or sum(segments) != int(duration):
            errors.append(f'Incorrect schedule: {duration}')
    for lab in labs:
        path = ROOT / 'labs' / lab / 'README.md'
        if not path.exists():
            continue
        content = path.read_text(encoding='utf-8')
        for heading in ['Goal', 'Before you begin', 'Learn', 'Predict', 'Do', 'Checkpoint', 'Hints', 'Reflect', 'Next']:
            if f'## {heading}\n' not in content:
                errors.append(f'{path.relative_to(ROOT)}: missing {heading}')
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
        for name in required:
            path = ROOT / name
            if path.exists() and re.search(r'\{\{[^}]+\}\}', path.read_text(encoding='utf-8')):
                errors.append(f'Unresolved authoring placeholders: {name}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', action='store_true')
    errors = check(parser.parse_args().release)
    print('\n'.join(errors) if errors else 'PASS: scaffold, schedules, lab structure, and local links')
    sys.exit(bool(errors))
