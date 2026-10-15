# Dataset catalog

[Back to overview](README.md) · [Paper catalog](papers.md)

Resources for six restoration tasks, including controlled capture, natural degradations, independent image domains, and datasets without clean references. Dataset names link to original project pages or primary papers; no dataset files are hosted here.

Paired dataset organization does not require paired training: degraded and clean images may be sampled independently, with held-out pairs used for evaluation. Preserve train–test separation and follow the original release protocol. Real capture does not establish pixel alignment; scene-level, non-aligned, approximate, and absent references are identified below.

Input denotes degraded observations; clean denotes either corresponding targets or independent clean-domain images, according to the stated relationship. Sizes retain the reported units and split notation. Images, crops, frames, clips, exposures, and groups are not interchangeable; NR means not reported and N/A means not applicable. Multi-task releases are listed under each relevant task.

[Denoising](#denoising) · [Deblurring](#deblurring) · [Dehazing](#dehazing) · [Low-light enhancement](#low-light-enhancement) · [Deraining](#deraining) · [Desnowing](#desnowing)

## Denoising

RENOIR provides captured low-light camera noise with corresponding low-noise references. The wider resources cover smartphone and DSLR sensors, RAW and processed images, repeated captures, and noisy images without clean references.

| Dataset / publication | Reference / domain relationship | Degradation / coverage | Reported size | Resolution |
|---|---|---|---|---|
| [CC15](https://doi.org/10.1109/cvpr.2016.186)<br>CVPR 2016 | Real paired | Camera noise | Input: 15<br>Clean: 15 | Mixed |
| [DND](https://noise.visinf.tu-darmstadt.de/)<br>CVPR 2017 | Real paired | Camera noise | Input: 50<br>Clean: 50 | Mixed |
| [SIDD](https://abdokamel.github.io/sidd/)<br>CVPR 2018 | Real paired | Smartphone camera/ISP noise | Input: 3,000<br>Clean: 3,000 | Mixed |
| [PolyU](https://arxiv.org/abs/1804.02603)<br>arXiv 2018 | Real paired | Camera noise | Input: 100<br>Clean: 100 | 512×512 |
| [RENOIR](https://adrianbarburesearch.blogspot.com/p/renoir-dataset.html)<br>JVCIR 2018 | Real paired | Camera noise | Input: 240<br>Clean: 240 | Mixed |
| [NIND](https://doi.org/10.1109/cvprw.2019.00228)<br>CVPRW 2019 | Real paired | High-ISO camera noise | Input: 515<br>Clean: 101 | Mixed |
| [HighISO](https://doi.org/10.1109/tip.2019.2909805)<br>TIP 2019 | Real paired | High-ISO JPEG camera noise | Input: 100<br>Clean: 100 | 512×512 |
| [PMRID](https://doi.org/10.1007/978-3-030-58539-6_1)<br>ECCV 2020 | Real paired | Mobile RAW camera noise | Input: 40<br>Clean: 40 | 3000×4000 |
| [SIDD+](https://doi.org/10.1109/cvprw50498.2020.00256)<br>CVPRW 2020 | Real paired | Smartphone camera/ISP noise | Input: 2,048<br>Clean: 2,048 | 256×256 |
| [RID](https://doi.org/10.1109/tpami.2019.2921548)<br>TPAMI 2020 | Real paired | Real-world camera noise | Input: 200<br>Clean: 200 | 6000×4000 |
| [SenseNoise-500](https://doi.org/10.1109/cvpr52688.2022.00214)<br>CVPR 2022 | Real paired | Smartphone RAW camera noise | Input: 2,000<br>Clean: 500 | 3000×4000 |
| [BVI-Lowlight](https://doi.org/10.1016/j.sigpro.2023.109081)<br>Signal Process. 2023 | Real paired | Low-light ISO camera noise | Input: 31,800<br>Clean: 40 | 4928×3264 |
| [IOCI](https://arxiv.org/abs/2304.08990)<br>arXiv 2023 | Real paired | Indoor–outdoor camera noise | Input: 848<br>Clean: 848 | 1024×1024 |
| [MIDD](https://doi.org/10.1109/cvpr52733.2024.02111)<br>CVPR 2024 | Real paired | Mobile RAW camera noise | Input: 400,000<br>Clean: 20,000 | Mixed |
| [AIM 2025 RAW](https://doi.org/10.1109/iccvw69036.2025.00600)<br>ICCVW 2025 | Real mixed | Multi-camera low-light RAW noise | Input: 400<br>Clean: 40 | Mixed |
| [Noise Clinic](https://doi.org/10.5201/ipol.2015.125)<br>IPOL 2015 | Real unpaired | Mixed or unknown real noise | Input: 12<br>Clean: 0 | Mixed |
| [RNI15](https://doi.org/10.1109/tip.2018.2839891)<br>TIP 2018 | Real unpaired | Camera noise and JPEG compression | Input: 15<br>Clean: 0 | Mixed |
| [OTUR Raw ToF](https://doi.org/10.1109/TPAMI.2022.3170155)<br>TPAMI 2023 | Real unpaired | Raw ToF depth noise | Input: 1,430<br>Clean: 0 | NR |

## Deblurring

DPDD provides captured defocus blur with all-in-focus references and dual-pixel data. Other resources cover motion blur, dynamic scenes, camera motion, and unaligned or reference-free captures; specify whether evaluation uses a single image, multiple frames, or auxiliary sensor inputs.

| Dataset / publication | Reference / domain relationship | Degradation / coverage | Reported size | Resolution |
|---|---|---|---|---|
| [RealBlur-R/J](https://github.com/rimchang/RealBlur)<br>ECCV 2020 | Real paired | Camera motion | Input: 4,738<br>Clean: 4,738 | 680×773 |
| [RealBlur-Tele](https://github.com/rimchang/RealBlur)<br>ECCV 2020 | Real paired | Camera motion, telephoto | Input: 996<br>Clean: 996 | 950×598 |
| [DPDD](https://github.com/Abdullah-Abuolaim/defocus-deblurring-dual-pixel)<br>ECCV 2020 | Real paired | Defocus blur | Input: 500<br>Clean: 500 | 6720×4480 |
| [BS-RSCD](https://doi.org/10.1109/cvpr46437.2021.00910)<br>CVPR 2021 | Real paired | Rolling-shutter motion | Input: 4,000<br>Clean: 4,000 | 640×460 |
| [RealDOF](https://doi.org/10.1109/cvpr46437.2021.00207)<br>CVPR 2021 | Real paired | Defocus blur | Input: 50<br>Clean: 50 | 2376×1586 |
| [RSBlur](https://doi.org/10.1007/978-3-031-20071-7_29)<br>ECCV 2022 | Real paired | Camera and object motion | Input: 13,358<br>Clean: 13,358 | 1920×1200 |
| [ReLoBlur](https://doi.org/10.1609/aaai.v37i1.25215)<br>AAAI 2023 | Real paired | Object motion | Input: 2,405<br>Clean: 2,405 | 2152×1436 |
| [SDD](https://doi.org/10.1609/aaai.v37i2.25235)<br>AAAI 2023 | Real paired, misaligned | Defocus blur | Input: 150<br>Clean: 150 | 4096×2160 |
| [RB2V-Street](https://doi.org/10.1109/cvpr52729.2023.00949)<br>CVPR 2023 | Real paired | Camera and object motion | Input: 11,053<br>Clean: 11,053 | NR |
| [iDFD](https://doi.org/10.1007/978-3-031-31435-3_5)<br>SCIA 2023 | Real paired | Defocus blur | Input: 764<br>Clean: 764 | NR |
| [BSD](https://doi.org/10.1007/s11263-022-01705-6)<br>IJCV 2023 | Real paired | Camera and object motion | Input: 33,000<br>Clean: 33,000 | 640×480 |
| [MC-Blur-LSD](https://doi.org/10.1109/tcsvt.2023.3319330)<br>TCSVT 2024 | Real paired | Defocus blur | Input: 2,800<br>Clean: 2,800 | ≥3600×2400 |
| [LPBlur](https://arxiv.org/abs/2404.13677)<br>IJCAI 2024 | Real paired | Object motion, license plate | Input: 10,288<br>Clean: 10,288 | 224×112 |
| [QPDD](https://doi.org/10.1109/cvpr52734.2025.00536)<br>CVPR 2025 | Real paired | Defocus blur | Input: 4,935<br>Clean: 4,935 | mixed |
| [LICAM](https://doi.org/10.1109/icip55913.2025.11084288)<br>ICIP 2025 | Real paired | Low-light motion and noise | Input: 400<br>Clean: 400 | 1024×1024 |
| [EvRGB-Deblur](https://doi.org/10.1109/iccvw69036.2025.00409)<br>ICCVW 2025 | Real paired | Camera and object motion | Input: 1,000<br>Clean: 1,000 | 624×840 |
| [RSBlur-AIM2025 Extension](https://doi.org/10.1109/iccvw69036.2025.00602)<br>ICCVW 2025 | Real paired | Camera and object motion | Input: 420<br>Clean: 420 | 1920×1200 |
| [RealDefocus](https://doi.org/10.1109/iccv51701.2025.00833)<br>ICCV 2025 | Real paired | Defocus blur | Input: 23,000<br>Clean: 4,400 | 6000×4000 |
| [Lai Real](https://openaccess.thecvf.com/content_cvpr_2016/html/Lai_A_Comparative_Study_CVPR_2016_paper.html)<br>CVPR 2016 | Real unpaired | Unspecified motion blur | Input: 100<br>Clean: 0 | mixed |
| [RWBI](https://doi.org/10.1109/cvpr42600.2020.00281)<br>CVPR 2020 | Real unpaired | Unspecified motion blur | Input: 3,112<br>Clean: 0 | mixed |
| [Real-LOLBlur](https://doi.org/10.1007/978-3-031-20068-7_33)<br>ECCV 2022 | Real unpaired | Low-light motion blur | Input: 1,354<br>Clean: 0 | mixed |
| [LBLP](https://doi.org/10.1016/j.cviu.2023.103879)<br>CVIU 2024 | Real unpaired | Motion blur, low-resolution plate | Input: 2,779<br>Clean: 0 | mixed |
| [MC-Blur-RMBQ](https://doi.org/10.1109/tcsvt.2023.3319330)<br>TCSVT 2024 | Real unpaired | Mixed real-world blur | Input: 10,000<br>Clean: 0 | mixed |
| [HCBlur-Real](https://doi.org/10.1145/3641519.3657507)<br>SIGGRAPH 2024 | Real unpaired | Camera and object motion | Input: 471<br>Clean: 0 | 3840×2160 |
| [PhoneCraft](https://doi.org/10.1109/cvpr52733.2024.00271)<br>CVPR 2024 | Real unpaired | Camera and object motion | Input: 12<br>Clean: 11 | NR |
| [ReBlurSR-Real](https://doi.org/10.1007/978-3-031-73390-1_4)<br>ECCV 2024 | Real unpaired | Defocus and motion blur, SR | Input: 2,330<br>Clean: 0 | mixed |
| [GyroBlur-Real](https://doi.org/10.1109/cvpr52734.2025.02152)<br>CVPR 2025 | Real unpaired | Camera motion | Input: 117<br>Clean: 0 | mixed |
| [HVD](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_SelfHVD_Self-Supervised_Handheld_Video_Deblurring_CVPR_2026_paper.html)<br>CVPR 2026 | Real unpaired | Handheld camera and object motion | Input: 180<br>Clean: 0 | NR |
| [GyroVD-Real](https://openaccess.thecvf.com/content/CVPR2026/html/Rim_Gyro-based_Deep_Video_Deblurring_CVPR_2026_paper.html)<br>CVPR 2026 | Real unpaired | Camera motion | Input: 10,000<br>Clean: 0 | NR |

## Dehazing

LMHaze covers indoor and outdoor scenes with physically generated haze at multiple intensities. Other datasets span controlled haze capture, natural fog, adverse-weather driving, and scene-corresponding clear observations; captured haze does not by itself guarantee pixel alignment.

| Dataset / publication | Reference / domain relationship | Degradation / coverage | Reported size | Resolution |
|---|---|---|---|---|
| [CHIC-Static](https://doi.org/10.1007/978-3-319-33618-3_12)<br>ICISP 2016 | Real paired | Indoor multi-density physical fog | Input: 18<br>Clean: 2 | 6000×4000 |
| [I-HAZE](https://arxiv.org/abs/1804.05091)<br>ACIVS 2018 | Real paired | Indoor homogeneous physical haze | Input: 35<br>Clean: 35 | 5456×3632 |
| [O-HAZE](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Ancuti_O-HAZE_A_Dehazing_CVPR_2018_paper.html)<br>CVPRW 2018 | Real paired | Outdoor homogeneous physical haze | Input: 45<br>Clean: 45 | 5456×3632 |
| [Dense-Haze](https://doi.org/10.1109/icip.2019.8803046)<br>ICIP 2019 | Real paired | Outdoor dense homogeneous physical haze | Input: 33<br>Clean: 33 | 5456×3632 |
| [NH-HAZE](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ancuti_NH-HAZE_An_Image_Dehazing_Benchmark_With_Non-Homogeneous_Hazy_and_Haze-Free_CVPRW_2020_paper.pdf)<br>CVPRW 2020 | Real paired | Outdoor non-homogeneous physical haze | Input: 55<br>Clean: 55 | 5456×3632 |
| [BeDDE](https://doi.org/10.1109/tip.2020.2995264)<br>TIP 2020 | Real paired (multi-temporal) | Outdoor multi-density natural haze | Input: 208<br>Clean: 208 | Mixed |
| [MRFID](https://doi.org/10.1109/tip.2020.3033402)<br>TIP 2021 | Real paired (multi-temporal) | Outdoor multi-density natural fog | Input: 800<br>Clean: 200 | Mixed |
| [NH-HAZE2](https://doi.org/10.1109/cvprw53098.2021.00074)<br>CVPRW 2021 | Real paired | Outdoor non-homogeneous physical haze | Input: 35<br>Clean: 35 | 1200×1600 |
| [ACDC-Fog](https://acdc.vision.ee.ethz.ch/)<br>ICCV 2021 | Scene-level paired | Traffic/urban natural fog | Input: 1,000<br>Clean: 1,000 | 1920×1080 |
| [RW-HAZE](https://doi.org/10.1109/icip46576.2022.9897706)<br>ICIP 2022 | Real paired (multi-temporal) | Outdoor urban multi-density natural haze | Input: 210<br>Clean: 210 | 2560×1440 |
| [HD-NH-HAZE](https://doi.org/10.1109/cvprw59228.2023.00180)<br>CVPRW 2023 | Real paired | Outdoor high-resolution non-homogeneous physical haze | Input: 50<br>Clean: 50 | 4000×6000 |
| [WeatherStream-Fog (test subset)](https://doi.org/10.1109/cvpr52729.2023.01297)<br>CVPR 2023 | Real paired (multi-temporal) | Outdoor natural fog/fog-dominant weather | Input: 4,500<br>Clean: 4,500 | ≥1280×720 |
| [DNH-HAZE](https://doi.org/10.1109/cvprw63382.2024.00646)<br>CVPRW 2024 | Real paired | Outdoor dense non-homogeneous physical haze | Input: 50<br>Clean: 50 | 4000×6000 |
| [STEREOFOG](https://doi.org/10.1364/oe.532576)<br>Optics Express 2024 | Real paired (non-aligned) | Indoor multi-density physical fog | Input: 10,067<br>Clean: 10,067 | Mixed |
| [LMHaze](https://github.com/wangzrk/LMHaze)<br>ACM MMAsia 2024 | Real paired | Indoor/outdoor multi-intensity physical haze | Input: 5,040<br>Clean: 5,040 | 1200×800 |
| [Phone-Hazy](https://doi.org/10.1109/tcsvt.2025.3573040)<br>TCSVT 2025 | Real paired (non-aligned) | Outdoor mobile-captured natural haze | Input: 415<br>Clean: 415 | Mixed |
| [RW²AH](https://doi.org/10.1609/aaai.v39i3.32297)<br>AAAI 2025 | Real paired (multi-temporal) | Outdoor stationary-camera natural haze | Input: 1,758<br>Clean: 1,758 | Mixed |
| [WeatherBench-Haze](https://doi.org/10.1145/3746027.3758196)<br>ACM MM 2025 | Real paired | Outdoor day/night physical haze | Input: 13,614/ 200<br>Clean: 13,614/ 200 | 512×512 |
| [NT-HAZE](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Ancuti_NT-HAZE_A_Benchmark_Dataset_for_Realistic_Night-time_Image_Dehazing_CVPRW_2026_paper.html)<br>CVPRW 2026 | Real paired | Indoor nighttime physical haze with glow | Input: 40<br>Clean: 40 | NR |
| [Fattal collection](https://doi.org/10.1145/2651362)<br>ACM TOG 2014 | Real unpaired | Outdoor mixed-density natural haze | Input: 31<br>Clean: 0 | Mixed |
| [LIVE Image Defogging](https://doi.org/10.1109/tip.2015.2456502)<br>TIP 2015 | Real unpaired | Mixed natural fog/haze | Input: 500<br>Clean: 500 | Mixed |
| [Waterloo IVC-Real](https://doi.org/10.1109/icip.2015.7351475)<br>ICIP 2015 | Real unpaired | Outdoor mixed-density natural haze | Input: 22<br>Clean: 0 | Mixed |
| [Foggy Driving](https://doi.org/10.1007/s11263-018-1072-8)<br>IJCV 2018 | Real unpaired | Traffic/urban natural fog | Input: 101<br>Clean: 0 | up to 960×1280 |
| [Foggy Zurich](https://doi.org/10.1007/978-3-030-01261-8_42)<br>ECCV 2018 | Real unpaired | Traffic/urban dense natural fog | Input: 3,808<br>Clean: 0 | Mixed |
| [HazyCity](https://doi.org/10.1609/aaai.v32i1.12317)<br>AAAI 2018 | Real unpaired | Outdoor urban natural haze | Input: 845<br>Clean: 1,891 | Mixed |
| [RESIDE-RTTS](https://sites.google.com/view/reside-dehaze-datasets/reside-v0)<br>TIP 2019 | Real unpaired | Traffic/urban natural haze | Input: 4,322<br>Clean: 0 | Mixed |
| [RESIDE-URHI](https://sites.google.com/view/reside-dehaze-datasets/reside-v0)<br>TIP 2019 | Real unpaired | Outdoor mixed natural haze | Input: 4,807<br>Clean: 0 | Mixed |
| [HazyWater](https://doi.org/10.3390/electronics9111877)<br>Electronics 2020 | Real unpaired | Overwater natural haze | Input: 2,090<br>Clean: 2,441 | 640×480 |
| [VHD (real subset)](https://doi.org/10.1109/cvpr52688.2022.00575)<br>CVPR 2022 | Real unpaired | Outdoor varicolored natural haze | Input: 1,254<br>Clean: 0 | Mixed |
| [HUDRS](https://doi.org/10.1007/s00371-022-02534-x)<br>TVC 2023 | Real unpaired | Outdoor roadside natural fog | Input: 522<br>Clean: 1,050 | 4608×3456 |
| [IDD-AW-Fog](https://doi.org/10.1109/wacv57701.2024.00455)<br>WACV 2024 | Real unpaired | Unstructured traffic natural fog | Input: 1,500<br>Clean: 0 | Mixed |
| [Diff-Dehazer training set](https://doi.org/10.1609/aaai.v39i4.32469)<br>AAAI 2025 | Real unpaired | Mixed real-world haze | Input: 6,519<br>Clean: 11,293 | Mixed |

## Low-light enhancement

LSRW provides low-/normal-light pairs from a DSLR camera and a smartphone across indoor and outdoor scenes. The broader resources include multi-exposure scenes, backlighting, nighttime driving, videos, and low-light images without normal-light references.

| Dataset / publication | Reference / domain relationship | Degradation / coverage | Reported size | Resolution |
|---|---|---|---|---|
| [Phos](https://doi.org/10.1088/0957-0233/24/7/074024)<br>MST 2013 | Real paired | Multi-exposure; Controlled illumination | Input: 60<br>Clean: 15 | mixed |
| [SICE](https://csjcai.github.io/papers/SICE.pdf)<br>TIP 2018 | Real paired | Multi-exposure; Multi-level illumination | Input: 4,413<br>Clean: 589 | mixed |
| [LOL-v1](https://arxiv.org/abs/1808.04560)<br>BMVC 2018 | Real paired | Global dim | Input: 500<br>Clean: 500 | 600×400 |
| [Dark Zurich](https://doi.org/10.1109/iccv.2019.00747)<br>ICCV 2019 | Scene-level paired | Nighttime/twilight street; Complex illumination | Input: 5,336+201<br>Clean: 3,041+201 | 1920×1080 |
| [LOL-v2-real](https://doi.org/10.1109/tip.2021.3050850)<br>TIP 2021 | Real paired | Global dim | Input: 789<br>Clean: 789 | 600×400 |
| [VE-LOL-L-Cap](https://doi.org/10.1007/s11263-020-01418-8)<br>IJCV 2021 | Real paired | Multi-level illumination | Input: 1,500<br>Clean: 1,500 | 1080×720 |
| [SDSD](https://doi.org/10.1109/iccv48922.2021.00956)<br>ICCV 2021 | Real paired | Extreme/photon-limited; Dynamic | Input: 150 clips<br>Clean: 150 clips | 1920×1080 |
| [ACDC-Night](https://acdc.vision.ee.ethz.ch/)<br>ICCV 2021 | Scene-level paired | Outdoor nighttime driving | Input: 1,006<br>Clean: 1,006 | 1920×1080 |
| [PNLI](https://doi.org/10.1016/j.knosys.2021.108010)<br>KBS 2022 | Real paired | Multi-level illumination; Varied real-world | Input: 2,000<br>Clean: 2,000 | 6720×4480 |
| [BAID](https://doi.org/10.1016/j.cviu.2022.103403)<br>CVIU 2022 | Real paired | Backlit/HDR | Input: 3,000<br>Clean: 3,000 | mixed |
| [UHD-LL](https://arxiv.org/abs/2302.11831)<br>ICLR 2023 | Real paired | Global dim; Varied real-world | Input: 2,150<br>Clean: 2,150 | 3840×2160 |
| [LSRW](https://github.com/JianghaiSCU/R2RNet)<br>JVCIR 2023 | Real paired | Global dim; Varied real-world | Input: 5,650<br>Clean: 5,650 | 960×720 |
| [DID](https://doi.org/10.1109/iccv51070.2023.01183)<br>ICCV 2023 | Real paired | Multi-level illumination; Dynamic | Input: 41,038 frames<br>Clean: 41,038 frames | mixed |
| [NTIRE 2024 LLIE](https://doi.org/10.1109/cvprw63382.2024.00655)<br>CVPRW 2024 | Real paired | Non-uniform/local; Extreme; Backlit/HDR | Input: 300<br>Clean: 230 | mixed |
| [BVI-RLV](https://arxiv.org/abs/2407.03535)<br>arXiv 2024 | Real paired | Multi-level illumination; Dynamic | Input: 31,800 frames<br>Clean: 31,800 frames | 1920×1080 |
| [NTIRE 2025 LLIE](https://doi.org/10.1109/cvprw67362.2025.00114)<br>CVPRW 2025 | Real paired | Non-uniform/local; Extreme; Backlit/HDR | Input: 295<br>Clean: 219 | mixed |
| [LSD-Paired](https://doi.org/10.1109/wacv61042.2026.00224)<br>WACV 2026 | Real paired | Extreme/photon-limited; Varied real-world | Input: 6,425<br>Clean: 6,425 | mixed |
| [LENVIZ](https://doi.org/10.1109/wacv61042.2026.00249)<br>WACV 2026 | Real paired | Multi-exposure; Multi-level illumination | Input: 210,606<br>Clean: 24,082 | mixed |
| [DarkDriving](https://doi.org/10.1109/icra57385.2026.11695948)<br>ICRA 2026 | Real paired | Night driving; Complex illumination | Input: 9,538<br>Clean: 9,538 | 2448×2048 |
| [MILL](https://openaccess.thecvf.com/content/CVPR2026F/html/Pilligua_Evaluating_Low-Light_Image_Enhancement_Across_Multiple_Intensity_Levels_CVPRF_2026_paper.html)<br>CVPR Findings 2026 | Real paired | Multi-level illumination; Controlled indoor | Input: 1,000<br>Clean: 100 | mixed |
| [NTIRE 2026 E-LLIE](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Yan_NTIRE_2026_Challenge_on_Efficient_Low_Light_Image_Enhancement_Methods_CVPRW_2026_paper.html)<br>CVPRW 2026 | Real paired | Extreme; Backlit/HDR; Non-uniform/local | Input: 500<br>Clean: 398 | 4032×3024 |
| [NPE](https://doi.org/10.1109/tip.2013.2261309)<br>TIP 2013 | Real unpaired | Non-uniform/local | Input: 85<br>Clean: 0 | mixed |
| [DICM](https://doi.org/10.1109/tip.2013.2284059)<br>TIP 2013 | Real unpaired | Non-uniform/local | Input: 69<br>Clean: 0 | mixed |
| [MEF](https://doi.org/10.1109/tip.2015.2442920)<br>TIP 2015 | Real unpaired | Multi-exposure illumination | Input: 17<br>Clean: 0 | mixed |
| [LIME](https://doi.org/10.1109/tip.2016.2639450)<br>TIP 2017 | Real unpaired | Non-uniform/local | Input: 10<br>Clean: 0 | mixed |
| [VV](https://doi.org/10.1007/s11042-017-4783-x)<br>MTAP 2018 | Real unpaired | Mixed exposure | Input: 24<br>Clean: 0 | mixed |
| [NightOwls](https://doi.org/10.1007/978-3-030-20887-5_43)<br>ACCV 2018 | Real unpaired | Night driving; Complex illumination | Input: 279,000 frames<br>Clean: 0 | 1024×640 |
| [DarkFace](https://arxiv.org/abs/1904.04474)<br>CVPRW 2019 | Real unpaired | Extreme/photon-limited; Faces | Input: 15,000<br>Clean: 0 | mixed |
| [ExDark](https://doi.org/10.1016/j.cviu.2018.10.010)<br>CVIU 2019 | Real unpaired | Varied real-world illumination | Input: 7,363<br>Clean: 0 | mixed |
| [NightCity](https://doi.org/10.1109/tip.2021.3122004)<br>TIP 2021 | Real unpaired | Urban nighttime; Mixed exposure | Input: 4,297<br>Clean: 0 | 1024×512 |
| [VE-LOL-H](https://doi.org/10.1007/s11263-020-01418-8)<br>IJCV 2021 | Real unpaired | Underexposure; Faces | Input: 10,940<br>Clean: 0 | 1080×720 |
| [LLIV-Phone](https://doi.org/10.1109/tpami.2021.3126387)<br>TPAMI 2022 | Real unpaired | Mobile; Varied real-world illumination | Input: 45,148 frames<br>Clean: 0 | 1280×720/ 1920×1080 |
| [Backlit300](https://doi.org/10.1109/iccv51070.2023.00743)<br>ICCV 2023 | Real unpaired | Backlit/HDR | Input: 305<br>Clean: 0 | mixed |
| [LoLI-Street-RLLT](https://doi.org/10.1007/978-981-96-0917-8_20)<br>ACCV 2024 | Real unpaired | Global dim; Street scenes | Input: 1,000<br>Clean: 0 | mixed |
| [LSD-Unpaired](https://doi.org/10.1109/wacv61042.2026.00224)<br>WACV 2026 | Real unpaired | Extreme/photon-limited; Varied real-world | Input: 2,117<br>Clean: 0 | mixed |
| [FoundIR-Lowlight](https://doi.org/10.1109/iccv51701.2025.01173)<br>ICCV 2025 | Not specified | Low-light exposure | Input: 40,012<br>Clean: 40,012 | Mixed |

## Deraining

SPA-Data contains real rain-streak images and references constructed from videos. Other resources cover rain streaks, adherent drops, rainy driving, mixed weather, and independent rainy/clear collections, whose reference-construction procedures differ.

| Dataset / publication | Reference / domain relationship | Degradation / coverage | Reported size | Resolution |
|---|---|---|---|---|
| [Raindrop Dataset](https://doi.org/10.1109/cvpr.2018.00263)<br>CVPR 2018 | Real paired | Raindrops | Input: 1,119<br>Clean: 1,119 | NR |
| [SPA-Data](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Spatial_Attentive_Single-Image_Deraining_With_a_High_Quality_Real_Rain_CVPR_2019_paper.html)<br>CVPR 2019 | Real paired | Rain streaks | Input: 28,500/ 1,000<br>Clean: 28,500/ 1,000 | NR |
| [RobotCar-Rainy](https://doi.org/10.1109/icra.2019.8793486)<br>ICRA 2019 | Real paired | Raindrops | Input: 4,818<br>Clean: 4,818 | 1280×960 |
| [RainDS-real](https://doi.org/10.1109/cvpr46437.2021.00903)<br>CVPR 2021 | Real paired | Rain streaks+Raindrops+mix | Input: 750<br>Clean: 250 | NR |
| [Stereo Waterdrop](https://doi.org/10.1109/iros51168.2021.9636216)<br>IROS 2021 | Real paired | Raindrops | Input: 642/ 89/ 106<br>Clean: 642/ 89/ 106 | 624×336 |
| [ACDC-Rain](https://acdc.vision.ee.ethz.ch/)<br>ICCV 2021 | Scene-level paired | Rain streaks+Rain accumulation | Input: 400/ 100/ 500<br>Clean: 400/ 100/ 500 | 1920×1080 |
| [DeepRaindrops](https://doi.org/10.1016/j.eswa.2022.118232)<br>ESWA 2022 | Real paired | Rain streaks+Raindrops | Input: 30,000/ 751<br>Clean: 30,000/ 751 | 1920×1080 |
| [GT-RAIN](https://github.com/UCLA-VMG/GT-RAIN)<br>ECCV 2022 | Real paired | Rain streaks+Rain accumulation | Input: 26,124/ 3,300/ 2,100<br>Clean: 26,124/ 3,300/ 2,100 | mixed |
| [RealRain-1k](https://arxiv.org/abs/2206.05514)<br>arXiv 2022 | Real paired | Rain streaks+Rain accumulation | Input: 1,120<br>Clean: 1,120 | 1512×973 |
| [WeatherStream-Rain](https://doi.org/10.1109/cvpr52729.2023.01297)<br>CVPR 2023 | Approx. real paired | Rain streaks+rain-fog | Input: NR<br>Clean: NR | NR |
| [LHP-Rain](https://doi.org/10.1109/iccv51070.2023.01111)<br>ICCV 2023 | Real paired | Rain streaks+Rain accumulation | Input: 3,000<br>Clean: 3,000 | 1920×1080 |
| [Real-Waterdrop Dataset](https://doi.org/10.1109/tpami.2024.3442955)<br>TPAMI 2024 | Real paired | Raindrops | Input: 255<br>Clean: 255 | NR |
| [Raindrop Clarity](https://doi.org/10.1007/978-3-031-72658-3_1)<br>ECCV 2024 | Real paired | Raindrops | Input: 15,186 groups<br>Clean: 15,186 groups | NR |
| [WeatherBench-Rain](https://doi.org/10.1145/3746027.3758196)<br>ACM MM 2025 | Real paired | Rain streaks | Input: 14,729/ 200<br>Clean: 14,729/ 200 | 512×512 |
| [FoundIR-Rain](https://doi.org/10.1109/iccv51701.2025.01173)<br>ICCV 2025 | Real paired | Rain streaks | Input: 39,900/ 100<br>Clean: 39,900/ 100 | NR |
| [FoundIR-Raindrop](https://doi.org/10.1109/iccv51701.2025.01173)<br>ICCV 2025 | Real paired | Raindrops | Input: 44,828/ 100<br>Clean: 44,828/ 100 | NR |
| [Raw-Rain Stereo](https://doi.org/10.1109/wacv61042.2026.00515)<br>WACV 2026 | Real paired | Rain streaks+Raindrops | Input: 48,000/ 9,000/ 6,000<br>Clean: train/test GT | NR |
| [SIRR-Data](https://doi.org/10.1109/CVPR.2019.00400)<br>CVPR 2019 | Real unpaired | Rain streaks | Input: 147<br>Clean: 0 | NR |
| [RID](https://doi.org/10.1109/cvpr.2019.00396)<br>CVPR 2019 | Real unpaired | Raindrops | Input: 2,495<br>Clean: 0 | 1920×990 |
| [RIS](https://doi.org/10.1109/cvpr.2019.00396)<br>CVPR 2019 | Real unpaired | Rain accumulation/mist | Input: 2,048<br>Clean: 0 | 640×368 |
| [Real200](https://arxiv.org/abs/2001.08388)<br>arXiv 2020 | Real unpaired | Rain streaks | Input: 200<br>Clean: 0 | NR |
| [Real3000](https://doi.org/10.1109/iccv48922.2021.00471)<br>ICCV 2021 | Real unpaired | Rain streaks | Input: 2,700/ 300<br>Clean: 0 | NR |
| [SSID](https://doi.org/10.1109/TPAMI.2022.3180560)<br>TPAMI 2023 | Synthetic paired + Real unpaired | Rain streaks | Input: 37,600 Synthetic; 10,000/ 200 Real<br>Clean: 37,600 Synthetic | NR |
| [RE-RAIN](https://arxiv.org/abs/2310.03535)<br>TPAMI 2025 | Real unpaired | Rain streaks | Input: 300 test<br>Clean: 0 | NR |
| [Low-Light-Rainy](https://arxiv.org/abs/2305.03997)<br>TCSVT 2025 | Synthetic paired + Real unpaired | Rain streaks+low-light | Input: 8,200/ 800 Synthetic; 430 Real<br>Clean: 8,200/ 800 Synthetic | NR |
| [HQ-NightRain](https://proceedings.nips.cc/paper_files/paper/2025/hash/04b7126c370f175204442098356dc239-Abstract-Conference.html)<br>NeurIPS 2025 | Synthetic paired + Real unpaired | Night Rain streaks+Raindrops | Input: 10,000/ 900/ 300 Synthetic; 512 Real<br>Clean: 10,000/ 900/ 300 Synthetic | 1280×720 |
| [RHR1K](https://doi.org/10.1016/j.eswa.2025.131010)<br>ESWA 2026 | Real unpaired | Rain streaks | Input: 1,000<br>Clean: 0 | NR |
| [4K-RealRain](https://doi.org/10.1109/tmm.2026.3660153)<br>TMM 2026 | Real unpaired | Rain streaks | Input: 320<br>Clean: 0 | 3840×2160 |

## Desnowing

RealSnow constructs snowy/clear samples from videos with static backgrounds. The remaining resources cover varying snowfall, particle scales, driving scenes, and reference-free photographs; scene-level clear observations and pixel-aligned targets should be distinguished.

| Dataset / publication | Reference / domain relationship | Degradation / coverage | Reported size | Resolution |
|---|---|---|---|---|
| [ACDC-Snow](https://acdc.vision.ee.ethz.ch/)<br>ICCV 2021 | Scene-level paired | Falling snow + Accumulated snow | Input: 1,000<br>Clean: 1,000 | NR |
| [RealSnow](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_Learning_Weather-General_and_Weather-Specific_Features_for_Image_Restoration_Under_Multiple_CVPR_2023_paper.pdf)<br>CVPR 2023 | Real paired | Falling snow | Input: 1,890<br>Clean: 1,890 | NR |
| [WeatherStream-Snow (test)](https://doi.org/10.1109/cvpr52729.2023.01297)<br>CVPR 2023 | Real paired | Falling snow | Input: 3,960<br>Clean: 3,960 | NR |
| [WeatherBench-Snow](https://doi.org/10.1145/3746027.3758196)<br>ACM MM 2025 | Real paired | Falling snow | Input: 13,259<br>Clean: 13,259 | NR |
| [MWD-Snow (RSCM)](https://doi.org/10.1109/tip.2017.2695883)<br>TIP 2017 | Real unpaired | Falling snow + Accumulated snow | Input: 10,000<br>Clean: 10,000 | NR |
| [Image2Weather-Snow](https://doi.org/10.1016/j.jvcir.2017.04.002)<br>JVCIR 2017 | Real unpaired | Falling snow + Accumulated snow | Input: 1,252<br>Clean: 70,501 | NR |
| [Snow100K-Realistic](https://sites.google.com/view/yunfuliu/desnownet)<br>TIP 2018 | Real unpaired | Falling snow + Accumulated snow | Input: 1,329<br>Clean: 0 | NR |
| [RFS-Snow](https://doi.org/10.1109/ahs.2018.8541482)<br>IEEE AHS 2018 | Real unpaired | Falling snow + Accumulated snow | Input: 1,100<br>Clean: 0 | NR |
| [SRRS-Real](https://doi.org/10.1007/978-3-030-58589-1_45)<br>ECCV 2020 | Real unpaired | Falling snow + Snow veil | Input: 1,000<br>Clean: 0 | NR |
| [DAWN-Snow](https://arxiv.org/abs/2008.05402)<br>arXiv 2020 | Real unpaired | Falling snow + Accumulated snow | Input: 204<br>Clean: 0 | NR |
| [WEAPD-Snow](https://doi.org/10.1029/2020ea001604)<br>Earth Space Sci. 2021 | Real unpaired | Falling snow + Accumulated snow | Input: 621<br>Clean: 0 | NR |
| [SnowWorld24](https://doi.org/10.1016/j.cviu.2023.103819)<br>CVIU 2023 | Real unpaired | Falling snow | Input: 24<br>Clean: 0 | NR |
| [RSOD](https://doi.org/10.1109/tits.2023.3285035)<br>IEEE T-ITS 2023 | Real unpaired | Falling snow + Accumulated snow | Input: 2,100<br>Clean: 0 | NR |
| [RDSBW-Snow](https://doi.org/10.3390/s23031548)<br>Sensors 2023 | Real unpaired | Falling snow + Accumulated snow + Snow veil | Input: 4,777<br>Clean: 2,831 | NR |
| [RealSnow85](https://doi.org/10.1007/978-3-031-72684-2_5)<br>ECCV 2024 | Real unpaired | Falling snow + Snow veil | Input: 85 videos<br>Clean: 0 | NR |
| [SRSD-Real](https://doi.org/10.1049/cvi2.12274)<br>IET CV 2024 | Real unpaired | Falling snow | Input: 2,000<br>Clean: 0 | NR |
| [WReal-Snow](https://doi.org/10.1007/978-3-031-72649-1_9)<br>ECCV 2024 | Real unpaired | Falling snow + Accumulated snow | Input: 2,018<br>Clean: 0 | NR |
| [RealSnow10K](https://doi.org/10.1109/cvpr52734.2025.00406)<br>CVPR 2025 | Real unpaired | Falling snow + Accumulated snow + Snow veil | Input: 12,676<br>Clean: 0 | NR |

Each linked resource retains its own access conditions and license. Consult the source for downloads, exact splits, reference generation, alignment, and permitted use.
