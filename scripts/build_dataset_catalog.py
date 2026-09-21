"""Build and validate the public dataset catalog from the two metadata CSVs.

The build is standalone: it requires neither manuscript sources nor a TeX setup.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
TASKS = [('denoising', 'Denoising'), ('deblurring', 'Deblurring'),
         ('dehazing', 'Dehazing'), ('low-light', 'Low-light enhancement'),
         ('deraining', 'Deraining'), ('desnowing', 'Desnowing')]
MAIN_COUNTS = dict(zip(['denoising', 'deraining', 'dehazing', 'deblurring', 'low-light', 'desnowing'],
                       [6, 9, 15, 10, 15, 4]))
FULL_COUNTS = dict(zip(['denoising', 'deraining', 'dehazing', 'deblurring', 'low-light', 'desnowing'],
                       [18, 28, 32, 29, 35, 18]))
SELECTED = {'denoising': 'RENOIR', 'deblurring': 'DPDD', 'dehazing': 'LMHaze',
            'low-light': 'LSRW', 'deraining': 'SPA-Data', 'desnowing': 'RealSnow'}
FIELDS = ['task', 'name', 'input_count', 'reference_count', 'resolution',
          'input_source', 'same_domain', 'pairing', 'degradation_profile',
          'year_venue', 'citation_key', 'source_title', 'source_url',
          'selected_evaluation']
PROTOCOLS = {
    'RENOIR': 'Real camera noise; distinguish RAW and processed releases and the camera subsets.',
    'DPDD': 'Real defocus blur; distinguish single-image input from the dual-pixel track.',
    'LMHaze': 'Physically generated haze captured in indoor and outdoor scenes at multiple intensities.',
    'LSRW': 'Captured low/normal-light pairs; some outdoor pairs contain local offsets.',
    'SPA-Data': 'Real rain videos with reference construction using temporal information.',
    'RealSnow': 'Real snowy scenes with reference construction from dedicated capture sequences.',
}


def read_rows(filename):
    with (ROOT / 'data' / filename).open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == FIELDS, (filename, reader.fieldnames)
        return list(reader)


def validate(rows, counts, main=False):
    assert Counter(r['task'] for r in rows) == counts
    identities = [(r['task'], r['name'].lower()) for r in rows]
    assert len(identities) == len(set(identities)), 'Duplicate task-specific dataset entry.'
    for r in rows:
        assert all(r[k] for k in ['name', 'input_count', 'reference_count', 'resolution',
                                  'input_source', 'degradation_profile', 'year_venue',
                                  'citation_key', 'source_title']), r
        assert r['input_source'] in {'Real', 'Real and synthetic'}, r
        if main: assert r['input_source'] == 'Real', r
        assert r['selected_evaluation'] in {'yes', 'no'}, r
        assert re.fullmatch(r'[A-Za-z0-9_-]+', r['citation_key']), r
        if r['source_url']:
            url = urlparse(r['source_url'])
            assert url.scheme in {'http', 'https'} and url.netloc
            assert not url.username and not url.password
            assert not re.search(r'\s', r['source_url'])
        for value in r.values():
            assert not re.search(r'(?:(?<![A-Za-z])[A-Za-z]:[\\/]|file://|\\(?:Users|Manuscript)\\)', value), value
    chosen = {r['task']: r['name'] for r in rows if r['selected_evaluation'] == 'yes'}
    assert chosen == SELECTED, chosen
    assert all(r['source_url'] for r in rows if r['selected_evaluation'] == 'yes')


def md(value):
    return str(value).replace('|', '&#124;').replace('<', '&lt;').replace('>', '&gt;')


def source_id(row):
    return 'source-' + row['citation_key'].lower()


def dataset_name(row):
    name = md(row['name'])
    if row['source_url']: name = f'[{name}]({row["source_url"]})'
    return name + f' · [ref](#{source_id(row)})'


def table_row(values):
    return '| ' + ' | '.join(values) + ' |'


def render(main, full):
    out = [
        '# Dataset catalog', '', '[Back to overview](../README.md) · [Protocol guide](DATASETS.md)', '',
        'This catalog has two complementary views: **59 task-specific entries** used in the '
        'six-task distribution comparison, and **160 task-specific entries** in the extended '
        'six-task inventory. Multi-task releases appear under each relevant task; these totals '
        'are not counts of unique dataset releases. The separate [26-entry protocol guide](DATASETS.md) '
        'is a curated starting point, not the complete catalog.', '',
        '**Real/Synth.** describes the degraded-input source. **Real** includes controlled '
        'physical capture, such as photographed artificial haze. It does not assert pixel alignment '
        'or imply that reference images were obtained without processing. Pairing is recorded '
        'separately: scene correspondence, approximate correspondence, unpaired data, and mixed '
        'supervision remain distinct.', '',
        'The 59-entry view aggregates the reported splits for its input/reference counts. The '
        'extended inventory preserves source count units and split notation, including frames, '
        'clips, groups, and synthetic/real subsets. Counts in different units must not be summed. '
        '**NR** means not reported; **N/A** means not applicable. A blank metadata field is shown '
        'as an em dash. Each row links to bibliographic metadata; a direct source link is supplied '
        'where available. No datasets are redistributed.', '',
        '| Task | Distribution comparison | Extended inventory | Selected evaluation dataset |',
        '|---|---:|---:|---|',
    ]
    for task, label in TASKS:
        chosen = next(r for r in main if r['task'] == task and r['selected_evaluation'] == 'yes')
        out.append(table_row([label, str(MAIN_COUNTS[task]), str(FULL_COUNTS[task]), dataset_name(chosen)]))
    out += ['', '## Six selected evaluation datasets', '',
            'These six resources cover the selected evaluation tasks. Unpaired training and '
            'reference-based evaluation are separate choices: training correspondence can be '
            'withheld while held-out references support evaluation. Follow the original release '
            'splits, registration rules, input tracks, and reference construction.', '',
            '| Task | Dataset | Capture / protocol focus |', '|---|---|---|']
    for task, label in TASKS:
        r = next(r for r in main if r['task'] == task and r['selected_evaluation'] == 'yes')
        eval_label = 'Defocus deblurring' if task == 'deblurring' else label
        out.append(table_row([eval_label, dataset_name(r), PROTOCOLS[r['name']]]))
    out += ['', '## Distribution-comparison catalog: 59 entries', '',
            'Machine-readable file: [datasets_main.csv](../data/datasets_main.csv). All 59 '
            'degraded-input sources are classified as Real. Pairing information below is '
            'carried separately from the extended inventory where a matching entry exists.', '']
    for task, label in TASKS:
        out += [f'### {label}: distribution comparison', '',
                '| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |',
                '|---|---|---|---|---|---|---|']
        for r in main:
            if r['task'] != task: continue
            out.append(table_row([dataset_name(r), md(r['input_source']),
                md(r['input_count'] + ' / ' + r['reference_count']), md(r['resolution']),
                md(r['pairing']) or '—', md(r['degradation_profile']), md(r['year_venue'])]))
        out.append('')
    out += ['## Extended inventory: 160 entries', '',
            'Machine-readable file: [datasets_supplementary.csv](../data/datasets_supplementary.csv). '
            'This view also retains video, auxiliary sensing, recognition-oriented, unpaired, '
            'and mixed-supervision resources. Inclusion does not make a collection eligible '
            'for pixelwise restoration evaluation. The two views retain their original coverage: '
            'FoundIR-Lowlight is present in the 59-entry view but not in this 160-entry inventory.', '',
            'In the tables below, “same domain” concerns scene-domain comparability, not '
            'pixel correspondence. RS = rain streaks, RD = raindrops, RA = rain accumulation.', '']
    for task, label in TASKS:
        out += [f'### {label}: extended inventory', '',
                '| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |',
                '|---|---|---|---|---|---|---|']
        for r in full:
            if r['task'] != task: continue
            out.append(table_row([dataset_name(r), md(r['input_count'] + ' / ' + r['reference_count']),
                md(r['resolution']), md(r['same_domain']), md(r['pairing']),
                md(r['degradation_profile']), md(r['year_venue'])]))
        out.append('')
    refs = {}
    for r in main + full:
        if r['citation_key'] not in refs or r['source_url']:
            refs[r['citation_key']] = r
    out += ['## Source bibliography', '',
            'Titles identify the public papers associated with the dataset releases. '
            'A missing direct URL is left unfilled rather than inferred from the title.', '']
    for key, r in sorted(refs.items(), key=lambda x: x[0].lower()):
        title = md(r['source_title'])
        if r['source_url']: title = f'[{title}]({r["source_url"]})'
        out += [f'<a id="{source_id(r)}"></a>', '', f'- **{md(key)}** — {title}.', '']
    out += ['## Rebuild', '',
            'The CSV files contain public dataset metadata only. Rebuild this page locally with:', '',
            '```bash', 'python scripts/build_dataset_catalog.py',
            'python scripts/build_dataset_catalog.py --check', '```', '']
    return '\n'.join(out)


def build(check=False):
    main = read_rows('datasets_main.csv')
    full = read_rows('datasets_supplementary.csv')
    validate(main, MAIN_COUNTS, main=True)
    validate(full, FULL_COUNTS)
    content = render(main, full)
    target = ROOT / 'docs/DATASET_CATALOG.md'
    if check:
        assert target.read_text(encoding='utf-8') == content, 'Generated dataset catalog is out of date.'
    else:
        target.write_text(content, encoding='utf-8')
    return {'distribution_dataset_entries': len(main), 'extended_dataset_entries': len(full),
            'dataset_tasks': len(TASKS), 'selected_evaluation_datasets': SELECTED,
            'distribution_entries_real': sum(r['input_source'] == 'Real' for r in main),
            'source_references': len({r['citation_key'] for r in main + full})}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    print(json.dumps(build(args.check), indent=2))
