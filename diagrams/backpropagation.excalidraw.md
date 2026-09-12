---

excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Computational Graph & Backpropagation

## 🌿 1. Concept Intuition & Mental Model
Backpropagation is reverse-mode automatic differentiation applied to an acyclic computation graph:
- **Forward:** Information cascades from input variables to compute objective scalar loss $\mathcal{L}$.
- **Backward:** A scalar perturbation of 1.0 at $\mathcal{L}$ propagates upstream, calculating sensitivity derivatives $\frac{\partial \mathcal{L}}{\partial \theta}$ for every parameter.

---

## 📐 2. Mathematical Foundations (KaTeX / LaTeX)
### Forward Equations

$$\mathbf{z}^{[l]} = \mathbf{W}^{[l]} \mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}, \quad \mathbf{a}^{[l]} = \sigma(\mathbf{z}^{[l]})$$

### Backward Adjoint Error Vector

$$\boldsymbol{\delta}^{[l]} \equiv \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{[l]}} = \left( (\mathbf{W}^{[l+1]})^T \boldsymbol{\delta}^{[l+1]} \right) \odot \sigma'(\mathbf{z}^{[l]})$$

### Parameter Gradient Outer Products

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}} = \boldsymbol{\delta}^{[l]} (\mathbf{a}^{[l-1]})^T, \quad \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}} = \sum_{\text{batch}} \boldsymbol{\delta}^{[l]}$$

---

## 💡 3. Senior Engineering & Performance Notes
- **Gradient Saturation Trap:** If sigmoid or tanh activations are used, saturation occurs when $|z| \gg 1$, driving $\sigma'(z) \to 0$ and killing gradient flow. ReLU, GELU, and SwiGLU avoid negative saturation.
- **Gradient Checkpointing:** Recomputes activations dynamically in the backward pass rather than caching all layer outputs, reducing peak activation VRAM by $4\times$.

---

# Excalidraw Data

## Text Elements
Libraries ^ELj8b3Ti

torch.autograd ^nyTthEEo

torch.nn ^azDz0XxT

Methods ^HpBZXTRb

Architecture ^RTIOL091

Computational Graph & Backpropagation ^RY1mJDss

Forward Activation Pass ^1e4WJEcU

z = torch.matmul(W, a_prev) + b ^uo1CsceK

Computes affine linear weighted sum of upstream layer activations. ^wPSx4d6Z

a = torch.relu(z) ^jtqivDyi

Applies non-linear activation gate producing layer representations. ^Qz6JOsFW

Activation Caching Requirement: Intermediate tensors a_prev and z must be retained in memory during forward pass to compute gradients during backward pass. ^qGJIGMgb

Reverse Adjoint Chain Rule ^b5Zyvsqt

delta = W_next.T @ delta_next * relu'(z) ^B5zo4pUo

Propagates adjoint error vector delta upstream via transposed weights and local derivative. ^cvpGUYxq

grad_W = torch.outer(delta, a_prev) ^fX7fszKZ

Calculates exact weight gradient as outer product of error and activations. ^L9Hq6O8q

Reverse-Mode Auto-Differentiation: Chain Rule: dL/dW = delta * (a_prev)^T Adjoint error vectors propagate perturbation backward in reverse topological order in O(1) pass. ^QvK8ijY8

Optimizer Update Step ^0dFABy5j

W.data.add_(-lr * grad_W) ^Zlw7Zhzd

Adjusts weights against the direction of steepest loss ascent. ^YSP5Cdhx

optimizer.zero_grad( set_to_none=True) ^egbzYuRb

Frees accumulated gradient buffers to prevent gradient leakage across training steps. ^2F2HWVC8

Numerical Stability in Deep Nets: Gradient clipping bounds parameter updates. AMP dynamic loss scaling avoids FP16 underflow to zero on subtle weight adjustments. ^CcyzWjls

Input Tensor a_0 ^hHghJM5W

Affine Linear Sum Wx+b ^aYeXZ7Jk

Activation Gate sigma(z) ^jt8sHs6r

Loss Criterion L(y, y_hat) ^1fM4Nv7Y

Accumulate Gradients ^uHyxJ7eY

Compute Loss Adjoint dL/dy_hat ^2laCxkzR

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "1uPWqxtuVPBc8Wov",
      "type": "rectangle",
      "x": 560.0,
      "y": 37.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4392996,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "ELj8b3Ti"
        },
        {
          "type": "arrow",
          "id": "nrkurFha"
        },
        {
          "type": "arrow",
          "id": "d5DenvVd"
        },
        {
          "type": "arrow",
          "id": "5KQmw2vj"
        }
      ],
      "updated": 1789189625740,
      "link": null,
      "locked": false
    },
    {
      "id": "ELj8b3Ti",
      "type": "text",
      "x": 610.0,
      "y": 57.5,
      "width": 81.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 463776,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625740,
      "link": null,
      "locked": false,
      "text": "Libraries",
      "rawText": "Libraries",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "1uPWqxtuVPBc8Wov",
      "originalText": "Libraries",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "MMdXLhDgOXP6plle",
      "type": "rectangle",
      "x": 880.0,
      "y": -5.5,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1467538,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "nyTthEEo"
        },
        {
          "type": "arrow",
          "id": "nrkurFha"
        }
      ],
      "updated": 1789189625740,
      "link": null,
      "locked": false
    },
    {
      "id": "nyTthEEo",
      "type": "text",
      "x": 907.5,
      "y": 15.0,
      "width": 126.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3646730,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625740,
      "link": null,
      "locked": false,
      "text": "torch.autograd",
      "rawText": "torch.autograd",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "MMdXLhDgOXP6plle",
      "originalText": "torch.autograd",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "nrkurFha",
      "type": "arrow",
      "x": 741.0,
      "y": 69.0,
      "width": 139.0,
      "height": 42.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 207530,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625740,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          -42.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "1uPWqxtuVPBc8Wov",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "MMdXLhDgOXP6plle",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "sWkNgRHxECnHAfoy",
      "type": "rectangle",
      "x": 880.0,
      "y": 79.5,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7027882,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "azDz0XxT"
        },
        {
          "type": "arrow",
          "id": "d5DenvVd"
        }
      ],
      "updated": 1789189625740,
      "link": null,
      "locked": false
    },
    {
      "id": "azDz0XxT",
      "type": "text",
      "x": 934.5,
      "y": 100.0,
      "width": 72.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5953969,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625740,
      "link": null,
      "locked": false,
      "text": "torch.nn",
      "rawText": "torch.nn",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "sWkNgRHxECnHAfoy",
      "originalText": "torch.nn",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "d5DenvVd",
      "type": "arrow",
      "x": 741.0,
      "y": 69.0,
      "width": 139.0,
      "height": 42.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2702098,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          42.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "1uPWqxtuVPBc8Wov",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "sWkNgRHxECnHAfoy",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "I0gTlI3m48LDJMzY",
      "type": "rectangle",
      "x": 560.0,
      "y": 511.875,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6682913,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "HpBZXTRb"
        },
        {
          "type": "arrow",
          "id": "nY25RXf6"
        },
        {
          "type": "arrow",
          "id": "tI7X1bM3"
        },
        {
          "type": "arrow",
          "id": "qwnOcMIy"
        },
        {
          "type": "arrow",
          "id": "wp5Jqxfg"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "HpBZXTRb",
      "type": "text",
      "x": 619.0,
      "y": 532.4,
      "width": 63.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5931886,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "Methods",
      "rawText": "Methods",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "I0gTlI3m48LDJMzY",
      "originalText": "Methods",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "XKS2DOGVT5vIcqiV",
      "type": "rectangle",
      "x": 560.0,
      "y": 1150.0,
      "width": 181.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4494647,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "RTIOL091"
        },
        {
          "type": "arrow",
          "id": "UFmOxJPQ"
        },
        {
          "type": "arrow",
          "id": "r3zUHjbU"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "RTIOL091",
      "type": "text",
      "x": 596.5,
      "y": 1170.5,
      "width": 108.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4726916,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "Architecture",
      "rawText": "Architecture",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "XKS2DOGVT5vIcqiV",
      "originalText": "Architecture",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "rWMA8MNIRApKY2C5",
      "type": "rectangle",
      "x": 140.0,
      "y": 588.0,
      "width": 220.0,
      "height": 75.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9142772,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "RY1mJDss"
        },
        {
          "type": "arrow",
          "id": "5KQmw2vj"
        },
        {
          "type": "arrow",
          "id": "nY25RXf6"
        },
        {
          "type": "arrow",
          "id": "UFmOxJPQ"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "RY1mJDss",
      "type": "text",
      "x": 164.5,
      "y": 602.5,
      "width": 171.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8966977,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "Computational Graph\n& Backpropagation",
      "rawText": "Computational Graph & Backpropagation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "rWMA8MNIRApKY2C5",
      "originalText": "Computational Graph\n& Backpropagation",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "5KQmw2vj",
      "type": "arrow",
      "x": 360.0,
      "y": 625.5,
      "width": 200.0,
      "height": 556.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2504353,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          200.0,
          -556.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "rWMA8MNIRApKY2C5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "1uPWqxtuVPBc8Wov",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "nY25RXf6",
      "type": "arrow",
      "x": 360.0,
      "y": 625.5,
      "width": 200.0,
      "height": 81.625,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 165823,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          200.0,
          -81.625
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "rWMA8MNIRApKY2C5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "I0gTlI3m48LDJMzY",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "UFmOxJPQ",
      "type": "arrow",
      "x": 360.0,
      "y": 625.5,
      "width": 200.0,
      "height": 556.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6817319,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          200.0,
          556.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "rWMA8MNIRApKY2C5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "XKS2DOGVT5vIcqiV",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "MajGOjumYp5v9Pyu",
      "type": "rectangle",
      "x": 880.0,
      "y": 267.0,
      "width": 200.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8851229,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "1e4WJEcU"
        },
        {
          "type": "arrow",
          "id": "tI7X1bM3"
        },
        {
          "type": "arrow",
          "id": "Ol7o2Za8"
        },
        {
          "type": "arrow",
          "id": "tMeabgdq"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "1e4WJEcU",
      "type": "text",
      "x": 899.0,
      "y": 276.0,
      "width": 162.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9001808,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "Forward Activation\nPass",
      "rawText": "Forward Activation Pass",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "MajGOjumYp5v9Pyu",
      "originalText": "Forward Activation\nPass",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "tI7X1bM3",
      "type": "arrow",
      "x": 741.0,
      "y": 543.875,
      "width": 139.0,
      "height": 244.875,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4525573,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          -244.875
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "I0gTlI3m48LDJMzY",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "MajGOjumYp5v9Pyu",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "NDqp3Kus5hLhXtM3",
      "type": "rectangle",
      "x": 1200.0,
      "y": 220.0,
      "width": 240.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2073902,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "uo1CsceK"
        },
        {
          "type": "arrow",
          "id": "Ol7o2Za8"
        },
        {
          "type": "arrow",
          "id": "sqQxj9ir"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "uo1CsceK",
      "type": "text",
      "x": 1234.5,
      "y": 229.0,
      "width": 171.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9315037,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "z = torch.matmul(W,\na_prev) + b",
      "rawText": "z = torch.matmul(W, a_prev) + b",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "NDqp3Kus5hLhXtM3",
      "originalText": "z = torch.matmul(W,\na_prev) + b",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Ol7o2Za8",
      "type": "arrow",
      "x": 1080.0,
      "y": 299.0,
      "width": 120.0,
      "height": 47.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1429248,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          -47.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "MajGOjumYp5v9Pyu",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "NDqp3Kus5hLhXtM3",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "XpkJv4WCswOiJwjs",
      "type": "rectangle",
      "x": 1560.0,
      "y": 220.0,
      "width": 360.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 980419,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "wPSx4d6Z"
        },
        {
          "type": "arrow",
          "id": "sqQxj9ir"
        },
        {
          "type": "arrow",
          "id": "4nALhAd9"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "wPSx4d6Z",
      "type": "text",
      "x": 1587.0,
      "y": 229.0,
      "width": 306.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5085046,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "Computes affine linear weighted\nsum of upstream layer activations.",
      "rawText": "Computes affine linear weighted sum of upstream layer activations.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "XpkJv4WCswOiJwjs",
      "originalText": "Computes affine linear weighted\nsum of upstream layer activations.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "sqQxj9ir",
      "type": "arrow",
      "x": 1440.0,
      "y": 252.0,
      "width": 120.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4330538,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "NDqp3Kus5hLhXtM3",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "XpkJv4WCswOiJwjs",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "OMZR8SWnHZVkrfd7",
      "type": "rectangle",
      "x": 1200.0,
      "y": 314.0,
      "width": 240.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2262148,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "jtqivDyi"
        },
        {
          "type": "arrow",
          "id": "tMeabgdq"
        },
        {
          "type": "arrow",
          "id": "Z2aBcO2a"
        }
      ],
      "updated": 1789189625741,
      "link": null,
      "locked": false
    },
    {
      "id": "jtqivDyi",
      "type": "text",
      "x": 1243.5,
      "y": 334.5,
      "width": 153.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3492030,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "text": "a = torch.relu(z)",
      "rawText": "a = torch.relu(z)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "OMZR8SWnHZVkrfd7",
      "originalText": "a = torch.relu(z)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "tMeabgdq",
      "type": "arrow",
      "x": 1080.0,
      "y": 299.0,
      "width": 120.0,
      "height": 47.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 698061,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625741,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          47.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "MajGOjumYp5v9Pyu",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "OMZR8SWnHZVkrfd7",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "i0NlBumRm69uKTDr",
      "type": "rectangle",
      "x": 1560.0,
      "y": 314.0,
      "width": 360.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 242107,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Qz6JOsFW"
        },
        {
          "type": "arrow",
          "id": "Z2aBcO2a"
        },
        {
          "type": "arrow",
          "id": "cwN3vAav"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "Qz6JOsFW",
      "type": "text",
      "x": 1587.0,
      "y": 323.0,
      "width": 306.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 161679,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "Applies non-linear activation gate\nproducing layer representations.",
      "rawText": "Applies non-linear activation gate producing layer representations.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "i0NlBumRm69uKTDr",
      "originalText": "Applies non-linear activation gate\nproducing layer representations.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Z2aBcO2a",
      "type": "arrow",
      "x": 1440.0,
      "y": 346.0,
      "width": 120.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2306921,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "OMZR8SWnHZVkrfd7",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "i0NlBumRm69uKTDr",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "8TEbHoXLtcEAoGDJ",
      "type": "rectangle",
      "x": 2060.0,
      "y": 236.5,
      "width": 380.0,
      "height": 125.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4558321,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "qGJIGMgb"
        },
        {
          "type": "arrow",
          "id": "4nALhAd9"
        },
        {
          "type": "arrow",
          "id": "cwN3vAav"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "qGJIGMgb",
      "type": "text",
      "x": 2101.5,
      "y": 241.5,
      "width": 297.0,
      "height": 115.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8490883,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "Activation Caching Requirement:\nIntermediate tensors a_prev and z\nmust be retained in memory during\nforward pass to compute gradients\nduring backward pass.",
      "rawText": "Activation Caching Requirement: Intermediate tensors a_prev and z must be retained in memory during forward pass to compute gradients during backward pass.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "8TEbHoXLtcEAoGDJ",
      "originalText": "Activation Caching Requirement:\nIntermediate tensors a_prev and z\nmust be retained in memory during\nforward pass to compute gradients\nduring backward pass.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "4nALhAd9",
      "type": "arrow",
      "x": 1920.0,
      "y": 252.0,
      "width": 140.0,
      "height": 47.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 5475984,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          140.0,
          47.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "XpkJv4WCswOiJwjs",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "8TEbHoXLtcEAoGDJ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "cwN3vAav",
      "type": "arrow",
      "x": 1920.0,
      "y": 346.0,
      "width": 140.0,
      "height": 47.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 640617,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          140.0,
          -47.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "i0NlBumRm69uKTDr",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "8TEbHoXLtcEAoGDJ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "BEFiNcrVbWd095Hb",
      "type": "rectangle",
      "x": 880.0,
      "y": 510.0,
      "width": 200.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1403386,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "b5Zyvsqt"
        },
        {
          "type": "arrow",
          "id": "qwnOcMIy"
        },
        {
          "type": "arrow",
          "id": "Vd5scKFW"
        },
        {
          "type": "arrow",
          "id": "GTf4GKQ6"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "b5Zyvsqt",
      "type": "text",
      "x": 912.5,
      "y": 519.0,
      "width": 135.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2177026,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "Reverse Adjoint\nChain Rule",
      "rawText": "Reverse Adjoint Chain Rule",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "BEFiNcrVbWd095Hb",
      "originalText": "Reverse Adjoint\nChain Rule",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "qwnOcMIy",
      "type": "arrow",
      "x": 741.0,
      "y": 543.875,
      "width": 139.0,
      "height": 1.875,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 3195168,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          -1.875
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "I0gTlI3m48LDJMzY",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "BEFiNcrVbWd095Hb",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "8LvkmbYEPgy2FgdW",
      "type": "rectangle",
      "x": 1200.0,
      "y": 455.5,
      "width": 240.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2467119,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "B5zo4pUo"
        },
        {
          "type": "arrow",
          "id": "Vd5scKFW"
        },
        {
          "type": "arrow",
          "id": "jjBHACZz"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "B5zo4pUo",
      "type": "text",
      "x": 1225.5,
      "y": 464.5,
      "width": 189.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6001662,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "delta = W_next.T @\ndelta_next * relu'(z)",
      "rawText": "delta = W_next.T @ delta_next * relu'(z)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "8LvkmbYEPgy2FgdW",
      "originalText": "delta = W_next.T @\ndelta_next * relu'(z)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Vd5scKFW",
      "type": "arrow",
      "x": 1080.0,
      "y": 542.0,
      "width": 120.0,
      "height": 54.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9849817,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          -54.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "BEFiNcrVbWd095Hb",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "8LvkmbYEPgy2FgdW",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "1Kn5stAkGHoNlOTY",
      "type": "rectangle",
      "x": 1560.0,
      "y": 448.0,
      "width": 360.0,
      "height": 79.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9880992,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "cvpGUYxq"
        },
        {
          "type": "arrow",
          "id": "jjBHACZz"
        },
        {
          "type": "arrow",
          "id": "gIoSwTDT"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "cvpGUYxq",
      "type": "text",
      "x": 1600.5,
      "y": 453.0,
      "width": 279.0,
      "height": 69.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4924754,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "Propagates adjoint error vector\ndelta upstream via transposed\nweights and local derivative.",
      "rawText": "Propagates adjoint error vector delta upstream via transposed weights and local derivative.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "1Kn5stAkGHoNlOTY",
      "originalText": "Propagates adjoint error vector\ndelta upstream via transposed\nweights and local derivative.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "jjBHACZz",
      "type": "arrow",
      "x": 1440.0,
      "y": 487.5,
      "width": 120.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 5077713,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "8LvkmbYEPgy2FgdW",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "1Kn5stAkGHoNlOTY",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "UCmB8SA9yYAKmiVA",
      "type": "rectangle",
      "x": 1200.0,
      "y": 557.0,
      "width": 240.0,
      "height": 79.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4260980,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "fX7fszKZ"
        },
        {
          "type": "arrow",
          "id": "GTf4GKQ6"
        },
        {
          "type": "arrow",
          "id": "36ZNbXOB"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "fX7fszKZ",
      "type": "text",
      "x": 1239.0,
      "y": 562.0,
      "width": 162.0,
      "height": 69.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1595171,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "grad_W =\ntorch.outer(delta,\na_prev)",
      "rawText": "grad_W = torch.outer(delta, a_prev)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "UCmB8SA9yYAKmiVA",
      "originalText": "grad_W =\ntorch.outer(delta,\na_prev)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "GTf4GKQ6",
      "type": "arrow",
      "x": 1080.0,
      "y": 542.0,
      "width": 120.0,
      "height": 54.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 608546,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          54.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "BEFiNcrVbWd095Hb",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "UCmB8SA9yYAKmiVA",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "lpYg7IDa5aQSx3EB",
      "type": "rectangle",
      "x": 1560.0,
      "y": 557.0,
      "width": 360.0,
      "height": 79.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6924936,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "L9Hq6O8q"
        },
        {
          "type": "arrow",
          "id": "36ZNbXOB"
        },
        {
          "type": "arrow",
          "id": "sfLkZyjH"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "L9Hq6O8q",
      "type": "text",
      "x": 1596.0,
      "y": 562.0,
      "width": 288.0,
      "height": 69.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3813709,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "Calculates exact weight gradient\nas outer product of error and\nactivations.",
      "rawText": "Calculates exact weight gradient as outer product of error and activations.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "lpYg7IDa5aQSx3EB",
      "originalText": "Calculates exact weight gradient\nas outer product of error and\nactivations.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "36ZNbXOB",
      "type": "arrow",
      "x": 1440.0,
      "y": 596.5,
      "width": 120.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 2458740,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "UCmB8SA9yYAKmiVA",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "lpYg7IDa5aQSx3EB",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "CehU7XUO27X5FoT9",
      "type": "rectangle",
      "x": 2060.0,
      "y": 468.0,
      "width": 380.0,
      "height": 148.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4020429,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "QvK8ijY8"
        },
        {
          "type": "arrow",
          "id": "gIoSwTDT"
        },
        {
          "type": "arrow",
          "id": "sfLkZyjH"
        }
      ],
      "updated": 1789189625742,
      "link": null,
      "locked": false
    },
    {
      "id": "QvK8ijY8",
      "type": "text",
      "x": 2097.0,
      "y": 473.0,
      "width": 306.0,
      "height": 138.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6386812,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625742,
      "link": null,
      "locked": false,
      "text": "Reverse-Mode Auto-Differentiation:\nChain Rule: dL/dW = delta *\n(a_prev)^T\nAdjoint error vectors propagate\nperturbation backward in reverse\ntopological order in O(1) pass.",
      "rawText": "Reverse-Mode Auto-Differentiation: Chain Rule: dL/dW = delta * (a_prev)^T Adjoint error vectors propagate perturbation backward in reverse topological order in O(1) pass.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "CehU7XUO27X5FoT9",
      "originalText": "Reverse-Mode Auto-Differentiation:\nChain Rule: dL/dW = delta *\n(a_prev)^T\nAdjoint error vectors propagate\nperturbation backward in reverse\ntopological order in O(1) pass.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "gIoSwTDT",
      "type": "arrow",
      "x": 1920.0,
      "y": 487.5,
      "width": 140.0,
      "height": 54.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6693853,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          140.0,
          54.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "1Kn5stAkGHoNlOTY",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "CehU7XUO27X5FoT9",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "sfLkZyjH",
      "type": "arrow",
      "x": 1920.0,
      "y": 596.5,
      "width": 140.0,
      "height": 54.5,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9724248,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          140.0,
          -54.5
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "lpYg7IDa5aQSx3EB",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "CehU7XUO27X5FoT9",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "nMIFfyn9s4KaNTtt",
      "type": "rectangle",
      "x": 880.0,
      "y": 756.75,
      "width": 200.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2399957,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "0dFABy5j"
        },
        {
          "type": "arrow",
          "id": "wp5Jqxfg"
        },
        {
          "type": "arrow",
          "id": "kFHrkpQY"
        },
        {
          "type": "arrow",
          "id": "ftTh8xV5"
        }
      ],
      "updated": 1789189625743,
      "link": null,
      "locked": false
    },
    {
      "id": "0dFABy5j",
      "type": "text",
      "x": 908.0,
      "y": 765.8,
      "width": 144.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7476645,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "text": "Optimizer Update\nStep",
      "rawText": "Optimizer Update Step",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "nMIFfyn9s4KaNTtt",
      "originalText": "Optimizer Update\nStep",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "wp5Jqxfg",
      "type": "arrow",
      "x": 741.0,
      "y": 543.875,
      "width": 139.0,
      "height": 244.875,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6150830,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          244.875
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "I0gTlI3m48LDJMzY",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "nMIFfyn9s4KaNTtt",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "TsVOUpSx3qsb0o5g",
      "type": "rectangle",
      "x": 1200.0,
      "y": 706.0,
      "width": 240.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5690469,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Zlw7Zhzd"
        },
        {
          "type": "arrow",
          "id": "kFHrkpQY"
        },
        {
          "type": "arrow",
          "id": "n3u8Q7D4"
        }
      ],
      "updated": 1789189625743,
      "link": null,
      "locked": false
    },
    {
      "id": "Zlw7Zhzd",
      "type": "text",
      "x": 1243.5,
      "y": 715.0,
      "width": 153.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5939023,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "text": "W.data.add_(-lr *\ngrad_W)",
      "rawText": "W.data.add_(-lr * grad_W)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "TsVOUpSx3qsb0o5g",
      "originalText": "W.data.add_(-lr *\ngrad_W)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "kFHrkpQY",
      "type": "arrow",
      "x": 1080.0,
      "y": 788.75,
      "width": 120.0,
      "height": 50.75,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6506110,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          -50.75
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "nMIFfyn9s4KaNTtt",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "TsVOUpSx3qsb0o5g",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "oZMRkBVgCbJp0sZw",
      "type": "rectangle",
      "x": 1560.0,
      "y": 706.0,
      "width": 360.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2120032,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "YSP5Cdhx"
        },
        {
          "type": "arrow",
          "id": "n3u8Q7D4"
        },
        {
          "type": "arrow",
          "id": "pTqVm2Y0"
        }
      ],
      "updated": 1789189625743,
      "link": null,
      "locked": false
    },
    {
      "id": "YSP5Cdhx",
      "type": "text",
      "x": 1587.0,
      "y": 715.0,
      "width": 306.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8175515,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "text": "Adjusts weights against the\ndirection of steepest loss ascent.",
      "rawText": "Adjusts weights against the direction of steepest loss ascent.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "oZMRkBVgCbJp0sZw",
      "originalText": "Adjusts weights against the\ndirection of steepest loss ascent.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "n3u8Q7D4",
      "type": "arrow",
      "x": 1440.0,
      "y": 738.0,
      "width": 120.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 8987909,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "TsVOUpSx3qsb0o5g",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "oZMRkBVgCbJp0sZw",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "0zAFldV3pRnDYgwh",
      "type": "rectangle",
      "x": 1200.0,
      "y": 807.5,
      "width": 240.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3213797,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "egbzYuRb"
        },
        {
          "type": "arrow",
          "id": "ftTh8xV5"
        },
        {
          "type": "arrow",
          "id": "HPnTsQFq"
        }
      ],
      "updated": 1789189625743,
      "link": null,
      "locked": false
    },
    {
      "id": "egbzYuRb",
      "type": "text",
      "x": 1230.0,
      "y": 816.5,
      "width": 180.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5860729,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "text": "optimizer.zero_grad(\nset_to_none=True)",
      "rawText": "optimizer.zero_grad( set_to_none=True)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "0zAFldV3pRnDYgwh",
      "originalText": "optimizer.zero_grad(\nset_to_none=True)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "ftTh8xV5",
      "type": "arrow",
      "x": 1080.0,
      "y": 788.75,
      "width": 120.0,
      "height": 50.75,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6811839,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          50.75
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "nMIFfyn9s4KaNTtt",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "0zAFldV3pRnDYgwh",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "Qd5TiOQoZYWHv9Yz",
      "type": "rectangle",
      "x": 1560.0,
      "y": 800.0,
      "width": 360.0,
      "height": 79.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1430870,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "2F2HWVC8"
        },
        {
          "type": "arrow",
          "id": "HPnTsQFq"
        },
        {
          "type": "arrow",
          "id": "wAMEDnTY"
        }
      ],
      "updated": 1789189625743,
      "link": null,
      "locked": false
    },
    {
      "id": "2F2HWVC8",
      "type": "text",
      "x": 1587.0,
      "y": 805.0,
      "width": 306.0,
      "height": 69.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9465334,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "text": "Frees accumulated gradient buffers\nto prevent gradient leakage across\ntraining steps.",
      "rawText": "Frees accumulated gradient buffers to prevent gradient leakage across training steps.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "Qd5TiOQoZYWHv9Yz",
      "originalText": "Frees accumulated gradient buffers\nto prevent gradient leakage across\ntraining steps.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "HPnTsQFq",
      "type": "arrow",
      "x": 1440.0,
      "y": 839.5,
      "width": 120.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 6068304,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625743,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          120.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "0zAFldV3pRnDYgwh",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "Qd5TiOQoZYWHv9Yz",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "ThvtMNl8JOIrpY9X",
      "type": "rectangle",
      "x": 2060.0,
      "y": 714.75,
      "width": 380.0,
      "height": 148.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7750531,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "CcyzWjls"
        },
        {
          "type": "arrow",
          "id": "pTqVm2Y0"
        },
        {
          "type": "arrow",
          "id": "wAMEDnTY"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "CcyzWjls",
      "type": "text",
      "x": 2088.0,
      "y": 719.8,
      "width": 324.0,
      "height": 138.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9695917,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Numerical Stability in Deep Nets:\nGradient clipping bounds parameter\nupdates.\nAMP dynamic loss scaling avoids FP16\nunderflow to zero on subtle weight\nadjustments.",
      "rawText": "Numerical Stability in Deep Nets: Gradient clipping bounds parameter updates. AMP dynamic loss scaling avoids FP16 underflow to zero on subtle weight adjustments.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "ThvtMNl8JOIrpY9X",
      "originalText": "Numerical Stability in Deep Nets:\nGradient clipping bounds parameter\nupdates.\nAMP dynamic loss scaling avoids FP16\nunderflow to zero on subtle weight\nadjustments.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "pTqVm2Y0",
      "type": "arrow",
      "x": 1920.0,
      "y": 738.0,
      "width": 140.0,
      "height": 50.75,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 8092143,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          140.0,
          50.75
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "oZMRkBVgCbJp0sZw",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "ThvtMNl8JOIrpY9X",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "wAMEDnTY",
      "type": "arrow",
      "x": 1920.0,
      "y": 839.5,
      "width": 140.0,
      "height": 50.75,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 5418953,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          140.0,
          -50.75
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "Qd5TiOQoZYWHv9Yz",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "ThvtMNl8JOIrpY9X",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "HH9XWu9EtHkGRg1o",
      "type": "rectangle",
      "x": 880.0,
      "y": 1150.0,
      "width": 190.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5574217,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "hHghJM5W"
        },
        {
          "type": "arrow",
          "id": "r3zUHjbU"
        },
        {
          "type": "arrow",
          "id": "W43Qx4Fk"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "hHghJM5W",
      "type": "text",
      "x": 903.0,
      "y": 1170.5,
      "width": 144.0,
      "height": 23.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 3701635,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Input Tensor a_0",
      "rawText": "Input Tensor a_0",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "HH9XWu9EtHkGRg1o",
      "originalText": "Input Tensor a_0",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "r3zUHjbU",
      "type": "arrow",
      "x": 741.0,
      "y": 1182.0,
      "width": 139.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1623762,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "XKS2DOGVT5vIcqiV",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "HH9XWu9EtHkGRg1o",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "c5QnEsmKwYdHJYtE",
      "type": "rectangle",
      "x": 1135.0,
      "y": 1150.0,
      "width": 190.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9742783,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "aYeXZ7Jk"
        },
        {
          "type": "arrow",
          "id": "W43Qx4Fk"
        },
        {
          "type": "arrow",
          "id": "dsXuSb0r"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "aYeXZ7Jk",
      "type": "text",
      "x": 1171.5,
      "y": 1159.0,
      "width": 117.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 5169603,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Affine Linear\nSum Wx+b",
      "rawText": "Affine Linear Sum Wx+b",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "c5QnEsmKwYdHJYtE",
      "originalText": "Affine Linear\nSum Wx+b",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "W43Qx4Fk",
      "type": "arrow",
      "x": 1070.0,
      "y": 1182.0,
      "width": 65.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4997288,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          65.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "HH9XWu9EtHkGRg1o",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "c5QnEsmKwYdHJYtE",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "PSLnKRMgH1FRqMgt",
      "type": "rectangle",
      "x": 1390.0,
      "y": 1150.0,
      "width": 190.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2706295,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "jt8sHs6r"
        },
        {
          "type": "arrow",
          "id": "dsXuSb0r"
        },
        {
          "type": "arrow",
          "id": "wKW3qy0J"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "jt8sHs6r",
      "type": "text",
      "x": 1417.5,
      "y": 1159.0,
      "width": 135.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1588400,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Activation Gate\nsigma(z)",
      "rawText": "Activation Gate sigma(z)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "PSLnKRMgH1FRqMgt",
      "originalText": "Activation Gate\nsigma(z)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "dsXuSb0r",
      "type": "arrow",
      "x": 1325.0,
      "y": 1182.0,
      "width": 65.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1589839,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          65.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "c5QnEsmKwYdHJYtE",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "PSLnKRMgH1FRqMgt",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "q8yX1C7x1gKNSGj9",
      "type": "rectangle",
      "x": 1645.0,
      "y": 1150.0,
      "width": 190.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 6078527,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "1fM4Nv7Y"
        },
        {
          "type": "arrow",
          "id": "wKW3qy0J"
        },
        {
          "type": "arrow",
          "id": "kiANepy4"
        },
        {
          "type": "arrow",
          "id": "nG4atrak"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "1fM4Nv7Y",
      "type": "text",
      "x": 1677.0,
      "y": 1159.0,
      "width": 126.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8899400,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Loss Criterion\nL(y, y_hat)",
      "rawText": "Loss Criterion L(y, y_hat)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "q8yX1C7x1gKNSGj9",
      "originalText": "Loss Criterion\nL(y, y_hat)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "wKW3qy0J",
      "type": "arrow",
      "x": 1580.0,
      "y": 1182.0,
      "width": 65.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 9636812,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          65.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "PSLnKRMgH1FRqMgt",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "q8yX1C7x1gKNSGj9",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "cBPmeemcrYTRtpgm",
      "type": "rectangle",
      "x": 1900.0,
      "y": 1150.0,
      "width": 190.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7437470,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "uHyxJ7eY"
        },
        {
          "type": "arrow",
          "id": "kiANepy4"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "uHyxJ7eY",
      "type": "text",
      "x": 1950.0,
      "y": 1159.0,
      "width": 90.0,
      "height": 46.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 8556655,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Accumulate\nGradients",
      "rawText": "Accumulate Gradients",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "cBPmeemcrYTRtpgm",
      "originalText": "Accumulate\nGradients",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "kiANepy4",
      "type": "arrow",
      "x": 1835.0,
      "y": 1182.0,
      "width": 65.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 8930477,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          65.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "q8yX1C7x1gKNSGj9",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "cBPmeemcrYTRtpgm",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "rxPeO7XjQ3pxd7Q4",
      "type": "rectangle",
      "x": 1645.0,
      "y": 1030.0,
      "width": 190.0,
      "height": 79.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 9342704,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "2laCxkzR"
        },
        {
          "type": "arrow",
          "id": "nG4atrak"
        }
      ],
      "updated": 1789189625744,
      "link": null,
      "locked": false
    },
    {
      "id": "2laCxkzR",
      "type": "text",
      "x": 1686.0,
      "y": 1035.0,
      "width": 108.0,
      "height": 69.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 7514620,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "text": "Compute Loss\nAdjoint\ndL/dy_hat",
      "rawText": "Compute Loss Adjoint dL/dy_hat",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "rxPeO7XjQ3pxd7Q4",
      "originalText": "Compute Loss\nAdjoint\ndL/dy_hat",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "nG4atrak",
      "type": "arrow",
      "x": 1740.0,
      "y": 1150.0,
      "width": 0.0,
      "height": 41.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 4,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 4136896,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189625744,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          0.0,
          -41.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "q8yX1C7x1gKNSGj9",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "rxPeO7XjQ3pxd7Q4",
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
    "currentItemTextAlign": "center",
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
