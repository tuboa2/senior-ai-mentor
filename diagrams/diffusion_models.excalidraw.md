---

excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Denoising Diffusion
Probabilistic Models

## 🌿 1. Concept Intuition & Mental Model
Diffusion models generate complex probability distributions through learned thermodynamic reversal:
- **Forward Markov Process ($q$):** Pure information $\mathbf{x}_0$ is systematically corrupted with Gaussian perturbation over $T$ steps until matching isotropic noise $\mathcal{N}(0, \mathbf{I})$.
- **Reverse Denoising ($p_\theta$):** A neural network learns the local vector field pointing back toward regions of high probability density (the score function).

---

## 📐 2. Mathematical Foundations (KaTeX / LaTeX)
### Forward Transition Dynamics

$$q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) = \mathcal{N}\left(\mathbf{x}_t; \sqrt{1 - \beta_t}\mathbf{x}_{t-1}, \beta_t \mathbf{I}\right)$$

Marginal closed-form distribution jumping directly from $t=0$ to $t$:
$$q(\mathbf{x}_t \mid \mathbf{x}_0) = \mathcal{N}\left(\mathbf{x}_t; \sqrt{\bar{\alpha}_t}\mathbf{x}_0, (1 - \bar{\alpha}_t)\mathbf{I}\right)$$

Where $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$.

### Simplified Training Objective

$$\mathcal{L}_{\text{simple}}(\theta) = \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}}\left[ \left\| \boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t) \right\|^2 \right]$$

### Reverse Denoising Transition

$$p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t) = \mathcal{N}\left(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t), \sigma_t^2 \mathbf{I}\right)$$

$$\boldsymbol{\mu}_\theta(\mathbf{x}_t, t) = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\right)$$

---

## 💡 3. Senior Engineering & Performance Notes
- **Latent Space Compression:** Running diffusion in raw pixel space ($3 \times 512 \times 512 = 786{,}432$ dimensions) is computationally prohibitive. A VAE compresses images into latent space ($4 \times 64 \times 64 = 16{,}384$ dimensions), accelerating training by $48\times$.
- **Classifier-Free Guidance (CFG):** Interpolating between unconditional and conditional noise estimates $\tilde{\epsilon} = \epsilon_\emptyset + s \cdot (\epsilon_c - \epsilon_\emptyset)$ with scale $s \in [5, 8]$ improves prompt adherence at the cost of sample diversity.

---

# Excalidraw Data

## Text Elements
Denoising Diffusion Probabilistic Models ^Yj8YqMCe

Libraries ^iaDShI0S

torch ^0zsi4iGL

diffusers ^saoaetyW

einops ^Dy0pRHV9

Methods ^7akL1B7F

Forward Noise Perturbation ^vheaqvtl

torch.randn_like(x_0) ^Ea5aLYyC

Samples standard normal isotropic Gaussian noise vector epsilon ~ N(0, I). ^w81iEpqS

x_t = sqrt(alpha_bar)*x_0 + sqrt(1-alpha_bar)*eps ^8yvdGlfk

Computes marginal noisy state directly at arbitrary timestep t in O(1). ^3JGOw3oR

Reparameterization property: q(x_t | x_0) = N(x_t; sqrt(alpha_bar_t)*x_0, (1-alpha_bar_t)*I). This eliminates sequential Markov simulation during training, allowing parallel loss evaluation at random timesteps. ^PiKl5OtW

Reverse Noise Estimator ^qSOSaHzl

eps_pred = unet(x_t, t) ^OX4iojuq

U-Net with cross-attention predicts the exact injected noise vector epsilon. ^CqvzLJT2

loss = F.mse_loss(eps_pred, eps) ^eVvjtAhR

Calculates simplified variational bound loss ||eps - eps_pred||^2. ^WqOckwJD

Optimizing MSE on predicted noise matches denoising score matching: nabla_{x_t} log q(x_t) = -eps_theta(x_t, t) / sqrt(1 - alpha_bar_t). The neural network directly learns the score function of data distribution. ^2aS41ISV

Inference Denoising Loop ^hJUmaQ98

scheduler.step(eps_pred, t, x_t) ^Us892zm0

Subtracts estimated noise and injects scaled variance sigma_t * z. ^X31m5L6m

torch.clamp(x_pred, -1.0, 1.0) ^q3GEKItc

Restricts reconstructed latent coordinates to valid physical tensor range. ^23WDKR8p

DDIM (Denoising Diffusion Implicit Models) enables non-Markovian deterministic sampling trajectories, reducing inference latency from 1,000 steps to 20-50 steps without retraining. ^frURmBNW

Architecture ^xSsYckw8

Clean Data Ingress x_0 ^xhSsaIDx

Noise Schedule beta_t ^92GfX2o0

U-Net Score Prediction ^Xm6q7sIL

Reverse Langevin Step ^U4sJGs0u

Denoised Output x_0 ^YZpjRV7b

Conditioning Prompt Embeddings ^3VpKQKe7

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "WSQ70KhX2spegH8N",
      "type": "rectangle",
      "x": 168.0,
      "y": 490.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4984627,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Yj8YqMCe"
        },
        {
          "type": "arrow",
          "id": "Xd7gKRpa"
        },
        {
          "type": "arrow",
          "id": "5tBYCdP3"
        },
        {
          "type": "arrow",
          "id": "xXaQ5Z2G"
        }
      ],
      "updated": 1789187294952,
      "link": null,
      "locked": false
    },
    {
      "id": "Yj8YqMCe",
      "type": "text",
      "x": 178.0,
      "y": 499.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3131843,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294952,
      "link": null,
      "locked": false,
      "text": "Denoising Diffusion\nProbabilistic Models",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "WSQ70KhX2spegH8N",
      "originalText": "Denoising Diffusion\nProbabilistic Models",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "eMxN2z8Z0qNQmPPT",
      "type": "rectangle",
      "x": 590.0,
      "y": 37.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9973408,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "iaDShI0S"
        },
        {
          "type": "arrow",
          "id": "Xd7gKRpa"
        },
        {
          "type": "arrow",
          "id": "SjhFzxv9"
        },
        {
          "type": "arrow",
          "id": "GUvvGy2W"
        },
        {
          "type": "arrow",
          "id": "1YVS7wpK"
        }
      ],
      "updated": 1789187294952,
      "link": null,
      "locked": false
    },
    {
      "id": "iaDShI0S",
      "type": "text",
      "x": 600.0,
      "y": 46.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3512652,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294952,
      "link": null,
      "locked": false,
      "text": "Libraries",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "eMxN2z8Z0qNQmPPT",
      "originalText": "Libraries",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Xd7gKRpa",
      "type": "arrow",
      "x": 349.0,
      "y": 522.0,
      "width": 241.0,
      "height": 453.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 3236992,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294952,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          241.0,
          -453.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "WSQ70KhX2spegH8N",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "eMxN2z8Z0qNQmPPT",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "lyI6PEvsIiEPYUXZ",
      "type": "rectangle",
      "x": 900.0,
      "y": -23.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3910594,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "0zsi4iGL"
        },
        {
          "type": "arrow",
          "id": "SjhFzxv9"
        }
      ],
      "updated": 1789187294952,
      "link": null,
      "locked": false
    },
    {
      "id": "0zsi4iGL",
      "type": "text",
      "x": 910.0,
      "y": -14.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8415371,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294952,
      "link": null,
      "locked": false,
      "text": "torch",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "lyI6PEvsIiEPYUXZ",
      "originalText": "torch",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "SjhFzxv9",
      "type": "arrow",
      "x": 771.0,
      "y": 69.0,
      "width": 129.0,
      "height": 60.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1914089,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          -60.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "eMxN2z8Z0qNQmPPT",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "lyI6PEvsIiEPYUXZ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "C9Mtv1HH446tz4zr",
      "type": "rectangle",
      "x": 900.0,
      "y": 82.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1169618,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "saoaetyW"
        },
        {
          "type": "arrow",
          "id": "GUvvGy2W"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "saoaetyW",
      "type": "text",
      "x": 910.0,
      "y": 91.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5874589,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "diffusers",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "C9Mtv1HH446tz4zr",
      "originalText": "diffusers",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "GUvvGy2W",
      "type": "arrow",
      "x": 771.0,
      "y": 69.0,
      "width": 129.0,
      "height": 45.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 596395,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          45.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "eMxN2z8Z0qNQmPPT",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "C9Mtv1HH446tz4zr",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "LpeHipkdq7EiStrJ",
      "type": "rectangle",
      "x": 900.0,
      "y": 187.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 788838,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Dy0pRHV9"
        },
        {
          "type": "arrow",
          "id": "1YVS7wpK"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "Dy0pRHV9",
      "type": "text",
      "x": 910.0,
      "y": 196.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1986637,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "einops",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "LpeHipkdq7EiStrJ",
      "originalText": "einops",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "1YVS7wpK",
      "type": "arrow",
      "x": 771.0,
      "y": 69.0,
      "width": 129.0,
      "height": 150.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4955814,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          150.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "eMxN2z8Z0qNQmPPT",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "LpeHipkdq7EiStrJ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "DMD5tjQl4LfJvyDc",
      "type": "rectangle",
      "x": 590.0,
      "y": 488.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5829854,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "7akL1B7F"
        },
        {
          "type": "arrow",
          "id": "5tBYCdP3"
        },
        {
          "type": "arrow",
          "id": "72WdGB8z"
        },
        {
          "type": "arrow",
          "id": "40ZKc7lh"
        },
        {
          "type": "arrow",
          "id": "JgcUme36"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "7akL1B7F",
      "type": "text",
      "x": 600.0,
      "y": 497.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3935152,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "Methods",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "DMD5tjQl4LfJvyDc",
      "originalText": "Methods",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "5tBYCdP3",
      "type": "arrow",
      "x": 349.0,
      "y": 522.0,
      "width": 241.0,
      "height": 2.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4437089,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          241.0,
          -2.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "WSQ70KhX2spegH8N",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "DMD5tjQl4LfJvyDc",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "HUlAoMFq07dUzLKb",
      "type": "rectangle",
      "x": 900.0,
      "y": 280.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2484762,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "vheaqvtl"
        },
        {
          "type": "arrow",
          "id": "72WdGB8z"
        },
        {
          "type": "arrow",
          "id": "C3jwm2R5"
        },
        {
          "type": "arrow",
          "id": "ve7CBbbJ"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "vheaqvtl",
      "type": "text",
      "x": 910.0,
      "y": 289.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8153967,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "Forward Noise Perturbation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "HUlAoMFq07dUzLKb",
      "originalText": "Forward Noise Perturbation",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "72WdGB8z",
      "type": "arrow",
      "x": 771.0,
      "y": 520.0,
      "width": 129.0,
      "height": 208.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6022234,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          -208.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "DMD5tjQl4LfJvyDc",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "HUlAoMFq07dUzLKb",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "2gnaefDdt3Xyxcpa",
      "type": "rectangle",
      "x": 1170.0,
      "y": 220.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4320404,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Ea5aLYyC"
        },
        {
          "type": "arrow",
          "id": "C3jwm2R5"
        },
        {
          "type": "arrow",
          "id": "mjJWRINM"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "Ea5aLYyC",
      "type": "text",
      "x": 1180.0,
      "y": 229.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4636940,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "torch.randn_like(x_0)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "2gnaefDdt3Xyxcpa",
      "originalText": "torch.randn_like(x_0)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "C3jwm2R5",
      "type": "arrow",
      "x": 1081.0,
      "y": 312.0,
      "width": 89.0,
      "height": 60.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4307697,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          89.0,
          -60.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "HUlAoMFq07dUzLKb",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "2gnaefDdt3Xyxcpa",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "gmU1DTJSpuXCy4qY",
      "type": "rectangle",
      "x": 1425.0,
      "y": 220.0,
      "width": 347.0,
      "height": 88.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9536646,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "w81iEpqS"
        },
        {
          "type": "arrow",
          "id": "mjJWRINM"
        },
        {
          "type": "arrow",
          "id": "9T3SEMpc"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "w81iEpqS",
      "type": "text",
      "x": 1435.0,
      "y": 229.0,
      "width": 327.0,
      "height": 70.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4527375,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "Samples standard normal isotropic Gaussian noise vector epsilon ~ N(0, I).",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "gmU1DTJSpuXCy4qY",
      "originalText": "Samples standard normal isotropic Gaussian noise vector epsilon ~ N(0, I).",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "mjJWRINM",
      "type": "arrow",
      "x": 1351.0,
      "y": 252.0,
      "width": 74.0,
      "height": 12.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9964300,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          74.0,
          12.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "2gnaefDdt3Xyxcpa",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "gmU1DTJSpuXCy4qY",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "v87nKwHLLYZReXHu",
      "type": "rectangle",
      "x": 1170.0,
      "y": 332.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3322282,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "8yvdGlfk"
        },
        {
          "type": "arrow",
          "id": "ve7CBbbJ"
        },
        {
          "type": "arrow",
          "id": "NvbX7YNm"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "8yvdGlfk",
      "type": "text",
      "x": 1180.0,
      "y": 341.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5915888,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "x_t = sqrt(alpha_bar)*x_0 + sqrt(1-alpha_bar)*eps",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "v87nKwHLLYZReXHu",
      "originalText": "x_t = sqrt(alpha_bar)*x_0 + sqrt(1-alpha_bar)*eps",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "ve7CBbbJ",
      "type": "arrow",
      "x": 1081.0,
      "y": 312.0,
      "width": 89.0,
      "height": 52.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 3923574,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          89.0,
          52.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "HUlAoMFq07dUzLKb",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "v87nKwHLLYZReXHu",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "nH3TiJ32rAyHxDeC",
      "type": "rectangle",
      "x": 1425.0,
      "y": 332.0,
      "width": 347.0,
      "height": 88.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4858560,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "3JGOw3oR"
        },
        {
          "type": "arrow",
          "id": "NvbX7YNm"
        },
        {
          "type": "arrow",
          "id": "rSZ2B5Ha"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "3JGOw3oR",
      "type": "text",
      "x": 1435.0,
      "y": 341.0,
      "width": 327.0,
      "height": 70.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6930113,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "Computes marginal noisy state directly at arbitrary timestep t in O(1).",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "nH3TiJ32rAyHxDeC",
      "originalText": "Computes marginal noisy state directly at arbitrary timestep t in O(1).",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "NvbX7YNm",
      "type": "arrow",
      "x": 1351.0,
      "y": 364.0,
      "width": 74.0,
      "height": 12.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 796238,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          74.0,
          12.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "v87nKwHLLYZReXHu",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "nH3TiJ32rAyHxDeC",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "V1p3aZvOzNLJCPLV",
      "type": "rectangle",
      "x": 1895.0,
      "y": 260.0,
      "width": 347.0,
      "height": 135.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5371152,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "PiKl5OtW"
        },
        {
          "type": "arrow",
          "id": "9T3SEMpc"
        },
        {
          "type": "arrow",
          "id": "rSZ2B5Ha"
        }
      ],
      "updated": 1789187294953,
      "link": null,
      "locked": false
    },
    {
      "id": "PiKl5OtW",
      "type": "text",
      "x": 1905.0,
      "y": 269.0,
      "width": 327.0,
      "height": 117.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6972925,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "text": "Reparameterization property: q(x_t | x_0) = N(x_t; sqrt(alpha_bar_t)*x_0, (1-alpha_bar_t)*I). This eliminates sequential Markov simulation during training, allowing parallel loss evaluation at random timesteps.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "V1p3aZvOzNLJCPLV",
      "originalText": "Reparameterization property: q(x_t | x_0) = N(x_t; sqrt(alpha_bar_t)*x_0, (1-alpha_bar_t)*I). This eliminates sequential Markov simulation during training, allowing parallel loss evaluation at random timesteps.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "9T3SEMpc",
      "type": "arrow",
      "x": 1772.0,
      "y": 264.0,
      "width": 123.0,
      "height": 63.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9977724,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294953,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          123.0,
          63.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gmU1DTJSpuXCy4qY",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "V1p3aZvOzNLJCPLV",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "rSZ2B5Ha",
      "type": "arrow",
      "x": 1772.0,
      "y": 376.0,
      "width": 123.0,
      "height": 48.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6279578,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          123.0,
          -48.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "nH3TiJ32rAyHxDeC",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "V1p3aZvOzNLJCPLV",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "kA1oWKgShvoOBArm",
      "type": "rectangle",
      "x": 900.0,
      "y": 524.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5581944,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "qSOSaHzl"
        },
        {
          "type": "arrow",
          "id": "40ZKc7lh"
        },
        {
          "type": "arrow",
          "id": "E6Yu46X6"
        },
        {
          "type": "arrow",
          "id": "92DHBGQO"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "qSOSaHzl",
      "type": "text",
      "x": 910.0,
      "y": 533.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8471360,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "Reverse Noise Estimator",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "kA1oWKgShvoOBArm",
      "originalText": "Reverse Noise Estimator",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "40ZKc7lh",
      "type": "arrow",
      "x": 771.0,
      "y": 520.0,
      "width": 129.0,
      "height": 36.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6534011,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          36.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "DMD5tjQl4LfJvyDc",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "kA1oWKgShvoOBArm",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "CD1ep8ZEg2UDN9Gn",
      "type": "rectangle",
      "x": 1170.0,
      "y": 464.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6824541,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "OX4iojuq"
        },
        {
          "type": "arrow",
          "id": "E6Yu46X6"
        },
        {
          "type": "arrow",
          "id": "qvRCsNXT"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "OX4iojuq",
      "type": "text",
      "x": 1180.0,
      "y": 473.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6490588,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "eps_pred = unet(x_t, t)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "CD1ep8ZEg2UDN9Gn",
      "originalText": "eps_pred = unet(x_t, t)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "E6Yu46X6",
      "type": "arrow",
      "x": 1081.0,
      "y": 556.0,
      "width": 89.0,
      "height": 60.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 5498938,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          89.0,
          -60.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "kA1oWKgShvoOBArm",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "CD1ep8ZEg2UDN9Gn",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "FnxjIrO3xhbZrJr1",
      "type": "rectangle",
      "x": 1425.0,
      "y": 464.0,
      "width": 347.0,
      "height": 88.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4431443,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "CqvzLJT2"
        },
        {
          "type": "arrow",
          "id": "qvRCsNXT"
        },
        {
          "type": "arrow",
          "id": "xuP0F92D"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "CqvzLJT2",
      "type": "text",
      "x": 1435.0,
      "y": 473.0,
      "width": 327.0,
      "height": 70.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1855219,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "U-Net with cross-attention predicts the exact injected noise vector epsilon.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "FnxjIrO3xhbZrJr1",
      "originalText": "U-Net with cross-attention predicts the exact injected noise vector epsilon.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "qvRCsNXT",
      "type": "arrow",
      "x": 1351.0,
      "y": 496.0,
      "width": 74.0,
      "height": 12.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2190028,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          74.0,
          12.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "CD1ep8ZEg2UDN9Gn",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "FnxjIrO3xhbZrJr1",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "VHcLr1pQTNmRBUTe",
      "type": "rectangle",
      "x": 1170.0,
      "y": 576.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3983245,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "eVvjtAhR"
        },
        {
          "type": "arrow",
          "id": "92DHBGQO"
        },
        {
          "type": "arrow",
          "id": "LXgx1kxH"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "eVvjtAhR",
      "type": "text",
      "x": 1180.0,
      "y": 585.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4843675,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "loss = F.mse_loss(eps_pred, eps)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "VHcLr1pQTNmRBUTe",
      "originalText": "loss = F.mse_loss(eps_pred, eps)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "92DHBGQO",
      "type": "arrow",
      "x": 1081.0,
      "y": 556.0,
      "width": 89.0,
      "height": 52.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 8615887,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          89.0,
          52.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "kA1oWKgShvoOBArm",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "VHcLr1pQTNmRBUTe",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "rwgA0xZd7elHlXMk",
      "type": "rectangle",
      "x": 1425.0,
      "y": 576.0,
      "width": 347.0,
      "height": 75.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9026464,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "WqOckwJD"
        },
        {
          "type": "arrow",
          "id": "LXgx1kxH"
        },
        {
          "type": "arrow",
          "id": "1vQz1Wuy"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "WqOckwJD",
      "type": "text",
      "x": 1435.0,
      "y": 585.0,
      "width": 327.0,
      "height": 57.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2729366,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "Calculates simplified variational bound loss ||eps - eps_pred||^2.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "rwgA0xZd7elHlXMk",
      "originalText": "Calculates simplified variational bound loss ||eps - eps_pred||^2.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "LXgx1kxH",
      "type": "arrow",
      "x": 1351.0,
      "y": 608.0,
      "width": 74.0,
      "height": 5.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 3339250,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          74.0,
          5.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "VHcLr1pQTNmRBUTe",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "rwgA0xZd7elHlXMk",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "28JTaYZLGkQrvt3c",
      "type": "rectangle",
      "x": 1895.0,
      "y": 504.0,
      "width": 347.0,
      "height": 135.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9712670,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "2aS41ISV"
        },
        {
          "type": "arrow",
          "id": "xuP0F92D"
        },
        {
          "type": "arrow",
          "id": "1vQz1Wuy"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "2aS41ISV",
      "type": "text",
      "x": 1905.0,
      "y": 513.0,
      "width": 327.0,
      "height": 117.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5772030,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "Optimizing MSE on predicted noise matches denoising score matching: nabla_{x_t} log q(x_t) = -eps_theta(x_t, t) / sqrt(1 - alpha_bar_t). The neural network directly learns the score function of data distribution.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "28JTaYZLGkQrvt3c",
      "originalText": "Optimizing MSE on predicted noise matches denoising score matching: nabla_{x_t} log q(x_t) = -eps_theta(x_t, t) / sqrt(1 - alpha_bar_t). The neural network directly learns the score function of data distribution.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "xuP0F92D",
      "type": "arrow",
      "x": 1772.0,
      "y": 508.0,
      "width": 123.0,
      "height": 63.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6080262,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          123.0,
          63.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "FnxjIrO3xhbZrJr1",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "28JTaYZLGkQrvt3c",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "1vQz1Wuy",
      "type": "arrow",
      "x": 1772.0,
      "y": 613.5,
      "width": 123.0,
      "height": 42.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 193432,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          123.0,
          -42.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "rwgA0xZd7elHlXMk",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "28JTaYZLGkQrvt3c",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "Oa9bLpdtRJVARMF7",
      "type": "rectangle",
      "x": 900.0,
      "y": 768.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2746957,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "hJUmaQ98"
        },
        {
          "type": "arrow",
          "id": "JgcUme36"
        },
        {
          "type": "arrow",
          "id": "Q8cbPvoS"
        },
        {
          "type": "arrow",
          "id": "P8Jy9NAZ"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "hJUmaQ98",
      "type": "text",
      "x": 910.0,
      "y": 777.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4382457,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "Inference Denoising Loop",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "Oa9bLpdtRJVARMF7",
      "originalText": "Inference Denoising Loop",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "JgcUme36",
      "type": "arrow",
      "x": 771.0,
      "y": 520.0,
      "width": 129.0,
      "height": 280.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9351321,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          280.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "DMD5tjQl4LfJvyDc",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "Oa9bLpdtRJVARMF7",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "0kXlIKTaiEaAAdLr",
      "type": "rectangle",
      "x": 1170.0,
      "y": 708.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1208635,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Us892zm0"
        },
        {
          "type": "arrow",
          "id": "Q8cbPvoS"
        },
        {
          "type": "arrow",
          "id": "04JcpVTG"
        }
      ],
      "updated": 1789187294954,
      "link": null,
      "locked": false
    },
    {
      "id": "Us892zm0",
      "type": "text",
      "x": 1180.0,
      "y": 717.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7012659,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "text": "scheduler.step(eps_pred, t, x_t)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "0kXlIKTaiEaAAdLr",
      "originalText": "scheduler.step(eps_pred, t, x_t)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Q8cbPvoS",
      "type": "arrow",
      "x": 1081.0,
      "y": 800.0,
      "width": 89.0,
      "height": 60.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1330429,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294954,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          89.0,
          -60.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "Oa9bLpdtRJVARMF7",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "0kXlIKTaiEaAAdLr",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "KRGbXbcOWzlwY6Qw",
      "type": "rectangle",
      "x": 1425.0,
      "y": 708.0,
      "width": 347.0,
      "height": 75.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4462545,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "X31m5L6m"
        },
        {
          "type": "arrow",
          "id": "04JcpVTG"
        },
        {
          "type": "arrow",
          "id": "Ngk6xGSV"
        }
      ],
      "updated": 1789187294955,
      "link": null,
      "locked": false
    },
    {
      "id": "X31m5L6m",
      "type": "text",
      "x": 1435.0,
      "y": 717.0,
      "width": 327.0,
      "height": 57.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 364884,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "text": "Subtracts estimated noise and injects scaled variance sigma_t * z.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "KRGbXbcOWzlwY6Qw",
      "originalText": "Subtracts estimated noise and injects scaled variance sigma_t * z.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "04JcpVTG",
      "type": "arrow",
      "x": 1351.0,
      "y": 740.0,
      "width": 74.0,
      "height": 5.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 568259,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          74.0,
          5.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "0kXlIKTaiEaAAdLr",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "KRGbXbcOWzlwY6Qw",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "lj41AQTYOz3dIgOJ",
      "type": "rectangle",
      "x": 1170.0,
      "y": 820.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1356396,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "q3GEKItc"
        },
        {
          "type": "arrow",
          "id": "P8Jy9NAZ"
        },
        {
          "type": "arrow",
          "id": "aeuJD6ta"
        }
      ],
      "updated": 1789187294955,
      "link": null,
      "locked": false
    },
    {
      "id": "q3GEKItc",
      "type": "text",
      "x": 1180.0,
      "y": 829.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4036782,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "text": "torch.clamp(x_pred, -1.0, 1.0)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "lj41AQTYOz3dIgOJ",
      "originalText": "torch.clamp(x_pred, -1.0, 1.0)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "P8Jy9NAZ",
      "type": "arrow",
      "x": 1081.0,
      "y": 800.0,
      "width": 89.0,
      "height": 52.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 7892857,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          89.0,
          52.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "Oa9bLpdtRJVARMF7",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "lj41AQTYOz3dIgOJ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "EGz63AilRR0ljIZh",
      "type": "rectangle",
      "x": 1425.0,
      "y": 820.0,
      "width": 347.0,
      "height": 88.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9791772,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "23WDKR8p"
        },
        {
          "type": "arrow",
          "id": "aeuJD6ta"
        },
        {
          "type": "arrow",
          "id": "CrkSpAFZ"
        }
      ],
      "updated": 1789187294955,
      "link": null,
      "locked": false
    },
    {
      "id": "23WDKR8p",
      "type": "text",
      "x": 1435.0,
      "y": 829.0,
      "width": 327.0,
      "height": 70.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 333789,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "text": "Restricts reconstructed latent coordinates to valid physical tensor range.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "EGz63AilRR0ljIZh",
      "originalText": "Restricts reconstructed latent coordinates to valid physical tensor range.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "aeuJD6ta",
      "type": "arrow",
      "x": 1351.0,
      "y": 852.0,
      "width": 74.0,
      "height": 12.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1514745,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          74.0,
          12.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "lj41AQTYOz3dIgOJ",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "EGz63AilRR0ljIZh",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "7mb5qnygj8Llxw3B",
      "type": "rectangle",
      "x": 1895.0,
      "y": 748.0,
      "width": 347.0,
      "height": 135.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2016918,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "frURmBNW"
        },
        {
          "type": "arrow",
          "id": "Ngk6xGSV"
        },
        {
          "type": "arrow",
          "id": "CrkSpAFZ"
        }
      ],
      "updated": 1789187294955,
      "link": null,
      "locked": false
    },
    {
      "id": "frURmBNW",
      "type": "text",
      "x": 1905.0,
      "y": 757.0,
      "width": 327.0,
      "height": 117.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5389543,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "text": "DDIM (Denoising Diffusion Implicit Models) enables non-Markovian deterministic sampling trajectories, reducing inference latency from 1,000 steps to 20-50 steps without retraining.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "7mb5qnygj8Llxw3B",
      "originalText": "DDIM (Denoising Diffusion Implicit Models) enables non-Markovian deterministic sampling trajectories, reducing inference latency from 1,000 steps to 20-50 steps without retraining.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Ngk6xGSV",
      "type": "arrow",
      "x": 1772.0,
      "y": 745.5,
      "width": 123.0,
      "height": 70.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1663580,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          123.0,
          70.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "KRGbXbcOWzlwY6Qw",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "7mb5qnygj8Llxw3B",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "CrkSpAFZ",
      "type": "arrow",
      "x": 1772.0,
      "y": 864.0,
      "width": 123.0,
      "height": 48.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9654149,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          123.0,
          -48.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "EGz63AilRR0ljIZh",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "7mb5qnygj8Llxw3B",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "KLCPUstNsXdSVRnY",
      "type": "rectangle",
      "x": 590.0,
      "y": 1000.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1477684,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "xSsYckw8"
        },
        {
          "type": "arrow",
          "id": "xXaQ5Z2G"
        },
        {
          "type": "arrow",
          "id": "0QnXiphb"
        }
      ],
      "updated": 1789187294955,
      "link": null,
      "locked": false
    },
    {
      "id": "xSsYckw8",
      "type": "text",
      "x": 600.0,
      "y": 1009.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1690427,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294955,
      "link": null,
      "locked": false,
      "text": "Architecture",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "KLCPUstNsXdSVRnY",
      "originalText": "Architecture",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "xXaQ5Z2G",
      "type": "arrow",
      "x": 349.0,
      "y": 522.0,
      "width": 241.0,
      "height": 510.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 3147963,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          241.0,
          510.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "WSQ70KhX2spegH8N",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "KLCPUstNsXdSVRnY",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "pEI2JOuvgFgHicje",
      "type": "rectangle",
      "x": 900.0,
      "y": 1000.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5282629,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "xhSsaIDx"
        },
        {
          "type": "arrow",
          "id": "0QnXiphb"
        },
        {
          "type": "arrow",
          "id": "FE4ry1gK"
        }
      ],
      "updated": 1789187294956,
      "link": null,
      "locked": false
    },
    {
      "id": "xhSsaIDx",
      "type": "text",
      "x": 910.0,
      "y": 1009.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3619717,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "text": "Clean Data Ingress x_0",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "pEI2JOuvgFgHicje",
      "originalText": "Clean Data Ingress x_0",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "0QnXiphb",
      "type": "arrow",
      "x": 771.0,
      "y": 1032.0,
      "width": 129.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 7611526,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          129.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "KLCPUstNsXdSVRnY",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "pEI2JOuvgFgHicje",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "KDmxzn3K7YhtjdNG",
      "type": "rectangle",
      "x": 1156.0,
      "y": 1000.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6993110,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "92GfX2o0"
        },
        {
          "type": "arrow",
          "id": "FE4ry1gK"
        },
        {
          "type": "arrow",
          "id": "8xmlg5lt"
        }
      ],
      "updated": 1789187294956,
      "link": null,
      "locked": false
    },
    {
      "id": "92GfX2o0",
      "type": "text",
      "x": 1166.0,
      "y": 1009.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8061315,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "text": "Noise Schedule beta_t",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "KDmxzn3K7YhtjdNG",
      "originalText": "Noise Schedule beta_t",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "FE4ry1gK",
      "type": "arrow",
      "x": 1081.0,
      "y": 1032.0,
      "width": 75.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2065606,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          75.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "pEI2JOuvgFgHicje",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "KDmxzn3K7YhtjdNG",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "iNoStnTpkzWsSWOe",
      "type": "rectangle",
      "x": 1412.0,
      "y": 1000.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8084379,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Xm6q7sIL"
        },
        {
          "type": "arrow",
          "id": "8xmlg5lt"
        },
        {
          "type": "arrow",
          "id": "gwtbfYhJ"
        },
        {
          "type": "arrow",
          "id": "Pd3vLQBl"
        }
      ],
      "updated": 1789187294956,
      "link": null,
      "locked": false
    },
    {
      "id": "Xm6q7sIL",
      "type": "text",
      "x": 1422.0,
      "y": 1009.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5340940,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "text": "U-Net Score Prediction",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "iNoStnTpkzWsSWOe",
      "originalText": "U-Net Score Prediction",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "8xmlg5lt",
      "type": "arrow",
      "x": 1337.0,
      "y": 1032.0,
      "width": 75.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2587577,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          75.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "KDmxzn3K7YhtjdNG",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "iNoStnTpkzWsSWOe",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "cTxRimVB9Oy4eYXi",
      "type": "rectangle",
      "x": 1668.0,
      "y": 1000.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9750931,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "U4sJGs0u"
        },
        {
          "type": "arrow",
          "id": "gwtbfYhJ"
        },
        {
          "type": "arrow",
          "id": "E09BEXxJ"
        }
      ],
      "updated": 1789187294956,
      "link": null,
      "locked": false
    },
    {
      "id": "U4sJGs0u",
      "type": "text",
      "x": 1678.0,
      "y": 1009.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1711921,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "text": "Reverse Langevin Step",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "cTxRimVB9Oy4eYXi",
      "originalText": "Reverse Langevin Step",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "gwtbfYhJ",
      "type": "arrow",
      "x": 1593.0,
      "y": 1032.0,
      "width": 75.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 8455375,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          75.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "iNoStnTpkzWsSWOe",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "cTxRimVB9Oy4eYXi",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "nfjkxf8xJlAlIZAI",
      "type": "rectangle",
      "x": 1924.0,
      "y": 1000.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 685240,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "YZpjRV7b"
        },
        {
          "type": "arrow",
          "id": "E09BEXxJ"
        }
      ],
      "updated": 1789187294956,
      "link": null,
      "locked": false
    },
    {
      "id": "YZpjRV7b",
      "type": "text",
      "x": 1934.0,
      "y": 1009.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9163069,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "text": "Denoised Output x_0",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "nfjkxf8xJlAlIZAI",
      "originalText": "Denoised Output x_0",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "E09BEXxJ",
      "type": "arrow",
      "x": 1849.0,
      "y": 1032.0,
      "width": 75.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6958201,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          75.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "cTxRimVB9Oy4eYXi",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "nfjkxf8xJlAlIZAI",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "WXvCuQkpBW9HuEAS",
      "type": "rectangle",
      "x": 1412.0,
      "y": 876.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6728366,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "3VpKQKe7"
        },
        {
          "type": "arrow",
          "id": "Pd3vLQBl"
        }
      ],
      "updated": 1789187294956,
      "link": null,
      "locked": false
    },
    {
      "id": "3VpKQKe7",
      "type": "text",
      "x": 1422.0,
      "y": 885.0,
      "width": 161.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7169349,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "text": "Conditioning Prompt Embeddings",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "WXvCuQkpBW9HuEAS",
      "originalText": "Conditioning Prompt Embeddings",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Pd3vLQBl",
      "type": "arrow",
      "x": 1502.5,
      "y": 1000.0,
      "width": 0.0,
      "height": 60.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 332902,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187294956,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          0.0,
          -60.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "iNoStnTpkzWsSWOe",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "WXvCuQkpBW9HuEAS",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    }
  ],
  "appState": {
    "theme": "dark",
    "viewBackgroundColor": "#ffffff",
    "currentItemStrokeColor": "#1e1e1e",
    "currentItemBackgroundColor": "transparent",
    "currentItemFillStyle": "solid",
    "currentItemStrokeWidthKey": "bold",
    "currentItemStrokeStyle": "solid",
    "currentItemRoughness": 0,
    "currentItemOpacity": 100,
    "currentItemFontFamily": 7,
    "currentItemFontSize": 20,
    "currentItemTextAlign": "left",
    "currentItemEndArrowhead": "arrow",
    "gridSize": 20,
    "zoom": {
      "value": 0.4
    }
  },
  "files": {}
}
```
%%
