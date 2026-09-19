# Dataset guide

[Back to overview](../README.md)

Training pairing and evaluation pairing are separate choices. References can be directly captured, processed estimates or scene correspondences. Follow the original release terms; this directory does not redistribute data.

<a id="captured-paired-data"></a>

## Captured paired data

| Dataset / primary source | Tasks | Capture and reference regime | Protocol note |
|---|---|---|---|
| [RENOIR](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html) | denoising | captured; paired | Distinguish RAW and processed releases; lower-noise references retain residual noise. |
| [SIDD](https://abdokamel.github.io/sidd/) | denoising | captured; paired | RAW and sRGB are separate tracks; preserve the official scene and device splits. |
| [DND](https://noise.visinf.tu-darmstadt.de/) | denoising | captured; paired | Use the official regions and evaluation protocol; hidden references are not a clean training pool. |
| [DPDD](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel) | deblurring | captured; paired | Specify single-image or dual-pixel input; defocus results are distinct from motion deblurring. |
| [RealBlur](https://github.com/rimchang/RealBlur) | deblurring | captured; paired | Keep RealBlur-J and RealBlur-R separate and follow the stated alignment and intensity protocol. |
| [I-HAZE](https://arxiv.org/abs/1804.05091) | dehazing | controlled physical haze; paired | Haze is physically generated and photographed; this is not digital synthesis or natural fog sampling. |
| [O-HAZE](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Ancuti_O-HAZE_A_Dehazing_CVPR_2018_paper.html) | dehazing | controlled physical haze; paired | Record the benchmark release and split; references are separately captured clear scenes. |
| [NH-HAZE](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ancuti_NH-HAZE_An_Image_Dehazing_Benchmark_With_Non-Homogeneous_Hazy_and_Haze-Free_CVPRW_2020_paper.pdf) | dehazing | controlled physical haze; paired | Spatially nonuniform haze tests a different capture regime from uniform controlled haze. |
| [LOL](https://arxiv.org/abs/1808.04560) | low-light | captured; paired | Identify LOL-v1 or the exact later release; normal-light exposure is a selected target. |
| [LSRW](https://github.com/JianghaiSCU/R2RNet) | low-light | captured; paired | Some outdoor pairs have local offsets; report registration and device subsets. |
| [SICE](https://csjcai.github.io/papers/SICE.pdf) | low-light | captured multiexposure; paired | Keep source exposure sequences disjoint; references involve selected enhancement or fusion outputs. |
| [SPA-Data](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html) | deraining | captured video; paired estimated target | Clean targets use temporal information and semi-automatic construction; avoid source-video leakage. |
| [RealRain-1k](https://arxiv.org/abs/2206.05514) | deraining | captured video; paired estimated target | Keep density subsets and reference construction explicit; SynRain-13k is a separate synthetic dataset. |
| [GT-RAIN](https://github.com/UCLA-VMG/GT-RAIN) | deraining | captured; paired | Rainy and clear captures are temporally separated; identify the release and alignment protocol. |
| [RealSnow](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf) | desnowing | captured video; paired estimated target | Background references derive from static-scene videos; keep source sequences disjoint. |

<a id="synthetic-paired-data"></a>

## Synthetic paired data

| Dataset / primary source | Tasks | Capture and reference regime | Protocol note |
|---|---|---|---|
| [GoPro](https://openaccess.thecvf.com/content_cvpr_2017/html/Nah_Deep_Multi-Scale_Convolutional_CVPR_2017_paper.html) | deblurring | video-integrated blur; paired synthetic degradation | Sharp real frames are integrated to create blur; this is not a captured long exposure. |
| [HIDE](https://openaccess.thecvf.com/content_ICCV_2019/html/Shen_Human-Aware_Motion_Deblurring_ICCV_2019_paper.html) | deblurring | video-derived blur; paired synthetic degradation | Specify subset and use of human-region annotations; preserve the video split. |
| [RESIDE SOTS](https://sites.google.com/view/reside-dehaze-datasets/reside-standard) | dehazing | digital haze synthesis; paired synthetic degradation | Separate indoor and outdoor subsets; synthetic fidelity does not establish natural-fog generalization. |
| [Rain100L and Rain100H](https://openaccess.thecvf.com/content_cvpr_2017/html/Yang_Deep_Joint_Rain_CVPR_2017_paper.html) | deraining | digital rain synthesis; paired synthetic degradation | Keep the light and heavy variants and their release-specific image lists separate. |
| [CSD](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_ALL_Snow_Removed_Single_Image_Desnowing_Algorithm_Using_Hierarchical_Dual-Tree_ICCV_2021_paper.html) | desnowing | digital snow synthesis; paired synthetic degradation | Synthetic flakes and veiling effects are distinct from naturally captured snowfall. |
| [Snow100K synthetic subsets](https://sites.google.com/view/yunfuliu/desnownet) | desnowing | digital snow synthesis; paired synthetic degradation | Identify S/M/L particle-size subsets; do not mix these with the separate realistic collection. |

<a id="unpaired-collections"></a>

## Unpaired collections

| Dataset / primary source | Tasks | Capture and reference regime | Protocol note |
|---|---|---|---|
| [RESIDE URHI](https://sites.google.com/view/reside-dehaze-datasets/reside-v0) | dehazing | captured; unpaired | No aligned clear references; a separate clean training pool must be documented. |
| [RESIDE RTTS](https://sites.google.com/view/reside-dehaze-datasets/reside-v0) | dehazing | captured; unpaired | Object annotations support downstream tests; they are not aligned clean images. |
| [Snow100K realistic snowy collection](https://sites.google.com/view/yunfuliu/desnownet) | desnowing | captured; unpaired | The realistic snowy photographs are separate from the paired synthetic test subsets. |
| [EnlightenGAN low and normal-light pools](https://github.com/VITA-Group/EnlightenGAN) | low-light | captured collections; unpaired | Use the authors' dataset instructions; distinguish independent training pools from paired evaluation benchmarks. |

<a id="scene-correspondence"></a>

## Scene correspondence

| Dataset / primary source | Tasks | Capture and reference regime | Protocol note |
|---|---|---|---|
| [ACDC](https://acdc.vision.ee.ethz.ch/) | dehazing, low-light, deraining, desnowing | captured; scene correspondence | Adverse and normal-condition scenes are not pixel-aligned restoration ground truth. |
