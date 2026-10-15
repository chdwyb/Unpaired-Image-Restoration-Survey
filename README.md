# Unpaired Image Restoration

A research resource for learning image restoration without aligned degraded–clean training pairs. Browse methods by the information they use, explore datasets by task and reference type, and compare evaluation practices beyond a single quality score.

[Paper catalog](papers.md) · [Dataset catalog](datasets.md)

## Scope

The central setting uses independently collected degraded and clean images without revealing image-wise training correspondence. Methods may construct synthetic pairs internally or retain knowledge from pretrained models. Neither changes the need to explain where restoration supervision comes from.

The collection focuses on denoising, deblurring, dehazing, low-light enhancement, deraining, and desnowing. Related work on super-resolution, underwater enhancement, sand and dust removal, and image translation provides additional context. Noisy-only self-supervision, paired pretraining, auxiliary sensors, and scene-related reference images are distinct information settings; their presence should be recorded alongside a method's architecture.

## Learning mechanisms and implementations

Methods are organized in two layers. The first describes **what supplies a restoration constraint**; the second describes **how that constraint is implemented**.

| Mechanism | Role | Common implementations |
|---|---|---|
| **D · Distribution matching** | Align restored-image populations with a clean domain. | Adversarial learning, optimal transport, stochastic bridges |
| **C · Content consistency** | Constrain the scene information retained from each observation. | Cycle and identity constraints, latent representations, contrastive and pretrained features |
| **G · Degradation modeling** | Constrain image formation or synthesize correspondence for restoration training. | Imaging models, neural degradation generators, variational models, conditional flows |
| **P · Clean-image priors** | Restrict plausible candidate clean images. | Analytical regularizers, learned densities, diffusion scores, semantic and pretrained generative priors |

A method can combine several mechanisms. CNNs, Transformers, GANs, diffusion models, and normalizing flows can serve different roles depending on their objectives. A flow that synthesizes corruptions supports degradation modeling; a flow evaluating clean-image density supplies a prior. Likewise, an adversarial objective may align restored outputs or train a degradation generator. Architecture names alone do not establish the supervision setting.

## Browse by task

| Task | Main restoration issue | Resources |
|---|---|---|
| Denoising | Separate sensor noise from fine texture. | [Papers](papers.md#denoising) · [Datasets](datasets.md#denoising) |
| Deblurring | Recover structure under motion or defocus blur. | [Papers](papers.md#deblurring) · [Datasets](datasets.md#deblurring) |
| Dehazing | Resolve attenuation, airlight, and depth-dependent visibility. | [Papers](papers.md#dehazing) · [Datasets](datasets.md#dehazing) |
| Low-light enhancement | Correct illumination while handling noise, color, and clipping. | [Papers](papers.md#low-light-enhancement) · [Datasets](datasets.md#low-light-enhancement) |
| Deraining | Remove streaks or drops while retaining scene edges. | [Papers](papers.md#deraining) · [Datasets](datasets.md#deraining) |
| Desnowing | Handle varying particles and partial or opaque occlusion. | [Papers](papers.md#desnowing) · [Datasets](datasets.md#desnowing) |

## Evaluation essentials

Dataset capture and reference construction matter as much as dataset names. Real images, controlled physical degradations, synthetic corruptions, video-derived references, and scene-level correspondences support different comparisons. Unpaired training can be evaluated with paired test references; train–test separation and valid alignment still matter.

Use complementary evidence. PSNR and SSIM assess reference agreement; LPIPS measures perceptual distance; FID compares image populations. No-reference criteria such as NIQE, TOPIQ-NR, PIQE, ILNIQE, MUSIQ, and CLIP-IQA capture different quality preferences. None alone establishes that restored details belong to the original scene. Inspect residual corruption, altered geometry, text, and unsupported texture alongside aggregate scores.

Report complete inference costs: deployed parameters, FLOPs, latency, and peak GPU memory under stated hardware, resolution, precision, and sampling settings. Frozen components still incur deployment costs. For stochastic systems, separate scene variation from variation across repeated outputs.

## Open research questions

- **Generalization:** Can controlled degradation interventions reveal transferable constraints across unseen types, severities, and mixtures?
- **Generative control:** How should local observation reliability regulate inferred detail and uncertainty?
- **Quality assessment:** Can evaluation distinguish degradation removal, visual preference, scene faithfulness, and downstream usefulness?
- **Efficiency:** Can adaptive computation and distillation improve quality per unit of inference cost?
- **Pretrained adaptation:** How can unpaired target-domain learning specialize generative models while preserving structure and repeated-output consistency?

Follow the linked papers, datasets, and implementations for attribution and release terms; each resource retains its own copyright and license. Corrections and additional primary-source records are welcome through [issues](https://github.com/chdwyb/Unpaired-Image-Restoration-Survey/issues) or pull requests.
