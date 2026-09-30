"""Generate the method and evaluation-protocol guide from public metadata."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['citation_key', 'method', 'original_tasks', 'mechanism', 'strategy']


def read_csv(name):
    with (ROOT / 'data' / name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def build(check=False):
    rows = read_csv('comparison_methods.csv')
    assert len(rows) == 12 and len({r['citation_key'] for r in rows}) == 12
    assert list(rows[0]) == FIELDS
    catalog = {r['id']: r for r in read_csv('papers.csv')}
    catalog.update({r['citation_key']: r for r in read_csv('public_search_papers.csv')})
    for r in rows:
        assert all(r.values()) and r['citation_key'] in catalog

    def ref(key, name):
        return f'[{name}]({catalog[key]["paper_url"]})'

    out = ['# Learning mechanisms and comparison methods', '',
           '[Back to overview](../README.md) · [Code index](CODE.md) · [Dataset catalog](DATASET_CATALOG.md)', '',
           'Unpaired restoration learns from separate degraded and clean image collections. '
           'The central distinction is between matching the appearance of clean images and retaining the content of a particular observation. '
           'The five families below organize the constraints used to connect these goals. '
           'A method can combine several families, so these labels are not mutually exclusive.', '',
           '## Five mechanism families', '',
           '| Family | Main constraint | Representative reading | What the constraint leaves unresolved |',
           '|---|---|---|---|',
           f'| Domain translation | Adversarial domain alignment with cyclic or reconstruction constraints | {ref("Zhu2017ICCV", "CycleGAN")}, {ref("Wei2021TIP", "DerainCycleGAN")}, {ref("Jiang2021TIP", "EnlightenGAN")} | A clean-looking output and a consistent inverse mapping do not uniquely specify faithful scene recovery. |',
           f'| Representation learning | Contrastive features, disentangled representations or variational factors | {ref("Chen2022CVPR", "DCD-GAN")}, {ref("Zhao2022FCLGAN", "FCL-GAN")}, {ref("Zheng2023TPAMI", "LUD-VAE")} | Content preservation depends on what the selected features retain or discard. |',
           f'| Diffusion-based modeling and related continuous models | Generative priors, conditioned trajectories and learned bridges | {ref("Jiang2024ECCV", "LightenDiffusion")}, {ref("Lan2025ICCV", "DehazeSB")} | Plausible generated detail needs a separate connection to the degraded observation. |',
           f'| Prior-guided restoration | Physical, statistical and observation-model constraints, including transport costs | {ref("Yang2022CVPR", "D4")}, {ref("Zhang2023TPAMINeurMAP", "NeurMAP")}, {ref("Wen2026TMM", "SFTOT")} | A learned degradation model can be internally consistent while giving the wrong physical explanation. |',
           f'| Normalizing flows | Invertible density models for clean-image priors or degradation synthesis | {ref("Covkattakinda2020unpaired", "Flow-prior denoising")}, {ref("Liu2022LDCTFlow", "LDCT flow model")} | Likelihood agreement does not by itself select the correct clean image for an observation; CT evidence is modality-specific. |', '',
           'The normalizing-flow family is not limited to super-resolution. It includes clean-image-prior denoising and unpaired low-dose CT degradation modeling. '
           'An invertible architecture used for feature disentanglement should be distinguished from a flow trained as a likelihood model.', '',
           '## Twelve comparison methods', '',
           'Original tasks describe the source methods. In the six-task comparison, each method is separately retrained or adapted on each target task. '
           'The purpose is to examine the reuse of learning strategies under different degradations, together with their fidelity and appearance constraints.', '',
           '| Method | Original task focus | Main mechanism | Strategy | Implementation |',
           '|---|---|---|---|---|']
    for row in rows:
        r = catalog[row['citation_key']]
        code = (f'[Repository]({r["code_url"]}) — {r["code_status"].replace("_", " ")}'
                if r['code_url'] else 'No attributable link verified')
        out.append('| ' + ' | '.join([ref(row['citation_key'], row['method']),
                   row['original_tasks'], row['mechanism'], row['strategy'], code]) + ' |')
    out += ['', 'Repository access and reproduction are different claims. The [implementation index](CODE.md) records release qualifications.', '',
            '## Training and evaluation protocol', '',
            'The six datasets are **RENOIR** for denoising, **DPDD** for defocus deblurring, **LMHaze** for dehazing, '
            '**LSRW** for low-light enhancement, **SPA-Data** for deraining, and **RealSnow** for desnowing. '
            'Selection considers usable paired test references, representativeness within each task\'s dataset cohort, '
            'and within-dataset variation. The dataset maps describe relative cohort coverage rather than universal dataset quality.', '',
            'Training uses independent degraded and clean pools. The paired dataset organization is discarded for optimization: '
            'a degraded image is not supplied with its matched clean image as a training target. Corresponding references are used on the test split. '
            'All twelve methods undergo separate training or adaptation for each task, and methods within a task share the test images and evaluation criteria. '
            'This is task-specific adaptation, not a claim that one frozen checkpoint generalizes across six datasets.', '',
            '| Evaluation level | Metrics | Interpretation |', '|---|---|---|',
            '| Paired fidelity and feature agreement | PSNR, SSIM, LPIPS | Compare an output with its corresponding test reference. |',
            '| Image-set distribution agreement | FID | Compares feature distributions over image sets; it does not measure input-specific correspondence. |',
            '| No-reference quality | NIQE, TOPIQ-NR, PIQE, ILNIQE, MUSIQ, CLIP-IQA | Assess statistical or learned image quality without a paired target. |', '',
            'Metrics are interpreted within each dataset. Agreement between criteria can support a conclusion, while disagreement reveals which aspect of restoration a method favors. '
            'PSNR and SSIM are preferred when higher, LPIPS and FID when lower. Among the no-reference measures, NIQE, PIQE and ILNIQE are preferred when lower, '
            'and TOPIQ-NR, MUSIQ and CLIP-IQA when higher.', '',
            '## Rebuild', '', 'Edit [comparison_methods.csv](../data/comparison_methods.csv), then run '
            '`python scripts/build_resources.py` and `python scripts/check_public_bundle.py`.', '']
    content = '\n'.join(out)
    target = ROOT / 'docs/METHODS.md'
    if check:
        assert target.read_text(encoding='utf8') == content, 'Method guide is out of date.'
    else:
        target.write_text(content, encoding='utf8')
    return len(rows)


if __name__ == '__main__':
    build()
