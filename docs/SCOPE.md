# Scope, provenance and counting

[Back to overview](../README.md)

This is a selective, manually curated resource index, checked through **2026-09-19**. It is not a systematic-review census or a benchmark leaderboard.

## Inclusion categories

- **Core restoration (55 records):** papers whose documented task includes restoration under an unpaired or unsupervised learning regime. Read the per-paper training-access note: generated pairs, pretrained priors and related-scene references can change the information available.
- **Foundations (19 records):** general translation or generative methods that provide relevant tools but are not automatically restoration evaluations.
- **Adjacent settings (8 records):** related supervision or restoration approaches whose access assumptions differ from the core setting.

These labels organize reading. They do not establish that all papers share an identical supervision budget.

## Reproducible counts

The canonical source is [`data/papers.csv`](../data/papers.csv). Each row has a unique `id`; aliases and preprint revisions should not duplicate that row. Year grouping uses the catalog's explicit `year_basis`, normally the final conference/journal year, or the preprint year when only a preprint record is established. Multi-task labels are nonexclusive, so task counts need not sum to the number of papers.

The plot and [`year_counts.csv`](../data/year_counts.csv) are rebuilt with `python scripts/build_resources.py`. Annual bars count all records with scope shown separately. Pre-2017 records are grouped into one bar for readability; the CSV preserves each original year. The latest calendar year is incomplete. The task panel counts only core records carrying each of the six task tags. No missing-year extrapolation, global publication-volume estimate, citation impact or performance ranking is inferred.

## Access and evidence

Primary links point to publishers, proceedings, author manuscripts, projects or repositories. “Code linked” counts a nonempty attributable implementation URL. It is separate from license verification, training-code completeness, checkpoint availability and reproduced performance. Broken links or changed releases can be reported through an issue.

[`data/datasets.csv`](../data/datasets.csv) records acquisition and pairing at the release level. It contains metadata and protocol notes, not images or evaluation measurements. No performance measurements are included in this resource collection.

The source links remain the authority for each work's claims and reuse conditions. See [REUSE.md](../REUSE.md).
