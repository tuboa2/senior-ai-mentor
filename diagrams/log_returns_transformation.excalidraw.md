---

excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Log-Returns
Transformation

## 🌿 1. Concept Intuition & Mental Model
Log returns (continuously compounded returns) offer several decisive mathematical advantages over simple percentage changes:
- **Time Additivity:** Multi-period compounding is linear: $r_{0 \to T} = \sum_{t=1}^T r_t$.
- **Symmetry:** Equal percentage upward and downward shocks are represented symmetrically.
- **Statistical Tractability:** Prices are bounded below by zero, whereas log-prices and log-returns map smoothly to $(-\infty, +\infty)$.

---

## 📐 2. Mathematical Foundations (KaTeX / LaTeX)
### Mathematical Equivalence Formulation

$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

Relation to simple returns $R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$:
$$1 + R_t = \frac{P_t}{P_{t-1}} \implies r_t = \ln(1 + R_t)$$

First-order Taylor expansion around $R_t \approx 0$:
$$\ln(1 + R_t) = R_t - \frac{R_t^2}{2} + \frac{R_t^3}{3} - \dots \approx R_t$$

For small daily returns ($|R_t| < 0.05$), simple and log returns are almost indistinguishable, but over multi-day horizons additivity makes log returns vastly superior.

---

## 💡 3. Senior Engineering & Performance Notes
- **Boundary Condition Trap:** The first row after `.diff(1)` or `.shift(1)` evaluates to `NaN`. Always drop or handle row $t=0$ using `.dropna()` before feeding downstream models.
- **Performance (Cython Vectorization):** `np.log(df).diff()` is significantly faster than `np.log(df / df.shift(1))` because `DataFrame.diff()` executes vectorized in Cython without allocating intermediate shifted arrays.

---

# Excalidraw Data

## Text Elements
Log-Returns Transformation ^KoUWoXVi

Libraries ^M42V22WN

pandas ^UhN4PTH6

numpy ^qC0I8eC2

Methods ^Zlb4m7s3

Natural Log Differencing ^CxpbxqHZ

np.log(df) ^yZ1vaLLk

Computes the natural logarithm of every price value. ^5gHO9VXX

df.diff(1) ^seTFwZEr

Computes the difference between the current row and the previous row (row[t] - row[t-1]) ^muff6IHL

Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference:   log_returns = np.log(prices_df).diff() ^SJLufNpv

Ratio with Lag Shift ^JlWDG8HO

df.shift(1) ^Fj2gDtSb

Moves every row down by 1 position (bringing yesterday's price into today's row). ^qZ9k5vhM

np.log(df / df.shift(1)) ^QuNNev56

Divides today's price by yesterday's price, then takes the natural log. ^49VTJ1HG

Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython. ^JsUdbxhs

From Percentage Change ^YQ9J4Nkc

df.pct_change() ^ES0RvBad

Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday. ^T2iDFjKV

np.log1p(simple_returns) ^qqrhgjxf

Computes log(1 + R) with extra precision for numbers very close to zero. ^mh1YuZuP

Architecture ^2B16c5rR

Extract Close Prices ^vrtDMCG9

Assemble Price Matrix ^R5WCkWko

Apply Log Transformation ^olLl4H8c

Clean the Boundary Row ^oCvyjJlE

Combine into a single DataFrame ^HkVTMxhF

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "NTotTICaO6fv0xn4",
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
      "seed": 2606467,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "KoUWoXVi"
        },
        {
          "type": "arrow",
          "id": "7uQQdxcE"
        },
        {
          "type": "arrow",
          "id": "ohS9GBlK"
        },
        {
          "type": "arrow",
          "id": "hujqfGvH"
        }
      ],
      "updated": 1789187288006,
      "link": null,
      "locked": false
    },
    {
      "id": "KoUWoXVi",
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
      "seed": 5270342,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288006,
      "link": null,
      "locked": false,
      "text": "Log-Returns\nTransformation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "NTotTICaO6fv0xn4",
      "originalText": "Log-Returns\nTransformation",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "ElqzI8dcKHBvBCDS",
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
      "seed": 5140876,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "M42V22WN"
        },
        {
          "type": "arrow",
          "id": "7uQQdxcE"
        },
        {
          "type": "arrow",
          "id": "d6pVCIBE"
        },
        {
          "type": "arrow",
          "id": "8lOXpZNV"
        }
      ],
      "updated": 1789187288006,
      "link": null,
      "locked": false
    },
    {
      "id": "M42V22WN",
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
      "seed": 687728,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288006,
      "link": null,
      "locked": false,
      "text": "Libraries",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "ElqzI8dcKHBvBCDS",
      "originalText": "Libraries",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "7uQQdxcE",
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
      "seed": 1766593,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288006,
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
        "elementId": "NTotTICaO6fv0xn4",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "ElqzI8dcKHBvBCDS",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "yYVIASJlVUhlZSEO",
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
      "seed": 9240293,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "UhN4PTH6"
        },
        {
          "type": "arrow",
          "id": "d6pVCIBE"
        }
      ],
      "updated": 1789187288006,
      "link": null,
      "locked": false
    },
    {
      "id": "UhN4PTH6",
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
      "seed": 4942691,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288006,
      "link": null,
      "locked": false,
      "text": "pandas",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "yYVIASJlVUhlZSEO",
      "originalText": "pandas",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "d6pVCIBE",
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
      "seed": 3465382,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288006,
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
        "elementId": "ElqzI8dcKHBvBCDS",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "yYVIASJlVUhlZSEO",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "31uwQTg2nvQ4YBm1",
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
      "seed": 6870957,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "qC0I8eC2"
        },
        {
          "type": "arrow",
          "id": "8lOXpZNV"
        }
      ],
      "updated": 1789187288018,
      "link": null,
      "locked": false
    },
    {
      "id": "qC0I8eC2",
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
      "seed": 2697294,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288018,
      "link": null,
      "locked": false,
      "text": "numpy",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "31uwQTg2nvQ4YBm1",
      "originalText": "numpy",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "8lOXpZNV",
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
      "seed": 7538302,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288018,
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
        "elementId": "ElqzI8dcKHBvBCDS",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "31uwQTg2nvQ4YBm1",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "SqMXhT8elZY8iS3H",
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
      "seed": 3433587,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Zlb4m7s3"
        },
        {
          "type": "arrow",
          "id": "ohS9GBlK"
        },
        {
          "type": "arrow",
          "id": "A7IFpupt"
        },
        {
          "type": "arrow",
          "id": "a5cMJF63"
        },
        {
          "type": "arrow",
          "id": "NpjpcOEs"
        }
      ],
      "updated": 1789187288018,
      "link": null,
      "locked": false
    },
    {
      "id": "Zlb4m7s3",
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
      "seed": 8224650,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288018,
      "link": null,
      "locked": false,
      "text": "Methods",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "SqMXhT8elZY8iS3H",
      "originalText": "Methods",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "ohS9GBlK",
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
      "seed": 8561239,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288018,
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
        "elementId": "NTotTICaO6fv0xn4",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "SqMXhT8elZY8iS3H",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "oER84kbd7mVrUUZI",
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
      "seed": 3955526,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "CxpbxqHZ"
        },
        {
          "type": "arrow",
          "id": "A7IFpupt"
        },
        {
          "type": "arrow",
          "id": "9UBiPAVY"
        },
        {
          "type": "arrow",
          "id": "iOE28Lfo"
        }
      ],
      "updated": 1789187288018,
      "link": null,
      "locked": false
    },
    {
      "id": "CxpbxqHZ",
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
      "seed": 8234891,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288018,
      "link": null,
      "locked": false,
      "text": "Natural Log Differencing",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "oER84kbd7mVrUUZI",
      "originalText": "Natural Log Differencing",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "A7IFpupt",
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
      "seed": 2486769,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "SqMXhT8elZY8iS3H",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "oER84kbd7mVrUUZI",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "ygvDQgjmq1aKohwm",
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
      "seed": 5141855,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "yZ1vaLLk"
        },
        {
          "type": "arrow",
          "id": "9UBiPAVY"
        },
        {
          "type": "arrow",
          "id": "ba5qnlY3"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "yZ1vaLLk",
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
      "seed": 5216142,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "np.log(df)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "ygvDQgjmq1aKohwm",
      "originalText": "np.log(df)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "9UBiPAVY",
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
      "seed": 2349391,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "oER84kbd7mVrUUZI",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "ygvDQgjmq1aKohwm",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "zXalRUaXsOsQcBs3",
      "type": "rectangle",
      "x": 1425.0,
      "y": 220.0,
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
      "seed": 8865299,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "5gHO9VXX"
        },
        {
          "type": "arrow",
          "id": "ba5qnlY3"
        },
        {
          "type": "arrow",
          "id": "5LDgoT5K"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "5gHO9VXX",
      "type": "text",
      "x": 1435.0,
      "y": 229.0,
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
      "seed": 3868337,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Computes the natural logarithm of every price value.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "zXalRUaXsOsQcBs3",
      "originalText": "Computes the natural logarithm of every price value.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "ba5qnlY3",
      "type": "arrow",
      "x": 1351.0,
      "y": 252.0,
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
      "seed": 2984461,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "ygvDQgjmq1aKohwm",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "zXalRUaXsOsQcBs3",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "W3Vo6ORSoR4B4gZH",
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
      "seed": 5052396,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "seTFwZEr"
        },
        {
          "type": "arrow",
          "id": "iOE28Lfo"
        },
        {
          "type": "arrow",
          "id": "UfJ87HUf"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "seTFwZEr",
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
      "seed": 6278858,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "df.diff(1)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "W3Vo6ORSoR4B4gZH",
      "originalText": "df.diff(1)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "iOE28Lfo",
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
      "seed": 6898704,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "oER84kbd7mVrUUZI",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "W3Vo6ORSoR4B4gZH",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "bH7izjgu75QgewvQ",
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
      "seed": 2994652,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "muff6IHL"
        },
        {
          "type": "arrow",
          "id": "UfJ87HUf"
        },
        {
          "type": "arrow",
          "id": "SGeDQkBd"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "muff6IHL",
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
      "seed": 1955527,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Computes the difference between the current row and the previous row (row[t] - row[t-1])",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "bH7izjgu75QgewvQ",
      "originalText": "Computes the difference between the current row and the previous row (row[t] - row[t-1])",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "UfJ87HUf",
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
      "seed": 9029363,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "W3Vo6ORSoR4B4gZH",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "bH7izjgu75QgewvQ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "sKkRUfT4uGwbZ9T1",
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
      "seed": 8892240,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "SJLufNpv"
        },
        {
          "type": "arrow",
          "id": "5LDgoT5K"
        },
        {
          "type": "arrow",
          "id": "SGeDQkBd"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "SJLufNpv",
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
      "seed": 1319029,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference:\n  log_returns = np.log(prices_df).diff()",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "sKkRUfT4uGwbZ9T1",
      "originalText": "Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference:\n  log_returns = np.log(prices_df).diff()",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "5LDgoT5K",
      "type": "arrow",
      "x": 1772.0,
      "y": 257.5,
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
      "seed": 2085624,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "zXalRUaXsOsQcBs3",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "sKkRUfT4uGwbZ9T1",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "SGeDQkBd",
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
      "seed": 3796964,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "bH7izjgu75QgewvQ",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "sKkRUfT4uGwbZ9T1",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "7T6Ctw2jbUkIJ2SZ",
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
      "seed": 1111527,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "JlWDG8HO"
        },
        {
          "type": "arrow",
          "id": "a5cMJF63"
        },
        {
          "type": "arrow",
          "id": "grZPdQiQ"
        },
        {
          "type": "arrow",
          "id": "luas0Jgt"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "JlWDG8HO",
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
      "seed": 4649269,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Ratio with Lag Shift",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "7T6Ctw2jbUkIJ2SZ",
      "originalText": "Ratio with Lag Shift",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "a5cMJF63",
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
      "seed": 1566389,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "SqMXhT8elZY8iS3H",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "7T6Ctw2jbUkIJ2SZ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "QECBFvbEtKNLsaBR",
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
      "seed": 7867757,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Fj2gDtSb"
        },
        {
          "type": "arrow",
          "id": "grZPdQiQ"
        },
        {
          "type": "arrow",
          "id": "8e2oWsyO"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "Fj2gDtSb",
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
      "seed": 5023465,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "df.shift(1)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "QECBFvbEtKNLsaBR",
      "originalText": "df.shift(1)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "grZPdQiQ",
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
      "seed": 8327155,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "7T6Ctw2jbUkIJ2SZ",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "QECBFvbEtKNLsaBR",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "RJRnzyPexugiP4yP",
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
      "seed": 2204172,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "qZ9k5vhM"
        },
        {
          "type": "arrow",
          "id": "8e2oWsyO"
        },
        {
          "type": "arrow",
          "id": "tMioVED1"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "qZ9k5vhM",
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
      "seed": 168928,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Moves every row down by 1 position (bringing yesterday's price into today's row).",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "RJRnzyPexugiP4yP",
      "originalText": "Moves every row down by 1 position (bringing yesterday's price into today's row).",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "8e2oWsyO",
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
      "seed": 5823593,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "QECBFvbEtKNLsaBR",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "RJRnzyPexugiP4yP",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "jtaU75XWgfS0nFpj",
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
      "seed": 7595256,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "QuNNev56"
        },
        {
          "type": "arrow",
          "id": "luas0Jgt"
        },
        {
          "type": "arrow",
          "id": "cZZj2T40"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "QuNNev56",
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
      "seed": 7418135,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "np.log(df / df.shift(1))",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "jtaU75XWgfS0nFpj",
      "originalText": "np.log(df / df.shift(1))",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "luas0Jgt",
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
      "seed": 1060413,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "7T6Ctw2jbUkIJ2SZ",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "jtaU75XWgfS0nFpj",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "QPrb9nwxUulbgKR9",
      "type": "rectangle",
      "x": 1425.0,
      "y": 576.0,
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
      "seed": 802964,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "49VTJ1HG"
        },
        {
          "type": "arrow",
          "id": "cZZj2T40"
        },
        {
          "type": "arrow",
          "id": "51MzRjK8"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "49VTJ1HG",
      "type": "text",
      "x": 1435.0,
      "y": 585.0,
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
      "seed": 9220645,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Divides today's price by yesterday's price, then takes the natural log.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "QPrb9nwxUulbgKR9",
      "originalText": "Divides today's price by yesterday's price, then takes the natural log.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "cZZj2T40",
      "type": "arrow",
      "x": 1351.0,
      "y": 608.0,
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
      "seed": 8723787,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
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
        "elementId": "jtaU75XWgfS0nFpj",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "QPrb9nwxUulbgKR9",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "XSyQZKO0OIfAwxqE",
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
      "seed": 141408,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "JsUdbxhs"
        },
        {
          "type": "arrow",
          "id": "tMioVED1"
        },
        {
          "type": "arrow",
          "id": "51MzRjK8"
        }
      ],
      "updated": 1789187288019,
      "link": null,
      "locked": false
    },
    {
      "id": "JsUdbxhs",
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
      "seed": 2057708,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288019,
      "link": null,
      "locked": false,
      "text": "Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "XSyQZKO0OIfAwxqE",
      "originalText": "Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "tMioVED1",
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
      "seed": 4269679,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "RJRnzyPexugiP4yP",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "XSyQZKO0OIfAwxqE",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "51MzRjK8",
      "type": "arrow",
      "x": 1772.0,
      "y": 620.0,
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
      "seed": 9335725,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "QPrb9nwxUulbgKR9",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "XSyQZKO0OIfAwxqE",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "O5lSfgRXSgmUVdtX",
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
      "seed": 3327257,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "YQ9J4Nkc"
        },
        {
          "type": "arrow",
          "id": "NpjpcOEs"
        },
        {
          "type": "arrow",
          "id": "EC1nk54H"
        },
        {
          "type": "arrow",
          "id": "kfC9TDnj"
        }
      ],
      "updated": 1789187288020,
      "link": null,
      "locked": false
    },
    {
      "id": "YQ9J4Nkc",
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
      "seed": 443567,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
      "link": null,
      "locked": false,
      "text": "From Percentage Change",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "O5lSfgRXSgmUVdtX",
      "originalText": "From Percentage Change",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "NpjpcOEs",
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
      "seed": 3475485,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "SqMXhT8elZY8iS3H",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "O5lSfgRXSgmUVdtX",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "VlLg5kS0xwAsZif9",
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
      "seed": 6010088,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "ES0RvBad"
        },
        {
          "type": "arrow",
          "id": "EC1nk54H"
        },
        {
          "type": "arrow",
          "id": "sAHM7fQ7"
        }
      ],
      "updated": 1789187288020,
      "link": null,
      "locked": false
    },
    {
      "id": "ES0RvBad",
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
      "seed": 852565,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
      "link": null,
      "locked": false,
      "text": "df.pct_change()",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "VlLg5kS0xwAsZif9",
      "originalText": "df.pct_change()",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "EC1nk54H",
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
      "seed": 3823567,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "O5lSfgRXSgmUVdtX",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "VlLg5kS0xwAsZif9",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "DBffNJJWN7HikZGU",
      "type": "rectangle",
      "x": 1425.0,
      "y": 708.0,
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
      "seed": 2638650,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "T2iDFjKV"
        },
        {
          "type": "arrow",
          "id": "sAHM7fQ7"
        }
      ],
      "updated": 1789187288020,
      "link": null,
      "locked": false
    },
    {
      "id": "T2iDFjKV",
      "type": "text",
      "x": 1435.0,
      "y": 717.0,
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
      "seed": 9320663,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
      "link": null,
      "locked": false,
      "text": "Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "DBffNJJWN7HikZGU",
      "originalText": "Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "sAHM7fQ7",
      "type": "arrow",
      "x": 1351.0,
      "y": 740.0,
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
      "seed": 2842783,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "VlLg5kS0xwAsZif9",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "DBffNJJWN7HikZGU",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "zJHVrmuegWXNLq0N",
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
      "seed": 8120004,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "qqrhgjxf"
        },
        {
          "type": "arrow",
          "id": "kfC9TDnj"
        },
        {
          "type": "arrow",
          "id": "NQIofqFP"
        }
      ],
      "updated": 1789187288020,
      "link": null,
      "locked": false
    },
    {
      "id": "qqrhgjxf",
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
      "seed": 2488366,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
      "link": null,
      "locked": false,
      "text": "np.log1p(simple_returns)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "zJHVrmuegWXNLq0N",
      "originalText": "np.log1p(simple_returns)",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "kfC9TDnj",
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
      "seed": 2911462,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "O5lSfgRXSgmUVdtX",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "zJHVrmuegWXNLq0N",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "L0sQ2unKVSjkf3sX",
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
      "seed": 3765413,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "mh1YuZuP"
        },
        {
          "type": "arrow",
          "id": "NQIofqFP"
        }
      ],
      "updated": 1789187288020,
      "link": null,
      "locked": false
    },
    {
      "id": "mh1YuZuP",
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
      "seed": 5525396,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
      "link": null,
      "locked": false,
      "text": "Computes log(1 + R) with extra precision for numbers very close to zero.",
      "fontSize": 18,
      "fontFamily": 7,
      "textAlign": "left",
      "verticalAlign": "middle",
      "containerId": "L0sQ2unKVSjkf3sX",
      "originalText": "Computes log(1 + R) with extra precision for numbers very close to zero.",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "NQIofqFP",
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
      "seed": 591452,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
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
        "elementId": "zJHVrmuegWXNLq0N",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "L0sQ2unKVSjkf3sX",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "mI3LvLkW63JJTssr",
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
      "seed": 918748,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "2B16c5rR"
        },
        {
          "type": "arrow",
          "id": "hujqfGvH"
        },
        {
          "type": "arrow",
          "id": "OClky2BH"
        }
      ],
      "updated": 1789187288020,
      "link": null,
      "locked": false
    },
    {
      "id": "2B16c5rR",
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
      "seed": 4318095,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288020,
      "link": null,
      "locked": false,
      "text": "Architecture",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "mI3LvLkW63JJTssr",
      "originalText": "Architecture",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "hujqfGvH",
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
      "seed": 3401262,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
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
        "elementId": "NTotTICaO6fv0xn4",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "mI3LvLkW63JJTssr",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "tsVOx3TGLqxW03aO",
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
      "seed": 2401653,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "vrtDMCG9"
        },
        {
          "type": "arrow",
          "id": "OClky2BH"
        },
        {
          "type": "arrow",
          "id": "Xofjmbip"
        }
      ],
      "updated": 1789187288021,
      "link": null,
      "locked": false
    },
    {
      "id": "vrtDMCG9",
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
      "seed": 7190399,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
      "link": null,
      "locked": false,
      "text": "Extract Close Prices",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "tsVOx3TGLqxW03aO",
      "originalText": "Extract Close Prices",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "OClky2BH",
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
      "seed": 5921023,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
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
        "elementId": "mI3LvLkW63JJTssr",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "tsVOx3TGLqxW03aO",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "4vqOM9o6Bdh6TXSe",
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
      "seed": 299669,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "R5WCkWko"
        },
        {
          "type": "arrow",
          "id": "Xofjmbip"
        },
        {
          "type": "arrow",
          "id": "Z4kSgcFi"
        },
        {
          "type": "arrow",
          "id": "lh1SlhU8"
        }
      ],
      "updated": 1789187288021,
      "link": null,
      "locked": false
    },
    {
      "id": "R5WCkWko",
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
      "seed": 1571039,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
      "link": null,
      "locked": false,
      "text": "Assemble Price Matrix",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "4vqOM9o6Bdh6TXSe",
      "originalText": "Assemble Price Matrix",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Xofjmbip",
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
      "seed": 9042006,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
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
        "elementId": "tsVOx3TGLqxW03aO",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "4vqOM9o6Bdh6TXSe",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "GUx5SnAZx3LEV0Ao",
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
      "seed": 8742193,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "olLl4H8c"
        },
        {
          "type": "arrow",
          "id": "Z4kSgcFi"
        },
        {
          "type": "arrow",
          "id": "RjXDL2j4"
        }
      ],
      "updated": 1789187288021,
      "link": null,
      "locked": false
    },
    {
      "id": "olLl4H8c",
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
      "seed": 2950777,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
      "link": null,
      "locked": false,
      "text": "Apply Log Transformation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "GUx5SnAZx3LEV0Ao",
      "originalText": "Apply Log Transformation",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Z4kSgcFi",
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
      "seed": 3614096,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
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
        "elementId": "4vqOM9o6Bdh6TXSe",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "GUx5SnAZx3LEV0Ao",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "kYKrQTew9E91Aly7",
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
      "seed": 6590502,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "oCvyjJlE"
        },
        {
          "type": "arrow",
          "id": "RjXDL2j4"
        }
      ],
      "updated": 1789187288021,
      "link": null,
      "locked": false
    },
    {
      "id": "oCvyjJlE",
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
      "seed": 4676931,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
      "link": null,
      "locked": false,
      "text": "Clean the Boundary Row",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "kYKrQTew9E91Aly7",
      "originalText": "Clean the Boundary Row",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "RjXDL2j4",
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
      "seed": 9508881,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
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
        "elementId": "GUx5SnAZx3LEV0Ao",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "kYKrQTew9E91Aly7",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "R7bLWD41GP9ol8v5",
      "type": "rectangle",
      "x": 1156.0,
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
      "seed": 5569020,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "HkVTMxhF"
        },
        {
          "type": "arrow",
          "id": "lh1SlhU8"
        }
      ],
      "updated": 1789187288021,
      "link": null,
      "locked": false
    },
    {
      "id": "HkVTMxhF",
      "type": "text",
      "x": 1166.0,
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
      "seed": 7324013,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
      "link": null,
      "locked": false,
      "text": "Combine into a single DataFrame",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "R7bLWD41GP9ol8v5",
      "originalText": "Combine into a single DataFrame",
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "lh1SlhU8",
      "type": "arrow",
      "x": 1246.5,
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
      "seed": 8109581,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789187288021,
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
        "elementId": "4vqOM9o6Bdh6TXSe",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "R7bLWD41GP9ol8v5",
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
