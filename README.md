# Unpaired Image Restoration

**A curated research resource for papers, implementations and datasets.**

Explore restoration learned without aligned task-specific degraded–clean targets, with related foundations and supervision settings labelled separately.

**142 counted papers** · **59 real-data entries** · **160 full-inventory entries** · **6 evaluation tasks**

Last curated: **2026-09-21**

[Full paper corpus](docs/PUBLIC_SEARCH_2026.md) · [Datasets](docs/DATASET_CATALOG.md) · [Six tasks](#six-task-index) · [Selected reading guide](#papers-by-year) · [Code index](docs/CODE.md) · [Scope and counting](docs/SCOPE.md)

## Collection overview

![Annual counts and coverage of the 142-paper corpus.](assets/corpus-overview.svg)

The counted corpus contains **68 six-task restoration papers**, **51 papers on super-resolution, underwater enhancement and sand/dust removal**, and **23 general or weather-translation papers**. Each paper belongs to one counting group and appears once. These are counts of the screened collection, not worldwide publication totals; 2026 is incomplete. [Full paper list and annual table](docs/PUBLIC_SEARCH_2026.md) · [Paper CSV](data/public_search_papers.csv) · [Year counts](data/public_search_year_counts.csv).

The **82-record selected reading guide** below also includes methodological foundations and adjacent supervision settings. It overlaps the counted corpus and is not an additional 82 papers. Its **30 author-code links** are listed with access notes. [Counting rules](docs/SCOPE.md).

## Evaluation datasets

| Task | Selected dataset | Input source |
|---|---|---|
| Denoising | RENOIR | Real |
| Defocus deblurring | DPDD | Real |
| Dehazing | LMHaze | Real |
| Low-light enhancement | LSRW | Real |
| Deraining | SPA-Data | Real |
| Desnowing | RealSnow | Real |

The [dataset catalog](docs/DATASET_CATALOG.md) links the original sources and lists **59 real-input entries** used in dataset coverage analysis, plus the **160-entry full inventory** in six task groups. The real-input table includes a **Real/Synth.** column; controlled physical capture is classified as real. Real input does not imply exact pixel alignment, and reference construction is described separately.

## Six-task index

| Task | Counted-corpus records | Browse |
|---|---:|---|
| Denoising | 11 | [Papers and access notes](docs/TASKS.md#denoising) |
| Deblurring | 10 | [Papers and access notes](docs/TASKS.md#deblurring) |
| Dehazing | 28 | [Papers and access notes](docs/TASKS.md#dehazing) |
| Low-light enhancement | 10 | [Papers and access notes](docs/TASKS.md#low-light) |
| Deraining | 18 | [Papers and access notes](docs/TASKS.md#deraining) |
| Desnowing | 2 | [Papers and access notes](docs/TASKS.md#desnowing) |

This navigation table counts the 68 papers in the six-task group. Task tags overlap and describe documented scope, not transfer to every benchmark. The [full corpus](docs/PUBLIC_SEARCH_2026.md) also includes broader restoration and general/weather translation; related foundations remain available in the selected reading guide.

## Dataset guide

Start with the data's **capture process and reference type**. Captured paired benchmarks, digitally synthesized pairs, independent image collections and scene correspondences support different evaluations.

The [complete dataset catalog](docs/DATASET_CATALOG.md) provides the two synchronized inventories. The following 26-entry primer highlights reference construction and protocol distinctions.

- [Captured paired data](docs/DATASETS.md#captured-paired-data): noisy/reference captures, real blur, controlled haze, exposure pairs, and video-derived rain or snow targets.
- [Synthetic paired data](docs/DATASETS.md#synthetic-paired-data): digital or video-integrated degradations with corresponding clean targets.
- [Unpaired collections](docs/DATASETS.md#unpaired-collections): independent-domain training pools and natural degraded images without aligned clean targets.
- [Scene correspondence](docs/DATASETS.md#scene-correspondence): related scenes that should not be treated as pixel-aligned restoration references.

Withholding correspondence can define an unpaired training protocol on paired data. It does not remove the need to document scene overlap, splits and reference use. The [dataset guide](docs/DATASETS.md) records these distinctions without combining incomparable scores.

## Papers by year

### Selected reading guide

The tables below contain 82 selected and background records. For all 142 counted papers, including expanded restoration and translation coverage, use the [full corpus](docs/PUBLIC_SEARCH_2026.md).

[2026](#year-2026) · [2025](#year-2025) · [2024](#year-2024) · [2023](#year-2023) · [2022](#year-2022) · [2021](#year-2021) · [2020](#year-2020) · [2019](#year-2019) · [2018](#year-2018) · [2017](#year-2017) · [2014](#year-2014) · [2009](#year-2009) · [2007](#year-2007) · [1971](#year-1971)

Titles link to primary papers or author records. “Author code” indicates a public implementation link, not a license or reproduction guarantee. See the [code index](docs/CODE.md) for release qualifications.

<a id="year-2026"></a>

### 2026

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Pham2026CVPR"></a>**BluRef** · [BluRef: Unsupervised Image Deblurring with Dense-Matching References](https://qualcomm-ai-research.github.io/BluRef/) | CVPR | deblurring | Not verified | Adjacent settings |
| <a id="paper-Kulkarni2026WACV"></a>**DTMIR-Pro** · [DTMIR-Pro: Domain Translation with Prompt-Based Latent-Space Generalization for Multi-Weather Image Restoration](https://doi.org/10.1109/WACV61042.2026.00375) | WACV | deraining, dehazing, desnowing | Not verified | Adjacent settings |
| <a id="paper-Han2026ESWA"></a>**NM-FlowGAN** · [NM-FlowGAN: Pixel-wise Noise and Spatial Correlation Modeling for sRGB Noise without Paired Images in Generation Time](https://www.sciencedirect.com/science/article/pii/S0957417426010225) | Expert Systems with Applications | denoising | Not verified | Adjacent settings |
| <a id="paper-Wen2026PR"></a>**Prompt-oriented frequency-regularized SB** · [Prompt-Oriented and Frequency-Regularized Schrödinger Bridge for Unpaired Rain Streaks and Raindrops Removal](https://www.sciencedirect.com/science/article/pii/S0031320325015250) | Pattern Recognition | deraining | Not verified | Core restoration |
| <a id="paper-Wen2026TMM"></a>**SFTOT** · [Structure-Preserving Frequency-Regularized Text-Guided Optimal Transport for Unpaired Rain Streaks and Raindrops Removal](https://ieeexplore.ieee.org/document/11340759) | IEEE TMM | deraining | Not verified | Core restoration |
| <a id="paper-Tran2026UIDKAT"></a>**UID-KAT** · [Unpaired Image Dehazing via Kolmogorov-Arnold Transformation of Latent Features](https://www.sciencedirect.com/science/article/abs/pii/S0031320326002694) | Pattern Recognition | dehazing | [Author code](https://github.com/tranleanh/uid-kat) | Core restoration |
| <a id="paper-Wen2026ESWA"></a>**UIPL** · [Unpaired Iterative Prompt Learning for Real-World Image Deraining](https://www.sciencedirect.com/science/article/abs/pii/S0957417425046251) | Expert Systems with Applications | deraining | Not verified | Core restoration |
| <a id="paper-Wen2026TNNLS"></a>**OBCOT** · [When Optimal Transport Meets Photo-Realistic Image Dehazing with Unpaired Training](https://pubmed.ncbi.nlm.nih.gov/41955147/) | IEEE TNNLS | dehazing | Not verified | Core restoration |

<a id="year-2025"></a>

### 2025

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Dong2025CVPR"></a>**CSUD** · [Channel Consistency Prior and Self-Reconstruction Strategy Based Unsupervised Image Deraining](https://doi.org/10.1109/CVPR52734.2025.00700) | CVPR | deraining | [Author code](https://github.com/GuangluDong0728/CSUD-Unsupervised-Deraining-CVPR2025) | Core restoration |
| <a id="paper-Zheng2025NeurIPS"></a>**DDSB** · [Degradation-Aware Dynamic Schrodinger Bridge for Unpaired Image Restoration](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | NeurIPS | deraining, low-light, deblurring | Not verified | Core restoration |
| <a id="paper-Lan2025AAAI"></a>**Diff-Dehazer** · [Exploiting Diffusion Prior for Real-World Image Dehazing with Unpaired Training](https://doi.org/10.1609/aaai.v39i4.32469) | AAAI | dehazing | Not verified | Core restoration |
| <a id="paper-Liu2025ICCV"></a>**FrDiff** · [Frequency Domain-Based Diffusion Model for Unpaired Image Dehazing](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Frequency_Domain-Based_Diffusion_Model_for_Unpaired_Image_Dehazing_ICCV_2025_paper.html) | ICCV | dehazing | Not verified | Core restoration |
| <a id="paper-Hu2025ICCV"></a>**TP-Diff** · [Learning Deblurring Texture Prior from Unpaired Data with Diffusion Model](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Learning_Deblurring_Texture_Prior_from_Unpaired_Data_with_Diffusion_Model_ICCV_2025_paper.html) | ICCV | deblurring | Not verified | Core restoration |
| <a id="paper-Lin2025TPAMI"></a>**RSCP2GAN** · [Re-Boosting Self-Collaboration Parallel Prompt GAN for Unsupervised Image Restoration](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | IEEE TPAMI | denoising, deraining, desnowing | [Author code](https://github.com/linxin0/RSCP2GAN) | Core restoration |
| <a id="paper-Tang2025TPAMI"></a>**DA-RCOT** · [Restoring Images Under Any Degradation: A Degradation-Aware Residual-Conditioned Optimal Transport Approach](https://doi.org/10.1109/TPAMI.2025.3562211) | IEEE TPAMI | denoising, deblurring, deraining, dehazing, low-light | Not verified | Core restoration |
| <a id="paper-Meanti2025ICCV"></a>**DDM** · [Unsupervised Imaging Inverse Problems with Diffusion Distribution Matching](https://openaccess.thecvf.com/content/ICCV2025/html/Meanti_Unsupervised_Imaging_Inverse_Problems_with_Diffusion_Distribution_Matching_ICCV_2025_paper.html) | ICCV | deblurring, super-resolution, operator calibration | Not verified | Core restoration |
| <a id="paper-Zhou2025arXivRFDM"></a>**RFDM** · [Unsupervised Real-World Super-Resolution via Rectified Flow Degradation Modelling](https://arxiv.org/abs/2508.07214) | arXiv preprint | super-resolution | Not verified | Core restoration |
| <a id="paper-Lan2025ICCV"></a>**DehazeSB** · [When Schrodinger Bridge Meets Real-World Image Dehazing with Unpaired Training](https://github.com/ywxjm/DehazeSB) | ICCV | dehazing | [Author code](https://github.com/ywxjm/DehazeSB) | Core restoration |

<a id="year-2024"></a>

### 2024

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Wu2024TMM"></a>**Cycle-Retinex** · [Cycle-Retinex: Unpaired Low-Light Image Enhancement via Retinex-Inline CycleGAN](https://github.com/mummmml/Cycle-Retinex) | IEEE TMM | low-light | [Author code](https://github.com/mummmml/Cycle-Retinex) | Core restoration |
| <a id="paper-Wang2024CVPRDictSR"></a>**DictSR** · [Learning Coupled Dictionaries from Unpaired Data for Image Super-Resolution](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Learning_Coupled_Dictionaries_from_Unpaired_Data_for_Image_Super-Resolution_CVPR_2024_paper.html) | CVPR | super-resolution | Not verified | Core restoration |
| <a id="paper-Sun2024TPAMI"></a>**SDFlow** · [Learning Many-to-Many Mapping for Unpaired Real-World Image Super-Resolution and Downscaling](https://doi.org/10.1109/TPAMI.2024.3428546) | IEEE TPAMI | super-resolution, downscaling | [Author code](https://github.com/sunwj/sdflow) | Core restoration |
| <a id="paper-Jiang2024ECCV"></a>**LightenDiffusion** · [LightenDiffusion: Unsupervised Low-Light Image Enhancement with Latent-Retinex Diffusion Models](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6440_ECCV_2024_paper.php) | ECCV | low-light | [Author code](https://github.com/JianghaiSCU/LightenDiffusion) | Core restoration |
| <a id="paper-Wen2024IS"></a>**NSB** · [Neural Schrödinger Bridge for Unpaired Real-World Image Deraining](https://www.sciencedirect.com/science/article/pii/S0020025524011137) | Information Sciences | deraining | Not verified | Core restoration |
| <a id="paper-Wang2024CVPR"></a>**ODCR** · [ODCR: Orthogonal Decoupling Contrastive Regularization for Unpaired Image Dehazing](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_ODCR_Orthogonal_Decoupling_Contrastive_Regularization_for_Unpaired_Image_Dehazing_CVPR_2024_paper.html) | CVPR | dehazing | Not verified | Core restoration |
| <a id="paper-Parmar2024OneStep"></a>**CycleGAN-Turbo / img2img-Turbo** · [One-Step Image Translation with Text-to-Image Models](https://arxiv.org/abs/2403.12036) | arXiv preprint | general image translation | [Author code](https://github.com/GaParmar/img2img-turbo) | Foundations |
| <a id="paper-Tang2024ICML"></a>**RCOT** · [Residual-Conditioned Optimal Transport: Towards Structure-Preserving Unpaired and Paired Image Restoration](https://proceedings.mlr.press/v235/tang24d.html) | ICML | denoising, super-resolution, deraining, dehazing | Not verified | Core restoration |
| <a id="paper-Yang2024IJCV"></a>**D4+** · [Robust Unpaired Image Dehazing via Density and Depth Decomposition](https://doi.org/10.1007/s11263-023-01940-5) | IJCV | dehazing | [Author code](https://github.com/YaN9-Y/D4_plus) | Core restoration |
| <a id="paper-Wang2024TIP"></a>**UCL-Dehaze** · [UCL-Dehaze: Toward Real-World Image Dehazing via Unsupervised Contrastive Learning](https://github.com/yz-wang/UCL-Dehaze) | IEEE TIP | dehazing | [Author code](https://github.com/yz-wang/UCL-Dehaze) | Core restoration |
| <a id="paper-Kim2024ICLR"></a>**UNSB** · [Unpaired Image-to-Image Translation via Neural Schrodinger Bridge](https://proceedings.iclr.cc/paper_files/paper/2024/hash/5491280797f3192b895bce84eb83df8d-Abstract-Conference.html) | ICLR | general image translation | Not verified | Foundations |
| <a id="paper-Wen2024ACMMM"></a>**UPID-EDM** · [Unpaired Photo-Realistic Image Deraining with Energy-Informed Diffusion Model](https://chdwyb.github.io/) | ACM Multimedia | deraining | Not verified | Core restoration |
| <a id="paper-Chen2024CVPRDeblur"></a>**SEMGUD** · [Unsupervised Blind Image Deblurring Based on Self-Enhancement](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Unsupervised_Blind_Image_Deblurring_Based_on_Self-Enhancement_CVPR_2024_paper.html) | CVPR | deblurring | Not verified | Core restoration |

<a id="year-2023"></a>

### 2023

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-lipman2023flow"></a>**Flow matching** · [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | ICLR | generative modeling | Not verified | Foundations |
| <a id="paper-liu2023reflow"></a>**Rectified flow** · [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](https://arxiv.org/abs/2209.03003) | ICLR | generative modeling | Not verified | Foundations |
| <a id="paper-liang2023iterative"></a>**CLIP-LIT** · [Iterative Prompt Learning for Unsupervised Backlit Image Enhancement](https://openaccess.thecvf.com/content/ICCV2023/papers/Liang_Iterative_Prompt_Learning_for_Unsupervised_Backlit_Image_Enhancement_ICCV_2023_paper.pdf) | ICCV | low-light | [Author code](https://github.com/ZhexinLiang/CLIP-LIT) | Core restoration |
| <a id="paper-Zheng2023TPAMI"></a>**LUD-VAE** · [Learn From Unpaired Data for Image Restoration: A Variational Bayes Approach](https://arxiv.org/abs/2204.10090) | IEEE TPAMI | denoising, super-resolution, low-light | [Author code](https://github.com/zhengdihan/LUD-VAE) | Core restoration |
| <a id="paper-Zhang2023TPAMINeurMAP"></a>**NeurMAP** · [Neural Maximum a Posteriori Estimation on Unpaired Data for Motion Deblurring](https://doi.org/10.1109/TPAMI.2023.3303450) | IEEE TPAMI | deblurring | [Author code](https://github.com/yjzhang96/NeurMAP-deblur) | Core restoration |
| <a id="paper-Wang2023TPAMIOTUR"></a>**OTUR** · [Optimal Transport for Unsupervised Denoising Learning](https://arxiv.org/abs/2108.02574) | IEEE TPAMI | denoising | [Author code](https://github.com/wangweiSJTU/OTUR) | Core restoration |
| <a id="paper-Lin2023ICCV"></a>**SCPGabNet** · [Unsupervised Image Denoising in Real-World Scenarios via Self-Collaboration Parallel Generative Adversarial Branches](https://openaccess.thecvf.com/content/ICCV2023/html/Lin_Unsupervised_Image_Denoising_in_Real-World_Scenarios_via_Self-Collaboration_Parallel_Generative_ICCV_2023_paper.html) | ICCV | denoising | [Author code](https://github.com/linxin0/SCPGabNet) | Core restoration |
| <a id="paper-Li2022TMM"></a>**USID-Net** · [USID-Net: Unsupervised Single Image Dehazing Network via Disentangled Representations](https://github.com/dehazing/USID-Net) | IEEE TMM | dehazing | [Author code](https://github.com/dehazing/USID-Net) | Core restoration |

<a id="year-2022"></a>

### 2022

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Zhao2022NeurIPS"></a>**EGSDE** · [EGSDE: Unpaired Image-to-Image Translation via Energy-Guided Stochastic Differential Equations](https://arxiv.org/abs/2207.06635) | NeurIPS | general image translation | Not verified | Foundations |
| <a id="paper-Zhao2022FCLGAN"></a>**FCL-GAN** · [FCL-GAN: A Lightweight and Real-Time Baseline for Unsupervised Blind Image Deblurring](https://opus.lib.uts.edu.au/handle/10453/169860) | ACM Multimedia | deblurring | [Author code](https://github.com/suiyizhao/FCL-GAN) | Core restoration |
| <a id="paper-Ning2022IJCAI"></a>**USR-DU** · [Learning Degradation Uncertainty for Unsupervised Real-World Image Super-Resolution](https://www.ijcai.org/proceedings/2022/176) | IJCAI | super-resolution | Not verified | Core restoration |
| <a id="paper-Yang2022CVPR"></a>**D4** · [Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Self-Augmented_Unpaired_Image_Dehazing_via_Density_and_Depth_Decomposition_CVPR_2022_paper.html) | CVPR | dehazing | [Author code](https://github.com/YaN9-Y/D4) | Core restoration |
| <a id="paper-Son2022TPAMI"></a>**ADL** · [Toward Real-World Super-Resolution via Adaptive Downsampling Models](https://arxiv.org/abs/2109.03444) | IEEE TPAMI | super-resolution | [Author code](https://github.com/JaehaKim97/Adaptive-Downsampling-Model) | Core restoration |
| <a id="paper-Chen2022ECCV"></a>**CDD-GAN** · [Unpaired Deep Image Dehazing Using Contrastive Disentanglement Learning](https://arxiv.org/abs/2203.07677) | ECCV | dehazing | Not verified | Core restoration |
| <a id="paper-Chen2022CVPR"></a>**DCD-GAN** · [Unpaired Deep Image Deraining Using Dual Contrastive Learning](https://openaccess.thecvf.com/content/CVPR2022/papers/Chen_Unpaired_Deep_Image_Deraining_Using_Dual_Contrastive_Learning_CVPR_2022_paper.pdf) | CVPR | deraining | [Author code](https://github.com/cschenxiang/DCD-GAN) | Core restoration |
| <a id="paper-Ye2022CVPR"></a>**NLCL** · [Unsupervised Deraining: Where Contrastive Learning Meets Self-Similarity](https://doi.org/10.1109/CVPR52688.2022.00573) | CVPR | deraining | [Author code](https://github.com/yunguo224/NLCL) | Core restoration |
| <a id="paper-Yasarla2022ICPR"></a>**DGP-CycleGAN** · [Unsupervised Restoration of Weather-Affected Images Using Deep Gaussian Process-Based CycleGAN](https://arxiv.org/abs/2204.10970) | ICPR | deraining, dehazing, desnowing | Not verified | Core restoration |

<a id="year-2021"></a>

### 2021

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Jang2021ICCV"></a>**C2N** · [C2N: Practical Generative Noise Modeling for Real-World Denoising](https://openaccess.thecvf.com/content/ICCV2021/papers/Jang_C2N_Practical_Generative_Noise_Modeling_for_Real-World_Denoising_ICCV_2021_paper.pdf) | ICCV | denoising | Not verified | Core restoration |
| <a id="paper-Wolf2021CVPR"></a>**DeFlow** · [DeFlow: Learning Complex Image Degradations from Unpaired Data with Conditional Flows](https://openaccess.thecvf.com/content/CVPR2021/html/Wolf_DeFlow_Learning_Complex_Image_Degradations_From_Unpaired_Data_With_Conditional_CVPR_2021_paper.html) | CVPR | super-resolution | Not verified | Core restoration |
| <a id="paper-Wei2021TIP"></a>**DerainCycleGAN** · [DerainCycleGAN: Rain Attentive CycleGAN for Single Image Deraining and Rainmaking](https://github.com/OaDsis/DerainCycleGAN) | IEEE TIP | deraining | [Author code](https://github.com/OaDsis/DerainCycleGAN) | Core restoration |
| <a id="paper-Jiang2021TIP"></a>**EnlightenGAN** · [EnlightenGAN: Deep Light Enhancement without Paired Supervision](https://github.com/VITA-Group/EnlightenGAN) | IEEE TIP | low-light | [Author code](https://github.com/VITA-Group/EnlightenGAN) | Core restoration |
| <a id="paper-Radford2021ICML"></a>**CLIP** · [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | ICML | vision-language representation | Not verified | Foundations |
| <a id="paper-Song2021ICLR"></a>**Score SDE** · [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) | ICLR | generative modeling | Not verified | Foundations |
| <a id="paper-Henz2021TVCG"></a>**Camera-noise synthesis GAN** · [Synthesizing Camera Noise Using Generative Adversarial Networks](https://bernardohenz.github.io/projects/synthesizing_noise/) | IEEE Transactions on Visualization and Computer Graphics | denoising | [Author code](https://github.com/bernardohenz/synt_noise_GANs) | Core restoration |
| <a id="paper-Yu2021ACMMM"></a>**UDGNet (single-image variant)** · [Unsupervised Image Deraining: Optimization Model Driven Deep CNN](https://arxiv.org/abs/2203.13699) | ACM Multimedia | deraining | Not verified | Adjacent settings |
| <a id="paper-Wei2021CVPRDDAT"></a>**DASR (domain-distance aware)** · [Unsupervised Real-World Image Super Resolution via Domain-Distance Aware Training](https://openaccess.thecvf.com/content/CVPR2021/html/Wei_Unsupervised_Real-World_Image_Super_Resolution_via_Domain-Distance_Aware_Training_CVPR_2021_paper.html) | CVPR | super-resolution | [Author code](https://github.com/ShuhangGu/DASR) | Core restoration |

<a id="year-2020"></a>

### 2020

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Park2020ECCV"></a>**CUT** · [Contrastive Learning for Unpaired Image-to-Image Translation](https://research.adobe.com/publication/contrastive-learning-for-unpairedimage-to-image-translation/) | ECCV | general image translation | Not verified | Foundations |
| <a id="paper-Ho2020NeurIPS"></a>**DDPM** · [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | NeurIPS | generative modeling | Not verified | Foundations |
| <a id="paper-Liu2020TIP"></a>**E-CycleGAN** · [End-to-End Single Image Fog Removal Using Enhanced Cycle Consistent Adversarial Networks](https://arxiv.org/abs/1902.01374) | IEEE TIP | dehazing | Not verified | Core restoration |
| <a id="paper-Hong2020AAAI"></a>**UIDNet** · [End-to-End Unpaired Image Denoising with Conditional Adversarial Networks](https://ojs.aaai.org/index.php/AAAI/article/view/5834) | AAAI | denoising | Not verified | Core restoration |
| <a id="paper-Ni2020TIP"></a>**UEGAN** · [Towards Unsupervised Deep Image Enhancement with Generative Adversarial Network](https://arxiv.org/abs/2012.15020) | IEEE TIP | photographic enhancement | [Author code](https://github.com/eezkni/UEGAN) | Adjacent settings |
| <a id="paper-Maeda2020CVPR"></a>**Pseudo-supervised SR** · [Unpaired Image Super-Resolution Using Pseudo-Supervision](https://openaccess.thecvf.com/content_CVPR_2020/html/Maeda_Unpaired_Image_Super-Resolution_Using_Pseudo-Supervision_CVPR_2020_paper.html) | CVPR | super-resolution | Not verified | Core restoration |
| <a id="paper-Wu2020ECCV"></a>**Unpaired denoising (DBSN)** · [Unpaired Learning of Deep Image Denoising](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123490341.pdf) | ECCV | denoising | [Author code](https://github.com/XHWXD/DBSN) | Core restoration |

<a id="year-2019"></a>

### 2019

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Krull2019CVPR"></a>**Noise2Void** · [Noise2Void: Learning Denoising from Single Noisy Images](https://arxiv.org/abs/1811.10980) | CVPR | denoising | Not verified | Adjacent settings |
| <a id="paper-Zhu2019AAAI"></a>**RR-GAN** · [Single Image Rain Removal with Unpaired Information: A Differentiable Programming Perspective](https://ojs.aaai.org/index.php/AAAI/article/view/4971) | AAAI | deraining | Not verified | Core restoration |
| <a id="paper-Lu2019CVPR"></a>**Disentangled deblurring** · [Unsupervised Domain-Specific Deblurring via Disentangled Representations](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_Unsupervised_Domain-Specific_Deblurring_via_Disentangled_Representations_CVPR_2019_paper.pdf) | CVPR | deblurring | [Author code](https://github.com/ustclby/Unsupervised-Domain-Specific-Deblurring) | Core restoration |
| <a id="paper-Jin2019ICIP"></a>**UD-GAN** · [Unsupervised Single Image Deraining with Self-Supervised Constraints](https://orca.cardiff.ac.uk/id/eprint/161670/) | ICIP | deraining | Not verified | Core restoration |

<a id="year-2018"></a>

### 2018

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-engin2018cycle"></a>**Cycle-Dehaze** · [Cycle-Dehaze: Enhanced CycleGAN for Single Image Dehazing](https://arxiv.org/abs/1805.05308) | CVPR Workshops | dehazing | [Author code](https://github.com/engindeniz/Cycle-Dehaze) | Core restoration |
| <a id="paper-Ulyanov2018CVPR"></a>**Deep image prior** · [Deep Image Prior](https://arxiv.org/abs/1711.10925) | CVPR | image restoration | Not verified | Adjacent settings |
| <a id="paper-Lee2018ECCV"></a>**DRIT** · [Diverse Image-to-Image Translation via Disentangled Representations](https://arxiv.org/abs/1808.00948) | ECCV | general image translation | Not verified | Foundations |
| <a id="paper-kingma2018glow"></a>**Glow** · [Glow: Generative flow with invertible 1x1 convolutions](https://arxiv.org/abs/1807.03039) | NeurIPS | density modeling | Not verified | Foundations |
| <a id="paper-Chen2018CVPR"></a>**GCBD** · [Image Blind Denoising with Generative Adversarial Network Based Noise Modeling](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Image_Blind_Denoising_CVPR_2018_paper.html) | CVPR | denoising | Not verified | Core restoration |
| <a id="paper-Huang2018ECCV"></a>**MUNIT** · [Multimodal Unsupervised Image-to-Image Translation](https://arxiv.org/abs/1804.04732) | ECCV | general image translation | Not verified | Foundations |
| <a id="paper-Lehtinen2018ICML"></a>**Noise2Noise** · [Noise2Noise: Learning Image Restoration without Clean Data](https://arxiv.org/abs/1803.04189) | ICML | denoising | Not verified | Adjacent settings |

<a id="year-2017"></a>

### 2017

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-dinh2017density"></a>**Real NVP** · [Density estimation using Real NVP](https://arxiv.org/abs/1605.08803) | ICLR | density modeling | Not verified | Foundations |
| <a id="paper-Zhu2017ICCV"></a>**CycleGAN** · [Unpaired Image-to-Image Translation Using Cycle-Consistent Adversarial Networks](https://junyanz.github.io/CycleGAN/) | ICCV | general image translation | [Author code](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) | Foundations |
| <a id="paper-Liu2017NeurIPS"></a>**UNIT** · [Unsupervised Image-to-Image Translation Networks](https://arxiv.org/abs/1703.00848) | NeurIPS | general image translation | Not verified | Foundations |

<a id="year-2014"></a>

### 2014

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Goodfellow2014NeurIPS"></a>**GAN** · [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661) | NeurIPS | generative modeling | Not verified | Foundations |

<a id="year-2009"></a>

### 2009

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-He2009CVPR"></a>**Dark channel prior** · [Single Image Haze Removal Using Dark Channel Prior](https://people.csail.mit.edu/kaiming/) | CVPR | dehazing | Not verified | Foundations |

<a id="year-2007"></a>

### 2007

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Dabov2007TIP"></a>**BM3D** · [Image Denoising by Sparse 3-D Transform-Domain Collaborative Filtering](https://webpages.tuni.fi/foi/GCF-BM3D/index.html) | IEEE TIP | denoising | Not verified | Foundations |

<a id="year-1971"></a>

### 1971

| Paper / method | Venue | Task tags | Implementation | Scope |
|---|---|---|---|---|
| <a id="paper-Land1971JOSA"></a>**Retinex** · [Lightness and Retinex Theory](https://doi.org/10.1364/JOSA.61.000001) | Journal of the Optical Society of America | low-light | Not verified | Foundations |

## Contributing and reuse

Corrections and additional primary-source records are welcome. Follow the [contribution guide](CONTRIBUTING.md) and regenerate the indexes from the CSV files. Cite the original papers and datasets when using their work; linked resources retain their own [reuse terms](REUSE.md).

The navigation conventions of the [All-in-One Image Restoration resource collection](https://github.com/Harbinzzy/All-in-One-Image-Restoration-Survey) informed this directory's organization. Its prose, figures and experimental results are not reproduced here.
