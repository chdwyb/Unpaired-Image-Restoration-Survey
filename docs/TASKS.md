# Task index

[Back to overview](../README.md)

Core records are grouped by documented restoration task. Multi-task papers appear in more than one section.

<a id="denoising"></a>

## Denoising

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TPAMI issue 2025; older preprint counted once. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [RCOT](https://proceedings.mlr.press/v235/tang24d.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. The paper studies paired and unpaired variants; count the paper once, not each regime. |
| [LUD-VAE](https://arxiv.org/abs/2204.10090) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Final issue 2023; first online/preprint 2022. Synthesis plus a downstream restorer. |
| [OTUR](https://arxiv.org/abs/2108.02574) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [SCPGabNet](https://openaccess.thecvf.com/content/ICCV2023/html/Lin_Unsupervised_Image_Denoising_in_Real-World_Scenarios_via_Self-Collaboration_Parallel_Generative_ICCV_2023_paper.html) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [C2N](https://openaccess.thecvf.com/content/ICCV2021/papers/Jang_C2N_Practical_Generative_Noise_Modeling_for_Real-World_Denoising_ICCV_2021_paper.pdf) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. DND protocol includes target noisy-image adaptation; retain this information budget. |
| [Camera-noise synthesis GAN](https://bernardohenz.github.io/projects/synthesizing_noise/) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. Unpaired camera-noise synthesis followed by DnCNN; camera-specific RENOIR evaluation. |
| [UIDNet](https://ojs.aaai.org/index.php/AAAI/article/view/5834) | 2020 | unpaired restoration; consult access note and paper for auxiliary supervision. Clean/noisy domains and generated pairs; not noisy-only learning. |
| [Unpaired denoising (DBSN)](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123490341.pdf) | 2020 | unpaired restoration; consult access note and paper for auxiliary supervision. Blind-spot/noise-model stage followed by independent-clean-image synthesis and distillation. |
| [GCBD](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Image_Blind_Denoising_CVPR_2018_paper.html) | 2018 | unpaired restoration; consult access note and paper for auxiliary supervision. Noise patches and independent clean images; generated pairs train the denoiser. |

<a id="deblurring"></a>

## Deblurring

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [DDSB](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [TP-Diff](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Learning_Deblurring_Texture_Prior_from_Unpaired_Data_with_Diffusion_Model_ICCV_2025_paper.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [DDM](https://openaccess.thecvf.com/content/ICCV2025/html/Meanti_Unsupervised_Imaging_Inverse_Problems_with_Diffusion_Distribution_Matching_ICCV_2025_paper.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Conditional flow matching with inverse-problem operator inference; calibration assumptions remain part of the setting. |
| [SEMGUD](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Unsupervised_Blind_Image_Deblurring_Based_on_Self-Enhancement_CVPR_2024_paper.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [NeurMAP](https://doi.org/10.1109/TPAMI.2023.3303450) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Public unsupervised and semi-supervised paths; initialization and motion-estimator training must be identified. |
| [FCL-GAN](https://opus.lib.uts.edu.au/handle/10453/169860) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [Disentangled deblurring](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_Unsupervised_Domain-Specific_Deblurring_via_Disentangled_Representations_CVPR_2019_paper.pdf) | 2019 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |

<a id="dehazing"></a>

## Dehazing

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [UID-KAT](https://www.sciencedirect.com/science/article/abs/pii/S0031320326002694) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Final Pattern Recognition 2026; 2025 arXiv preprint counted once. KAN latent transformation with adversarial/contrastive learning. |
| [OBCOT](https://pubmed.ncbi.nlm.nih.gov/41955147/) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TNNLS issue year 2026; transport-based dehazing. |
| [Diff-Dehazer](https://doi.org/10.1609/aaai.v39i4.32469) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [FrDiff](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Frequency_Domain-Based_Diffusion_Model_for_Unpaired_Image_Dehazing_ICCV_2025_paper.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [DehazeSB](https://github.com/ywxjm/DehazeSB) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Pretrained semantic guidance; final ICCV year 2025. |
| [ODCR](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_ODCR_Orthogonal_Decoupling_Contrastive_Regularization_for_Unpaired_Image_Dehazing_CVPR_2024_paper.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [RCOT](https://proceedings.mlr.press/v235/tang24d.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. The paper studies paired and unpaired variants; count the paper once, not each regime. |
| [D4+](https://doi.org/10.1007/s11263-023-01940-5) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [UCL-Dehaze](https://github.com/yz-wang/UCL-Dehaze) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TIP publication 2024; 2022 preprint deduplicated. |
| [USID-Net](https://github.com/dehazing/USID-Net) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [D4](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Self-Augmented_Unpaired_Image_Dehazing_via_Density_and_Depth_Decomposition_CVPR_2022_paper.html) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [CDD-GAN](https://arxiv.org/abs/2203.07677) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DGP-CycleGAN](https://arxiv.org/abs/2204.10970) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [E-CycleGAN](https://arxiv.org/abs/1902.01374) | 2020 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [Cycle-Dehaze](https://arxiv.org/abs/1805.05308) | 2018 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |

<a id="low-light"></a>

## Low-light enhancement

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [DDSB](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [Cycle-Retinex](https://github.com/mummmml/Cycle-Retinex) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [LightenDiffusion](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6440_ECCV_2024_paper.php) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [CLIP-LIT](https://openaccess.thecvf.com/content/ICCV2023/papers/Liang_Iterative_Prompt_Learning_for_Unsupervised_Backlit_Image_Enhancement_ICCV_2023_paper.pdf) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Backlit enhancement with pretrained CLIP; not a GAN architecture. Alias Liang2023ICCV is deduplicated. |
| [LUD-VAE](https://arxiv.org/abs/2204.10090) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Final issue 2023; first online/preprint 2022. Synthesis plus a downstream restorer. |
| [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. Final journal year 2021; the 2019 preprint is not a second paper. |

<a id="deraining"></a>

## Deraining

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [Prompt-oriented frequency-regularized SB](https://www.sciencedirect.com/science/article/pii/S0031320325015250) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [SFTOT](https://ieeexplore.ieee.org/document/11340759) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Published approach; attributable public code and primary numerical tables not verified in this audit. |
| [UIPL](https://www.sciencedirect.com/science/article/abs/pii/S0957417425046251) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Final ESWA issue year 2026; independent domains and perceptual guidance. |
| [CSUD](https://doi.org/10.1109/CVPR52734.2025.00700) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DDSB](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TPAMI issue 2025; older preprint counted once. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [NSB](https://www.sciencedirect.com/science/article/pii/S0020025524011137) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Pretrained CLIP guidance is part of the information budget. |
| [RCOT](https://proceedings.mlr.press/v235/tang24d.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. The paper studies paired and unpaired variants; count the paper once, not each regime. |
| [UPID-EDM](https://chdwyb.github.io/) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Energy-informed diffusion classification uses verified title-level evidence; no exact loss inventory asserted. |
| [DCD-GAN](https://openaccess.thecvf.com/content/CVPR2022/papers/Chen_Unpaired_Deep_Image_Deraining_Using_Dual_Contrastive_Learning_CVPR_2022_paper.pdf) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [NLCL](https://doi.org/10.1109/CVPR52688.2022.00573) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DGP-CycleGAN](https://arxiv.org/abs/2204.10970) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DerainCycleGAN](https://github.com/OaDsis/DerainCycleGAN) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. Final journal year 2021; the 2019 preprint is not a second paper. |
| [RR-GAN](https://ojs.aaai.org/index.php/AAAI/article/view/4971) | 2019 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [UD-GAN](https://orca.cardiff.ac.uk/id/eprint/161670/) | 2019 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |

<a id="desnowing"></a>

## Desnowing

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TPAMI issue 2025; older preprint counted once. |
| [DGP-CycleGAN](https://arxiv.org/abs/2204.10970) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |

## Related tasks and foundations

General translation foundations and other restoration tasks are listed here without relabelling them as six-task evaluations.

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| **BluRef** · [BluRef: Unsupervised Image Deblurring with Dense-Matching References](https://qualcomm-ai-research.github.io/BluRef/) | CVPR | deblurring | Not verified | Adjacent settings |
| **DTMIR-Pro** · [DTMIR-Pro: Domain Translation with Prompt-Based Latent-Space Generalization for Multi-Weather Image Restoration](https://doi.org/10.1109/WACV61042.2026.00375) | WACV | deraining, dehazing, desnowing | Not verified | Adjacent settings |
| **NM-FlowGAN** · [NM-FlowGAN: Pixel-wise Noise and Spatial Correlation Modeling for sRGB Noise without Paired Images in Generation Time](https://www.sciencedirect.com/science/article/pii/S0957417426010225) | Expert Systems with Applications | denoising | Not verified | Adjacent settings |
| **RFDM** · [Unsupervised Real-World Super-Resolution via Rectified Flow Degradation Modelling](https://arxiv.org/abs/2508.07214) | arXiv preprint | super-resolution | Not verified | Core restoration |
| **DictSR** · [Learning Coupled Dictionaries from Unpaired Data for Image Super-Resolution](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Learning_Coupled_Dictionaries_from_Unpaired_Data_for_Image_Super-Resolution_CVPR_2024_paper.html) | CVPR | super-resolution | Not verified | Core restoration |
| **SDFlow** · [Learning Many-to-Many Mapping for Unpaired Real-World Image Super-Resolution and Downscaling](https://doi.org/10.1109/TPAMI.2024.3428546) | IEEE TPAMI | super-resolution, downscaling | [Author code](https://github.com/sunwj/sdflow) | Core restoration |
| **CycleGAN-Turbo / img2img-Turbo** · [One-Step Image Translation with Text-to-Image Models](https://arxiv.org/abs/2403.12036) | arXiv preprint | general image translation | [Author code](https://github.com/GaParmar/img2img-turbo) | Foundations |
| **UNSB** · [Unpaired Image-to-Image Translation via Neural Schrodinger Bridge](https://proceedings.iclr.cc/paper_files/paper/2024/hash/5491280797f3192b895bce84eb83df8d-Abstract-Conference.html) | ICLR | general image translation | Not verified | Foundations |
| **Flow matching** · [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | ICLR | generative modeling | Not verified | Foundations |
| **Rectified flow** · [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](https://arxiv.org/abs/2209.03003) | ICLR | generative modeling | Not verified | Foundations |
| **EGSDE** · [EGSDE: Unpaired Image-to-Image Translation via Energy-Guided Stochastic Differential Equations](https://arxiv.org/abs/2207.06635) | NeurIPS | general image translation | Not verified | Foundations |
| **USR-DU** · [Learning Degradation Uncertainty for Unsupervised Real-World Image Super-Resolution](https://www.ijcai.org/proceedings/2022/176) | IJCAI | super-resolution | Not verified | Core restoration |
| **ADL** · [Toward Real-World Super-Resolution via Adaptive Downsampling Models](https://arxiv.org/abs/2109.03444) | IEEE TPAMI | super-resolution | [Author code](https://github.com/JaehaKim97/Adaptive-Downsampling-Model) | Core restoration |
| **DeFlow** · [DeFlow: Learning Complex Image Degradations from Unpaired Data with Conditional Flows](https://openaccess.thecvf.com/content/CVPR2021/html/Wolf_DeFlow_Learning_Complex_Image_Degradations_From_Unpaired_Data_With_Conditional_CVPR_2021_paper.html) | CVPR | super-resolution | Not verified | Core restoration |
| **CLIP** · [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | ICML | vision-language representation | Not verified | Foundations |
| **Score SDE** · [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) | ICLR | generative modeling | Not verified | Foundations |
| **UDGNet** · [Unsupervised Image Deraining: Optimization Model Driven Deep CNN](https://huayuuu.github.io/files/2021ACMMM_UDGNet.pdf) | ACM Multimedia | deraining | Not verified | Adjacent settings |
| **DASR (domain-distance aware)** · [Unsupervised Real-World Image Super Resolution via Domain-Distance Aware Training](https://openaccess.thecvf.com/content/CVPR2021/html/Wei_Unsupervised_Real-World_Image_Super_Resolution_via_Domain-Distance_Aware_Training_CVPR_2021_paper.html) | CVPR | super-resolution | [Author code](https://github.com/ShuhangGu/DASR) | Core restoration |
| **CUT** · [Contrastive Learning for Unpaired Image-to-Image Translation](https://research.adobe.com/publication/contrastive-learning-for-unpairedimage-to-image-translation/) | ECCV | general image translation | Not verified | Foundations |
| **DDPM** · [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | NeurIPS | generative modeling | Not verified | Foundations |
| **UEGAN** · [Towards Unsupervised Deep Image Enhancement with Generative Adversarial Network](https://arxiv.org/abs/2012.15020) | IEEE TIP | photographic enhancement | [Author code](https://github.com/eezkni/UEGAN) | Adjacent settings |
| **Pseudo-supervised SR** · [Unpaired Image Super-Resolution Using Pseudo-Supervision](https://openaccess.thecvf.com/content_CVPR_2020/html/Maeda_Unpaired_Image_Super-Resolution_Using_Pseudo-Supervision_CVPR_2020_paper.html) | CVPR | super-resolution | Not verified | Core restoration |
| **Noise2Void** · [Noise2Void: Learning Denoising from Single Noisy Images](https://arxiv.org/abs/1811.10980) | CVPR | denoising | Not verified | Adjacent settings |
| **Deep image prior** · [Deep Image Prior](https://arxiv.org/abs/1711.10925) | CVPR | image restoration | Not verified | Adjacent settings |
| **DRIT** · [Diverse Image-to-Image Translation via Disentangled Representations](https://arxiv.org/abs/1808.00948) | ECCV | general image translation | Not verified | Foundations |
| **Glow** · [Glow: Generative flow with invertible 1x1 convolutions](https://arxiv.org/abs/1807.03039) | NeurIPS | density modeling | Not verified | Foundations |
| **MUNIT** · [Multimodal Unsupervised Image-to-Image Translation](https://arxiv.org/abs/1804.04732) | ECCV | general image translation | Not verified | Foundations |
| **Noise2Noise** · [Noise2Noise: Learning Image Restoration without Clean Data](https://arxiv.org/abs/1803.04189) | ICML | denoising | Not verified | Adjacent settings |
| **Real NVP** · [Density estimation using Real NVP](https://arxiv.org/abs/1605.08803) | ICLR | density modeling | Not verified | Foundations |
| **CycleGAN** · [Unpaired Image-to-Image Translation Using Cycle-Consistent Adversarial Networks](https://junyanz.github.io/CycleGAN/) | ICCV | general image translation | [Author code](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) | Foundations |
| **UNIT** · [Unsupervised Image-to-Image Translation Networks](https://arxiv.org/abs/1703.00848) | NeurIPS | general image translation | Not verified | Foundations |
| **GAN** · [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661) | NeurIPS | generative modeling | Not verified | Foundations |
| **Dark channel prior** · [Single Image Haze Removal Using Dark Channel Prior](https://people.csail.mit.edu/kaiming/) | CVPR | dehazing | Not verified | Foundations |
| **BM3D** · [Image Denoising by Sparse 3-D Transform-Domain Collaborative Filtering](https://webpages.tuni.fi/foi/GCF-BM3D/index.html) | IEEE TIP | denoising | Not verified | Foundations |
| **Retinex** · [Lightness and Retinex Theory](https://doi.org/10.1364/JOSA.61.000001) | Journal of the Optical Society of America | low-light | Not verified | Foundations |
