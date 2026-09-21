# Contributing

Add a paper, correct an entry, or improve a dataset note through an issue or a pull request.

## Paper entries

For the counted corpus, edit `data/public_search_papers.csv` and supply its counting group, citation identifier and year basis. `data/papers.csv` is a separate selected/background reading guide; the two collections overlap and must not be added together. Supply a stable identifier, exact title, method name when one is used by the authors, publication year and venue, a primary paper link, task tags, and a supervision/access note. An author project or repository can establish an implementation link; a similarly named third-party repository is not an author release.

- Prefer the final journal or conference record. Keep a preprint visibly labelled when no publication record has been established.
- Use one canonical record per paper. Revisions of the same paper are not additional papers; a substantially expanded journal publication can be recorded separately when identified as such.
- State whether a method uses independent degraded/clean collections, noisy-only observations, generated pairs, related-scene references, or externally pretrained models.
- Separate core restoration papers from foundations and adjacent settings. Do not add all supervised restoration papers merely because their code is public.
- Record release limitations. Public source code, training code, pretrained weights, and a verified reproduction are different claims.
- Provide evidence for license assertions. If a license cannot be established, leave it unspecified rather than assuming that public access grants reuse rights.

## Dataset entries

Edit `data/datasets_main.csv` for the real-input coverage view, `data/datasets_supplementary.csv` for the extended six-task inventory, or `data/datasets.csv` for the shorter protocol guide. Link to the original paper, official dataset page, or author repository. Describe acquisition and reference construction separately: captured scenes can still have digital degradation, and scene correspondences need not be pixel-aligned references. `Real/Synth.` describes degraded-input origin; controlled physical capture belongs to `Real`. Preserve exact release and counting units when reporting sample counts.

## Regenerate and check

```sh
python -m pip install -r requirements.txt
python scripts/build_resources.py
python scripts/check_public_bundle.py
```

The build updates the README, indexes and statistical figures from the CSV files. The checks verify local consistency and privacy boundaries; they do not claim that every external endpoint is currently reachable. Check new external links manually before opening a pull request.

Include the primary sources supporting your change and briefly explain any change to scope or counting. Do not submit unpublished documents, private correspondence, credentials, model checkpoints, or experiment outputs.
