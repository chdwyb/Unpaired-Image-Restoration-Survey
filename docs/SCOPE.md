# Scope, provenance and counting

[Back to overview](../README.md)

This is a selective, manually curated resource index, checked through **2026-09-21**. It is not a systematic-review census or a benchmark leaderboard.

## Primary counted corpus

The main overview uses [public_search_papers.csv](../data/public_search_papers.csv): **142 canonical papers**, grouped into **68 six-task restoration**, **51 broader restoration**, and **23 general/weather translation** records. The [full corpus page](PUBLIC_SEARCH_2026.md) defines these mutually exclusive groups and provides the annual table. Its chart and [annual CSV](../data/public_search_year_counts.csv) use the same collection. The 2026 count is partial.

## Inclusion categories

The following categories refer to the separate **82-record selected reading guide**, not to the primary counted corpus. The collections overlap and must not be added together.

- **Core restoration (55 records):** papers whose documented task includes restoration under an unpaired or unsupervised learning regime. Read the per-paper training-access note: generated pairs, pretrained priors and related-scene references can change the information available.
- **Foundations (19 records):** general translation or generative methods that provide relevant tools but are not automatically restoration evaluations.
- **Adjacent settings (8 records):** related supervision or restoration approaches whose access assumptions differ from the core setting.

These labels organize reading. They do not establish that all papers share an identical supervision budget.

## Reproducible counts

The selected guide's source is [`data/papers.csv`](../data/papers.csv). Each row has a unique `id`; aliases and preprint revisions should not duplicate that row. Year grouping uses the catalog's explicit `year_basis`, normally the final conference/journal year, or the preprint year when only a preprint record is established. Multi-task labels are nonexclusive, so task counts need not sum to the number of papers.

The selected guide's auxiliary [plot](../assets/collection-overview.svg) and [`year_counts.csv`](../data/year_counts.csv) are rebuilt with `python scripts/build_resources.py`. Its annual bars count all guide records with scope shown separately; pre-2017 records are grouped into one bar. This auxiliary chart is separate from the primary 142-paper chart. The task panel counts guide core records carrying each of the six task tags. No missing-year extrapolation, worldwide publication estimate, citation impact or performance ranking is inferred.

## Dataset inventories

The [complete dataset catalog](DATASET_CATALOG.md) has **59 real-input task-specific entries** and **160 extended-inventory entries** across six task groups. These overlapping views have different purposes and their counts must not be added. A multi-task collection can occur in several task groups. The six selected evaluation datasets are RENOIR, DPDD, LMHaze, LSRW, SPA-Data and RealSnow. `Real/Synth.` describes the degraded input, independently of pairing, alignment or clean-reference construction.

## Access and evidence

Primary links point to publishers, proceedings, author manuscripts, projects or repositories. “Code linked” counts a nonempty attributable implementation URL. It is separate from license verification, training-code completeness, checkpoint availability and reproduced performance. Broken links or changed releases can be reported through an issue.

[`data/datasets.csv`](../data/datasets.csv) records acquisition and pairing at the release level. It contains metadata and protocol notes, not images or evaluation measurements. No performance measurements are included in this resource collection.

The source links remain the authority for each work's claims and reuse conditions. See [REUSE.md](../REUSE.md).
