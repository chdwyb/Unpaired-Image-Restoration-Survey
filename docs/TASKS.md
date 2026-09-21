# Task index

[Back to overview](../README.md)

The 68 six-task records in the [counted corpus](PUBLIC_SEARCH_2026.md) are grouped by documented restoration task. Multi-task papers appear in more than one section.

<a id="denoising"></a>

## Denoising

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TPAMI issue 2025; older preprint counted once. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [MSED](https://www.sciencedirect.com/science/article/abs/pii/S1047320323001827) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. Independent low-light and normal-light images; global/local multi-stream generator. |
| [OTUR](https://arxiv.org/abs/2108.02574) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [SCPGabNet](https://openaccess.thecvf.com/content/ICCV2023/html/Lin_Unsupervised_Image_Denoising_in_Real-World_Scenarios_via_Self-Collaboration_Parallel_Generative_ICCV_2023_paper.html) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [C2N](https://openaccess.thecvf.com/content/ICCV2021/papers/Jang_C2N_Practical_Generative_Noise_Modeling_for_Real-World_Denoising_ICCV_2021_paper.pdf) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. DND protocol includes target noisy-image adaptation; retain this information budget. |
| [Camera-noise synthesis GAN](https://bernardohenz.github.io/projects/synthesizing_noise/) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. Unpaired camera-noise synthesis followed by DnCNN; camera-specific RENOIR evaluation. |
| [UIDNet](https://ojs.aaai.org/index.php/AAAI/article/view/5834) | 2020 | unpaired restoration; consult access note and paper for auxiliary supervision. Clean/noisy domains and generated pairs; not noisy-only learning. |
| [Flow-prior unpaired denoising](https://arxiv.org/abs/2009.11532) | 2020 | independent-domain restoration branch; see access_note for auxiliary information. A flow prior learns from clean images independent of the noisy training set; a denoising network subsequently uses that prior without paired clean targets. The author repository explicitly separates clean/noisy/test folders. |
| [Unpaired denoising (DBSN)](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123490341.pdf) | 2020 | unpaired restoration; consult access note and paper for auxiliary supervision. Blind-spot/noise-model stage followed by independent-clean-image synthesis and distillation. |
| [GCBD](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Image_Blind_Denoising_CVPR_2018_paper.html) | 2018 | unpaired restoration; consult access note and paper for auxiliary supervision. Noise patches and independent clean images; generated pairs train the denoiser. |

<a id="deblurring"></a>

## Deblurring

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [EMP](https://openaccess.thecvf.com/content/CVPR2026/html/Cho_Event-based_Motion_Deblurring_with_Unpaired_Data_CVPR_2026_paper.html) | 2026 | independent blurry and sharp image domains; synchronized event observations supply auxiliary physical information. |
| [DDSB](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [TP-Diff](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Learning_Deblurring_Texture_Prior_from_Unpaired_Data_with_Diffusion_Model_ICCV_2025_paper.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [SEMGUD](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Unsupervised_Blind_Image_Deblurring_Based_on_Self-Enhancement_CVPR_2024_paper.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [Contrastive domain-translation deblurring](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/ipr2.12832) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. Unpaired motion-blur/sharp domains; contrastive constraint added to domain translation. |
| [NeurMAP](https://doi.org/10.1109/TPAMI.2023.3303450) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Public unsupervised and semi-supervised paths; initialization and motion-estimator training must be identified. |
| [FCL-GAN](https://opus.lib.uts.edu.au/handle/10453/169860) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [Disentangled deblurring](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_Unsupervised_Domain-Specific_Deblurring_via_Disentangled_Representations_CVPR_2019_paper.pdf) | 2019 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [Class-specific deblurring](https://openaccess.thecvf.com/content_ECCV_2018/html/Nimisha_T_M_Unsupervised_Class-Specific_Deblurring_ECCV_2018_paper.html) | 2018 | independent-domain restoration branch; see access_note for auxiliary information. Independent sharp/blurry sets within a class; adversarial sharp prior and learned reblurring. |

<a id="dehazing"></a>

## Dehazing

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [UD3Net](https://www.techscience.com/sdhm/v20n3/67386/html) | 2026 | independent-domain restoration branch; see access_note for auxiliary information. Independent hazy/clear domains with scattering-model reconstruction and frequency/Retinex priors. |
| [UID-KAT](https://www.sciencedirect.com/science/article/abs/pii/S0031320326002694) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Final Pattern Recognition 2026; 2025 arXiv preprint counted once. KAN latent transformation with adversarial/contrastive learning. |
| [VMCR-Net](https://onlinelibrary.wiley.com/doi/abs/10.1111/exsy.70309) | 2026 | independent-domain restoration branch; see access_note for auxiliary information. DisentGAN-based unpaired haze/clear mapping; Mamba representation with contrastive regularization. |
| [OBCOT](https://pubmed.ncbi.nlm.nih.gov/41955147/) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TNNLS issue year 2026; transport-based dehazing. |
| [Diff-Dehazer](https://doi.org/10.1609/aaai.v39i4.32469) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [FrDiff](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Frequency_Domain-Based_Diffusion_Model_for_Unpaired_Image_Dehazing_ICCV_2025_paper.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [DehazeSB](https://github.com/ywxjm/DehazeSB) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Pretrained semantic guidance; final ICCV year 2025. |
| [ODCR](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_ODCR_Orthogonal_Decoupling_Contrastive_Regularization_for_Unpaired_Image_Dehazing_CVPR_2024_paper.html) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [D4+](https://doi.org/10.1007/s11263-023-01940-5) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [UCL-Dehaze](https://github.com/yz-wang/UCL-Dehaze) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TIP publication 2024; 2022 preprint deduplicated. |
| [UBRFC-Net](https://www.sciencedirect.com/science/article/pii/S0893608024002387) | 2024 | independent-domain restoration branch; see access_note for auxiliary information. Bidirectional clear/hazy distribution matching with contrastive reconstruction, no matched supervision stated by primary paper. |
| [AGLC-GAN](https://www.sciencedirect.com/science/article/pii/S0262885623002330) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. Independent hazy/clear domains; global/local discrimination and cyclic perceptual consistency. |
| [ADCP-CycleGAN](https://www.mdpi.com/1099-4300/25/6/856) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. Unpaired hazy/clear cycles coupled by atmospheric model; pretrained segmentation is auxiliary access. |
| [Global/local unsupervised dehazing](https://link.springer.com/article/10.1007/s00530-021-00852-z) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. Independent clear/hazy images with global/local discriminators and dark-channel attention. |
| [USID-Net](https://github.com/dehazing/USID-Net) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [Cycle-SNSPGAN](https://github.com/yz-wang/Cycle-SNSPGAN) | 2022 | independent-domain restoration branch; see access_note for auxiliary information. Independent haze/clear training folders; cyclic self-perceptual matching and spectrally normalized discrimination. |
| [DCA-CycleGAN](https://www.sciencedirect.com/science/article/pii/S1047320321002923) | 2022 | independent-domain restoration branch; see access_note for auxiliary information. Unpaired hazy/clear CycleGAN with dark-channel attention and local discrimination. |
| [D4](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Self-Augmented_Unpaired_Image_Dehazing_via_Density_and_Depth_Decomposition_CVPR_2022_paper.html) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [CDD-GAN](https://arxiv.org/abs/2203.07677) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DGP-CycleGAN](https://arxiv.org/abs/2204.10970) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [RefineDNet](https://www.fst.um.edu.mo/personal/wp-content/uploads/2021/05/RefineDNet.pdf) | 2021 | independent-domain restoration branch; see access_note for auxiliary information. DCP initialization followed by adversarial refinement with independent hazy/clear images; weak supervision means prior-generated targets. |
| [Dehaze-GLCGAN](https://arxiv.org/abs/2008.06632) | 2020 | independent-domain restoration branch; see access_note for auxiliary information. Independent hazy/clear domains and global/local cyclic adversarial learning. |
| [Cyclic perceptual-depth dehazing](https://arxiv.org/abs/2007.05220) | 2020 | independent-domain restoration branch; see access_note for auxiliary information. Independent hazy/clear domains; pretrained depth estimator supplies auxiliary structural supervision. |
| [E-CycleGAN](https://arxiv.org/abs/1902.01374) | 2020 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [CDNet](https://doi.org/10.1109/WACV.2019.00127) | 2019 | unpaired adversarial cycle training for transmission estimation; author publication record and paper. |
| [Cycle-Dehaze](https://arxiv.org/abs/1805.05308) | 2018 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DisentGAN](https://aaai.org/papers/12317-towards-perceptual-image-dehazing-by-physics-based-disentanglement-and-adversarial-training/) | 2018 | independent-domain restoration branch; see access_note for auxiliary information. Unpaired natural clear/hazy sets; scattering-model decomposition and adversarial clean-domain constraint. |

<a id="low-light"></a>

## Low-light enhancement

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [DDSB](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [Cycle-Retinex](https://github.com/mummmml/Cycle-Retinex) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [LightenDiffusion](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6440_ECCV_2024_paper.php) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [CGAAN](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422370/) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. EnlightenGAN unpaired training collection; cyclic attention GAN and global/local discrimination. |
| [CLIP-LIT](https://openaccess.thecvf.com/content/ICCV2023/papers/Liang_Iterative_Prompt_Learning_for_Unsupervised_Backlit_Image_Enhancement_ICCV_2023_paper.pdf) | 2023 | unpaired restoration; consult access note and paper for auxiliary supervision. Backlit enhancement with pretrained CLIP; not a GAN architecture. Alias Liang2023ICCV is deduplicated. |
| [MSED](https://www.sciencedirect.com/science/article/abs/pii/S1047320323001827) | 2023 | independent-domain restoration branch; see access_note for auxiliary information. Independent low-light and normal-light images; global/local multi-stream generator. |
| [LE-GAN](https://www.sciencedirect.com/science/article/pii/S0950705121011151) | 2022 | independent-domain restoration branch; see access_note for auxiliary information. Independent low/normal-light domains; illumination attention and identity preservation. |
| [Decoupled-LLIE](https://arxiv.org/abs/2005.02818) | 2022 | unpaired GAN illumination enhancement and noise suppression with pseudo-label construction; ICPR2022 verified from author and IAPR proceedings. |
| [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. Final journal year 2021; the 2019 preprint is not a second paper. |

<a id="deraining"></a>

## Deraining

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [Prompt-oriented frequency-regularized SB](https://www.sciencedirect.com/science/article/pii/S0031320325015250) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [SFTOT](https://ieeexplore.ieee.org/document/11340759) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Published approach; attributable public code and primary numerical tables not verified in this audit. |
| [RGSUD](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Unpaired_Image_Deraining_Using_Reward-Guided_Self-Reinforcement_Strategy_CVPR_2026_paper.pdf) | 2026 | independent-domain restoration branch; see access_note for auxiliary information. Independent rainy/clear sets; IQA reward recycling and pseudo-pair self-reinforcement; pretrained IQA prior is extra access. |
| [UIPL](https://www.sciencedirect.com/science/article/abs/pii/S0957417425046251) | 2026 | unpaired restoration; consult access note and paper for auxiliary supervision. Final ESWA issue year 2026; independent domains and perceptual guidance. |
| [CSUD](https://doi.org/10.1109/CVPR52734.2025.00700) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DDSB](https://papers.neurips.cc/paper_files/paper/2025/hash/039c30e9af8039fbd1b58da9d04f38e9-Abstract-Conference.html) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TPAMI issue 2025; older preprint counted once. |
| [DA-RCOT](https://doi.org/10.1109/TPAMI.2025.3562211) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Paired and unpaired restoration variants; distinguish data access for each reported experiment. |
| [Mask-DerainGAN](https://www.sciencedirect.com/science/article/pii/S0031320324005910) | 2024 | independent-domain restoration branch; see access_note for auxiliary information. Unpaired rain/clean domains; mask-conditioned rain generation and contrastive content preservation. |
| [NSB](https://www.sciencedirect.com/science/article/pii/S0020025524011137) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Pretrained CLIP guidance is part of the information budget. |
| [UPID-EDM](https://chdwyb.github.io/) | 2024 | unpaired restoration; consult access note and paper for auxiliary supervision. Energy-informed diffusion classification uses verified title-level evidence; no exact loss inventory asserted. |
| [DCD-GAN](https://openaccess.thecvf.com/content/CVPR2022/papers/Chen_Unpaired_Deep_Image_Deraining_Using_Dual_Contrastive_Learning_CVPR_2022_paper.pdf) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [NLCL](https://doi.org/10.1109/CVPR52688.2022.00573) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DGP-CycleGAN](https://arxiv.org/abs/2204.10970) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [DerainCycleGAN](https://github.com/OaDsis/DerainCycleGAN) | 2021 | unpaired restoration; consult access note and paper for auxiliary supervision. Final journal year 2021; the 2019 preprint is not a second paper. |
| [UDGNet (full model)](https://arxiv.org/abs/2203.13699) | 2021 | independent rainy/clean domains in full model; separate single-image variant. Full model includes an adversarial clean-image prior; the single-image variant removes that adversarial term. The prior registry indexed only the single-image boundary variant. This corpus counts the full paper once. |
| [RR-GAN](https://ojs.aaai.org/index.php/AAAI/article/view/4971) | 2019 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |
| [UD-GAN](https://orca.cardiff.ac.uk/id/eprint/161670/) | 2019 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |

<a id="desnowing"></a>

## Desnowing

| Method / paper | Year | Supervision and access |
|---|---:|---|
| [RSCP2GAN](https://researchportal.hkust.edu.hk/en/publications/re-boosting-self-collaboration-parallel-prompt-gan-for-unsupervis/) | 2025 | unpaired restoration; consult access note and paper for auxiliary supervision. Final TPAMI issue 2025; older preprint counted once. |
| [DGP-CycleGAN](https://arxiv.org/abs/2204.10970) | 2022 | unpaired restoration; consult access note and paper for auxiliary supervision. Representative method; exact training pools and auxiliary pretraining require configuration-level disclosure. |

## Related tasks and foundations

The [full corpus](PUBLIC_SEARCH_2026.md) includes underwater enhancement, super-resolution, sand/dust removal, and general/weather translation. Selected background works below are not relabelled as six-task evaluations.

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
| **UDGNet (single-image variant)** · [Unsupervised Image Deraining: Optimization Model Driven Deep CNN](https://arxiv.org/abs/2203.13699) | ACM Multimedia | deraining | Not verified | Adjacent settings |
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
