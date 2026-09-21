# Dataset catalog

[Back to overview](../README.md) · [Protocol guide](DATASETS.md)

This catalog has two complementary views: **59 task-specific entries** used in the six-task distribution comparison, and **160 task-specific entries** in the extended six-task inventory. Multi-task releases appear under each relevant task; these totals are not counts of unique dataset releases. The separate [26-entry protocol guide](DATASETS.md) is a curated starting point, not the complete catalog.

**Real/Synth.** describes the degraded-input source. **Real** includes controlled physical capture, such as photographed artificial haze. It does not assert pixel alignment or imply that reference images were obtained without processing. Pairing is recorded separately: scene correspondence, approximate correspondence, unpaired data, and mixed supervision remain distinct.

The 59-entry view aggregates the reported splits for its input/reference counts. The extended inventory preserves source count units and split notation, including frames, clips, groups, and synthetic/real subsets. Counts in different units must not be summed. **NR** means not reported; **N/A** means not applicable. A blank metadata field is shown as an em dash. Each row links to bibliographic metadata; a direct source link is supplied where available. No datasets are redistributed.

| Task | Distribution comparison | Extended inventory | Selected evaluation dataset |
|---|---:|---:|---|
| Denoising | 6 | 18 | [RENOIR](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html) · [ref](#source-anaya2018renoir) |
| Deblurring | 10 | 29 | [DPDD](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel) · [ref](#source-abuolaim2020defocus) |
| Dehazing | 15 | 32 | [LMHaze](https://github.com/wangzrk/LMHaze) · [ref](#source-zhang2024lmhaze) |
| Low-light enhancement | 15 | 35 | [LSRW](https://github.com/JianghaiSCU/R2RNet) · [ref](#source-hai2023r2rnet) |
| Deraining | 9 | 28 | [SPA-Data](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html) · [ref](#source-wang2019spatial) |
| Desnowing | 4 | 18 | [RealSnow](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf) · [ref](#source-zhu2023learning) |

## Six selected evaluation datasets

These six resources cover the selected evaluation tasks. Unpaired training and reference-based evaluation are separate choices: training correspondence can be withheld while held-out references support evaluation. Follow the original release splits, registration rules, input tracks, and reference construction.

| Task | Dataset | Capture / protocol focus |
|---|---|---|
| Denoising | [RENOIR](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html) · [ref](#source-anaya2018renoir) | Real camera noise; distinguish RAW and processed releases and the camera subsets. |
| Defocus deblurring | [DPDD](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel) · [ref](#source-abuolaim2020defocus) | Real defocus blur; distinguish single-image input from the dual-pixel track. |
| Dehazing | [LMHaze](https://github.com/wangzrk/LMHaze) · [ref](#source-zhang2024lmhaze) | Physically generated haze captured in indoor and outdoor scenes at multiple intensities. |
| Low-light enhancement | [LSRW](https://github.com/JianghaiSCU/R2RNet) · [ref](#source-hai2023r2rnet) | Captured low/normal-light pairs; some outdoor pairs contain local offsets. |
| Deraining | [SPA-Data](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html) · [ref](#source-wang2019spatial) | Real rain videos with reference construction using temporal information. |
| Desnowing | [RealSnow](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf) · [ref](#source-zhu2023learning) | Real snowy scenes with reference construction from dedicated capture sequences. |

## Distribution-comparison catalog: 59 entries

Machine-readable file: [datasets_main.csv](../data/datasets_main.csv). All 59 degraded-input sources are classified as Real. Pairing information below is carried separately from the extended inventory where a matching entry exists.

### Denoising: distribution comparison

| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| CC15 · [ref](#source-nam2016holistic) | Real | 15 / 15 | Mixed | Real paired | Camera noise | CVPR 2016 |
| [SIDD](https://abdokamel.github.io/sidd/) · [ref](#source-abdelhamed2018high) | Real | 3,000 / 3,000 | Mixed | Real paired | Smartphone camera/ISP noise | CVPR 2018 |
| [PolyU](https://arxiv.org/abs/1804.02603) · [ref](#source-xu2018real) | Real | 100 / 100 | 512×512 | Real paired | Camera noise | arXiv 2018 |
| [RENOIR](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html) · [ref](#source-anaya2018renoir) | Real | 240 / 240 | Mixed | Real paired | Camera noise | JVCIR 2018 |
| SIDD+ · [ref](#source-abdelhamed2020ntire) | Real | 2,048 / 2,048 | 256×256 | Real paired | Smartphone camera/ISP noise | CVPRW 2020 |
| SenseNoise-500 · [ref](#source-zhang2022idr) | Real | 2,000 / 500 | 3000×4000 | Real paired | Smartphone RAW camera noise | CVPR 2022 |

### Deblurring: distribution comparison

| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [RealBlur-R/J](https://github.com/rimchang/RealBlur) · [ref](#source-rim2020real) | Real | 4,738 / 4,738 | 680×773 | Real paired | Camera motion | ECCV 2020 |
| [RealBlur-Tele](https://github.com/rimchang/RealBlur) · [ref](#source-rim2020real) | Real | 996 / 996 | 950×598 | Real paired | Camera motion, telephoto | ECCV 2020 |
| [DPDD](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel) · [ref](#source-abuolaim2020defocus) | Real | 500 / 500 | 6720×4480 | Real paired | Defocus blur | ECCV 2020 |
| RealDOF · [ref](#source-lee2021iterative) | Real | 50 / 50 | 2376×1586 | Real paired | Defocus blur | CVPR 2021 |
| RSBlur · [ref](#source-rim2022realistic) | Real | 13,358 / 13,358 | 1920×1200 | Real paired | Camera and object motion | ECCV 2022 |
| ReLoBlur · [ref](#source-li2023real) | Real | 2,405 / 2,405 | 2152×1436 | Real paired | Object motion | AAAI 2023 |
| SDD · [ref](#source-li2023learning) | Real | 150 / 150 | 4096×2160 | Real paired, misaligned | Defocus blur | AAAI 2023 |
| iDFD · [ref](#source-nazir2023idfd) | Real | 764 / 764 | NR | Real paired | Defocus blur | SCIA 2023 |
| [LPBlur](https://arxiv.org/abs/2404.13677) · [ref](#source-gong2024dataset) | Real | 10,288 / 10,288 | 224×112 | Real paired | Object motion, license plate | IJCAI 2024 |
| LICAM · [ref](#source-montanaro2025novel) | Real | 400 / 400 | 1024×1024 | Real paired | Low-light motion and noise | ICIP 2025 |

### Dehazing: distribution comparison

| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [I-HAZE](https://arxiv.org/abs/1804.05091) · [ref](#source-ancuti2018haze) | Real | 35 / 35 | 5456×3632 | Real paired | Indoor homogeneous physical haze | ACIVS 2018 |
| [O-HAZE](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Ancuti_O-HAZE_A_Dehazing_CVPR_2018_paper.html) · [ref](#source-ancuti2018ohaze) | Real | 45 / 45 | 5456×3632 | Real paired | Outdoor homogeneous physical haze | CVPRW 2018 |
| Dense-Haze · [ref](#source-ancuti2019dense) | Real | 33 / 33 | 5456×3632 | Real paired | Outdoor dense physical haze | ICIP 2019 |
| [NH-HAZE](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ancuti_NH-HAZE_An_Image_Dehazing_Benchmark_With_Non-Homogeneous_Hazy_and_Haze-Free_CVPRW_2020_paper.pdf) · [ref](#source-ancuti2020nh) | Real | 55 / 55 | 5456×3632 | Real paired | Outdoor non-homogeneous physical haze | CVPRW 2020 |
| BeDDE · [ref](#source-zhao2020dehazing) | Real | 208 / 208 | Mixed | Real paired (multi-temporal) | Outdoor multi-density natural haze | TIP 2020 |
| NH-HAZE2 · [ref](#source-ancuti2021ntire) | Real | 35 / 35 | 1200×1600 | Real paired | Outdoor non-homogeneous physical haze | CVPRW 2021 |
| [ACDC-Fog](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | Real | 1,000 / 1,000 | 1920×1080 | Scene-level paired | Traffic and urban natural fog | ICCV 2021 |
| RW-HAZE · [ref](#source-chen2022rw) | Real | 210 / 210 | 2560×1440 | Real paired (multi-temporal) | Outdoor urban natural haze | ICIP 2022 |
| HD-NH-HAZE · [ref](#source-ancuti2023ntire) | Real | 50 / 50 | 4000×6000 | Real paired | High-resolution non-homogeneous haze | CVPRW 2023 |
| WeatherStream-Fog · [ref](#source-zhang2023weatherstream) | Real | 4,500 / 4,500 | ≥1280×720 | Real paired (multi-temporal) | Outdoor natural fog | CVPR 2023 |
| [LMHaze](https://github.com/wangzrk/LMHaze) · [ref](#source-zhang2024lmhaze) | Real | 5,040 / 5,040 | 1200×800 | Real paired | Indoor and outdoor physical haze | ACM MMAsia 2024 |
| Phone-Hazy · [ref](#source-fan2025non) | Real | 415 / 415 | Mixed | Real paired (non-aligned) | Mobile-captured natural haze | TCSVT 2025 |
| RW²AH · [ref](#source-fang2025guided) | Real | 1,758 / 1,758 | Mixed | Real paired (multi-temporal) | Stationary-camera natural haze | AAAI 2025 |
| WeatherBench-Haze · [ref](#source-guan2025weatherbench) | Real | 13,814 / 13,814 | 512×512 | Real paired | Outdoor day/night physical haze | ACM MM 2025 |
| NT-HAZE · [ref](#source-ancuti2026nt) | Real | 40 / 40 | NR | Real paired | Nighttime physical haze with glow | CVPRW 2026 |

### Low-light enhancement: distribution comparison

| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [SICE](https://csjcai.github.io/papers/SICE.pdf) · [ref](#source-cai2018learning) | Real | 4,413 / 589 | Mixed | Real paired | Multi-exposure, multi-level illumination | TIP 2018 |
| [LOL-v1](https://arxiv.org/abs/1808.04560) · [ref](#source-wei2018deep) | Real | 500 / 500 | 600×400 | Real paired | Global dim | BMVC 2018 |
| Dark Zurich · [ref](#source-sakaridis2019guided) | Real | 5,537 / 3,242 | 1920×1080 | Scene-level paired | Nighttime street, complex illumination | ICCV 2019 |
| LOL-v2-real · [ref](#source-yang2021sparse) | Real | 789 / 789 | 600×400 | Real paired | Global dim | TIP 2021 |
| VE-LOL-L-Cap · [ref](#source-liu2021benchmarking) | Real | 1,500 / 1,500 | 1080×720 | Real paired | Multi-level illumination | IJCV 2021 |
| [ACDC-Night](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | Real | 1,006 / 1,006 | 1920×1080 | Scene-level paired | Outdoor nighttime driving | ICCV 2021 |
| BAID · [ref](#source-lv2022backlitnet) | Real | 3,000 / 3,000 | Mixed | Real paired | Backlit and HDR | CVIU 2022 |
| UHD-LL · [ref](#source-li2023embedding) | Real | 2,150 / 2,150 | 3840×2160 | Real paired | Global dim, varied real-world scenes | ICLR 2023 |
| [LSRW](https://github.com/JianghaiSCU/R2RNet) · [ref](#source-hai2023r2rnet) | Real | 5,650 / 5,650 | 960×720 | Real paired | Global dim, varied real-world scenes | JVCIR 2023 |
| NTIRE-2024-LLIE · [ref](#source-liu2024ntirellie) | Real | 300 / 230 | Mixed | Real paired | Non-uniform and extreme illumination | CVPRW 2024 |
| FoundIR-Lowlight · [ref](#source-li2025foundir) | Real | 40,012 / 40,012 | Mixed | — | Low-light exposure | ICCV 2025 |
| LSD-Paired · [ref](#source-sharif2026illuminating) | Real | 6,425 / 6,425 | Mixed | Real paired | Extreme and varied low light | WACV 2026 |
| LENVIZ · [ref](#source-aithal2026lenviz) | Real | 210,606 / 24,082 | Mixed | Real paired | Multi-exposure, multi-level illumination | WACV 2026 |
| MILL · [ref](#source-pilligua2026evaluating) | Real | 1,000 / 100 | Mixed | Real paired | Controlled multi-level illumination | CVPR Findings 2026 |
| NTIRE-2026-E-LLIE · [ref](#source-yan2026efficientllie) | Real | 500 / 398 | 4032×3024 | Real paired | Extreme and non-uniform illumination | CVPRW 2026 |

### Deraining: distribution comparison

| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [SPA-Data](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html) · [ref](#source-wang2019spatial) | Real | 29,500 / 29,500 | NR | Real paired | Rain streak | CVPR 2019 |
| RainDS-real · [ref](#source-quan2021removing) | Real | 750 / 250 | NR | Real paired | Streak, drop, and mixed rain | CVPR 2021 |
| [ACDC-Rain](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | Real | 1,000 / 1,000 | 1920×1080 | Scene-level paired | Streak and accumulation | ICCV 2021 |
| [GT-RAIN](https://github.com/UCLA-VMG/GT-RAIN) · [ref](#source-ba2022not) | Real | 31,524 / 31,524 | Mixed | Real paired | Streak and accumulation | ECCV 2022 |
| [RealRain-1K](https://arxiv.org/abs/2206.05514) · [ref](#source-li2022toward) | Real | 1,120 / 1,120 | 1512×973 | Real paired | Streak and accumulation | arXiv 2022 |
| WeatherStream-Rain · [ref](#source-zhang2023weatherstream) | Real | NR / NR | NR | Approx. real paired | Streak and rain-fog | CVPR 2023 |
| LHP-Rain · [ref](#source-guo2023sky) | Real | 3,000 / 3,000 | 1920×1080 | Real paired | Streak and accumulation | ICCV 2023 |
| WeatherBench-Rain · [ref](#source-guan2025weatherbench) | Real | 14,929 / 14,929 | 512×512 | Real paired | Rain streak | ACM MM 2025 |
| FoundIR-Rain · [ref](#source-li2025foundir) | Real | 40,000 / 40,000 | NR | Real paired | Rain streak | ICCV 2025 |

### Desnowing: distribution comparison

| Dataset / source | Real/Synth. | Input / reference | Resolution | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [ACDC-Snow](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | Real | 1,000 / 1,000 | NR | Scene-level paired | Falling and accumulated snow | ICCV 2021 |
| [RealSnow](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf) · [ref](#source-zhu2023learning) | Real | 1,890 / 1,890 | NR | Real paired | Falling snow | CVPR 2023 |
| WeatherStream-Snow · [ref](#source-zhang2023weatherstream) | Real | 3,960 / 3,960 | NR | Real paired | Falling snow | CVPR 2023 |
| WeatherBench-Snow · [ref](#source-guan2025weatherbench) | Real | 13,259 / 13,259 | NR | Real paired | Falling snow | ACM MM 2025 |

## Extended inventory: 160 entries

Machine-readable file: [datasets_supplementary.csv](../data/datasets_supplementary.csv). This view also retains video, auxiliary sensing, recognition-oriented, unpaired, and mixed-supervision resources. Inclusion does not make a collection eligible for pixelwise restoration evaluation. The two views retain their original coverage: FoundIR-Lowlight is present in the 59-entry view but not in this 160-entry inventory.

In the tables below, “same domain” concerns scene-domain comparability, not pixel correspondence. RS = rain streaks, RD = raindrops, RA = rain accumulation.

### Denoising: extended inventory

| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| CC15 · [ref](#source-nam2016holistic) | 15 / 15 | Mixed | Yes | Real paired | Camera noise | CVPR 2016 |
| [DND](https://noise.visinf.tu-darmstadt.de/) · [ref](#source-plotz2017benchmarking) | 50 / 50 | Mixed | Yes | Real paired | Camera noise | CVPR 2017 |
| [SIDD](https://abdokamel.github.io/sidd/) · [ref](#source-abdelhamed2018high) | 3,000 / 3,000 | Mixed | Yes | Real paired | Smartphone camera/ISP noise | CVPR 2018 |
| [PolyU](https://arxiv.org/abs/1804.02603) · [ref](#source-xu2018real) | 100 / 100 | 512×512 | Yes | Real paired | Camera noise | arXiv 2018 |
| [RENOIR](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html) · [ref](#source-anaya2018renoir) | 240 / 240 | Mixed | Yes | Real paired | Camera noise | JVCIR 2018 |
| NIND · [ref](#source-brummer2019natural) | 515 / 101 | Mixed | Yes | Real paired | High-ISO camera noise | CVPRW 2019 |
| HighISO · [ref](#source-yue2019high) | 100 / 100 | 512×512 | Yes | Real paired | High-ISO JPEG camera noise | TIP 2019 |
| PMRID · [ref](#source-wang2020practical) | 40 / 40 | 3000×4000 | Yes | Real paired | Mobile RAW camera noise | ECCV 2020 |
| SIDD+ · [ref](#source-abdelhamed2020ntire) | 2,048 / 2,048 | 256×256 | Yes | Real paired | Smartphone camera/ISP noise | CVPRW 2020 |
| RID · [ref](#source-chen2019real) | 200 / 200 | 6000×4000 | Yes | Real paired | Real-world camera noise | TPAMI 2020 |
| SenseNoise-500 · [ref](#source-zhang2022idr) | 2,000 / 500 | 3000×4000 | Yes | Real paired | Smartphone RAW camera noise | CVPR 2022 |
| BVI-Lowlight · [ref](#source-malyugina2023topological) | 31,800 / 40 | 4928×3264 | Yes | Real paired | Low-light ISO camera noise | Signal Process. 2023 |
| [IOCI](https://arxiv.org/abs/2304.08990) · [ref](#source-kong2023comparison) | 848 / 848 | 1024×1024 | Yes | Real paired | Indoor--outdoor camera noise | arXiv 2023 |
| MIDD · [ref](#source-flepp2024real) | 400,000 / 20,000 | Mixed | Yes | Real paired | Mobile RAW camera noise | CVPR 2024 |
| AIM 2025 RAW · [ref](#source-li2025aim) | 400 / 40 | Mixed | Partial | Real mixed | Multi-camera low-light RAW noise | ICCVW 2025 |
| Noise Clinic · [ref](#source-lebrun2015noise) | 12 / 0 | Mixed | N/A | Real unpaired | Mixed or unknown real noise | IPOL 2015 |
| RNI15 · [ref](#source-zhang2018ffdnet) | 15 / 0 | Mixed | N/A | Real unpaired | Camera noise and JPEG compression | TIP 2018 |
| [OTUR Raw ToF](https://doi.org/10.1109/TPAMI.2022.3170155) · [ref](#source-wang2023tpamiotur) | 1,430 / 0 | NR | No | Real unpaired | Raw ToF depth noise | TPAMI 2023 |

### Deblurring: extended inventory

| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [RealBlur-R/J](https://github.com/rimchang/RealBlur) · [ref](#source-rim2020real) | 4,738 / 4,738 | 680×773 | Yes | Real paired | Camera motion | ECCV 2020 |
| [RealBlur-Tele](https://github.com/rimchang/RealBlur) · [ref](#source-rim2020real) | 996 / 996 | 950×598 | Yes | Real paired | Camera motion, telephoto | ECCV 2020 |
| [DPDD](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel) · [ref](#source-abuolaim2020defocus) | 500 / 500 | 6720×4480 | Yes | Real paired | Defocus blur | ECCV 2020 |
| BS-RSCD · [ref](#source-zhong2021towards) | 4,000 / 4,000 | 640×460 | Yes | Real paired | Rolling-shutter motion | CVPR 2021 |
| RealDOF · [ref](#source-lee2021iterative) | 50 / 50 | 2376×1586 | Yes | Real paired | Defocus blur | CVPR 2021 |
| RSBlur · [ref](#source-rim2022realistic) | 13,358 / 13,358 | 1920×1200 | Yes | Real paired | Camera and object motion | ECCV 2022 |
| ReLoBlur · [ref](#source-li2023real) | 2,405 / 2,405 | 2152×1436 | Yes | Real paired | Object motion | AAAI 2023 |
| SDD · [ref](#source-li2023learning) | 150 / 150 | 4096×2160 | Yes | Real paired, misaligned | Defocus blur | AAAI 2023 |
| RB2V-Street · [ref](#source-pham2023hypercut) | 11,053 / 11,053 | NR | Yes | Real paired | Camera and object motion | CVPR 2023 |
| iDFD · [ref](#source-nazir2023idfd) | 764 / 764 | NR | Yes | Real paired | Defocus blur | SCIA 2023 |
| BSD · [ref](#source-zhong2023real) | 33,000 / 33,000 | 640×480 | Yes | Real paired | Camera and object motion | IJCV 2023 |
| MC-Blur-LSD · [ref](#source-zhang2023mc) | 2,800 / 2,800 | ≥3600×2400 | Yes | Real paired | Defocus blur | TCSVT 2024 |
| [LPBlur](https://arxiv.org/abs/2404.13677) · [ref](#source-gong2024dataset) | 10,288 / 10,288 | 224×112 | Yes | Real paired | Object motion, license plate | IJCAI 2024 |
| QPDD · [ref](#source-chen2025quad) | 4,935 / 4,935 | mixed | Yes | Real paired | Defocus blur | CVPR 2025 |
| LICAM · [ref](#source-montanaro2025novel) | 400 / 400 | 1024×1024 | Yes | Real paired | Low-light motion and noise | ICIP 2025 |
| EvRGB-Deblur · [ref](#source-teng2025monochromatic) | 1,000 / 1,000 | 624×840 | Yes | Real paired | Camera and object motion | ICCVW 2025 |
| RSBlur-AIM2025 Extension · [ref](#source-feijoo2025efficient) | 420 / 420 | 1920×1200 | Yes | Real paired | Camera and object motion | ICCVW 2025 |
| RealDefocus · [ref](#source-seizinger2025bokehlicious) | 23,000 / 4,400 | 6000×4000 | Yes | Real paired | Defocus blur | ICCV 2025 |
| Lai Real · [ref](#source-lai2016comparative) | 100 / 0 | mixed | N/A | Real unpaired | Unspecified motion blur | CVPR 2016 |
| RWBI · [ref](#source-zhang2020deblurring) | 3,112 / 0 | mixed | N/A | Real unpaired | Unspecified motion blur | CVPR 2020 |
| Real-LOLBlur · [ref](#source-zhou2022lednet) | 1,354 / 0 | mixed | N/A | Real unpaired | Low-light motion blur | ECCV 2022 |
| [LBLP](https://doi.org/10.1016/j.cviu.2023.103879) · [ref](#source-kim2024afa) | 2,779 / 0 | mixed | N/A | Real unpaired | Motion blur, low-resolution plate | CVIU 2024 |
| MC-Blur-RMBQ · [ref](#source-zhang2023mc) | 10,000 / 0 | mixed | N/A | Real unpaired | Mixed real-world blur | TCSVT 2024 |
| HCBlur-Real · [ref](#source-rim2024deep) | 471 / 0 | 3840×2160 | N/A | Real unpaired | Camera and object motion | SIGGRAPH 2024 |
| PhoneCraft · [ref](#source-pham2024blur2blur) | 12 / 11 | NR | Yes | Real unpaired | Camera and object motion | CVPR 2024 |
| ReBlurSR-Real · [ref](#source-qin2024new) | 2,330 / 0 | mixed | N/A | Real unpaired | Defocus and motion blur, SR | ECCV 2024 |
| GyroBlur-Real · [ref](#source-yang2025gyro) | 117 / 0 | mixed | N/A | Real unpaired | Camera motion | CVPR 2025 |
| HVD · [ref](#source-xu2026selfhvd) | 180 / 0 | NR | N/A | Real unpaired | Handheld camera and object motion | CVPR 2026 |
| GyroVD-Real · [ref](#source-rim2026gyro) | 10,000 / 0 | NR | N/A | Real unpaired | Camera motion | CVPR 2026 |

### Dehazing: extended inventory

| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| CHIC-Static · [ref](#source-el2016color) | 18 / 2 | 6000×4000 | Yes | Real paired | Indoor multi-density physical fog | ICISP 2016 |
| [I-HAZE](https://arxiv.org/abs/1804.05091) · [ref](#source-ancuti2018haze) | 35 / 35 | 5456×3632 | Yes | Real paired | Indoor homogeneous physical haze | ACIVS 2018 |
| [O-HAZE](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Ancuti_O-HAZE_A_Dehazing_CVPR_2018_paper.html) · [ref](#source-ancuti2018ohaze) | 45 / 45 | 5456×3632 | Yes | Real paired | Outdoor homogeneous physical haze | CVPRW 2018 |
| Dense-Haze · [ref](#source-ancuti2019dense) | 33 / 33 | 5456×3632 | Yes | Real paired | Outdoor dense homogeneous physical haze | ICIP 2019 |
| [NH-HAZE](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ancuti_NH-HAZE_An_Image_Dehazing_Benchmark_With_Non-Homogeneous_Hazy_and_Haze-Free_CVPRW_2020_paper.pdf) · [ref](#source-ancuti2020nh) | 55 / 55 | 5456×3632 | Yes | Real paired | Outdoor non-homogeneous physical haze | CVPRW 2020 |
| BeDDE · [ref](#source-zhao2020dehazing) | 208 / 208 | Mixed | Yes | Real paired (multi-temporal) | Outdoor multi-density natural haze | TIP 2020 |
| MRFID · [ref](#source-liu2020image) | 800 / 200 | Mixed | Yes | Real paired (multi-temporal) | Outdoor multi-density natural fog | TIP 2021 |
| NH-HAZE2 · [ref](#source-ancuti2021ntire) | 35 / 35 | 1200×1600 | Yes | Real paired | Outdoor non-homogeneous physical haze | CVPRW 2021 |
| [ACDC-Fog](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | 1,000 / 1,000 | 1920×1080 | Yes | Scene-level paired | Traffic/urban natural fog | ICCV 2021 |
| RW-HAZE · [ref](#source-chen2022rw) | 210 / 210 | 2560×1440 | Yes | Real paired (multi-temporal) | Outdoor urban multi-density natural haze | ICIP 2022 |
| HD-NH-HAZE · [ref](#source-ancuti2023ntire) | 50 / 50 | 4000×6000 | Yes | Real paired | Outdoor high-resolution non-homogeneous physical haze | CVPRW 2023 |
| WeatherStream-Fog (test subset) · [ref](#source-zhang2023weatherstream) | 4,500 / 4,500 | ≥1280×720 | Yes | Real paired (multi-temporal) | Outdoor natural fog/fog-dominant weather | CVPR 2023 |
| DNH-HAZE · [ref](#source-ancuti2024ntire) | 50 / 50 | 4000×6000 | Yes | Real paired | Outdoor dense non-homogeneous physical haze | CVPRW 2024 |
| STEREOFOG · [ref](#source-pollak2024image) | 10,067 / 10,067 | Mixed | Yes | Real paired (non-aligned) | Indoor multi-density physical fog | Optics Express 2024 |
| [LMHaze](https://github.com/wangzrk/LMHaze) · [ref](#source-zhang2024lmhaze) | 5,040 / 5,040 | 1200×800 | Yes | Real paired | Indoor/outdoor multi-intensity physical haze | ACM MMAsia 2024 |
| Phone-Hazy · [ref](#source-fan2025non) | 415 / 415 | Mixed | Yes | Real paired (non-aligned) | Outdoor mobile-captured natural haze | TCSVT 2025 |
| RW²AH · [ref](#source-fang2025guided) | 1,758 / 1,758 | Mixed | Yes | Real paired (multi-temporal) | Outdoor stationary-camera natural haze | AAAI 2025 |
| WeatherBench-Haze · [ref](#source-guan2025weatherbench) | 13,614/ 200 / 13,614/ 200 | 512×512 | Yes | Real paired | Outdoor day/night physical haze | ACM MM 2025 |
| NT-HAZE · [ref](#source-ancuti2026nt) | 40 / 40 | NR | Yes | Real paired | Indoor nighttime physical haze with glow | CVPRW 2026 |
| Fattal collection · [ref](#source-fattal2014dehazing) | 31 / 0 | Mixed | No | Real unpaired | Outdoor mixed-density natural haze | ACM TOG 2014 |
| LIVE Image Defogging · [ref](#source-choi2015referenceless) | 500 / 500 | Mixed | Yes | Real unpaired | Mixed natural fog/haze | TIP 2015 |
| Waterloo IVC-Real · [ref](#source-ma2015dehazing) | 22 / 0 | Mixed | No | Real unpaired | Outdoor mixed-density natural haze | ICIP 2015 |
| Foggy Driving · [ref](#source-sakaridis2018semantic) | 101 / 0 | up to 960×1280 | No | Real unpaired | Traffic/urban natural fog | IJCV 2018 |
| Foggy Zurich · [ref](#source-sakaridis2018model) | 3,808 / 0 | Mixed | No | Real unpaired | Traffic/urban dense natural fog | ECCV 2018 |
| HazyCity · [ref](#source-yang2018towards) | 845 / 1,891 | Mixed | Yes | Real unpaired | Outdoor urban natural haze | AAAI 2018 |
| [RESIDE-RTTS](https://sites.google.com/view/reside-dehaze-datasets/reside-v0) · [ref](#source-li2018benchmarking) | 4,322 / 0 | Mixed | No | Real unpaired | Traffic/urban natural haze | TIP 2019 |
| [RESIDE-URHI](https://sites.google.com/view/reside-dehaze-datasets/reside-v0) · [ref](#source-li2018benchmarking) | 4,807 / 0 | Mixed | No | Real unpaired | Outdoor mixed natural haze | TIP 2019 |
| HazyWater · [ref](#source-zheng2020overwater) | 2,090 / 2,441 | 640×480 | Yes | Real unpaired | Overwater natural haze | ACCV 2020 |
| VHD (real subset) · [ref](#source-li2022physically) | 1,254 / 0 | Mixed | No | Real unpaired | Outdoor varicolored natural haze | CVPR 2022 |
| HUDRS · [ref](#source-juneja2023hudrs) | 522 / 1,050 | 4608×3456 | Yes | Real unpaired | Outdoor roadside natural fog | TVC 2023 |
| IDD-AW-Fog · [ref](#source-shaik2024idd) | 1,500 / 0 | Mixed | No | Real unpaired | Unstructured traffic natural fog | WACV 2024 |
| [Diff-Dehazer training set](https://doi.org/10.1609/aaai.v39i4.32469) · [ref](#source-lan2025aaai) | 6,519 / 11,293 | Mixed | Partial | Real unpaired | Mixed real-world haze | AAAI 2025 |

### Low-light enhancement: extended inventory

| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| Phos · [ref](#source-vonikakis2013biologically) | 60 / 15 | mixed | Yes | Real paired | Multi-exposure; Controlled illumination | MST 2013 |
| [SICE](https://csjcai.github.io/papers/SICE.pdf) · [ref](#source-cai2018learning) | 4,413 / 589 | mixed | Yes | Real paired | Multi-exposure; Multi-level illumination | TIP 2018 |
| [LOL-v1](https://arxiv.org/abs/1808.04560) · [ref](#source-wei2018deep) | 500 / 500 | 600×400 | Yes | Real paired | Global dim | BMVC 2018 |
| Dark Zurich · [ref](#source-sakaridis2019guided) | 5,336+201 / 3,041+201 | 1920×1080 | Yes | Scene-level paired | Nighttime/twilight street; Complex illumination | ICCV 2019 |
| LOL-v2-real · [ref](#source-yang2021sparse) | 789 / 789 | 600×400 | Yes | Real paired | Global dim | TIP 2021 |
| VE-LOL-L-Cap · [ref](#source-liu2021benchmarking) | 1,500 / 1,500 | 1080×720 | Yes | Real paired | Multi-level illumination | IJCV 2021 |
| SDSD · [ref](#source-wang2021seeing) | 150 clips / 150 clips | 1920×1080 | Yes | Real paired | Extreme/photon-limited; Dynamic | ICCV 2021 |
| [ACDC-Night](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | 1,006 / 1,006 | 1920×1080 | Yes | Scene-level paired | Outdoor nighttime driving | ICCV 2021 |
| PNLI · [ref](#source-fu2022legan) | 2,000 / 2,000 | 6720×4480 | Yes | Real paired | Multi-level illumination; Varied real-world | KBS 2022 |
| BAID · [ref](#source-lv2022backlitnet) | 3,000 / 3,000 | mixed | Yes | Real paired | Backlit/HDR | CVIU 2022 |
| UHD-LL · [ref](#source-li2023embedding) | 2,150 / 2,150 | 3840×2160 | Yes | Real paired | Global dim; Varied real-world | ICLR 2023 |
| [LSRW](https://github.com/JianghaiSCU/R2RNet) · [ref](#source-hai2023r2rnet) | 5,650 / 5,650 | 960×720 | Yes | Real paired | Global dim; Varied real-world | JVCIR 2023 |
| DID · [ref](#source-fu2023dancing) | 41,038 frames / 41,038 frames | mixed | Yes | Real paired | Multi-level illumination; Dynamic | ICCV 2023 |
| NTIRE 2024 LLIE · [ref](#source-liu2024ntirellie) | 300 / 230 | mixed | Yes | Real paired | Non-uniform/local; Extreme; Backlit/HDR | CVPRW 2024 |
| [BVI-RLV](https://arxiv.org/abs/2407.03535) · [ref](#source-lin2024bvirlv) | 31,800 frames / 31,800 frames | 1920×1080 | Yes | Real paired | Multi-level illumination; Dynamic | arXiv 2024 |
| NTIRE 2025 LLIE · [ref](#source-liu2025ntirellie) | 295 / 219 | mixed | Yes | Real paired | Non-uniform/local; Extreme; Backlit/HDR | CVPRW 2025 |
| LSD-Paired · [ref](#source-sharif2026illuminating) | 6,425 / 6,425 | mixed | Yes | Real paired | Extreme/photon-limited; Varied real-world | WACV 2026 |
| LENVIZ · [ref](#source-aithal2026lenviz) | 210,606 / 24,082 | mixed | Yes | Real paired | Multi-exposure; Multi-level illumination | WACV 2026 |
| DarkDriving · [ref](#source-wang2026darkdriving) | 9,538 / 9,538 | 2448×2048 | Yes | Real paired | Night driving; Complex illumination | ICRA 2026 |
| MILL · [ref](#source-pilligua2026evaluating) | 1,000 / 100 | mixed | Yes | Real paired | Multi-level illumination; Controlled indoor | CVPR Findings 2026 |
| NTIRE 2026 E-LLIE · [ref](#source-yan2026efficientllie) | 500 / 398 | 4032×3024 | Yes | Real paired | Extreme; Backlit/HDR; Non-uniform/local | CVPRW 2026 |
| NPE · [ref](#source-wang2013naturalness) | 85 / 0 | mixed | N/A | Real unpaired | Non-uniform/local | TIP 2013 |
| DICM · [ref](#source-lee2013contrast) | 69 / 0 | mixed | N/A | Real unpaired | Non-uniform/local | TIP 2013 |
| MEF · [ref](#source-ma2015perceptual) | 17 / 0 | mixed | N/A | Real unpaired | Multi-exposure illumination | TIP 2015 |
| LIME · [ref](#source-guo2016lime) | 10 / 0 | mixed | N/A | Real unpaired | Non-uniform/local | TIP 2017 |
| VV · [ref](#source-vonikakis2018evaluation) | 24 / 0 | mixed | N/A | Real unpaired | Mixed exposure | MTAP 2018 |
| NightOwls · [ref](#source-neumann2018nightowls) | 279,000 frames / 0 | 1024×640 | N/A | Real unpaired | Night driving; Complex illumination | ACCV 2018 |
| [DarkFace](https://arxiv.org/abs/1904.04474) · [ref](#source-yuan2019ug2) | 15,000 / 0 | mixed | N/A | Real unpaired | Extreme/photon-limited; Faces | CVPRW 2019 |
| ExDark · [ref](#source-loh2019getting) | 7,363 / 0 | mixed | N/A | Real unpaired | Varied real-world illumination | CVIU 2019 |
| NightCity · [ref](#source-tan2021nighttime) | 4,297 / 0 | 1024×512 | N/A | Real unpaired | Urban nighttime; Mixed exposure | TIP 2021 |
| VE-LOL-H · [ref](#source-liu2021benchmarking) | 10,940 / 0 | 1080×720 | N/A | Real unpaired | Underexposure; Faces | IJCV 2021 |
| LLIV-Phone · [ref](#source-li2021low) | 45,148 frames / 0 | 1280×720/ 1920×1080 | N/A | Real unpaired | Mobile; Varied real-world illumination | TPAMI 2021 |
| Backlit300 · [ref](#source-liang2023iccv) | 305 / 0 | mixed | N/A | Real unpaired | Backlit/HDR | ICCV 2023 |
| LoLI-Street-RLLT · [ref](#source-islam2024loli) | 1,000 / 0 | mixed | N/A | Real unpaired | Global dim; Street scenes | ACCV 2024 |
| LSD-Unpaired · [ref](#source-sharif2026illuminating) | 2,117 / 0 | mixed | N/A | Real unpaired | Extreme/photon-limited; Varied real-world | WACV 2026 |

### Deraining: extended inventory

| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| Raindrop Dataset · [ref](#source-qian2018attentive) | 1,119 / 1,119 | NR | Yes | Real paired | RD | CVPR 2018 |
| [SPA-Data](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html) · [ref](#source-wang2019spatial) | 28,500/ 1,000 / 28,500/ 1,000 | NR | Yes | Real paired | RS | CVPR 2019 |
| RobotCar-Rainy · [ref](#source-porav2019can) | 4,818 / 4,818 | 1280×960 | Yes | Real paired | RD | ICRA 2019 |
| RainDS-real · [ref](#source-quan2021removing) | 750 / 250 | NR | Yes | Real paired | RS+RD+mix | CVPR 2021 |
| Stereo Waterdrop · [ref](#source-shi2021stereo) | 642/ 89/ 106 / 642/ 89/ 106 | 624×336 | Yes | Real paired | RD | IROS 2021 |
| [ACDC-Rain](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | 400/ 100/ 500 / 400/ 100/ 500 | 1920×1080 | Yes | Scene-level paired | RS+RA | ICCV 2021 |
| DeepRaindrops · [ref](#source-nguyen2022unfairgan) | 30,000/ 751 / 30,000/ 751 | 1920×1080 | Yes | Real paired | RS+RD | ESWA 2022 |
| [GT-RAIN](https://github.com/UCLA-VMG/GT-RAIN) · [ref](#source-ba2022not) | 26,124/ 3,300/ 2,100 / 26,124/ 3,300/ 2,100 | mixed | Yes | Real paired | RS+RA | ECCV 2022 |
| [RealRain-1k](https://arxiv.org/abs/2206.05514) · [ref](#source-li2022toward) | 1,120 / 1,120 | 1512×973 | Yes | Real paired | RS+RA | arXiv 2022 |
| WeatherStream-Rain · [ref](#source-zhang2023weatherstream) | NR / NR | NR | Yes | Approx. real paired | RS+rain-fog | CVPR 2023 |
| LHP-Rain · [ref](#source-guo2023sky) | 3,000 / 3,000 | 1920×1080 | Yes | Real paired | RS+RA | ICCV 2023 |
| Real-Waterdrop Dataset · [ref](#source-li2024dual) | 255 / 255 | NR | Yes | Real paired | RD | TPAMI 2024 |
| Raindrop Clarity · [ref](#source-jin2024raindrop) | 15,186 groups / 15,186 groups | NR | Yes | Real paired | RD | ECCV 2024 |
| WeatherBench-Rain · [ref](#source-guan2025weatherbench) | 14,729/ 200 / 14,729/ 200 | 512×512 | Yes | Real paired | RS | ACM MM 2025 |
| FoundIR-Rain · [ref](#source-li2025foundir) | 39,900/ 100 / 39,900/ 100 | NR | Yes | Real paired | RS | ICCV 2025 |
| FoundIR-Raindrop · [ref](#source-li2025foundir) | 44,828/ 100 / 44,828/ 100 | NR | Yes | Real paired | RD | ICCV 2025 |
| Raw-Rain Stereo · [ref](#source-rothschild2026r) | 48,000/ 9,000/ 6,000 / train/test GT | NR | Yes | Real paired | RS+RD | WACV 2026 |
| SIRR-Data · [ref](#source-wei2019semi) | 147 / 0 | NR | No | Real unpaired | RS | CVPR 2019 |
| RID · [ref](#source-li2019single) | 2,495 / 0 | 1920×990 | No | Real unpaired | RD | CVPR 2019 |
| RIS · [ref](#source-li2019single) | 2,048 / 0 | 640×368 | No | Real unpaired | RA/mist | CVPR 2019 |
| [Real200](https://arxiv.org/abs/2001.08388) · [ref](#source-wei2020semi) | 200 / 0 | NR | No | Real unpaired | RS | arXiv 2020 |
| Real3000 · [ref](#source-liu2021unpaired) | 2,700/ 300 / 0 | NR | No | Real unpaired | RS | ICCV 2021 |
| SSID · [ref](#source-huang2022memory) | 37,600 Syn; 10,000/ 200 Real / 37,600 Syn | NR | Partial | Syn paired + Real unpaired | RS | TPAMI 2023 |
| RE-RAIN · [ref](#source-chen2025towards) | 300 test / 0 | NR | No | Real unpaired | RS | TPAMI 2025 |
| Low-Light-Rainy · [ref](#source-lin2024dual) | 8,200/ 800 Syn; 430 Real / 8,200/ 800 Syn | NR | Partial | Syn paired + Real unpaired | RS+low-light | TCSVT 2025 |
| HQ-NightRain · [ref](#source-guan2026rethinking) | 10,000/ 900/ 300 Syn; 512 Real / 10,000/ 900/ 300 Syn | 1280×720 | Partial | Syn paired + Real unpaired | Night RS+RD | NeurIPS 2025 |
| [RHR1K](https://doi.org/10.1016/j.eswa.2025.131010) · [ref](#source-wen2026eswa) | 1,000 / 0 | NR | No | Real unpaired | RS | ESWA 2026 |
| 4K-RealRain · [ref](#source-chen2026towards) | 320 / 0 | 3840×2160 | No | Real unpaired | RS | TMM 2026 |

### Desnowing: extended inventory

| Dataset / source | Input / reference | Resolution | Same domain | Pairing | Degradation profile | Year / venue |
|---|---|---|---|---|---|---|
| [ACDC-Snow](https://acdc.vision.ee.ethz.ch/) · [ref](#source-sakaridis2021acdc) | 1,000 / 1,000 | NR | Partial | Scene-level paired | Falling + Ground | ICCV 2021 |
| [RealSnow](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf) · [ref](#source-zhu2023learning) | 1,890 / 1,890 | NR | Yes | Real paired | Falling | CVPR 2023 |
| WeatherStream-Snow (test) · [ref](#source-zhang2023weatherstream) | 3,960 / 3,960 | NR | Yes | Real paired | Falling | CVPR 2023 |
| WeatherBench-Snow · [ref](#source-guan2025weatherbench) | 13,259 / 13,259 | NR | Yes | Real paired | Falling | ACM MM 2025 |
| MWD-Snow (RSCM) · [ref](#source-lin2017rscm) | 10,000 / 10,000 | NR | Yes | Real unpaired | Falling + Ground | TIP 2017 |
| Image2Weather-Snow · [ref](#source-chu2017camera) | 1,252 / 70,501 | NR | Yes | Real unpaired | Falling + Ground | JVCIR 2017 |
| [Snow100K-Realistic](https://sites.google.com/view/yunfuliu/desnownet) · [ref](#source-liu2018desnownet) | 1,329 / 0 | NR | N/A | Real unpaired | Falling + Ground | TIP 2018 |
| RFS-Snow · [ref](#source-guerra2018weather) | 1,100 / 0 | NR | N/A | Real unpaired | Falling + Ground | IEEE AHS 2018 |
| SRRS-Real · [ref](#source-chen2020jstasr) | 1,000 / 0 | NR | N/A | Real unpaired | Falling + Veil | ECCV 2020 |
| [DAWN-Snow](https://arxiv.org/abs/2008.05402) · [ref](#source-kenk2020dawn) | 204 / 0 | NR | N/A | Real unpaired | Falling + Ground | arXiv 2020 |
| WEAPD-Snow · [ref](#source-xiao2021classification) | 621 / 0 | NR | N/A | Real unpaired | Falling + Ground | Earth Space Sci. 2021 |
| SnowWorld24 · [ref](#source-cheng2023snow) | 24 / 0 | NR | N/A | Real unpaired | Falling | CVIU 2023 |
| RSOD · [ref](#source-ding2023cf) | 2,100 / 0 | NR | N/A | Real unpaired | Falling + Ground | IEEE T-ITS 2023 |
| [RDSBW-Snow](https://doi.org/10.3390/s23031548) · [ref](#source-yang2023framework) | 4,777 / 2,831 | NR | Yes | Real unpaired | Falling + Ground + Veil | Sensors 2023 |
| RealSnow85 · [ref](#source-wu2024semi) | 85 videos / 0 | NR | N/A | Real unpaired | Falling + Veil | ECCV 2024 |
| SRSD-Real · [ref](#source-wang2024joint) | 2,000 / 0 | NR | N/A | Real unpaired | Falling | IET CV 2024 |
| WReal-Snow · [ref](#source-xu2024towards) | 2,018 / 0 | NR | N/A | Real unpaired | Falling + Ground | ECCV 2024 |
| RealSnow10K · [ref](#source-lai2025snowmaster) | 12,676 / 0 | NR | N/A | Real unpaired | Falling + Ground + Veil | CVPR 2025 |

## Source bibliography

Titles identify the public papers associated with the dataset releases. A missing direct URL is left unfilled rather than inferred from the title.

<a id="source-abdelhamed2018high"></a>

- **abdelhamed2018high** — [A high-quality denoising dataset for smartphone cameras](https://abdokamel.github.io/sidd/).

<a id="source-abdelhamed2020ntire"></a>

- **abdelhamed2020ntire** — Ntire 2020 challenge on real image denoising: Dataset, methods and results.

<a id="source-abuolaim2020defocus"></a>

- **abuolaim2020defocus** — [Defocus deblurring using dual-pixel data](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel).

<a id="source-aithal2026lenviz"></a>

- **aithal2026lenviz** — LENVIZ: A high-resolution low-exposure night vision benchmark dataset.

<a id="source-anaya2018renoir"></a>

- **anaya2018renoir** — [Renoir--a dataset for real low-light image noise reduction](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html).

<a id="source-ancuti2018haze"></a>

- **ancuti2018haze** — [I-HAZE: A dehazing benchmark with real hazy and haze-free indoor images](https://arxiv.org/abs/1804.05091).

<a id="source-ancuti2018ohaze"></a>

- **ancuti2018ohaze** — [O-haze: a dehazing benchmark with real hazy and haze-free outdoor images](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Ancuti_O-HAZE_A_Dehazing_CVPR_2018_paper.html).

<a id="source-ancuti2019dense"></a>

- **ancuti2019dense** — Dense-haze: A benchmark for image dehazing with dense-haze and haze-free images.

<a id="source-ancuti2020nh"></a>

- **ancuti2020nh** — [NH-HAZE: An image dehazing benchmark with non-homogeneous hazy and haze-free images](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ancuti_NH-HAZE_An_Image_Dehazing_Benchmark_With_Non-Homogeneous_Hazy_and_Haze-Free_CVPRW_2020_paper.pdf).

<a id="source-ancuti2021ntire"></a>

- **ancuti2021ntire** — NTIRE 2021 nonhomogeneous dehazing challenge report.

<a id="source-ancuti2023ntire"></a>

- **ancuti2023ntire** — Ntire 2023 hr nonhomogeneous dehazing challenge report.

<a id="source-ancuti2024ntire"></a>

- **ancuti2024ntire** — NTIRE 2024 dense and non-homogeneous dehazing challenge report.

<a id="source-ancuti2026nt"></a>

- **ancuti2026nt** — NT-HAZE: A Benchmark Dataset for Realistic Night-time Image Dehazing.

<a id="source-ba2022not"></a>

- **ba2022not** — [Not just streaks: Towards ground truth for single image deraining](https://github.com/UCLA-VMG/GT-RAIN).

<a id="source-brummer2019natural"></a>

- **brummer2019natural** — Natural image noise dataset.

<a id="source-cai2018learning"></a>

- **cai2018learning** — [Learning a deep single image contrast enhancer from multi-exposure images](https://csjcai.github.io/papers/SICE.pdf).

<a id="source-chen2019real"></a>

- **chen2019real** — Real-world image denoising with deep boosting.

<a id="source-chen2020jstasr"></a>

- **chen2020jstasr** — JSTASR: Joint size and transparency-aware snow removal algorithm based on modified partial convolution and veiling effect removal.

<a id="source-chen2022rw"></a>

- **chen2022rw** — Rw-haze: A real-world benchmark dataset to evaluate quantitatively dehazing algorithms.

<a id="source-chen2025quad"></a>

- **chen2025quad** — Quad-Pixel Image Defocus Deblurring: A New Benchmark and Model.

<a id="source-chen2025towards"></a>

- **chen2025towards** — Towards unified deep image deraining: A survey and a new benchmark.

<a id="source-chen2026towards"></a>

- **chen2026towards** — Towards ultra-high-definition image deraining: A benchmark and an efficient method.

<a id="source-cheng2023snow"></a>

- **cheng2023snow** — Snow mask guided adaptive residual network for image snow removal.

<a id="source-choi2015referenceless"></a>

- **choi2015referenceless** — Referenceless prediction of perceptual fog density and perceptual image defogging.

<a id="source-chu2017camera"></a>

- **chu2017camera** — Camera as weather sensor: Estimating weather information from single images.

<a id="source-ding2023cf"></a>

- **ding2023cf** — Cf-yolo: Cross fusion yolo for object detection in adverse weather with a high-quality real snow dataset.

<a id="source-el2016color"></a>

- **el2016color** — A color image database for haze model and dehazing methods evaluation.

<a id="source-fan2025non"></a>

- **fan2025non** — Non-aligned supervision for real image dehazing.

<a id="source-fang2025guided"></a>

- **fang2025guided** — Guided real image dehazing using ycbcr color space.

<a id="source-fattal2014dehazing"></a>

- **fattal2014dehazing** — Dehazing using color-lines.

<a id="source-feijoo2025efficient"></a>

- **feijoo2025efficient** — Efficient real-world deblurring using single images: AIM 2025 challenge report.

<a id="source-flepp2024real"></a>

- **flepp2024real** — Real-world mobile image denoising dataset with efficient baselines.

<a id="source-fu2022legan"></a>

- **fu2022legan** — LE-GAN: Unsupervised low-light image enhancement network using attention module and identity invariant loss.

<a id="source-fu2023dancing"></a>

- **fu2023dancing** — Dancing in the dark: A benchmark towards general low-light video enhancement.

<a id="source-gong2024dataset"></a>

- **gong2024dataset** — [A dataset and model for realistic license plate deblurring](https://arxiv.org/abs/2404.13677).

<a id="source-guan2025weatherbench"></a>

- **guan2025weatherbench** — Weatherbench: A real-world benchmark dataset for all-in-one adverse weather image restoration.

<a id="source-guan2026rethinking"></a>

- **guan2026rethinking** — Rethinking nighttime image deraining via learnable color space transformation.

<a id="source-guerra2018weather"></a>

- **guerra2018weather** — Weather Classification: A new multi-class dataset, data augmentation approach and comprehensive evaluations of Convolutional Neural Networks.

<a id="source-guo2016lime"></a>

- **guo2016lime** — LIME: Low-light image enhancement via illumination map estimation.

<a id="source-guo2023sky"></a>

- **guo2023sky** — From sky to the ground: A large-scale benchmark and simple baseline towards real rain removal.

<a id="source-hai2023r2rnet"></a>

- **hai2023r2rnet** — [R2rnet: Low-light image enhancement via real-low to real-normal network](https://github.com/JianghaiSCU/R2RNet).

<a id="source-huang2022memory"></a>

- **huang2022memory** — Memory uncertainty learning for real-world single image deraining.

<a id="source-islam2024loli"></a>

- **islam2024loli** — Loli-street: Benchmarking low-light image enhancement and beyond.

<a id="source-jin2024raindrop"></a>

- **jin2024raindrop** — Raindrop clarity: A dual-focused dataset for day and night raindrop removal.

<a id="source-juneja2023hudrs"></a>

- **juneja2023hudrs** — HUDRS: hazy unpaired dataset for road safety.

<a id="source-kenk2020dawn"></a>

- **kenk2020dawn** — [Dawn: vehicle detection in adverse weather nature dataset](https://arxiv.org/abs/2008.05402).

<a id="source-kim2024afa"></a>

- **kim2024afa** — [AFA-Net: Adaptive Feature Attention Network in Image Deblurring and Super-Resolution for Improving License Plate Recognition](https://doi.org/10.1016/j.cviu.2023.103879).

<a id="source-kong2023comparison"></a>

- **kong2023comparison** — [A comparison of image denoising methods](https://arxiv.org/abs/2304.08990).

<a id="source-lai2016comparative"></a>

- **lai2016comparative** — A comparative study for single image blind deblurring.

<a id="source-lai2025snowmaster"></a>

- **lai2025snowmaster** — Snowmaster: Comprehensive real-world image desnowing via mllm with multi-model feedback optimization.

<a id="source-lan2025aaai"></a>

- **Lan2025AAAI** — [Exploiting Diffusion Prior for Real-World Image Dehazing with Unpaired Training](https://doi.org/10.1609/aaai.v39i4.32469).

<a id="source-lebrun2015noise"></a>

- **lebrun2015noise** — The noise clinic: a blind image denoising algorithm.

<a id="source-lee2013contrast"></a>

- **lee2013contrast** — Contrast enhancement based on layered difference representation of 2D histograms.

<a id="source-lee2021iterative"></a>

- **lee2021iterative** — Iterative Filter Adaptive Network for Single Image Defocus Deblurring.

<a id="source-li2018benchmarking"></a>

- **li2018benchmarking** — [Benchmarking single-image dehazing and beyond](https://sites.google.com/view/reside-dehaze-datasets/reside-v0).

<a id="source-li2019single"></a>

- **li2019single** — Single image deraining: A comprehensive benchmark analysis.

<a id="source-li2021low"></a>

- **li2021low** — Low-light image and video enhancement using deep learning: A survey.

<a id="source-li2022physically"></a>

- **li2022physically** — Physically disentangled intra-and inter-domain adaptation for varicolored haze removal.

<a id="source-li2022toward"></a>

- **li2022toward** — [Toward real-world single image deraining: A new benchmark and beyond](https://arxiv.org/abs/2206.05514).

<a id="source-li2023embedding"></a>

- **li2023embedding** — Embedding Fourier for ultra-high-definition low-light image enhancement.

<a id="source-li2023learning"></a>

- **li2023learning** — Learning single image defocus deblurring with misaligned training pairs.

<a id="source-li2023real"></a>

- **li2023real** — Real-world deep local motion deblurring.

<a id="source-li2024dual"></a>

- **li2024dual** — Dual-pixel raindrop removal.

<a id="source-li2025aim"></a>

- **li2025aim** — Aim 2025 challenge on real-world raw image denoising.

<a id="source-li2025foundir"></a>

- **li2025foundir** — Foundir: Unleashing million-scale training data to advance foundation models for image restoration.

<a id="source-liang2023iccv"></a>

- **Liang2023ICCV** — Iterative Prompt Learning for Unsupervised Backlit Image Enhancement.

<a id="source-lin2017rscm"></a>

- **lin2017rscm** — RSCM: Region selection and concurrency model for multi-class weather recognition.

<a id="source-lin2024bvirlv"></a>

- **lin2024bvirlv** — [BVI-RLV: A fully registered dataset and benchmarks for low-light video enhancement](https://arxiv.org/abs/2407.03535).

<a id="source-lin2024dual"></a>

- **lin2024dual** — Dual degradation representation for joint deraining and low-light enhancement in the dark.

<a id="source-liu2018desnownet"></a>

- **liu2018desnownet** — [Desnownet: Context-aware deep network for snow removal](https://sites.google.com/view/yunfuliu/desnownet).

<a id="source-liu2020image"></a>

- **liu2020image** — Image defogging quality assessment: Real-world database and method.

<a id="source-liu2021benchmarking"></a>

- **liu2021benchmarking** — Benchmarking low-light image enhancement and beyond.

<a id="source-liu2021unpaired"></a>

- **liu2021unpaired** — Unpaired learning for deep image deraining with rain direction regularizer.

<a id="source-liu2024ntirellie"></a>

- **liu2024ntirellie** — NTIRE 2024 challenge on low light image enhancement: Methods and results.

<a id="source-liu2025ntirellie"></a>

- **liu2025ntirellie** — NTIRE 2025 challenge on low light image enhancement: Methods and results.

<a id="source-loh2019getting"></a>

- **loh2019getting** — Getting to know low-light images with the exclusively dark dataset.

<a id="source-lv2022backlitnet"></a>

- **lv2022backlitnet** — BacklitNet: A dataset and network for backlit image enhancement.

<a id="source-ma2015dehazing"></a>

- **ma2015dehazing** — Perceptual evaluation of single image dehazing algorithms.

<a id="source-ma2015perceptual"></a>

- **ma2015perceptual** — Perceptual quality assessment for multi-exposure image fusion.

<a id="source-malyugina2023topological"></a>

- **malyugina2023topological** — A topological loss function for image Denoising on a new BVI-lowlight dataset.

<a id="source-montanaro2025novel"></a>

- **montanaro2025novel** — A novel method and dataset for depth-guided image deblurring from smartphone Lidar.

<a id="source-nam2016holistic"></a>

- **nam2016holistic** — A holistic approach to cross-channel image noise modeling and its application to image denoising.

<a id="source-nazir2023idfd"></a>

- **nazir2023idfd** — idfd: A dataset annotated for depth and defocus.

<a id="source-neumann2018nightowls"></a>

- **neumann2018nightowls** — NightOwls: A pedestrians at night dataset.

<a id="source-nguyen2022unfairgan"></a>

- **nguyen2022unfairgan** — UnfairGAN: An enhanced generative adversarial network for raindrop removal from a single image.

<a id="source-pham2023hypercut"></a>

- **pham2023hypercut** — Hypercut: Video sequence from a single blurry image using unsupervised ordering.

<a id="source-pham2024blur2blur"></a>

- **pham2024blur2blur** — Blur2blur: Blur conversion for unsupervised image deblurring on unknown domains.

<a id="source-pilligua2026evaluating"></a>

- **pilligua2026evaluating** — Evaluating low-light image enhancement across multiple intensity levels.

<a id="source-plotz2017benchmarking"></a>

- **plotz2017benchmarking** — [Benchmarking denoising algorithms with real photographs](https://noise.visinf.tu-darmstadt.de/).

<a id="source-pollak2024image"></a>

- **pollak2024image** — Image-to-image machine translation enables computational defogging in real-world images.

<a id="source-porav2019can"></a>

- **porav2019can** — I can see clearly now: Image restoration via de-raining.

<a id="source-qian2018attentive"></a>

- **qian2018attentive** — Attentive generative adversarial network for raindrop removal from a single image.

<a id="source-qin2024new"></a>

- **qin2024new** — A new dataset and framework for real-world blurred images super-resolution.

<a id="source-quan2021removing"></a>

- **quan2021removing** — Removing raindrops and rain streaks in one go.

<a id="source-rim2020real"></a>

- **rim2020real** — [Real-world blur dataset for learning and benchmarking deblurring algorithms](https://github.com/rimchang/RealBlur).

<a id="source-rim2022realistic"></a>

- **rim2022realistic** — Realistic blur synthesis for learning image deblurring.

<a id="source-rim2024deep"></a>

- **rim2024deep** — Deep hybrid camera deblurring for smartphone cameras.

<a id="source-rim2026gyro"></a>

- **rim2026gyro** — Gyro-based Deep Video Deblurring.

<a id="source-rothschild2026r"></a>

- **rothschild2026r** — R 3: Reconstruction, Raw, and Rain: Deraining Directly in the Bayer Domain.

<a id="source-sakaridis2018model"></a>

- **sakaridis2018model** — Model adaptation with synthetic and real data for semantic dense foggy scene understanding.

<a id="source-sakaridis2018semantic"></a>

- **sakaridis2018semantic** — Semantic foggy scene understanding with synthetic data.

<a id="source-sakaridis2019guided"></a>

- **sakaridis2019guided** — Guided curriculum model adaptation and uncertainty-aware evaluation for semantic nighttime image segmentation.

<a id="source-sakaridis2021acdc"></a>

- **sakaridis2021acdc** — [ACDC: The adverse conditions dataset with correspondences for semantic driving scene understanding](https://acdc.vision.ee.ethz.ch/).

<a id="source-seizinger2025bokehlicious"></a>

- **seizinger2025bokehlicious** — Bokehlicious: Photorealistic bokeh rendering with controllable apertures.

<a id="source-shaik2024idd"></a>

- **shaik2024idd** — Idd-aw: A benchmark for safe and robust segmentation of drive scenes in unstructured traffic and adverse weather.

<a id="source-sharif2026illuminating"></a>

- **sharif2026illuminating** — Illuminating darkness: Learning to enhance low-light images in-the-wild.

<a id="source-shi2021stereo"></a>

- **shi2021stereo** — Stereo waterdrop removal with row-wise dilated attention.

<a id="source-tan2021nighttime"></a>

- **tan2021nighttime** — Night-time scene parsing with a large real dataset.

<a id="source-teng2025monochromatic"></a>

- **teng2025monochromatic** — Monochromatic Event Guided Image Deblurring with Event-Triggering-Aware Decomposition.

<a id="source-vonikakis2013biologically"></a>

- **vonikakis2013biologically** — A biologically inspired scale-space for illumination invariant feature detection.

<a id="source-vonikakis2018evaluation"></a>

- **vonikakis2018evaluation** — On the evaluation of illumination compensation algorithms.

<a id="source-wang2013naturalness"></a>

- **wang2013naturalness** — Naturalness preserved enhancement algorithm for non-uniform illumination images.

<a id="source-wang2019spatial"></a>

- **wang2019spatial** — [Spatial attentive single-image deraining with a high quality real rain dataset](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html).

<a id="source-wang2020practical"></a>

- **wang2020practical** — Practical deep raw image denoising on mobile devices.

<a id="source-wang2021seeing"></a>

- **wang2021seeing** — Seeing dynamic scene in the dark: A high-quality video dataset with mechatronic alignment.

<a id="source-wang2023tpamiotur"></a>

- **Wang2023TPAMIOTUR** — [Optimal Transport for Unsupervised Denoising Learning](https://doi.org/10.1109/TPAMI.2022.3170155).

<a id="source-wang2024joint"></a>

- **wang2024joint** — Joint image restoration for object detection in snowy weather.

<a id="source-wang2026darkdriving"></a>

- **wang2026darkdriving** — DarkDriving: A real-world day and night aligned dataset for autonomous driving in the dark environment.

<a id="source-wei2018deep"></a>

- **wei2018deep** — [Deep retinex decomposition for low-light enhancement](https://arxiv.org/abs/1808.04560).

<a id="source-wei2019semi"></a>

- **wei2019semi** — Semi-supervised transfer learning for image rain removal.

<a id="source-wei2020semi"></a>

- **wei2020semi** — [Semi-deraingan: A new semi-supervised single image deraining network](https://arxiv.org/abs/2001.08388).

<a id="source-wen2026eswa"></a>

- **Wen2026ESWA** — [Unpaired Iterative Prompt Learning for Real-World Image Deraining](https://doi.org/10.1016/j.eswa.2025.131010).

<a id="source-wu2024semi"></a>

- **wu2024semi** — Semi-supervised video desnowing network via temporal decoupling experts and distribution-driven contrastive regularization.

<a id="source-xiao2021classification"></a>

- **xiao2021classification** — Classification of weather phenomenon from images by using deep convolutional neural network.

<a id="source-xu2018real"></a>

- **xu2018real** — [Real-world noisy image denoising: A new benchmark](https://arxiv.org/abs/1804.02603).

<a id="source-xu2024towards"></a>

- **xu2024towards** — Towards real-world adverse weather image restoration: Enhancing clearness and semantics with vision-language models.

<a id="source-xu2026selfhvd"></a>

- **xu2026selfhvd** — Selfhvd: Self-supervised handheld video deblurring.

<a id="source-yan2026efficientllie"></a>

- **yan2026efficientllie** — Efficient low light image enhancement: NTIRE 2026 challenge report.

<a id="source-yang2018towards"></a>

- **yang2018towards** — Towards perceptual image dehazing by physics-based disentanglement and adversarial training.

<a id="source-yang2021sparse"></a>

- **yang2021sparse** — Sparse gradient regularized deep retinex network for robust low-light image enhancement.

<a id="source-yang2023framework"></a>

- **yang2023framework** — [Framework for Generation and Removal of Multiple Types of Adverse Weather from Driving Scene Images](https://doi.org/10.3390/s23031548).

<a id="source-yang2025gyro"></a>

- **yang2025gyro** — Gyro-based neural single image deblurring.

<a id="source-yuan2019ug2"></a>

- **yuan2019ug2** — [UG2+ track 2: A collective benchmark effort for evaluating and advancing image understanding in poor visibility environments](https://arxiv.org/abs/1904.04474).

<a id="source-yue2019high"></a>

- **yue2019high** — High iso jpeg image denoising by deep fusion of collaborative and convolutional filtering.

<a id="source-zhang2018ffdnet"></a>

- **zhang2018ffdnet** — FFDNet: Toward a fast and flexible solution for CNN-based image denoising.

<a id="source-zhang2020deblurring"></a>

- **zhang2020deblurring** — Deblurring by realistic blurring.

<a id="source-zhang2022idr"></a>

- **zhang2022idr** — Idr: Self-supervised image denoising via iterative data refinement.

<a id="source-zhang2023mc"></a>

- **zhang2023mc** — MC-Blur: A comprehensive benchmark for image deblurring.

<a id="source-zhang2023weatherstream"></a>

- **zhang2023weatherstream** — Weatherstream: Light transport automation of single image deweathering.

<a id="source-zhang2024lmhaze"></a>

- **zhang2024lmhaze** — [Lmhaze: intensity-aware image dehazing with a large-scale multi-intensity real haze dataset](https://github.com/wangzrk/LMHaze).

<a id="source-zhao2020dehazing"></a>

- **zhao2020dehazing** — Dehazing evaluation: Real-world benchmark datasets, criteria, and baselines.

<a id="source-zheng2020overwater"></a>

- **zheng2020overwater** — Overwater image dehazing via cycle-consistent generative adversarial network.

<a id="source-zhong2021towards"></a>

- **zhong2021towards** — Towards rolling shutter correction and deblurring in dynamic scenes.

<a id="source-zhong2023real"></a>

- **zhong2023real** — Real-world video deblurring: A benchmark dataset and an efficient recurrent neural network.

<a id="source-zhou2022lednet"></a>

- **zhou2022lednet** — Lednet: Joint low-light enhancement and deblurring in the dark.

<a id="source-zhu2023learning"></a>

- **zhu2023learning** — [Learning weather-general and weather-specific features for image restoration under multiple adverse weather conditions](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf).

## Rebuild

The CSV files contain public dataset metadata only. Rebuild this page locally with:

```bash
python scripts/build_dataset_catalog.py
python scripts/build_dataset_catalog.py --check
```
