# Learning mechanisms and comparison methods

[Back to overview](../README.md) · [Code index](CODE.md) · [Dataset catalog](DATASET_CATALOG.md)

Unpaired restoration learns from separate degraded and clean image collections. The central distinction is between matching the appearance of clean images and retaining the content of a particular observation. The five families below organize the constraints used to connect these goals. A method can combine several families, so these labels are not mutually exclusive.

## Five mechanism families

| Family | Main constraint | Representative reading | What the constraint leaves unresolved |
|---|---|---|---|
| Domain translation | Adversarial domain alignment with cyclic or reconstruction constraints | [CycleGAN](https://junyanz.github.io/CycleGAN/), [DerainCycleGAN](https://github.com/OaDsis/DerainCycleGAN), [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN) | A clean-looking output and a consistent inverse mapping do not uniquely specify faithful scene recovery. |
| Representation learning | Contrastive features, disentangled representations or variational factors | [DCD-GAN](https://openaccess.thecvf.com/content/CVPR2022/papers/Chen_Unpaired_Deep_Image_Deraining_Using_Dual_Contrastive_Learning_CVPR_2022_paper.pdf), [FCL-GAN](https://opus.lib.uts.edu.au/handle/10453/169860), [LUD-VAE](https://arxiv.org/abs/2204.10090) | Content preservation depends on what the selected features retain or discard. |
| Diffusion-based modeling and related continuous models | Generative priors, conditioned trajectories and learned bridges | [LightenDiffusion](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6440_ECCV_2024_paper.php), [DehazeSB](https://github.com/ywxjm/DehazeSB) | Plausible generated detail needs a separate connection to the degraded observation. |
| Prior-guided restoration | Physical, statistical and observation-model constraints, including transport costs | [D4](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Self-Augmented_Unpaired_Image_Dehazing_via_Density_and_Depth_Decomposition_CVPR_2022_paper.html), [NeurMAP](https://doi.org/10.1109/TPAMI.2023.3303450), [SFTOT](https://ieeexplore.ieee.org/document/11340759) | A learned degradation model can be internally consistent while giving the wrong physical explanation. |
| Normalizing flows | Invertible density models for clean-image priors or degradation synthesis | [Flow-prior denoising](https://arxiv.org/abs/2009.11532), [LDCT flow model](https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.15886) | Likelihood agreement does not by itself select the correct clean image for an observation; CT evidence is modality-specific. |

The normalizing-flow family is not limited to super-resolution. It includes clean-image-prior denoising and unpaired low-dose CT degradation modeling. An invertible architecture used for feature disentanglement should be distinguished from a flow trained as a likelihood model.

## Twelve comparison methods

Original tasks describe the source methods. In the six-task comparison, each method is separately retrained or adapted on each target task. The purpose is to examine the reuse of learning strategies under different degradations, together with their fidelity and appearance constraints.

| Method | Original task focus | Main mechanism | Strategy | Implementation |
|---|---|---|---|---|
| [CycleGAN](https://junyanz.github.io/CycleGAN/) | General image translation | Domain translation | Adversarial translation with cycle consistency. | [Repository](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) — official public repository |
| [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN) | Low-light enhancement | Domain translation | Global and local discrimination with feature preservation for illumination correction. | [Repository](https://github.com/VITA-Group/EnlightenGAN) — official public repository |
| [DerainCycleGAN](https://github.com/OaDsis/DerainCycleGAN) | Deraining | Domain translation | Rain-attentive detection couples rain removal and rain generation. | [Repository](https://github.com/OaDsis/DerainCycleGAN) — official public repository |
| [DCD-GAN](https://openaccess.thecvf.com/content/CVPR2022/papers/Chen_Unpaired_Deep_Image_Deraining_Using_Dual_Contrastive_Learning_CVPR_2022_paper.pdf) | Deraining | Representation learning | Dual contrastive guidance distinguishes rainy and clean patch representations. | [Repository](https://github.com/cschenxiang/DCD-GAN) — official public repository |
| [FCL-GAN](https://opus.lib.uts.edu.au/handle/10453/169860) | Motion deblurring | Representation learning | Lightweight deblurring with frequency-domain contrastive learning. | [Repository](https://github.com/suiyizhao/FCL-GAN) — official public repository |
| [LUD-VAE](https://arxiv.org/abs/2204.10090) | Denoising / low-light enhancement / super-resolution | Variational representation learning | Models degradation from independent image domains and synthesizes restoration training pairs. | [Repository](https://github.com/zhengdihan/LUD-VAE) — official public repository |
| [UCL-Dehaze](https://github.com/yz-wang/UCL-Dehaze) | Dehazing | Representation learning | Contrastive feature constraints guide restored images toward clean exemplars and away from haze. | [Repository](https://github.com/yz-wang/UCL-Dehaze) — official public repository |
| [img2img-Turbo](https://arxiv.org/abs/2403.12036) | General image translation | Diffusion-based translation | Adapts a one-step generator with adversarial and cycle-consistency objectives. | [Repository](https://github.com/GaParmar/img2img-turbo) — official public repository |
| [DehazeSB](https://github.com/ywxjm/DehazeSB) | Dehazing | Generative bridge | Uses a hazy-to-clear stochastic bridge with detail preservation and haze-aware CLIP guidance. | [Repository](https://github.com/ywxjm/DehazeSB) — official public repository |
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | Denoising / deraining / desnowing | Pseudo-pair learning | Collaborating restorers and degradation prompts progressively improve constructed training pairs. | [Repository](https://github.com/linxin0/RSCP2GAN) — official public repository |
| [SFTOT](https://ieeexplore.ieee.org/document/11340759) | Deraining | Prior-guided optimal transport | Combines a structure-preserving transport cost with frequency regularization and text guidance. | No attributable link verified |
| [UID-KAT](https://www.sciencedirect.com/science/article/abs/pii/S0031320326002694) | Dehazing | Latent-feature transformation | Uses Kolmogorov-Arnold transformations in a latent-feature transformer. | [Repository](https://github.com/tranleanh/uid-kat) — official public repository |

Repository access and reproduction are different claims. The [implementation index](CODE.md) records release qualifications.

## Training and evaluation protocol

The six datasets are **RENOIR** for denoising, **DPDD** for defocus deblurring, **LMHaze** for dehazing, **LSRW** for low-light enhancement, **SPA-Data** for deraining, and **RealSnow** for desnowing. Selection considers usable paired test references, representativeness within each task's dataset cohort, and within-dataset variation. The dataset maps describe relative cohort coverage rather than universal dataset quality.

Training uses independent degraded and clean pools. The paired dataset organization is discarded for optimization: a degraded image is not supplied with its matched clean image as a training target. Corresponding references are used on the test split. All twelve methods undergo separate training or adaptation for each task, and methods within a task share the test images and evaluation criteria. This is task-specific adaptation, not a claim that one frozen checkpoint generalizes across six datasets.

| Evaluation level | Metrics | Interpretation |
|---|---|---|
| Paired fidelity and feature agreement | PSNR, SSIM, LPIPS | Compare an output with its corresponding test reference. |
| Image-set distribution agreement | FID | Compares feature distributions over image sets; it does not measure input-specific correspondence. |
| No-reference quality | NIQE, TOPIQ-NR, PIQE, ILNIQE, MUSIQ, CLIP-IQA | Assess statistical or learned image quality without a paired target. |

Metrics are interpreted within each dataset. Agreement between criteria can support a conclusion, while disagreement reveals which aspect of restoration a method favors. PSNR and SSIM are preferred when higher, LPIPS and FID when lower. Among the no-reference measures, NIQE, PIQE and ILNIQE are preferred when lower, and TOPIQ-NR, MUSIQ and CLIP-IQA when higher.

## Rebuild

Edit [comparison_methods.csv](../data/comparison_methods.csv), then run `python scripts/build_resources.py` and `python scripts/check_public_bundle.py`.
