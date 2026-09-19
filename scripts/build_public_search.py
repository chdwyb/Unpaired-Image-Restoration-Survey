"""Build the separate public search appendix from bibliographic metadata only."""
from __future__ import annotations
import argparse
from collections import Counter
import csv
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['id', 'method', 'title', 'year', 'venue', 'tasks', 'paradigm',
          'paper_url', 'code_url', 'code_status', 'access_note', 'year_basis', 'checked_on']
FAMILIES = {'domain_translation': 'Domain translation',
            'representation': 'Representation learning',
            'prior_guided': 'Prior-guided learning',
            'generative_transport': 'Diffusion / generative transport',
            'normalizing_flow': 'Normalizing flows'}
START = '<!-- PUBLIC_SEARCH_APPENDIX_START -->'
END = '<!-- PUBLIC_SEARCH_APPENDIX_END -->'

def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))

def write_csv(path, rows, fields):
    with Path(path).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: row.get(key, '') for key in fields} for row in rows)

def md(value):
    return str(value).replace('|', '&#124;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', ' ')

def public_url(url):
    parsed = urlsplit(url)
    return parsed.scheme in {'http', 'https'} and bool(parsed.netloc) and not parsed.username and not parsed.password

def validate(rows):
    assert rows, 'Empty search catalogue'
    assert len(rows) == len({r['id'] for r in rows}), 'Duplicate search IDs'
    identities = [re.sub('[^a-z0-9]', '', r['title'].lower()) for r in rows]
    assert len(identities) == len(set(identities)), 'Duplicate search titles'
    for row in rows:
        assert row['paradigm'] in FAMILIES, row['id']
        assert 2017 <= int(row['year']) <= 2026, row['id']
        assert public_url(row['paper_url']), row['id']
        assert not row['code_url'] or public_url(row['code_url']), row['id']
        assert row['access_note'] and row['year_basis'], row['id']
    return rows

def import_catalog(path):
    """Explicit whitelist: no measurements, local paths or manuscript contents."""
    selected = []
    for item in read_csv(path):
        if item.get('scope') != 'core' or item.get('count_in_year_stats') != 'true':
            continue
        row = {key: item.get(key, '') for key in FIELDS}
        row['id'] = item.get('canonical_key') or item.get('record_id') or item.get('id')
        selected.append(row)
    validate(selected)
    write_csv(ROOT / 'data/public_search_papers.csv', selected, FIELDS)

def year_counts(rows):
    cutoff = max(r['checked_on'] for r in rows)
    output = []
    for year in range(2017, 2027):
        annual = [r for r in rows if int(r['year']) == year]
        row = {'year': year, 'verified_core_count': len(annual),
               **{key: sum(r['paradigm'] == key for r in annual) for key in FAMILIES},
               'is_partial_year': str(year == int(cutoff[:4])).lower(),
               'cutoff_date': cutoff,
               'count_basis': 'bounded publicly sourced corpus; not exhaustive field totals'}
        assert row['verified_core_count'] == sum(row[key] for key in FAMILIES)
        output.append(row)
    assert sum(r['verified_core_count'] for r in output) == len(rows)
    return output

def build():
    rows = validate(read_csv(ROOT / 'data/public_search_papers.csv'))
    counts = year_counts(rows)
    write_csv(ROOT / 'data/public_search_year_counts.csv', counts, list(counts[0]))
    cutoff = counts[-1]['cutoff_date']
    main = read_csv(ROOT / 'data/papers.csv')
    main_core = sum(r['scope'] == 'core' for r in main)
    main_ids = {r['id'] for r in main}
    new = sum(r['id'] not in main_ids for r in rows)
    doc = ['# Public search appendix: unpaired image restoration', '', '[Back to the curated overview](../README.md)', '',
           f'**{len(rows)} included papers · search cutoff {cutoff} · 2026 is a partial year.**', '',
           'This is a bounded collection of publicly discoverable papers with an independent degraded/clean-domain restoration branch. It is **not a global publication census**. A zero count means no included record in this search, not proof that no relevant paper existed.', '',
           '## How this differs from the main collection', '',
           f'The main [curated catalogue](../data/papers.csv) contains {len(main)} reading-guide records: {main_core} core restoration papers, plus foundations and adjacent settings. This appendix contains only included restoration papers and broadens the search to super-resolution, underwater enhancement and dedusting as well as the six main tasks. It adds {new} discovered core papers. UDGNet is included here as the full paper with an adversarial clean-image prior; the main guide retains the single-image variant as an adjacent setting. Thus the two collections have different purposes and should not be added together.', '',
           'The main catalogue, its counts and its overview chart remain unchanged. The search appendix is a separate snapshot, with paper-level primary links and access qualifications rather than numerical performance results.', '',
           '## Publication-year counts', '',
           '[Included-paper CSV](../data/public_search_papers.csv) · [Annual-count CSV](../data/public_search_year_counts.csv) · [Search query ledger](../data/public_search_queries.csv)', '',
           '| Year | Included papers | Domain translation | Representation | Prior-guided | Diffusion / transport | Normalizing flows |',
           '|---|---:|---:|---:|---:|---:|---:|']
    for count in counts:
        label = str(count['year']) + (' (partial)' if count['is_partial_year'] == 'true' else '')
        doc.append('| ' + label + ' | ' + ' | '.join(str(count[key]) for key in ['verified_core_count', *FAMILIES]) + ' |')
    doc += ['| **Total** | **' + str(len(rows)) + '** | ' + ' | '.join(str(sum(count[key] for count in counts)) for key in FAMILIES) + ' |', '',
            '## Scope, evidence and limitations', '',
            'Included branches learn from independent degraded and clean/high-quality domains. Internally generated pseudo pairs are allowed. A paper with paired and unpaired variants is counted once for the documented unpaired branch. Auxiliary depth, semantic, quality or pretrained models remain explicit in the access notes; these papers do not all have the same information budget.', '',
            'Noisy-only or single-image methods, same-scene reference guidance, generic foundations, and methods whose evaluated target adaptation depends on source-paired supervision are excluded from these counts. Unresolved access protocols were held out, including dSRVAE, UM-GAN postprocessing and DA-AGLC-GAN; PDD, PDUNet, JRGR and UDRDR remain related settings rather than additions to this total. Desnowing coverage is sparse.', '',
            'Years follow the verified final proceedings or journal issue; a preprint year is used when no final venue was verified. A later preprint posting, online-first date or DOI year does not override the final year. Preprints and final versions are merged. Close conference/journal precursors are conservatively merged when not established as independently distinct contributions (for example CWR).', '',
            'One dominant mechanism is assigned per paper to make category counts additive. Hybrids can use several mechanisms: these are editorial labels, not disjoint scientific properties. The counts measure retrieved papers, not method effectiveness, popularity, research quality or worldwide publication volume. Task tags can overlap.', '',
            'The English-language search combined broad task queries with exact-title, alias, venue-year and author-code follow-ups. Primary sources include CVF/ECVA, author arXiv records and project repositories, and publisher pages or indexed publisher text. The query ledger preserves 72 main-pass discovery and metadata searches; additional SR/underwater searches used unpaired real-world SR, unsupervised SR, degradation learning, unpaired underwater enhancement, contrastive learning and GAN terms. It is not an export of every search result.', '',
            'Not every full paper or implementation was audited. Publisher/author abstracts and accessible method/data excerpts support screening; source links and row-level notes preserve the evidence boundary. Blank code URLs mean that an attributable implementation was not verified, not that none exists. Search indexing, access limits, terminology and the partial 2026 year can leave omissions. No benchmark results or experimental measurements are provided here.', '',
            '## Rebuild and contribute', '',
            'Run `python scripts/build_public_search.py` to rebuild this appendix and its annual counts from the public paper CSV. `python scripts/build_resources.py` also refreshes the appendix when its CSV is present. Run `python scripts/check_public_bundle.py` to check counts, identifiers, public fields and local links. Corrections should include a primary URL, independent-domain access evidence and a publication-year basis; see the [contribution guide](../CONTRIBUTING.md).', '',
            '## Included papers and access notes']
    for year in range(2026, 2016, -1):
        annual = sorted((r for r in rows if int(r['year']) == year), key=lambda r: r['method'].casefold())
        if not annual:
            continue
        doc += ['', f'### {year}', '', '| Paper / method | Venue · mechanism | Tasks | Access qualification / code |', '|---|---|---|---|']
        for row in annual:
            code = f' [Author code]({row["code_url"]}).' if row['code_url'] else ''
            doc.append(f'| **{md(row["method"])}** · [{md(row["title"])}]({row["paper_url"]}) | {md(row["venue"])} · {FAMILIES[row["paradigm"]]} | {md(row["tasks"].replace(";", ", "))} | {md(row["access_note"])}{code} |')
    (ROOT / 'docs/PUBLIC_SEARCH_2026.md').write_text('\n'.join(doc) + '\n', encoding='utf-8')
    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text(encoding='utf-8')
    block = '\n'.join([START, '## Broader public search appendix', '',
        f'The **{len(main)}-record curated guide** above supports structured reading across methods, foundations and related settings. A separate **{len(rows)}-paper search corpus** broadens discovery to super-resolution, underwater enhancement and other restoration tasks. These collections overlap and serve different purposes; neither is a global publication census.', '',
        f'[Browse the search appendix and annual table](docs/PUBLIC_SEARCH_2026.md) · [Paper CSV](data/public_search_papers.csv) · [Year counts](data/public_search_year_counts.csv). Search cutoff: **{cutoff}**; 2026 is incomplete.', END])
    if START in readme:
        readme = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: block, readme, flags=re.S)
    else:
        readme = readme.replace('## Six-task index', block + '\n\n## Six-task index', 1)
    readme_path.write_text(readme, encoding='utf-8')
    print(f'Public search appendix: {len(rows)} papers; annual sum {sum(r["verified_core_count"] for r in counts)}; {new} newly discovered records; cutoff {cutoff}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--import-catalog', type=Path)
    args = parser.parse_args()
    if args.import_catalog:
        import_catalog(args.import_catalog)
    build()
