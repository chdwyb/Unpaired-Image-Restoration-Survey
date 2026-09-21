"""Build the public resource index solely from bibliographic CSV metadata."""
from __future__ import annotations

import argparse
import collections
import csv
from datetime import date
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['id', 'method', 'title', 'year', 'venue', 'tasks', 'scope', 'paradigm',
          'paper_url', 'code_url', 'code_status', 'training_regime', 'access_note', 'year_basis']
TASKS = [('denoising', 'Denoising'), ('deblurring', 'Deblurring'),
         ('dehazing', 'Dehazing'), ('low-light', 'Low-light enhancement'),
         ('deraining', 'Deraining'), ('desnowing', 'Desnowing')]
SCOPE_LABELS = {'core': 'Core restoration', 'foundation': 'Foundations', 'adjacent': 'Adjacent settings'}
COLORS = {'core': '#0072B2', 'foundation': '#E69F00', 'adjacent': '#999999'}


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, fields):
    with Path(path).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean(value):
    return str(value or '').replace('\n', ' ').strip()


def md(value):
    return clean(value).replace('|', '&#124;').replace('<', '&lt;').replace('>', '&gt;')


def link(label, url):
    if not url:
        return '—'
    if not re.match(r'^https?://[^\s]+$', url):
        raise ValueError(f'Non-web or malformed source link: {url!r}')
    return f'[{md(label)}]({url})'


def task_tags(value):
    aliases = {'low-light enhancement': 'low-light', 'low light': 'low-light',
               'image denoising': 'denoising', 'motion deblurring': 'deblurring',
               'defocus deblurring': 'deblurring', 'image dehazing': 'dehazing',
               'rain removal': 'deraining', 'snow removal': 'desnowing',
               'sr': 'super-resolution', 'super resolution': 'super-resolution',
               'backlit enhancement': 'low-light'}
    return list(dict.fromkeys(aliases.get(x.strip().lower(), x.strip().lower())
                             for x in re.split(r'[;,]', value) if x.strip()))


def import_catalog(path):
    """Whitelist public bibliography fields; never import scores or manuscript text."""
    rows = []
    for item in read_csv(path):
        row = {key: clean(item.get(key, '')) for key in FIELDS}
        row['id'] = clean(item.get('id') or item.get('citation_key') or item.get('key'))
        row['title'] = clean(item.get('title') or item.get('paper_title'))
        row['tasks'] = ';'.join(task_tags(item.get('tasks') or item.get('task') or ''))
        row['scope'] = clean(item.get('scope') or item.get('category')).lower()
        row['access_note'] = clean(item.get('access_note') or item.get('inclusion_note'))
        rows.append(row)
    write_csv(ROOT / 'data/papers.csv', rows, FIELDS)


def validate(rows):
    assert rows, 'The paper catalog is empty.'
    ids = [r['id'] for r in rows]
    assert len(ids) == len(set(ids)), 'Duplicate canonical paper identifiers.'
    for r in rows:
        assert all(r[k] for k in ['id', 'title', 'year', 'venue', 'scope', 'paper_url']), r
        assert re.fullmatch(r'[A-Za-z0-9_-]+', r['id']), r['id']
        assert r['scope'] in SCOPE_LABELS, (r['id'], r['scope'])
        assert 1900 <= int(r['year']) <= date.today().year, (r['id'], r['year'])
        link('Paper', r['paper_url'])
        if r['code_url']:
            link('Code', r['code_url'])
    return rows


def paper_name(r):
    return r['method'] or r['title']


def access_text(r):
    return '. '.join(dict.fromkeys(x.rstrip('.') for x in
                                  [r['training_regime'], r.get('access_note', '')] if x)) + '.'


def paper_row(r, anchor=True):
    prefix = f'<a id="paper-{r["id"]}"></a>' if anchor else ''
    method = f'**{md(r["method"])}** · ' if r['method'] else ''
    code = link('Author code', r['code_url']) if r['code_url'] else 'Not verified'
    if r['code_url'] and any(x in r['code_status'].lower() for x in ['partial', 'pending', 'inference']):
        code += ' (partial release)'
    return ('| ' + prefix + method + link(r['title'], r['paper_url']) + ' | ' +
            md(r['venue']) + ' | ' + md(', '.join(task_tags(r['tasks']))) + ' | ' +
            code + ' | ' + SCOPE_LABELS[r['scope']] + ' |')


def paper_table(rows, anchor=True):
    return '\n'.join(['| Paper / method | Venue | Task tags | Implementation | Scope |',
                      '|---|---|---|---|---|'] + [paper_row(r, anchor) for r in rows])


def build_chart(rows, checked):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    from PIL import Image
    years = sorted({int(r['year']) for r in rows} | set(range(2017, max(int(r['year']) for r in rows) + 1)))
    counts = {s: collections.Counter(int(r['year']) for r in rows if r['scope'] == s) for s in SCOPE_LABELS}
    chart_years = [y for y in years if y >= 2017]
    has_older = any(y < 2017 for y in years)
    chart_labels = (['≤2016'] if has_older else []) + [str(y) for y in chart_years]
    positions = list(range(len(chart_labels)))
    core = [r for r in rows if r['scope'] == 'core']
    coverage = {task: sum(task in task_tags(r['tasks']) for r in core) for task, _ in TASKS}
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'svg.fonttype': 'none',
                         'svg.hashsalt': 'unpaired-reading-guide',
                         'axes.spines.top': False, 'axes.spines.right': False, 'axes.labelcolor': '#344054',
                         'text.color': '#182230', 'xtick.color': '#475467', 'ytick.color': '#475467'})
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.7), gridspec_kw={'width_ratios': [1.4, 1]})
    fig.patch.set_facecolor('#FFFFFF')
    bottom = [0] * len(positions)
    for scope, hatch in [('core', ''), ('foundation', '//'), ('adjacent', '..')]:
        values = ([sum(n for y, n in counts[scope].items() if y < 2017)] if has_older else []) + [counts[scope][y] for y in chart_years]
        axes[0].bar(positions, values, bottom=bottom, color=COLORS[scope], width=.68,
                    edgecolor='white', linewidth=.6, hatch=hatch, label=SCOPE_LABELS[scope])
        bottom = [a + b for a, b in zip(bottom, values)]
    for year, total in zip(positions, bottom):
        if total:
            axes[0].text(year, total + .25, str(total), ha='center', va='bottom', fontsize=10)
    axes[0].set_xticks(positions, chart_labels)
    axes[0].tick_params(axis='x', labelrotation=45, labelsize=10)
    axes[0].yaxis.set_major_locator(MaxNLocator(integer=True))
    axes[0].set_ylim(0, max(bottom) * 1.18 + 1)
    axes[0].set_ylabel('Catalog records')
    axes[0].set_title('Publication-year distribution', loc='left', fontweight='bold', pad=16)
    axes[0].legend(frameon=False, loc='upper left', fontsize=9)
    labels = [label for _, label in TASKS]
    values = [coverage[t] for t, _ in TASKS]
    bars = axes[1].barh(labels, values, color='#0072B2', height=.57)
    axes[1].invert_yaxis()
    axes[1].bar_label(bars, padding=5, fontsize=10)
    axes[1].set_xlim(0, max(values + [1]) * 1.25 + 1)
    axes[1].xaxis.set_major_locator(MaxNLocator(integer=True))
    axes[1].set_xlabel('Core records with this task tag')
    axes[1].set_title('Six-task coverage', loc='left', fontweight='bold', pad=16)
    for ax in axes:
        ax.set_axisbelow(True)
        ax.grid(axis='y' if ax is axes[0] else 'x', alpha=.13)
        ax.tick_params(length=0, pad=6)
    fig.text(.055, .965, 'UNPAIRED IMAGE RESTORATION  /  COLLECTION SNAPSHOT',
             fontsize=10, fontweight='bold', color='#667085')
    fig.text(.055, .035, f'Curated collection · {checked} · One record per paper; task tags overlap. Latest year incomplete. Not a field-wide census.',
             fontsize=9, color='#667085')
    fig.subplots_adjust(left=.06, right=.97, top=.81, bottom=.24, wspace=.52)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    outside = []
    for artist in fig.findobj(match=lambda x: hasattr(x, 'get_text')):
        if not artist.get_visible() or not artist.get_text():
            continue
        bbox = artist.get_window_extent(renderer)
        if not (fig.bbox.contains(*bbox.get_points()[0]) and fig.bbox.contains(*bbox.get_points()[1])):
            outside.append(artist.get_text())
    assert not outside, ('Text outside chart canvas', outside)
    path = ROOT / 'assets/collection-overview'
    fig.savefig(path.with_suffix('.png'), dpi=180)
    fig.savefig(path.with_suffix('.svg'), metadata={'Date': None})
    (ROOT / '.preview').mkdir(exist_ok=True)
    Image.open(path.with_suffix('.png')).convert('L').save(ROOT / '.preview/overview-grayscale.png')
    plt.close(fig)
    year_rows = [{'year': y, **{s: counts[s][y] for s in SCOPE_LABELS},
                  'total': sum(counts[s][y] for s in SCOPE_LABELS)} for y in years]
    write_csv(ROOT / 'data/year_counts.csv', year_rows, ['year', *SCOPE_LABELS, 'total'])
    return coverage, year_rows


def build(checked):
    for folder in ['assets', 'docs', 'data']:
        (ROOT / folder).mkdir(exist_ok=True)
    from build_public_search import build as build_public_search
    build_public_search()
    from build_dataset_catalog import build as build_dataset_catalog
    build_dataset_catalog()
    corpus = read_csv(ROOT / 'data/public_search_papers.csv')
    corpus_scopes = collections.Counter(r['scope'] for r in corpus)
    corpus.sort(key=lambda r: (-int(r['year']), r['title'].lower()))
    corpus_coverage = {task: sum(r['scope'] == 'six_task' and task in task_tags(r['tasks'])
                               for r in corpus) for task, _ in TASKS}
    main_datasets = read_csv(ROOT / 'data/datasets_main.csv')
    full_datasets = read_csv(ROOT / 'data/datasets_supplementary.csv')
    rows = validate(read_csv(ROOT / 'data/papers.csv'))
    rows.sort(key=lambda r: (-int(r['year']), r['title'].lower()))
    datasets = read_csv(ROOT / 'data/datasets.csv')
    coverage, year_rows = build_chart(rows, checked)
    scopes = collections.Counter(r['scope'] for r in rows)
    linked = sum(bool(r['code_url']) for r in rows)
    years = sorted({int(r['year']) for r in rows}, reverse=True)
    nav = ' · '.join(f'[{y}](#year-{y})' for y in years)
    task_index = ['| Task | Counted-corpus records | Browse |', '|---|---:|---|']
    for task, label in TASKS:
        task_index.append(f'| {label} | {corpus_coverage[task]} | [Papers and access notes](docs/TASKS.md#{task}) |')
    summary = f'''# Unpaired Image Restoration

**A curated research resource for papers, implementations and datasets.**

Explore restoration learned without aligned task-specific degraded–clean targets, with related foundations and supervision settings labelled separately.

**{len(corpus)} counted papers** · **{len(main_datasets)} real-data entries** · **{len(full_datasets)} full-inventory entries** · **6 evaluation tasks**

Last curated: **{checked}**

[Full paper corpus](docs/PUBLIC_SEARCH_2026.md) · [Datasets](docs/DATASET_CATALOG.md) · [Six tasks](#six-task-index) · [Selected reading guide](#papers-by-year) · [Code index](docs/CODE.md) · [Scope and counting](docs/SCOPE.md)

## Collection overview

![Annual counts and coverage of the {len(corpus)}-paper corpus.](assets/corpus-overview.svg)

The counted corpus contains **{corpus_scopes['six_task']} six-task restoration papers**, **{corpus_scopes['broader_restoration']} papers on super-resolution, underwater enhancement and sand/dust removal**, and **{corpus_scopes['translation']} general or weather-translation papers**. Each paper belongs to one counting group and appears once. These are counts of the screened collection, not worldwide publication totals; 2026 is incomplete. [Full paper list and annual table](docs/PUBLIC_SEARCH_2026.md) · [Paper CSV](data/public_search_papers.csv) · [Year counts](data/public_search_year_counts.csv).

The **{len(rows)}-record selected reading guide** below also includes methodological foundations and adjacent supervision settings. It overlaps the counted corpus and is not an additional {len(rows)} papers. Its **{linked} author-code links** are listed with access notes. [Counting rules](docs/SCOPE.md).

## Evaluation datasets

| Task | Selected dataset | Input source |
|---|---|---|
| Denoising | RENOIR | Real |
| Defocus deblurring | DPDD | Real |
| Dehazing | LMHaze | Real |
| Low-light enhancement | LSRW | Real |
| Deraining | SPA-Data | Real |
| Desnowing | RealSnow | Real |

The [dataset catalog](docs/DATASET_CATALOG.md) links the original sources and lists **{len(main_datasets)} real-input entries** used in dataset coverage analysis, plus the **{len(full_datasets)}-entry full inventory** in six task groups. The real-input table includes a **Real/Synth.** column; controlled physical capture is classified as real. Real input does not imply exact pixel alignment, and reference construction is described separately.

## Six-task index

{chr(10).join(task_index)}

This navigation table counts the {corpus_scopes['six_task']} papers in the six-task group. Task tags overlap and describe documented scope, not transfer to every benchmark. The [full corpus](docs/PUBLIC_SEARCH_2026.md) also includes broader restoration and general/weather translation; related foundations remain available in the selected reading guide.

## Dataset guide

Start with the data's **capture process and reference type**. Captured paired benchmarks, digitally synthesized pairs, independent image collections and scene correspondences support different evaluations.

The [complete dataset catalog](docs/DATASET_CATALOG.md) provides the two synchronized inventories. The following {len(datasets)}-entry primer highlights reference construction and protocol distinctions.

- [Captured paired data](docs/DATASETS.md#captured-paired-data): noisy/reference captures, real blur, controlled haze, exposure pairs, and video-derived rain or snow targets.
- [Synthetic paired data](docs/DATASETS.md#synthetic-paired-data): digital or video-integrated degradations with corresponding clean targets.
- [Unpaired collections](docs/DATASETS.md#unpaired-collections): independent-domain training pools and natural degraded images without aligned clean targets.
- [Scene correspondence](docs/DATASETS.md#scene-correspondence): related scenes that should not be treated as pixel-aligned restoration references.

Withholding correspondence can define an unpaired training protocol on paired data. It does not remove the need to document scene overlap, splits and reference use. The [dataset guide](docs/DATASETS.md) records these distinctions without combining incomparable scores.

## Papers by year

### Selected reading guide

The tables below contain {len(rows)} selected and background records. For all {len(corpus)} counted papers, including expanded restoration and translation coverage, use the [full corpus](docs/PUBLIC_SEARCH_2026.md).

{nav}

Titles link to primary papers or author records. “Author code” indicates a public implementation link, not a license or reproduction guarantee. See the [code index](docs/CODE.md) for release qualifications.
'''
    for year in years:
        subset = [r for r in rows if int(r['year']) == year]
        summary += f'\n<a id="year-{year}"></a>\n\n### {year}\n\n' + paper_table(subset) + '\n'
    summary += '''
## Contributing and reuse

Corrections and additional primary-source records are welcome. Follow the [contribution guide](CONTRIBUTING.md) and regenerate the indexes from the CSV files. Cite the original papers and datasets when using their work; linked resources retain their own [reuse terms](REUSE.md).

The navigation conventions of the [All-in-One Image Restoration resource collection](https://github.com/Harbinzzy/All-in-One-Image-Restoration-Survey) informed this directory's organization. Its prose, figures and experimental results are not reproduced here.
'''
    (ROOT / 'README.md').write_text(summary, encoding='utf-8')
    taskdoc = ['# Task index', '', '[Back to overview](../README.md)', '',
               f'The {corpus_scopes["six_task"]} six-task records in the [counted corpus](PUBLIC_SEARCH_2026.md) are grouped by documented restoration task. Multi-task papers appear in more than one section.']
    for task, label in TASKS:
        taskdoc += ['', f'<a id="{task}"></a>', '', f'## {label}', '',
                    '| Method / paper | Year | Supervision and access |', '|---|---:|---|']
        for r in corpus:
            if r['scope'] == 'six_task' and task in task_tags(r['tasks']):
                taskdoc.append(f'| {link(paper_name(r), r["paper_url"])} | {r["year"]} | {md(access_text(r))} |')
    taskdoc += ['', '## Related tasks and foundations', '',
                'The [full corpus](PUBLIC_SEARCH_2026.md) includes underwater enhancement, super-resolution, sand/dust removal, and general/weather translation. Selected background works below are not relabelled as six-task evaluations.', '',
                paper_table([r for r in rows if r['scope'] != 'core' or not set(task_tags(r['tasks'])) & {t for t, _ in TASKS}], False)]
    (ROOT / 'docs/TASKS.md').write_text('\n'.join(taskdoc) + '\n', encoding='utf-8')
    code_catalog = {re.sub(r'[^a-z0-9]', '', r['title'].lower()): r for r in rows}
    code_catalog.update({re.sub(r'[^a-z0-9]', '', r['title'].lower()): r for r in corpus})
    code_rows = sorted(code_catalog.values(), key=lambda r: (-int(r['year']), r['title'].lower()))
    codedoc = ['# Implementation index', '', '[Back to overview](../README.md)', '',
               f'This index combines the {len(corpus)}-paper counted corpus with the selected reading guide, merging overlapping titles. The counted corpus supplies {sum(bool(r["code_url"]) for r in corpus)} author-code links.', '',
               'Author-linked public repositories are access records, not reproduced experiments. A repository can omit training components or checkpoints. Consult each license before reuse.', '',
               '| Method / paper | Year | Public implementation | Release status | Access conditions |', '|---|---:|---|---|---|']
    for r in code_rows:
        if r['code_url']:
            codedoc.append(f'| {link(paper_name(r), r["paper_url"])} | {r["year"]} | {link("Repository", r["code_url"])} | {md(r["code_status"].replace("_", " "))} | {md(access_text(r))} |')
    codedoc += ['', '## No implementation link verified', '',
                ', '.join(link(paper_name(r), r['paper_url']) for r in code_rows if not r['code_url']) + '.', '',
                'A missing link means that this collection has not established an attributable public implementation; it is not a claim that no implementation exists.']
    (ROOT / 'docs/CODE.md').write_text('\n'.join(codedoc) + '\n', encoding='utf-8')
    datasetdoc = ['# Dataset guide', '', '[Back to overview](../README.md)', '',
                  f'For the {len(main_datasets)}-entry real-input table, the full {len(full_datasets)}-entry inventory, and the six selected evaluation datasets, see the [complete dataset catalog](DATASET_CATALOG.md). This page is a smaller protocol-oriented primer.', '',
                  'Training pairing and evaluation pairing are separate choices. References can be directly captured, processed estimates or scene correspondences. Follow the original release terms; this directory does not redistribute data.']
    groups = [('captured-paired-data', 'Captured paired data', lambda r: r['pairing'] in ['paired', 'paired estimated target']),
              ('synthetic-paired-data', 'Synthetic paired data', lambda r: r['pairing'] == 'paired synthetic degradation'),
              ('unpaired-collections', 'Unpaired collections', lambda r: r['pairing'] == 'unpaired'),
              ('scene-correspondence', 'Scene correspondence', lambda r: r['pairing'] == 'scene correspondence')]
    for slug, title, select in groups:
        datasetdoc += ['', f'<a id="{slug}"></a>', '', f'## {title}', '',
                       '| Dataset / primary source | Tasks | Capture and reference regime | Protocol note |', '|---|---|---|---|']
        for r in datasets:
            if select(r):
                datasetdoc.append(f'| {link(r["name"], r["source_url"])} | {md(r["tasks"].replace(";", ", "))} | {md(r["acquisition"] + "; " + r["pairing"])} | {md(r["protocol_note"])} |')
    (ROOT / 'docs/DATASETS.md').write_text('\n'.join(datasetdoc) + '\n', encoding='utf-8')
    scope = f'''# Scope, provenance and counting

[Back to overview](../README.md)

This is a selective, manually curated resource index, checked through **{checked}**. It is not a systematic-review census or a benchmark leaderboard.

## Primary counted corpus

The main overview uses [public_search_papers.csv](../data/public_search_papers.csv): **{len(corpus)} canonical papers**, grouped into **{corpus_scopes['six_task']} six-task restoration**, **{corpus_scopes['broader_restoration']} broader restoration**, and **{corpus_scopes['translation']} general/weather translation** records. The [full corpus page](PUBLIC_SEARCH_2026.md) defines these mutually exclusive groups and provides the annual table. Its chart and [annual CSV](../data/public_search_year_counts.csv) use the same collection. The 2026 count is partial.

## Inclusion categories

The following categories refer to the separate **{len(rows)}-record selected reading guide**, not to the primary counted corpus. The collections overlap and must not be added together.

- **Core restoration ({scopes['core']} records):** papers whose documented task includes restoration under an unpaired or unsupervised learning regime. Read the per-paper training-access note: generated pairs, pretrained priors and related-scene references can change the information available.
- **Foundations ({scopes['foundation']} records):** general translation or generative methods that provide relevant tools but are not automatically restoration evaluations.
- **Adjacent settings ({scopes['adjacent']} records):** related supervision or restoration approaches whose access assumptions differ from the core setting.

These labels organize reading. They do not establish that all papers share an identical supervision budget.

## Reproducible counts

The selected guide's source is [`data/papers.csv`](../data/papers.csv). Each row has a unique `id`; aliases and preprint revisions should not duplicate that row. Year grouping uses the catalog's explicit `year_basis`, normally the final conference/journal year, or the preprint year when only a preprint record is established. Multi-task labels are nonexclusive, so task counts need not sum to the number of papers.

The selected guide's auxiliary [plot](../assets/collection-overview.svg) and [`year_counts.csv`](../data/year_counts.csv) are rebuilt with `python scripts/build_resources.py`. Its annual bars count all guide records with scope shown separately; pre-2017 records are grouped into one bar. This auxiliary chart is separate from the primary {len(corpus)}-paper chart. The task panel counts guide core records carrying each of the six task tags. No missing-year extrapolation, worldwide publication estimate, citation impact or performance ranking is inferred.

## Dataset inventories

The [complete dataset catalog](DATASET_CATALOG.md) has **{len(main_datasets)} real-input task-specific entries** and **{len(full_datasets)} extended-inventory entries** across six task groups. These overlapping views have different purposes and their counts must not be added. A multi-task collection can occur in several task groups. The six selected evaluation datasets are RENOIR, DPDD, LMHaze, LSRW, SPA-Data and RealSnow. `Real/Synth.` describes the degraded input, independently of pairing, alignment or clean-reference construction.

## Access and evidence

Primary links point to publishers, proceedings, author manuscripts, projects or repositories. “Code linked” counts a nonempty attributable implementation URL. It is separate from license verification, training-code completeness, checkpoint availability and reproduced performance. Broken links or changed releases can be reported through an issue.

[`data/datasets.csv`](../data/datasets.csv) records acquisition and pairing at the release level. It contains metadata and protocol notes, not images or evaluation measurements. No performance measurements are included in this resource collection.

The source links remain the authority for each work's claims and reuse conditions. See [REUSE.md](../REUSE.md).
'''
    (ROOT / 'docs/SCOPE.md').write_text(scope, encoding='utf-8')
    stats = {'last_curated': checked, 'paper_records': len(rows), 'scope_counts': dict(scopes),
             'counted_corpus_records': len(corpus), 'main_dataset_entries': len(main_datasets),
             'full_dataset_entries': len(full_datasets), 'selected_evaluation_tasks': 6,
             'counted_corpus_code_links': sum(bool(r['code_url']) for r in corpus),
             'counted_task_coverage_nonexclusive': corpus_coverage,
             'code_links': linked, 'dataset_records': len(datasets), 'task_counts_core_nonexclusive': coverage,
             'year_counts': year_rows, 'counting_unit': 'one canonical bibliographic record',
             'coverage': 'curated_collection_not_global_census', 'numeric_experiment_data': False}
    (ROOT / 'data/collection_stats.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in stats.items() if k != 'year_counts'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--import-catalog', type=Path)
    parser.add_argument('--date', default=date.today().isoformat())
    args = parser.parse_args()
    if args.import_catalog:
        import_catalog(args.import_catalog)
    build(args.date)
