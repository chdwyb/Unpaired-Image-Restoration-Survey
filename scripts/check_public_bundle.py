"""Check the publication allowlist, counts and local links without network calls."""
import csv
import json
from pathlib import Path
import re
from urllib.parse import unquote
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_ROOT_FILES = {'README.md', 'CONTRIBUTING.md', 'REUSE.md', 'requirements.txt', '.gitignore'}
ALLOWED_DIRS = {'data', 'docs', 'assets', 'scripts', '.github'}
FORBIDDEN_SUFFIXES = {'.tex', '.bib', '.pdf', '.aux', '.bbl', '.log', '.pt', '.pth', '.ckpt', '.safetensors'}
SCORE_FIELDS = {'PSNR', 'SSIM', 'LPIPS', 'FID', 'NIQE', 'TOPIQ-NR', 'PIQE', 'ILNIQE', 'MUSIQ', 'CLIP-IQA'}


def main():
    paths = [p for p in ROOT.rglob('*') if p.is_file() and not any(x in {'.git', '.preview', '__pycache__'} for x in p.relative_to(ROOT).parts)]
    errors = []
    for path in paths:
        rel = path.relative_to(ROOT)
        if len(rel.parts) == 1 and path.name not in ALLOWED_ROOT_FILES:
            errors.append(f'Unapproved root file: {rel}')
        if len(rel.parts) > 1 and rel.parts[0] not in ALLOWED_DIRS:
            errors.append(f'Unapproved folder: {rel}')
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f'Private/binary research artifact: {rel}')
        if any(x in path.name.lower() for x in ['manuscript', 'mock', 'comparison_metrics', 'main.tex']):
            errors.append(f'Private artifact name: {rel}')
        if path.suffix in {'.md', '.csv', '.json', '.yml'}:
            text = path.read_text(encoding='utf-8')
            if re.search(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{30,}|I:[/\\]Manuscript|C:[/\\]Users)', text):
                errors.append(f'Credential or private-path pattern: {rel}')
        if path.suffix == '.csv':
            with path.open(encoding='utf-8-sig') as handle:
                reader = csv.DictReader(handle)
                if set(reader.fieldnames or []) & SCORE_FIELDS:
                    errors.append(f'Experiment-score columns: {rel}')
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if target.startswith(('http://', 'https://', '#')):
                    continue
                local = (path.parent / unquote(target.split('#')[0])).resolve()
                if not local.is_relative_to(ROOT) or not local.exists():
                    errors.append(f'Broken/outside local link: {rel} -> {target}')
    with (ROOT/'data/papers.csv').open(encoding='utf-8-sig') as handle:
        papers = list(csv.DictReader(handle))
    stats = json.loads((ROOT/'data/collection_stats.json').read_text(encoding='utf-8'))
    if stats['paper_records'] != len(papers) or sum(r['total'] for r in stats['year_counts']) != len(papers):
        errors.append('Inconsistent paper/year counts')
    if stats['code_links'] != sum(bool(r['code_url']) for r in papers):
        errors.append('Inconsistent public-code count')
    ids = [r['id'] for r in papers]
    if len(set(ids)) != len(ids):
        errors.append('Duplicate canonical paper identifiers')
    titles = Counter(re.sub(r'[^a-z0-9]', '', r['title'].lower()) for r in papers)
    if any(n > 1 for n in titles.values()):
        errors.append('Duplicate normalized paper titles')
    if dict(Counter(r['scope'] for r in papers)) != stats['scope_counts']:
        errors.append('Inconsistent scope counts')
    for task, n in stats['task_counts_core_nonexclusive'].items():
        actual = sum(r['scope'] == 'core' and task in r['tasks'].split(';') for r in papers)
        if n != actual:
            errors.append(f'Inconsistent task count: {task}')
    for row in papers:
        if not row['paper_url'].startswith(('https://', 'http://')):
            errors.append(f'Missing primary paper URL: {row["id"]}')
        if row['code_url'] and row['code_status'] in ['', 'not_verified']:
            errors.append(f'Unqualified implementation URL: {row["id"]}')
    print(json.dumps({'status': 'FAIL' if errors else 'PASS', 'public_files': len(paths),
                      'paper_records': len(papers), 'errors': errors}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
