# Contributing

Add a paper, correct an entry, or improve a dataset note through an issue or a pull request.

## Paper entries

Edit `data/papers.csv`. Supply a stable identifier, exact title, method name when one is used by the authors, publication year and venue, a primary paper link, task tags, and a supervision/access note. An author project or repository can establish an implementation link; a similarly named third-party repository is not an author release.

- Prefer the final journal or conference record. Keep a preprint visibly labelled when no publication record has been established.
- Use one canonical record per paper. Revisions of the same paper are not additional papers; a substantially expanded journal publication can be recorded separately when identified as such.
- State whether a method uses independent degraded/clean collections, noisy-only observations, generated pairs, related-scene references, or externally pretrained models.
- Separate core restoration papers from foundations and adjacent settings. Do not add all supervised restoration papers merely because their code is public.
- Record release limitations. Public source code, training code, pretrained weights, and a verified reproduction are different claims.
- Provide evidence for license assertions. If a license cannot be established, leave it unspecified rather than assuming that public access grants reuse rights.

## Dataset entries

Edit `data/datasets.csv`. Link to the original paper, official dataset page, or author repository. Describe acquisition and reference construction separately: captured images can still have synthetic degradation, and scene correspondences need not be pixel-aligned references. Avoid adding sample counts unless the exact release and counting unit are specified.

## Regenerate and check

```sh
python -m pip install -r requirements.txt
python scripts/build_resources.py
python scripts/check_public_bundle.py
```

The build updates the README, indexes and statistical figures from the CSV files. The checks verify local consistency and privacy boundaries; they do not claim that every external endpoint is currently reachable. Check new external links manually before opening a pull request.

Include the primary sources supporting your change and briefly explain any change to scope or counting. Do not submit unpublished documents, private correspondence, credentials, model checkpoints, or experiment outputs.
