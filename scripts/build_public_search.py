"""Build the citation-linked public corpus from bibliographic metadata only.

The selected reading guide is independent. This module never rewrites its CSV
or the root README, and never copies manuscript text or benchmark measurements.
"""
from __future__ import annotations
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['id', 'citation_key', 'method', 'title', 'year', 'venue', 'tasks',
          'scope', 'count_group', 'paradigm', 'paper_url', 'code_url', 'code_status',
          'training_regime', 'access_note', 'year_basis', 'count_basis', 'checked_on']
GROUPS = {'six_task_restoration': 'Six-task restoration',
          'broader_restoration': 'Underwater / SR / sand-dust',
          'general_weather_translation': 'General / weather translation'}
GROUP_SCOPES = dict(zip(GROUPS.values(), ['six_task', 'broader_restoration', 'translation']))
FAMILIES = {'domain_translation', 'representation', 'prior_guided',
            'generative_transport', 'normalizing_flow', 'not_assigned'}
COUNT_BASIS = 'one canonical included paper; three disjoint scope groups; bounded corpus, not field-wide totals'

def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))

def write_csv(path, rows, fields):
    with Path(path).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: row.get(key, '') for key in fields} for row in rows)

def norm(value):
    return re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD', value).lower())

def md(value):
    return (str(value).replace('|', '&#124;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('\n', ' ').replace('{', '').replace('}', ''))

def public_url(url):
    parsed = urlsplit(url)
    return (parsed.scheme in {'http', 'https'} and bool(parsed.netloc)
            and not parsed.username and not parsed.password and not re.search(r'\s', url))

def validate(rows, check_bbl=None):
    assert rows, 'Empty paper corpus'
    for key in ['id', 'citation_key']:
        assert len(rows) == len({r[key] for r in rows}), f'Duplicate {key}'
    assert len(rows) == len({norm(r['title']) for r in rows}), 'Duplicate titles'
    for row in rows:
        assert row['paradigm'] in FAMILIES, row['id']
        assert row['count_group'] in GROUP_SCOPES, row['id']
        assert row['scope'] == GROUP_SCOPES[row['count_group']], row['id']
        assert 2017 <= int(row['year']) <= int(row['checked_on'][:4]), row['id']
        assert public_url(row['paper_url']), row['id']
        assert not row['code_url'] or public_url(row['code_url']), row['id']
        assert all(row[key] for key in ['citation_key', 'access_note', 'training_regime',
                                       'year_basis', 'count_basis', 'code_status']), row['id']
    if check_bbl:
        cited = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',
                               Path(check_bbl).read_text(encoding='utf-8')))
        missing = {r['citation_key'] for r in rows} - cited
        assert not missing, f'Uncited corpus records: {sorted(missing)}'
    return rows

def import_catalog(path):
    """Whitelist public fields; preserve verified code links by exact aliases."""
    legacy = []
    for name in ['data/papers.csv', 'data/public_search_papers.csv']:
        if (ROOT / name).exists():
            legacy += read_csv(ROOT / name)
    selected = []
    for item in read_csv(path):
        if item.get('count_in_year_stats', 'true').lower() != 'true':
            continue
        row = {key: item.get(key, '').strip() for key in FIELDS}
        row['id'] = item.get('canonical_key') or item.get('record_id') or item.get('id')
        row['scope'] = GROUP_SCOPES[row['count_group']]
        matches = [old for old in legacy if old.get('id') in {row['id'], row['citation_key']}
                   or norm(old['title']) == norm(row['title'])]
        if not row['code_url']:
            linked = next((old for old in matches if old.get('code_url')), None)
            if linked:
                row['code_url'], row['code_status'] = linked['code_url'], linked['code_status']
        row['code_status'] = row['code_status'] or (
            'primary_source_linked_repository' if row['code_url'] else 'not_verified')
        if not row['paradigm']:
            row['paradigm'] = next((old['paradigm'] for old in matches
                                   if old.get('paradigm') in FAMILIES), 'not_assigned')
        row['access_note'] = row['access_note'] or row['training_regime']
        row['count_basis'] = COUNT_BASIS
        selected.append(row)
    selected.sort(key=lambda r: (int(r['year']), r['count_group'], r['method'].casefold()))
    validate(selected)
    write_csv(ROOT / 'data/public_search_papers.csv', selected, FIELDS)

def year_counts(rows):
    cutoff = max(r['checked_on'] for r in rows)
    output = []
    for year in range(min(int(r['year']) for r in rows), int(cutoff[:4]) + 1):
        annual = [r for r in rows if int(r['year']) == year]
        row = {'year': year, 'total': len(annual),
               **{key: sum(r['count_group'] == label for r in annual) for key, label in GROUPS.items()},
               'is_partial_year': str(year == int(cutoff[:4])).lower(),
               'cutoff_date': cutoff, 'count_basis': COUNT_BASIS}
        assert row['total'] == sum(row[key] for key in GROUPS)
        output.append(row)
    assert sum(r['total'] for r in output) == len(rows)
    return output

def build_chart(rows, counts):
    """Plot additive counts of included papers, without population estimates."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    from PIL import Image
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'svg.fonttype': 'none', 'svg.hashsalt': 'unpaired-corpus-142',
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.labelcolor': '#344054', 'text.color': '#182230',
                         'xtick.color': '#475467', 'ytick.color': '#475467',
                         'hatch.linewidth': .5})
    colors, hatches = ['#0072B2', '#009E73', '#E69F00'], ['', '///', '...']
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.7), gridspec_kw={'width_ratios': [1.4, 1]})
    fig.patch.set_facecolor('#FFFFFF')
    positions, bottom = list(range(len(counts))), [0] * len(counts)
    for (key, label), color, hatch in zip(GROUPS.items(), colors, hatches):
        values = [r[key] for r in counts]
        axes[0].bar(positions, values, bottom=bottom, width=.67, color=color,
                    edgecolor='white', linewidth=.65, hatch=hatch, label=label)
        bottom = [a + b for a, b in zip(bottom, values)]
    for x, total in zip(positions, bottom):
        axes[0].text(x, total + .45, str(total), ha='center', va='bottom', fontsize=10)
    axes[0].set_xticks(positions, [str(r['year']) + ('*' if r['is_partial_year'] == 'true' else '') for r in counts])
    axes[0].tick_params(axis='x', labelrotation=40, labelsize=10)
    axes[0].set_ylim(0, max(bottom) + 5)
    axes[0].set_ylabel('Included papers')
    axes[0].yaxis.set_major_locator(MaxNLocator(integer=True))
    axes[0].set_title('Publication-year distribution', loc='left', fontweight='bold', pad=16)
    totals = [sum(r[key] for r in counts) for key in GROUPS]
    bars = axes[1].barh(range(3), totals, color=colors, height=.51, edgecolor='white', linewidth=.65)
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)
    axes[1].set_yticks(range(3), ['Six-task\nrestoration', 'Underwater / SR /\nsand-dust', 'General / weather\ntranslation'])
    axes[1].invert_yaxis()
    axes[1].bar_label(bars, padding=5, fontsize=12, fontweight='bold')
    axes[1].set_xlim(0, max(totals) + 15)
    axes[1].set_xlabel('Included papers')
    axes[1].set_xticks(range(0, max(totals) + 16, 20))
    axes[1].set_title('Three disjoint scope groups', loc='left', fontweight='bold', pad=16)
    for ax in axes:
        ax.set_axisbelow(True)
        ax.grid(axis='y' if ax is axes[0] else 'x', alpha=.13)
        ax.tick_params(length=0, pad=6)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper left', bbox_to_anchor=(.055, .89),
               ncol=3, frameon=False, fontsize=10, handlelength=1.8, columnspacing=2)
    fig.text(.055, .955, f'UNPAIRED IMAGE RESTORATION  /  {len(rows)}-PAPER CORPUS', fontsize=12, fontweight='bold', color='#344054')
    fig.text(.055, .034, f'Cutoff: {counts[-1]["cutoff_date"]}  ·  * Latest year is partial.  One canonical paper per count; curated coverage, not a field-wide census.', fontsize=9, color='#667085')
    fig.subplots_adjust(left=.06, right=.97, top=.70, bottom=.22, wspace=.54)
    fig.canvas.draw()
    renderer, outside = fig.canvas.get_renderer(), []
    for artist in fig.findobj(match=lambda x: hasattr(x, 'get_text')):
        if not artist.get_visible() or not artist.get_text():
            continue
        bbox = artist.get_window_extent(renderer)
        if not (fig.bbox.contains(*bbox.get_points()[0]) and fig.bbox.contains(*bbox.get_points()[1])):
            outside.append(artist.get_text())
    assert not outside, ('Text outside chart canvas', outside)
    path = ROOT / 'assets/corpus-overview'
    fig.savefig(path.with_suffix('.png'), dpi=180)
    fig.savefig(path.with_suffix('.svg'), metadata={'Date': None})
    (ROOT / '.preview').mkdir(exist_ok=True)
    Image.open(path.with_suffix('.png')).convert('L').save(ROOT / '.preview/corpus-grayscale.png')
    plt.close(fig)

def build(check_bbl=None):
    rows = validate(read_csv(ROOT / 'data/public_search_papers.csv'), check_bbl)
    counts = year_counts(rows)
    write_csv(ROOT / 'data/public_search_year_counts.csv', counts, list(counts[0]))
    build_chart(rows, counts)
    cutoff = counts[-1]['cutoff_date']
    guide = read_csv(ROOT / 'data/papers.csv')
    guide_titles = {norm(r['title']) for r in guide}
    overlap = sum(norm(r['title']) in guide_titles for r in rows)
    totals = {key: sum(r[key] for r in counts) for key in GROUPS}
    doc = ['# Citation-linked paper corpus: unpaired image restoration', '', '[Back to the resource overview](../README.md)', '',
           f'**{len(rows)} canonical papers · cutoff {cutoff} · 2026 is a partial year.**', '',
           'This corpus covers six restoration tasks, broader restoration settings and general/weather translation. Every row has a canonical identifier, a citation key, a primary paper link and a publication-year basis. The annual chart and table below count exactly this CSV.', '',
           '![Annual paper counts and the three disjoint scope groups.](../assets/corpus-overview.svg)', '',
           '## Scope and counting', '',
           f'- **Six-task restoration ({totals["six_task_restoration"]}):** denoising, deblurring, dehazing, low-light enhancement, deraining and desnowing.',
           f'- **Broader restoration ({totals["broader_restoration"]}):** underwater enhancement, super-resolution and sand/dust removal.',
           f'- **General/weather translation ({totals["general_weather_translation"]}):** general unpaired image translation, night/day and adverse-weather translation. A methodological or forward weather-generation contribution is not automatically an evaluated inverse-restoration method.', '',
           'Each canonical paper belongs to one count group, so these three groups sum to the total. Task tags can overlap. Preprint/final versions and citation aliases are merged; the `citation_key` column preserves the bibliography mapping. Years use the final proceedings or journal issue when verified, otherwise the first public preprint year. The current year is incomplete.', '',
           'The collection is a bounded literature snapshot, not an estimate of all worldwide publications. A zero count means no included record, not that no relevant work existed. The counts do not measure quality, popularity or restoration performance.', '',
           '## Annual counts', '',
           '[Paper CSV](../data/public_search_papers.csv) · [Annual-count CSV](../data/public_search_year_counts.csv) · [Discovery-query ledger](../data/public_search_queries.csv)', '',
           '| Year | Total | Six-task restoration | Underwater / SR / sand-dust | General / weather translation |', '|---|---:|---:|---:|---:|']
    for count in counts:
        label = str(count['year']) + (' (partial)' if count['is_partial_year'] == 'true' else '')
        doc.append('| ' + label + ' | ' + ' | '.join(str(count[key]) for key in ['total', *GROUPS]) + ' |')
    doc += ['| **Total** | **' + str(len(rows)) + '** | ' + ' | '.join(str(totals[key]) for key in GROUPS) + ' |', '',
            '## Relationship to the selected reading guide', '',
            f'The [selected reading guide](../data/papers.csv) contains {len(guide)} records, including historical foundations and adjacent supervision settings. It overlaps this corpus in {overlap} papers. It is a reading selection, not another group to add to the corpus total. The primary overview and annual chart use this complete counted corpus.', '',
            '## Evidence and access', '',
            'Primary links point to publisher/proceedings pages, author manuscripts, project pages or attributable repositories. Restoration entries document an independent-domain branch; internally generated pseudo pairs are allowed. Auxiliary depth, event observations, semantic/quality networks and pretrained priors are recorded in the access notes. These methods therefore do not all have an identical supervision budget.', '',
            'General translation is counted separately from restoration, including forward degradation generation. Noisy-only or single-image methods, same-scene reference guidance and methods relying on source-paired supervision without an established independent-domain branch are not automatically counted as unpaired restoration. Unresolved cases remain excluded from the counted corpus.', '',
            'The query ledger records the earlier main discovery pass; later coverage expansion used exact-title, publication-year, author-code and task-specific searches for underwater enhancement, super-resolution, sand/dust removal and general/weather translation. It is not an export of every search result. Not every full implementation has been audited. Blank code links mean an attributable implementation was not verified, not that none exists. Release status and access qualifications remain visible below. The corpus contains bibliography and resource metadata, without benchmark measurements.', '',
            '## Rebuild and contribute', '',
            'Run `python scripts/build_public_search.py` to rebuild this page, the annual CSV and chart from the public paper CSV. `python scripts/build_resources.py` refreshes these outputs along with the other resource indexes. Run `python scripts/check_public_bundle.py` for bundle validation. An optional `--check-bbl PATH` checks that every citation key appears in a supplied compiled bibliography; the bibliography itself is not copied into this repository. Corrections should provide a primary URL, access evidence and a publication-year basis; see [CONTRIBUTING.md](../CONTRIBUTING.md).', '',
            '## Included papers and access notes']
    for year in reversed([count['year'] for count in counts]):
        annual = sorted((r for r in rows if int(r['year']) == year), key=lambda r: (r['count_group'], r['method'].casefold()))
        if not annual:
            continue
        doc += ['', f'### {year}', '', '| Paper / method | Venue · count group | Tasks | Access qualification / code |', '|---|---|---|---|']
        for row in annual:
            code = (f' [Author code]({row["code_url"]}) ({md(row["code_status"].replace("_", " "))}).'
                    if row['code_url'] else ' Code link not verified.')
            access = '. '.join(dict.fromkeys(value.rstrip('.') for value in [row['training_regime'], row['access_note']] if value)) + '.'
            doc.append(f'| <a id="paper-{row["id"]}"></a>**{md(row["method"])}** · [{md(row["title"])}]({row["paper_url"]}) | {md(row["venue"])} · {md(row["count_group"])} | {md(row["tasks"].replace(";", ", "))} | {md(access)}{code} |')
    (ROOT / 'docs/PUBLIC_SEARCH_2026.md').write_text('\n'.join(doc) + '\n', encoding='utf-8')
    summary = {'paper_records': len(rows), 'scope_counts': totals,
               'annual_counts': {str(r['year']): r['total'] for r in counts},
               'code_links': sum(bool(r['code_url']) for r in rows),
               'reading_guide_records': len(guide), 'reading_guide_overlap': overlap,
               'cutoff_date': cutoff, 'all_keys_cited': bool(check_bbl)}
    print(json.dumps(summary, indent=2))
    return summary

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--import-catalog', type=Path)
    parser.add_argument('--check-bbl', type=Path)
    args = parser.parse_args()
    if args.import_catalog:
        import_catalog(args.import_catalog)
    build(args.check_bbl)
