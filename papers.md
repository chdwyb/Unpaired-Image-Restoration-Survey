# Papers and implementations

[Back to overview](README.md) · [Dataset catalog](datasets.md)

Browse restoration methods and related image-translation work by task. Methods covering several tasks appear under [Multiple restoration tasks](#multiple-restoration-tasks). Each paper is listed once; publication years refer to the listed venue, or to the preprint when no final publication is listed.

**Mechanism tags:** D = distribution matching; C = content consistency; G = degradation modeling; P = clean-image priors. Tags are nonexclusive and describe restoration constraints. Implementation labels describe networks or probabilistic formulations: optimal transport (OT) and Schrödinger bridges (SB) are formulations that can use different networks. Tags are supplied for selected methods; an untagged entry is not a claim that a mechanism is absent.

Code links point to author-associated implementations where available; project links are labeled separately. A dash means no implementation link is supplied here. Model variants and auxiliary training information are summarized in [Setting notes](#setting-notes).

[Denoising](#denoising) · [Deblurring](#deblurring) · [Dehazing](#dehazing) · [Low-light enhancement](#low-light-enhancement) · [Deraining](#deraining) · [Desnowing](#desnowing) · [Multiple restoration tasks](#multiple-restoration-tasks) · [Super-resolution](#super-resolution) · [Underwater enhancement](#underwater-enhancement) · [Other restoration settings](#other-restoration-settings) · [Image and weather translation](#image-and-weather-translation)

## Denoising

See also [methods covering multiple tasks](#multiple-restoration-tasks).

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2025 · TMI | **DADn** — [Unsupervised Domain Adaptation for EM Image Denoising with Invertible Networks](https://doi.org/10.1109/TMI.2024.3431192) | C · G<br>INN, CNN | [Code](https://github.com/sydeng99/DADn) |
| 2023 · TPAMI | **OTUR** — [Optimal Transport for Unsupervised Denoising Learning](https://doi.org/10.1109/TPAMI.2022.3170155) | D · C<br>OT, CNN | [Code](https://github.com/wangweiSJTU/OTUR) |
| 2023 · ICCV | **SCPGabNet** — [Unsupervised Image Denoising in Real-World Scenarios via Self-Collaboration Parallel Generative Adversarial Branches](https://doi.org/10.1109/iccv51070.2023.01162) | G<br>GAN, CNN | [Code](https://github.com/linxin0/SCPGabNet) |
| 2022 · Med. Phys. | **LDCT flow** — [Learning Low-Dose CT Degradation from Unpaired Data with Flow-Based Model](https://doi.org/10.1002/mp.15886) | G<br>Flow, CNN | — |
| 2021 · ICCV | **C2N** — [C2N: Practical Generative Noise Modeling for Real-World Denoising](https://doi.org/10.1109/iccv48922.2021.00235) | G<br>GAN, CNN | — |
| 2021 · TVCG | **Camera-noise GAN** — [Synthesizing Camera Noise Using Generative Adversarial Networks](https://doi.org/10.1109/TVCG.2020.3012120) | C · G<br>GAN, CNN | [Code](https://github.com/bernardohenz/synt_noise_GANs) |
| 2021 · TMI | **ISCL** — [ISCL: Interdependent Self-Cooperative Learning for Unpaired Image Denoising](https://doi.org/10.1109/TMI.2021.3096142) | D · C · G<br>GAN, CNN | — |
| 2020 · ICIP | **Flow-prior** — [Unpaired Image Denoising](https://doi.org/10.1109/icip40778.2020.9190932) | C · P<br>Flow, CNN | [Code](https://github.com/priyathamkat/unpaired-image-denoising) |
| 2020 · AAAI | **UIDNet** — [End-to-End Unpaired Image Denoising with Conditional Adversarial Networks](https://doi.org/10.1609/aaai.v34i04.5834) | G<br>GAN, CNN | — |
| 2020 · ECCV | **Unpaired-Dn** — [Unpaired Learning of Deep Image Denoising](https://doi.org/10.1007/978-3-030-58548-8_21) | G<br>CNN | [Code](https://github.com/XHWXD/DBSN) |
| 2018 · CVPR | **GCBD** — [Image Blind Denoising with Generative Adversarial Network Based Noise Modeling](https://doi.org/10.1109/cvpr.2018.00333) | G<br>GAN, CNN | — |

## Deblurring

See also [methods covering multiple tasks](#multiple-restoration-tasks).

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2026 · CVPR | **BluRef** — [BluRef: Unsupervised Image Deblurring with Dense-Matching References](https://openaccess.thecvf.com/content/CVPR2026/papers/Pham_BluRef_Unsupervised_Image_Deblurring_with_Dense-Matching_References_CVPR_2026_paper.pdf) | C<br>CNN | [Project](https://qualcomm-ai-research.github.io/BluRef/) |
| 2026 · CVPR | **EMP** — [Event-based Motion Deblurring with Unpaired Data](https://openaccess.thecvf.com/content/CVPR2026/html/Cho_Event-based_Motion_Deblurring_with_Unpaired_Data_CVPR_2026_paper.html) | G<br>CNN, Attention | [Code](https://github.com/Chohoonhee/EMP) |
| 2025 · ICCV | **TP-Diff** — [Learning Deblurring Texture Prior from Unpaired Data with Diffusion Model](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Learning_Deblurring_Texture_Prior_from_Unpaired_Data_with_Diffusion_Model_ICCV_2025_paper.html) | D · C · P<br>Diffusion | — |
| 2024 · CVPR | **SEMGUD** — [Unsupervised Blind Image Deblurring Based on Self-Enhancement](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Unsupervised_Blind_Image_Deblurring_Based_on_Self-Enhancement_CVPR_2024_paper.html) | G<br>CNN, GAN | — |
| 2023 · IET Image Process. | **Contrastive domain-translation deblurring** — [A domain translation network with contrastive constraint for unpaired motion image deblurring](https://doi.org/10.1049/ipr2.12832) | — | — |
| 2023 · TPAMI | **NeurMAP** — [Neural Maximum a Posteriori Estimation on Unpaired Data for Motion Deblurring](https://doi.org/10.1109/TPAMI.2023.3303450) | D · G<br>CNN | [Code](https://github.com/yjzhang96/NeurMAP-deblur) |
| 2022 · ACM MM | **FCL-GAN** — [FCL-GAN: A Lightweight and Real-Time Baseline for Unsupervised Blind Image Deblurring](https://doi.org/10.1145/3503161.3548113) | D · C<br>GAN | [Code](https://github.com/suiyizhao/FCL-GAN) |
| 2019 · CVPR | **Disentangled deblurring** — [Unsupervised Domain-Specific Deblurring via Disentangled Representations](https://doi.org/10.1109/cvpr.2019.01047) | — | [Code](https://github.com/ustclby/Unsupervised-Domain-Specific-Deblurring) |
| 2018 · ECCV | **Class-specific deblurring** — [Unsupervised Class-Specific Deblurring](https://doi.org/10.1007/978-3-030-01249-6_22) | — | — |

## Dehazing

See also [methods covering multiple tasks](#multiple-restoration-tasks).

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2026 · TOMM | **FAL-Net** — [Unsupervised Dehazing of Real-World Images with Frequency-Aware Learning](https://doi.org/10.1145/3803423) | D · C · G<br>SSM, GAN | — |
| 2026 · TNNLS | **OBCOT** — [When Optimal Transport Meets Photo-Realistic Image Dehazing with Unpaired Training](https://doi.org/10.1109/TNNLS.2026.3673760) | D · C<br>OT | — |
| 2026 · SDHM | **UD3Net** — [An Unpaired Dual-Domain Image Dehazing Framework Using Unsupervised Learning](https://doi.org/10.32604/sdhm.2026.077878) | D · C · G<br>CNN, GAN | — |
| 2026 · PR | **UID-KAT** — [Unpaired Image Dehazing via Kolmogorov-Arnold Transformation of Latent Features](https://doi.org/10.1016/j.patcog.2026.113304) | D · C<br>GAN, KAN | [Code](https://github.com/tranleanh/uid-kat) |
| 2026 · Expert Syst. | **VMCR-Net** — [Unsupervised Vision Mamba With Contrastive Regularization Network for Single Image Dehazing](https://doi.org/10.1111/exsy.70309) | D · C · G<br>SSM, GAN | — |
| 2025 · ICCV | **DehazeSB** — [When Schrodinger Bridge Meets Real-World Image Dehazing with Unpaired Training](https://doi.org/10.1109/iccv51701.2025.00819) | D · C · P<br>Diffusion, SB | [Code](https://github.com/ywxjm/DehazeSB) |
| 2025 · AAAI | **Diff-Dehazer** — [Exploiting Diffusion Prior for Real-World Image Dehazing with Unpaired Training](https://doi.org/10.1609/aaai.v39i4.32469) | D · C · G · P<br>Diffusion, GAN | — |
| 2025 · ICCV | **FrDiff** — [Frequency Domain-Based Diffusion Model for Unpaired Image Dehazing](https://doi.org/10.1109/iccv51701.2025.00707) | D · C<br>Diffusion | — |
| 2024 · IJCV | **D4+** — [Robust Unpaired Image Dehazing via Density and Depth Decomposition](https://doi.org/10.1007/s11263-023-01940-5) | D · C · G<br>CNN, GAN | [Code](https://github.com/YaN9-Y/D4_plus) |
| 2024 · CVPR | **ODCR** — [ODCR: Orthogonal Decoupling Contrastive Regularization for Unpaired Image Dehazing](https://doi.org/10.1109/cvpr52733.2024.02407) | D · C<br>GAN | — |
| 2024 · Neural Netw. | **UBRFC-Net** — [Unsupervised Bidirectional Contrastive Reconstruction and Adaptive Fine-Grained Channel Attention Networks for image dehazing](https://doi.org/10.1016/j.neunet.2024.106314) | — | [Code](https://github.com/Lose-Code/UBRFC-Net) |
| 2024 · TIP | **UCL-Dehaze** — [UCL-Dehaze: Toward Real-World Image Dehazing via Unsupervised Contrastive Learning](https://doi.org/10.1109/TIP.2024.3362153) | D · C<br>GAN | [Code](https://github.com/yz-wang/UCL-Dehaze) |
| 2023 · Entropy | **ADCP-CycleGAN** — [Enhanced CycleGAN Network with Adaptive Dark Channel Prior for Unpaired Single-Image Dehazing](https://doi.org/10.3390/e25060856) | — | — |
| 2023 · Image Vis. Comput. | **AGLC-GAN** — [AGLC-GAN: Attention-based global-local cycle-consistent generative adversarial networks for unpaired single image dehazing](https://doi.org/10.1016/j.imavis.2023.104859) | — | — |
| 2023 · Multimedia Syst. | **Global/local unsupervised dehazing** — [Unsupervised single image dehazing with generative adversarial network](https://doi.org/10.1007/s00530-021-00852-z) | — | — |
| 2023 · TMM | **USID-Net** — [USID-Net: Unsupervised Single Image Dehazing Network via Disentangled Representations](https://doi.org/10.1109/TMM.2022.3163554) | D · C<br>CNN, GAN | [Code](https://github.com/dehazing/USID-Net) |
| 2022 · ECCV | **CDD-GAN** — [Unpaired Deep Image Dehazing Using Contrastive Disentanglement Learning](https://doi.org/10.1007/978-3-031-19790-1_38) | D · C<br>GAN | — |
| 2022 · TITS | **Cycle-SNSPGAN** — [Cycle-SNSPGAN: Towards Real-World Image Dehazing via Cycle Spectral Normalized Soft Likelihood Estimation Patch GAN](https://doi.org/10.1109/tits.2022.3170328) | — | [Code](https://github.com/yz-wang/Cycle-SNSPGAN) |
| 2022 · CVPR | **D4** — [Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition](https://doi.org/10.1109/cvpr52688.2022.00208) | D · C · G<br>GAN, CNN | [Code](https://github.com/YaN9-Y/D4) |
| 2022 · J. Vis. Commun. Image Represent. | **DCA-CycleGAN** — [DCA-CycleGAN: Unsupervised single image dehazing using Dark Channel Attention optimized CycleGAN](https://doi.org/10.1016/j.jvcir.2021.103431) | — | — |
| 2021 · TIP | **RefineDNet** — [RefineDNet: A Weakly Supervised Refinement Framework for Single Image Dehazing](https://doi.org/10.1109/TIP.2021.3060873) | D · C · G<br>CNN, GAN | — |
| 2020 · arXiv preprint arXiv:2007.05220 | **Cyclic perceptual-depth dehazing** — [Efficient Unpaired Image Dehazing with Cyclic Perceptual-Depth Supervision](https://arxiv.org/abs/2007.05220) | — | — |
| 2020 · arXiv preprint arXiv:2008.06632 | **Dehaze-GLCGAN** — [Dehaze-GLCGAN: Unpaired Single Image De-hazing via Adversarial Training](https://arxiv.org/abs/2008.06632) | — | — |
| 2020 · TIP | **E-CycleGAN** — [End-to-End Single Image Fog Removal Using Enhanced Cycle Consistent Adversarial Networks](https://doi.org/10.1109/TIP.2020.3007844) | — | — |
| 2019 · WACV | **CDNet** — [CDNet: Single Image De-Hazing Using Unpaired Adversarial Training](https://doi.org/10.1109/WACV.2019.00127) | — | — |
| 2018 · CVPRW | **Cycle-Dehaze** — [Cycle-Dehaze: Enhanced CycleGAN for Single Image Dehazing](https://doi.org/10.1109/cvprw.2018.00127) | D · C<br>GAN | [Code](https://github.com/engindeniz/Cycle-Dehaze) |
| 2018 · AAAI | **DisentGAN** — [Towards perceptual image dehazing by physics-based disentanglement and adversarial training](https://doi.org/10.1609/aaai.v32i1.12317) | D · G<br>GAN | — |

## Low-light enhancement

See also [methods covering multiple tasks](#multiple-restoration-tasks).

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2024 · TMM | **Cycle-Retinex** — [Cycle-Retinex: Unpaired Low-Light Image Enhancement via Retinex-Inline CycleGAN](https://doi.org/10.1109/TMM.2023.3278385) | D · C · G<br>GAN, CNN | [Code](https://github.com/mummmml/Cycle-Retinex) |
| 2024 · ECCV | **LightenDiffusion** — [LightenDiffusion: Unsupervised Low-Light Image Enhancement with Latent-Retinex Diffusion Models](https://doi.org/10.1007/978-3-031-73195-2_10) | C · G<br>Diffusion | [Code](https://github.com/JianghaiSCU/LightenDiffusion) |
| 2023 · Sensors | **CGAAN** — [Cyclic Generative Attention-Adversarial Network for Low-Light Image Enhancement](https://doi.org/10.3390/s23156990) | — | — |
| 2023 · ICCV | **CLIP-LIT** — [Iterative Prompt Learning for Unsupervised Backlit Image Enhancement](https://doi.org/10.1109/iccv51070.2023.00743) | C · P<br>CNN, CLIP | [Code](https://github.com/ZhexinLiang/CLIP-LIT) |
| 2022 · ICPR | **Decoupled-LLIE** — [Unsupervised Low-light Image Enhancement with Decoupled Networks](https://arxiv.org/abs/2005.02818) | — | — |
| 2022 · KBS | **LE-GAN** — [LE-GAN: Unsupervised low-light image enhancement network using attention module and identity invariant loss](https://doi.org/10.1016/j.knosys.2021.108010) | D · C<br>GAN | — |
| 2021 · TIP | **EnlightenGAN** — [EnlightenGAN: Deep Light Enhancement without Paired Supervision](https://doi.org/10.1109/TIP.2021.3051462) | D · C<br>GAN | [Code](https://github.com/VITA-Group/EnlightenGAN) |

## Deraining

See also [methods covering multiple tasks](#multiple-restoration-tasks).

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2026 · PR | **PFSB** — [Prompt-Oriented and Frequency-Regularized Schrödinger Bridge for Unpaired Rain Streaks and Raindrops Removal](https://doi.org/10.1016/j.patcog.2025.112862) | — | — |
| 2026 · CVPR | **RGSUD** — [Unpaired Image Deraining Using Reward-Guided Self-Reinforcement Strategy](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Unpaired_Image_Deraining_Using_Reward-Guided_Self-Reinforcement_Strategy_CVPR_2026_paper.pdf) | G · P<br>CNN, GAN, VLM | — |
| 2026 · TMM | **SFTOT** — [Structure-Preserving Frequency-Regularized Text-Guided Optimal Transport for Unpaired Rain Streaks and Raindrops Removal](https://doi.org/10.1109/TMM.2026.3651132) | D · C · P<br>OT, Diffusion | — |
| 2026 · Expert Syst. Appl. | **UIPL** — [Unpaired Iterative Prompt Learning for Real-World Image Deraining](https://doi.org/10.1016/j.eswa.2025.131010) | — | — |
| 2025 · CVPR | **CSUD** — [Channel Consistency Prior and Self-Reconstruction Strategy Based Unsupervised Image Deraining](https://doi.org/10.1109/CVPR52734.2025.00700) | D · G · P<br>CNN, GAN | [Code](https://github.com/GuangluDong0728/CSUD-Unsupervised-Deraining-CVPR2025) |
| 2024 · Neural Netw. | **CCLformer** — [Cycle Contrastive Adversarial Learning with Structural Consistency for Unsupervised High-Quality Image Deraining Transformer](https://doi.org/10.1016/j.neunet.2024.106428) | D · C<br>GAN, ViT | [Code](https://github.com/ChenzhaoNju/CCLGAN) |
| 2024 · PR | **Mask-DerainGAN** — [Mask-DerainGAN: Learning to Remove Rain Streaks by Learning to Generate Rainy Images](https://doi.org/10.1016/j.patcog.2024.110840) | — | — |
| 2024 · Inf. Sci. | **NSB** — [Neural Schrödinger Bridge for Unpaired Real-World Image Deraining](https://doi.org/10.1016/j.ins.2024.121199) | D<br>Diffusion, SB | — |
| 2024 · ACM MM | **UPID-EDM** — [Unpaired Photo-Realistic Image Deraining with Energy-Informed Diffusion Model](https://doi.org/10.1145/3664647.3680560) | C · P<br>Diffusion | — |
| 2022 · CVPR | **DCD-GAN** — [Unpaired Deep Image Deraining Using Dual Contrastive Learning](https://doi.org/10.1109/cvpr52688.2022.00206) | D · C<br>GAN | [Code](https://github.com/cschenxiang/DCD-GAN) |
| 2022 · CVPR | **NLCL** — [Unsupervised Deraining: Where Contrastive Learning Meets Self-Similarity](https://doi.org/10.1109/CVPR52688.2022.00573) | D · C · G<br>GAN | [Code](https://github.com/yunguo224/NLCL) |
| 2021 · TIP | **DerainCycleGAN** — [DerainCycleGAN: Rain Attentive CycleGAN for Single Image Deraining and Rainmaking](https://doi.org/10.1109/TIP.2021.3074804) | D · C · G<br>GAN | [Code](https://github.com/OaDsis/DerainCycleGAN) |
| 2021 · ACM MM | **UDGNet** — [Unsupervised Image Deraining: Optimization Model Driven Deep CNN](https://doi.org/10.1145/3474085.3475441) | D · G · P<br>CNN | — |
| 2019 · AAAI | **RR-GAN** — [Singe Image Rain Removal with Unpaired Information: A Differentiable Programming Perspective](https://doi.org/10.1609/aaai.v33i01.33019332) | D<br>GAN | — |
| 2019 · ICIP | **UD-GAN** — [Unsupervised Single Image Deraining with Self-Supervised Constraints](https://doi.org/10.1109/ICIP.2019.8803238) | — | — |

## Desnowing

Desnowing is covered by cross-task approaches such as **RSCP²GAN** and **DGP-CycleGAN**, listed under [Multiple restoration tasks](#multiple-restoration-tasks). Consult their papers for snow-specific data and configurations.

## Multiple restoration tasks

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2025 · TPAMI | **DA-RCOT** — [Degradation-Aware Residual-Conditioned Optimal Transport for Unified Image Restoration](https://doi.org/10.1109/TPAMI.2025.3562211)<br>Denoising; Deblurring; Deraining; Dehazing; Low-light enhancement | D · C<br>OT, CNN | — |
| 2025 · ICCV | **DDM** — [Unsupervised Imaging Inverse Problems with Diffusion Distribution Matching](https://doi.org/10.1109/iccv51701.2025.02634)<br>Deblurring; Super-resolution; Operator calibration | G<br>Flow matching | — |
| 2025 · NeurIPS | **DDSB** — [Degradation-Aware Dynamic Schrodinger Bridge for Unpaired Image Restoration](https://doi.org/10.52202/085713-0086)<br>Deblurring; Low-light enhancement; Deraining; Raindrop removal | D · C<br>Diffusion, SB | — |
| 2025 · TPAMI | **RSCP²GAN** — [Re-Boosting Self-Collaboration Parallel Prompt GAN for Unsupervised Image Restoration](https://doi.org/10.1109/TPAMI.2025.3589606)<br>Denoising; Deraining; Desnowing | G<br>GAN, CNN | [Code](https://github.com/linxin0/RSCP2GAN) |
| 2024 · Expert Systems with Applications | **DedustGAN** — [DedustGAN: Unpaired learning for image dedusting based on Retinex with GANs](https://doi.org/10.1016/j.eswa.2023.122844)<br>Sand and dust removal; Underwater enhancement; Low-light enhancement | — | [Code](https://github.com/FrankLittleSui/DedustGAN) |
| 2024 · ICML | **RCOT** — [Residual-Conditioned Optimal Transport: Towards Structure-Preserving Unpaired and Paired Image Restoration](https://proceedings.mlr.press/v235/tang24d.html)<br>Denoising; Deraining; Dehazing; Super-resolution | D · C<br>OT, CNN | — |
| 2024 · Machine Vision and Applications | **USIR-Net** — [USIR-Net: sand-dust image restoration based on unsupervised learning](https://doi.org/10.1007/s00138-024-01528-0)<br>Sand and dust removal; Dehazing; Underwater enhancement | — | — |
| 2023 · Remote Sensing | **D-CycleGAN** — [Unsupervised Image Dedusting via a Cycle-Consistent Generative Adversarial Network](https://doi.org/10.3390/rs15051311)<br>Sand and dust removal; Underwater enhancement; Dehazing | — | — |
| 2023 · TPAMI | **LUD-VAE** — [Learn From Unpaired Data for Image Restoration: A Variational Bayes Approach](https://doi.org/10.1109/TPAMI.2022.3215571)<br>Denoising; Super-resolution; Low-light enhancement | G<br>VAE | [Code](https://github.com/zhengdihan/LUD-VAE) |
| 2023 · J. Vis. Commun. Image Represent. | **MSED** — [Low-light images enhancement and denoising network based on unsupervised learning multi-stream feature modeling](https://doi.org/10.1016/j.jvcir.2023.103932)<br>Low-light enhancement; Denoising | — | — |
| 2023 · Int. J. Intell. Syst. | **SIENet** — [Two-Step Unsupervised Approach for Sand-Dust Image Enhancement](https://doi.org/10.1155/2023/4506331)<br>Sand and dust removal; Underwater enhancement; Dehazing | — | — |
| 2022 · ICPR | **DGP-CycleGAN** — [Unsupervised Restoration of Weather-Affected Images Using Deep Gaussian Process-Based CycleGAN](https://doi.org/10.1109/ICPR56361.2022.9956257)<br>Deraining; Dehazing; Desnowing | D · C<br>GAN | — |
| 2021 · CVPR | **DeFlow** — [DeFlow: Learning Complex Image Degradations from Unpaired Data with Conditional Flows](https://doi.org/10.1109/cvpr46437.2021.00016)<br>Denoising; Super-resolution | G<br>Flow, CNN | — |
| 2019 · arXiv preprint arXiv:1906.05762 | **SCGAN** — [Unsupervised Image Noise Modeling with Self-Consistent GAN](https://arxiv.org/abs/1906.05762)<br>Denoising; Deraining; Super-resolution | — | — |
| 2018 · Lecture Notes in Computer Science | **High-to-Low / Low-to-High GAN** — [To learn image super-resolution, use a GAN to learn how to do image degradation first](https://doi.org/10.1007/978-3-030-01231-1_12)<br>Super-resolution; Face restoration | — | — |

## Super-resolution

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2025 · Signal Process. Image Commun. | **Cycle/diffusion recurrent SR** — [Unsupervised image super-resolution recurrent network based on diffusion model](https://doi.org/10.1016/j.image.2025.117398) | — | — |
| 2025 · JOTA | **OTS** — [An Optimal Transport Perspective on Unpaired Image Super-Resolution](https://doi.org/10.1007/s10957-025-02781-7) | D · C<br>OT, CNN | [Code](https://github.com/milenagazdieva/OT-Super-Resolution) |
| 2025 · arXiv preprint arXiv:2508.07214v1 | **RFDM** — [Unsupervised Real-World Super-Resolution via Rectified Flow Degradation Modelling](https://doi.org/10.48550/arXiv.2508.07214) | — | — |
| 2024 · CVPR | **DictSR** — [Learning Coupled Dictionaries from Unpaired Data for Image Super-Resolution](https://doi.org/10.1109/cvpr52733.2024.02429) | — | — |
| 2024 · TPAMI | **SDFlow** — [Learning Many-to-Many Mapping for Unpaired Real-World Image Super-Resolution and Downscaling](https://doi.org/10.1109/TPAMI.2024.3428546) | D · C · G<br>Flow, GAN | [Code](https://github.com/sunwj/sdflow) |
| 2023 · PR | **Lightweight INN-SR** — [Unpaired image super-resolution using a lightweight invertible neural network](https://doi.org/10.1016/j.patcog.2023.109822) | — | — |
| 2022 · TPAMI | **ADL** — [Toward Real-World Super-Resolution via Adaptive Downsampling Models](https://doi.org/10.1109/TPAMI.2021.3106790) | C · G<br>CNN, GAN | [Code](https://github.com/JaehaKim97/Adaptive-Downsampling-Model) |
| 2022 · IEEE Signal Process. Lett. | **DTSR** — [Unsupervised Real-World Image Super-Resolution via Dual Synthetic-to-Realistic and Realistic-to-Synthetic Translations](https://doi.org/10.1109/lsp.2022.3175411) | — | — |
| 2022 · Proc. Int. Joint Conf. Artif. Intell. | **USR-DU** — [Learning Degradation Uncertainty for Unsupervised Real-World Image Super-Resolution](https://doi.org/10.24963/ijcai.2022/176) | — | — |
| 2021 · CVPR | **DASR (domain-distance aware)** — [Unsupervised Real-World Image Super Resolution via Domain-Distance Aware Training](https://doi.org/10.1109/cvpr46437.2021.01318) | — | [Code](https://github.com/ShuhangGu/DASR) |
| 2021 · Proc. IEEE/CVF Int. Conf. Comput. Vis. Workshops | **Image-statistics SR** — [Simple and Efficient Unpaired Real-World Super-Resolution Using Image Statistics](https://doi.org/10.1109/iccvw54120.2021.00225) | — | — |
| 2021 · ICCV | **USR-DA** — [Unsupervised Real-World Super-Resolution: A Domain Adaptation Perspective](https://openaccess.thecvf.com/content/ICCV2021/html/Wang_Unsupervised_Real-World_Super-Resolution_A_Domain_Adaptation_Perspective_ICCV_2021_paper.html) | — | — |
| 2020 · CVPRW | **CycleGAN + domain discriminator SR** — [Unsupervised Real-World Super Resolution With Cycle Generative Adversarial Network and Domain Discriminator](https://doi.org/10.1109/cvprw50498.2020.00236) | — | — |
| 2020 · CVPR | **Pseudo-supervised SR** — [Unpaired Image Super-Resolution Using Pseudo-Supervision](https://doi.org/10.1109/cvpr42600.2020.00037) | — | — |
| 2020 · CVPRW | **RealSR (Ji et al.)** — [Real-World Super-Resolution via Kernel Estimation and Noise Injection](https://doi.org/10.1109/cvprw50498.2020.00241) | — | [Code](https://github.com/jixiaozhong/RealSR) |
| 2019 · Proc. IEEE/CVF Int. Conf. Comput. Vis. Workshops | **FSSR / DSGAN** — [Frequency Separation for Real-World Super-Resolution](https://doi.org/10.1109/iccvw.2019.00445) | — | — |
| 2019 · Proc. IEEE/CVF Int. Conf. Comput. Vis. Workshops | **Unsupervised degradation learning (Lugmayr et al.)** — [Unsupervised Learning for Real-World Super-Resolution](https://doi.org/10.1109/iccvw.2019.00423) | — | — |
| 2018 · CVPRW | **CinCGAN** — [Unsupervised Image Super-Resolution Using Cycle-in-Cycle Generative Adversarial Networks](https://doi.org/10.1109/cvprw.2018.00113) | — | — |

## Underwater enhancement

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2026 · Journal of Visual Communication and Image Representation | **CMDCL** — [Unpaired underwater image enhancement via Cross-Modal Dual Contrastive Learning](https://doi.org/10.1016/j.jvcir.2026.104839) | — | — |
| 2025 · J. Mar. Sci. Eng. | **MambaRA-GAN** — [MambaRA-GAN: Underwater Image Enhancement via Mamba and Intra-Domain Reconstruction Autoencoder](https://doi.org/10.3390/jmse13091745) | — | — |
| 2025 · Neurocomputing | **Physical-map-guided CycleGAN** — [Transmission map and background light guided enhancement of unpaired underwater image](https://doi.org/10.1016/j.neucom.2024.129270) | — | — |
| 2025 · Buildings | **Physics-constrained UNIT** — [Unsupervised Restoration of Underwater Structural Crack Images via Physics-Constrained Image Translation and Multi-Scale Feature Retention](https://doi.org/10.3390/buildings15132150) | — | — |
| 2025 · Opt. Lasers Eng. | **UCL-Diff** — [Underwater optical image enhancement via an unsupervised contrastive learning-guided diffusion model](https://doi.org/10.1016/j.optlaseng.2025.109144) | — | — |
| 2024 · IEEE Transactions on Geoscience and Remote Sensing | **DRDCL** — [Unsupervised Underwater Image Enhancement Based on Disentangled Representations via Double-Order Contrastive Loss](https://doi.org/10.1109/TGRS.2024.3353371) | — | — |
| 2024 · Frontiers in Marine Science | **Edge-extraction GAN** — [An unsupervised underwater image enhancement method based on generative adversarial networks with edge extraction](https://doi.org/10.3389/fmars.2024.1471014) | — | — |
| 2024 · IEEE Transactions on Multimedia | **PDD-Net** — [Perception-Driven Deep Underwater Image Enhancement Without Paired Supervision](https://doi.org/10.1109/TMM.2023.3327613) | — | — |
| 2024 · IEEE Journal of Oceanic Engineering | **UMRD** — [Unsupervised Multiple Representation Disentanglement Framework for Improved Underwater Visual Perception](https://doi.org/10.1109/JOE.2023.3317903) | — | — |
| 2023 · Signal Process. Image Commun. | **CDGAN** — [Cross-domain learning for underwater image enhancement](https://doi.org/10.1016/j.image.2022.116890) | — | — |
| 2023 · Displays | **RCA-CycleGAN** — [RCA-CycleGAN: Unsupervised underwater image enhancement using Red Channel attention optimized CycleGAN](https://doi.org/10.1016/j.displa.2022.102359) | — | — |
| 2023 · J. Mar. Sci. Eng. | **UMGAN** — [UMGAN: Underwater Image Enhancement Network for Unpaired Image-to-Image Translation](https://doi.org/10.3390/jmse11020447) | — | — |
| 2023 · Eng. Appl. Artif. Intell. | **URD-UIE** — [Unsupervised underwater image enhancement via content-style representation disentanglement](https://doi.org/10.1016/j.engappai.2023.106866) | — | — |
| 2022 · Remote Sensing | **CWR** — [Underwater Image Restoration via Contrastive Learning and a Real-World Dataset](https://doi.org/10.3390/rs14174297) | — | [Code](https://github.com/JunlinHan/CWR) |
| 2022 · TIP | **TACL** — [Twin Adversarial Contrastive Learning for Underwater Image Enhancement and Beyond](https://doi.org/10.1109/tip.2022.3190209) | — | [Code](https://github.com/Jzy2017/TACL) |
| 2022 · Information | **UW-CycleGAN** — [Unpaired Underwater Image Enhancement Based on CycleGAN](https://doi.org/10.3390/info13010001) | — | — |
| 2020 · RA-L | **FUnIE-GAN-UP** — [Fast Underwater Image Enhancement for Improved Visual Perception](https://doi.org/10.1109/LRA.2020.2974710) | — | [Code](https://github.com/xahidbuffon/FUnIE-GAN) |
| 2020 · Int. J. Control Autom. Syst. | **Underwater image-to-image dehazing** — [Underwater Image Dehazing via Unpaired Image-to-image Translation](https://doi.org/10.1007/s12555-019-0689-x) | — | — |
| 2019 · Optics and Laser Technology | **MCycleGAN** — [Multi-scale adversarial network for underwater image restoration](https://doi.org/10.1016/j.optlastec.2018.05.048) | — | — |
| 2018 · IEEE International Conference on Robotics and Automation | **UGAN** — [Enhancing Underwater Imagery Using Generative Adversarial Networks](https://doi.org/10.1109/ICRA.2018.8460552) | — | [Code](https://github.com/cameronfabbri/Underwater-Color-Correction) |
| 2018 · IEEE Signal Process. Lett. | **Underwater color transfer** — [Emerging From Water: Underwater Image Color Correction Based on Weakly Supervised Color Transfer](https://doi.org/10.1109/LSP.2018.2792050) | — | — |
| 2018 · RA-L | **WaterGAN** — [WaterGAN: Unsupervised Generative Network to Enable Real-time Color Correction of Monocular Underwater Images](https://doi.org/10.1109/LRA.2017.2730363) | — | — |

## Other restoration settings

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2022 · IEEE Access | **USDR-Net** — [Restoration of Single Sand-Dust Image Based on Style Transformation and Unsupervised Adversarial Learning](https://doi.org/10.1109/ACCESS.2022.3200163) | — | — |

## Image and weather translation

| Year / venue | Method and paper | Mechanisms / implementation | Resources |
|---|---|---|---|
| 2026 · TMM | **N2D3** — [Night-to-Day Translation via Illumination Degradation Disentanglement](https://doi.org/10.1109/TMM.2026.3700823) | — | — |
| 2026 · AAAI | **Target-class hallucination suppression** — [Bridging Day and Night: Target-Class Hallucination Suppression in Unpaired Image Translation](https://doi.org/10.1609/aaai.v40i8.37570) | — | — |
| 2024 · arXiv | **CycleGAN-Turbo / img2img-Turbo** — [One-Step Image Translation with Text-to-Image Models](https://arxiv.org/abs/2403.12036) | D · C · P<br>Diffusion, GAN | [Code](https://github.com/GaParmar/img2img-turbo) |
| 2024 · WACV | **TPSeNCE** — [TPSeNCE: Towards Artifact-Free Realistic Rain Generation for Deraining and Object Detection in Rain](https://openaccess.thecvf.com/content/WACV2024/html/Zheng_TPSeNCE_Towards_Artifact-Free_Realistic_Rain_Generation_for_Deraining_and_Object_WACV_2024_paper.html) | — | — |
| 2024 · ICLR | **UNSB** — [Unpaired Image-to-Image Translation via Neural Schrodinger Bridge](https://openreview.net/pdf/b459d0affc066174db8fd5688cf6947ccc2d23f5.pdf) | D · C<br>Diffusion, SB | — |
| 2023 · CVPRW | **N2D-LPNet** — [Learning To See in Nighttime Driving Scenes With Inter-Frequency Priors](https://openaccess.thecvf.com/content/CVPR2023W/UG2/html/Fan_Learning_To_See_in_Nighttime_Driving_Scenes_With_Inter-Frequency_Priors_CVPRW_2023_paper.html) | — | — |
| 2023 · WACV | **UVCGAN** — [UVCGAN: UNet Vision Transformer Cycle-Consistent GAN for Unpaired Image-to-Image Translation](https://doi.org/10.1109/wacv56688.2023.00077) | — | [Code](https://github.com/LS4GAN/uvcgan) |
| 2022 · NeurIPS | **EGSDE** — [EGSDE: Unpaired Image-to-Image Translation via Energy-Guided Stochastic Differential Equations](https://doi.org/10.52202/068431-0261) | C · P<br>Diffusion | — |
| 2022 · arXiv preprint arXiv:2203.16015 | **ITTR** — [ITTR: Unpaired Image-to-Image Translation with Transformers](https://arxiv.org/abs/2203.16015) | — | — |
| 2022 · CVPR | **QS-Attn** — [QS-Attn: Query-Selected Attention for Contrastive Learning in I2I Translation](https://doi.org/10.1109/cvpr52688.2022.01775) | — | — |
| 2021 · Proc. Brit. Mach. Vis. Conf. | **AU-GAN** — [Adverse Weather Image Translation with Asymmetric and Uncertainty-aware GAN](https://arxiv.org/abs/2112.04283) | — | [Code](https://github.com/jgkwak95/AU-GAN) |
| 2021 · CVPRW | **DCLGAN** — [Dual Contrastive Learning for Unsupervised Image-to-Image Translation](https://openaccess.thecvf.com/content/CVPR2021W/NTIRE/html/Han_Dual_Contrastive_Learning_for_Unsupervised_Image-to-Image_Translation_CVPRW_2021_paper.html) | — | — |
| 2020 · ECCV | **CUT** — [Contrastive Learning for Unpaired Image-to-Image Translation](https://doi.org/10.1007/978-3-030-58545-7_19) | D · C<br>GAN | — |
| 2020 · ECCV | **ForkGAN** — [ForkGAN: Seeing into the Rainy Night](https://doi.org/10.1007/978-3-030-58580-8_10) | — | — |
| 2020 · ICLR | **U-GAT-IT** — [U-GAT-IT: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation](https://openreview.net/pdf?id=BJlZ5ySKPH) | — | — |
| 2019 · Proc. IEEE Int. Conf. Robot. Autom. | **ToDayGAN** — [Night-to-Day Image Translation for Retrieval-based Localization](https://doi.org/10.1109/ICRA.2019.8794387) | — | [Code](https://github.com/AAnoosheh/ToDayGAN) |
| 2018 · ECCV | **DRIT** — [Diverse Image-to-Image Translation via Disentangled Representations](https://doi.org/10.1007/978-3-030-01246-5_3) | — | — |
| 2018 · ECCV | **MUNIT** — [Multimodal Unsupervised Image-to-Image Translation](https://openaccess.thecvf.com/content_ECCV_2018/html/Xun_Huang_Multimodal_Unsupervised_Image-to-image_ECCV_2018_paper.html) | — | — |
| 2018 · CVPR | **StarGAN** — [StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation](https://doi.org/10.1109/cvpr.2018.00916) | — | — |
| 2017 · ICCV | **CycleGAN** — [Unpaired Image-to-Image Translation Using Cycle-Consistent Adversarial Networks](https://doi.org/10.1109/ICCV.2017.244) | D · C<br>GAN | [Code](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) |
| 2017 · ICML | **DiscoGAN** — [Learning to Discover Cross-Domain Relations with Generative Adversarial Networks](https://proceedings.mlr.press/v70/kim17a.html) | — | [Code](https://github.com/SKTBrain/DiscoGAN) |
| 2017 · ICCV | **DualGAN** — [DualGAN: Unsupervised Dual Learning for Image-to-Image Translation](https://doi.org/10.1109/ICCV.2017.310) | — | — |
| 2017 · NeurIPS | **UNIT** — [Unsupervised Image-to-Image Translation Networks](https://proceedings.neurips.cc/paper/2017/hash/dc6a6489640ca02b0d42dabeb8e46bb7-Abstract.html) | — | — |

## Setting notes

- **BluRef:** unaligned sharp references from similar scenes support training; inference is reference-free.
- **DADn:** electron-microscopy adaptation uses paired synthetic source data and unpaired noisy target data.
- **LDCT flow:** independent low-dose and normal-dose CT collections support degradation synthesis and subsequent restoration training.
- **EMP:** event-assisted deblurring uses auxiliary event measurements.
- **LightenDiffusion:** unpaired low-/normal-light learning follows decomposition pretraining on paired low-quality SICE observations.
- **CycleGAN-Turbo / img2img-Turbo:** the unpaired CycleGAN-Turbo branch uses a pretrained diffusion prior; pix2pix-Turbo is a paired branch.
- **RCOT and DA-RCOT:** the papers describe paired and unpaired variants; the unpaired setting is relevant here.
- **WaterGAN:** in-air RGB–depth pairs support underwater/clean pair synthesis; deployment uses monocular underwater images.
- **UDGNet:** the full model uses adversarial clean-domain guidance; its single-image variant has a different information setting.

Image-translation foundations and domain-specific imaging studies provide related methodological context. Their inclusion does not imply an identical training protocol across all tasks.
