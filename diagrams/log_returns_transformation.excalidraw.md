---

excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Log-Returns Transformation

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
Libraries ^fIpfYxhM

pandas ^I07S6XBK

numpy ^5vpicJxo

Methods ^BCnbsHMi

Architecture ^eH08H6y3

Log-Returns Transformation ^zTkcN7qa

Natural Log Differencing ^85W0NteB

np.log(df) ^frzNAej1

Computes the natural logarithm of every price value. ^fSOg8WNw

df.diff(1) ^JXWsNgNT

Computes the difference between the current row and the previous row (row[t] - row[t-1]) ^TbBwadJd

Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference: log_returns = np.log(prices_df).diff() ^Dll0LUBI

Ratio with Lag Shift ^uXFQEmmr

df.shift(1) ^5r3QfUrY

Moves every row down by 1 position (bringing yesterday's price into today's row). ^lQapUlLv

np.log(df / df.shift(1)) ^JVNFdvJC

Divides today's price by yesterday's price, then takes the natural log. ^FTUAyUDj

Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython. ^iWxtUZcD

From Percentage Change ^BV9OUS60

df.pct_change() ^eq66aTig

Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday. ^bPTPLpAJ

np.log1p(simple_ returns) ^knbaswFU

Computes log(1 + R) with extra precision for numbers very close to zero. ^aBs1zQ6I

Extract Close Prices ^qnOwJqgt

Assemble Price Matrix ^3VHX0L43

Apply Log Transformation ^40pkQ3H9

Clean the Boundary Row ^FIYyZeZj

Combine into a single DataFrame ^lgOeJ5Ei

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "ookZ1FSuDrDfB8Ae",
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
      "seed": 2236855,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "fIpfYxhM"
        },
        {
          "type": "arrow",
          "id": "Gx19k1nw"
        },
        {
          "type": "arrow",
          "id": "cd7B26rp"
        },
        {
          "type": "arrow",
          "id": "WkJRT4s0"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "fIpfYxhM",
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
      "seed": 2222108,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "Libraries",
      "rawText": "Libraries",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "ookZ1FSuDrDfB8Ae",
      "originalText": "Libraries",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "kF0ow7sl31vlk72Z",
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
      "seed": 8427480,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "I07S6XBK"
        },
        {
          "type": "arrow",
          "id": "Gx19k1nw"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "I07S6XBK",
      "type": "text",
      "x": 943.5,
      "y": 15.0,
      "width": 54.0,
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
      "seed": 2501387,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "pandas",
      "rawText": "pandas",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "kF0ow7sl31vlk72Z",
      "originalText": "pandas",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Gx19k1nw",
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
      "seed": 8928562,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
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
        "elementId": "ookZ1FSuDrDfB8Ae",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "kF0ow7sl31vlk72Z",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "R52l3mdlPEfLubj1",
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
      "seed": 449027,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "5vpicJxo"
        },
        {
          "type": "arrow",
          "id": "cd7B26rp"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "5vpicJxo",
      "type": "text",
      "x": 948.0,
      "y": 100.0,
      "width": 45.0,
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
      "seed": 6402178,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "numpy",
      "rawText": "numpy",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "R52l3mdlPEfLubj1",
      "originalText": "numpy",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "cd7B26rp",
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
      "seed": 437739,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
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
        "elementId": "ookZ1FSuDrDfB8Ae",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "R52l3mdlPEfLubj1",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "9iINRm3d3rjM3Xbf",
      "type": "rectangle",
      "x": 560.0,
      "y": 526.875,
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
      "seed": 1678597,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "BCnbsHMi"
        },
        {
          "type": "arrow",
          "id": "lRRUhWUk"
        },
        {
          "type": "arrow",
          "id": "CVZLmgUJ"
        },
        {
          "type": "arrow",
          "id": "w5noiD2o"
        },
        {
          "type": "arrow",
          "id": "TV682pn1"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "BCnbsHMi",
      "type": "text",
      "x": 619.0,
      "y": 547.4,
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
      "seed": 2050017,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "Methods",
      "rawText": "Methods",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "9iINRm3d3rjM3Xbf",
      "originalText": "Methods",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "5Iru8VkOg2bW1O22",
      "type": "rectangle",
      "x": 560.0,
      "y": 1179.0,
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
      "seed": 8589443,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "eH08H6y3"
        },
        {
          "type": "arrow",
          "id": "lpm7ZAQB"
        },
        {
          "type": "arrow",
          "id": "64Y479bD"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "eH08H6y3",
      "type": "text",
      "x": 596.5,
      "y": 1199.5,
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
      "seed": 9377245,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "Architecture",
      "rawText": "Architecture",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "5Iru8VkOg2bW1O22",
      "originalText": "Architecture",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "KW8zPqYxbaH46uBN",
      "type": "rectangle",
      "x": 140.0,
      "y": 602.5,
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
      "seed": 718644,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "zTkcN7qa"
        },
        {
          "type": "arrow",
          "id": "WkJRT4s0"
        },
        {
          "type": "arrow",
          "id": "lRRUhWUk"
        },
        {
          "type": "arrow",
          "id": "lpm7ZAQB"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "zTkcN7qa",
      "type": "text",
      "x": 187.0,
      "y": 617.0,
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
      "seed": 4456031,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "Log-Returns\nTransformation",
      "rawText": "Log-Returns Transformation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "KW8zPqYxbaH46uBN",
      "originalText": "Log-Returns\nTransformation",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "WkJRT4s0",
      "type": "arrow",
      "x": 360.0,
      "y": 640.0,
      "width": 200.0,
      "height": 571.0,
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
      "seed": 5707250,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          200.0,
          -571.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "KW8zPqYxbaH46uBN",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "ookZ1FSuDrDfB8Ae",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "lRRUhWUk",
      "type": "arrow",
      "x": 360.0,
      "y": 640.0,
      "width": 200.0,
      "height": 81.125,
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
      "seed": 3702021,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          200.0,
          -81.125
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "KW8zPqYxbaH46uBN",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "9iINRm3d3rjM3Xbf",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "lpm7ZAQB",
      "type": "arrow",
      "x": 360.0,
      "y": 640.0,
      "width": 200.0,
      "height": 571.0,
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
      "seed": 5245072,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          200.0,
          571.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "KW8zPqYxbaH46uBN",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "5Iru8VkOg2bW1O22",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "PtQ7ZTa0lDI3kL24",
      "type": "rectangle",
      "x": 880.0,
      "y": 270.75,
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
      "seed": 397208,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "85W0NteB"
        },
        {
          "type": "arrow",
          "id": "CVZLmgUJ"
        },
        {
          "type": "arrow",
          "id": "qgL0sIOK"
        },
        {
          "type": "arrow",
          "id": "LpMrDYll"
        }
      ],
      "updated": 1789190075496,
      "link": null,
      "locked": false
    },
    {
      "id": "85W0NteB",
      "type": "text",
      "x": 926.0,
      "y": 279.8,
      "width": 108.0,
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
      "seed": 1155453,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "text": "Natural Log\nDifferencing",
      "rawText": "Natural Log Differencing",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "PtQ7ZTa0lDI3kL24",
      "originalText": "Natural Log\nDifferencing",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "CVZLmgUJ",
      "type": "arrow",
      "x": 741.0,
      "y": 558.875,
      "width": 139.0,
      "height": 256.125,
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
      "seed": 1826085,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075496,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          -256.125
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "9iINRm3d3rjM3Xbf",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "PtQ7ZTa0lDI3kL24",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "hUh3mJgn7khdWM5S",
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
      "seed": 1489699,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "frzNAej1"
        },
        {
          "type": "arrow",
          "id": "qgL0sIOK"
        },
        {
          "type": "arrow",
          "id": "2t8k24W7"
        }
      ],
      "updated": 1789190075504,
      "link": null,
      "locked": false
    },
    {
      "id": "frzNAej1",
      "type": "text",
      "x": 1275.0,
      "y": 240.5,
      "width": 90.0,
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
      "seed": 5138223,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
      "link": null,
      "locked": false,
      "text": "np.log(df)",
      "rawText": "np.log(df)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "hUh3mJgn7khdWM5S",
      "originalText": "np.log(df)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "qgL0sIOK",
      "type": "arrow",
      "x": 1080.0,
      "y": 302.75,
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
      "seed": 2813598,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
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
        "elementId": "PtQ7ZTa0lDI3kL24",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "hUh3mJgn7khdWM5S",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "axT8q3gSxTM2NBZm",
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
      "seed": 7873713,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "fSOg8WNw"
        },
        {
          "type": "arrow",
          "id": "2t8k24W7"
        },
        {
          "type": "arrow",
          "id": "xqsmWage"
        }
      ],
      "updated": 1789190075504,
      "link": null,
      "locked": false
    },
    {
      "id": "fSOg8WNw",
      "type": "text",
      "x": 1591.5,
      "y": 229.0,
      "width": 297.0,
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
      "seed": 6863511,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
      "link": null,
      "locked": false,
      "text": "Computes the natural logarithm of\nevery price value.",
      "rawText": "Computes the natural logarithm of every price value.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "axT8q3gSxTM2NBZm",
      "originalText": "Computes the natural logarithm of\nevery price value.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "2t8k24W7",
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
      "seed": 9248803,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
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
        "elementId": "hUh3mJgn7khdWM5S",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "axT8q3gSxTM2NBZm",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "VBgGr5KD5mcyK3gp",
      "type": "rectangle",
      "x": 1200.0,
      "y": 321.5,
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
      "seed": 336300,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "JXWsNgNT"
        },
        {
          "type": "arrow",
          "id": "LpMrDYll"
        },
        {
          "type": "arrow",
          "id": "wD8SWbXe"
        }
      ],
      "updated": 1789190075504,
      "link": null,
      "locked": false
    },
    {
      "id": "JXWsNgNT",
      "type": "text",
      "x": 1275.0,
      "y": 342.0,
      "width": 90.0,
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
      "seed": 2425651,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
      "link": null,
      "locked": false,
      "text": "df.diff(1)",
      "rawText": "df.diff(1)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "VBgGr5KD5mcyK3gp",
      "originalText": "df.diff(1)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "LpMrDYll",
      "type": "arrow",
      "x": 1080.0,
      "y": 302.75,
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
      "seed": 4772657,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
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
        "elementId": "PtQ7ZTa0lDI3kL24",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "VBgGr5KD5mcyK3gp",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "yWZlivUCn1eZNAY5",
      "type": "rectangle",
      "x": 1560.0,
      "y": 314.0,
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
      "seed": 235138,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "TbBwadJd"
        },
        {
          "type": "arrow",
          "id": "wD8SWbXe"
        },
        {
          "type": "arrow",
          "id": "Szvuyr6v"
        }
      ],
      "updated": 1789190075504,
      "link": null,
      "locked": false
    },
    {
      "id": "TbBwadJd",
      "type": "text",
      "x": 1596.0,
      "y": 319.0,
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
      "seed": 149183,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
      "link": null,
      "locked": false,
      "text": "Computes the difference between\nthe current row and the previous\nrow (row[t] - row[t-1])",
      "rawText": "Computes the difference between the current row and the previous row (row[t] - row[t-1])",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "yWZlivUCn1eZNAY5",
      "originalText": "Computes the difference between\nthe current row and the previous\nrow (row[t] - row[t-1])",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "wD8SWbXe",
      "type": "arrow",
      "x": 1440.0,
      "y": 353.5,
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
      "seed": 3152060,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
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
        "elementId": "VBgGr5KD5mcyK3gp",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "yWZlivUCn1eZNAY5",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "wx0Y29qkWZk2FxeU",
      "type": "rectangle",
      "x": 2060.0,
      "y": 228.75,
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
      "seed": 9369708,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Dll0LUBI"
        },
        {
          "type": "arrow",
          "id": "xqsmWage"
        },
        {
          "type": "arrow",
          "id": "Szvuyr6v"
        }
      ],
      "updated": 1789190075504,
      "link": null,
      "locked": false
    },
    {
      "id": "Dll0LUBI",
      "type": "text",
      "x": 2092.5,
      "y": 233.8,
      "width": 315.0,
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
      "seed": 4179204,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
      "link": null,
      "locked": false,
      "text": "Since log(A / B) = log(A) - log(B),\nyou can take the natural log of all\nprices first, then take the first\ndifference:\nlog_returns =\nnp.log(prices_df).diff()",
      "rawText": "Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference: log_returns = np.log(prices_df).diff()",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "wx0Y29qkWZk2FxeU",
      "originalText": "Since log(A / B) = log(A) - log(B),\nyou can take the natural log of all\nprices first, then take the first\ndifference:\nlog_returns =\nnp.log(prices_df).diff()",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "xqsmWage",
      "type": "arrow",
      "x": 1920.0,
      "y": 252.0,
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
      "seed": 7578905,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
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
        "elementId": "axT8q3gSxTM2NBZm",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "wx0Y29qkWZk2FxeU",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "Szvuyr6v",
      "type": "arrow",
      "x": 1920.0,
      "y": 353.5,
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
      "seed": 1885718,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
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
        "elementId": "yWZlivUCn1eZNAY5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "wx0Y29qkWZk2FxeU",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "Cl4QOj65QPuVfNhI",
      "type": "rectangle",
      "x": 880.0,
      "y": 525.0,
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
      "seed": 2010155,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "uXFQEmmr"
        },
        {
          "type": "arrow",
          "id": "w5noiD2o"
        },
        {
          "type": "arrow",
          "id": "9IyXPNjS"
        },
        {
          "type": "arrow",
          "id": "73pkzyMt"
        }
      ],
      "updated": 1789190075504,
      "link": null,
      "locked": false
    },
    {
      "id": "uXFQEmmr",
      "type": "text",
      "x": 917.0,
      "y": 534.0,
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
      "seed": 4379580,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075504,
      "link": null,
      "locked": false,
      "text": "Ratio with Lag\nShift",
      "rawText": "Ratio with Lag Shift",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "Cl4QOj65QPuVfNhI",
      "originalText": "Ratio with Lag\nShift",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "w5noiD2o",
      "type": "arrow",
      "x": 741.0,
      "y": 558.875,
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
      "seed": 8913557,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "9iINRm3d3rjM3Xbf",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "Cl4QOj65QPuVfNhI",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "4r5HbRTr32Sos9nX",
      "type": "rectangle",
      "x": 1200.0,
      "y": 470.5,
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
      "seed": 8803328,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "5r3QfUrY"
        },
        {
          "type": "arrow",
          "id": "9IyXPNjS"
        },
        {
          "type": "arrow",
          "id": "oKKPOLFJ"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "5r3QfUrY",
      "type": "text",
      "x": 1270.5,
      "y": 491.0,
      "width": 99.0,
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
      "seed": 4445767,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "df.shift(1)",
      "rawText": "df.shift(1)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "4r5HbRTr32Sos9nX",
      "originalText": "df.shift(1)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "9IyXPNjS",
      "type": "arrow",
      "x": 1080.0,
      "y": 557.0,
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
      "seed": 5820296,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "Cl4QOj65QPuVfNhI",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "4r5HbRTr32Sos9nX",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "sJhvlMC2mt3nNwKK",
      "type": "rectangle",
      "x": 1560.0,
      "y": 463.0,
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
      "seed": 2550888,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "lQapUlLv"
        },
        {
          "type": "arrow",
          "id": "oKKPOLFJ"
        },
        {
          "type": "arrow",
          "id": "tLxWniYe"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "lQapUlLv",
      "type": "text",
      "x": 1587.0,
      "y": 468.0,
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
      "seed": 2271814,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "Moves every row down by 1 position\n(bringing yesterday's price into\ntoday's row).",
      "rawText": "Moves every row down by 1 position (bringing yesterday's price into today's row).",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "sJhvlMC2mt3nNwKK",
      "originalText": "Moves every row down by 1 position\n(bringing yesterday's price into\ntoday's row).",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "oKKPOLFJ",
      "type": "arrow",
      "x": 1440.0,
      "y": 502.5,
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
      "seed": 9417037,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "4r5HbRTr32Sos9nX",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "sJhvlMC2mt3nNwKK",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "pHGmQOi2J9y0yrCE",
      "type": "rectangle",
      "x": 1200.0,
      "y": 579.5,
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
      "seed": 4669792,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "JVNFdvJC"
        },
        {
          "type": "arrow",
          "id": "73pkzyMt"
        },
        {
          "type": "arrow",
          "id": "YUcpE48v"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "JVNFdvJC",
      "type": "text",
      "x": 1266.0,
      "y": 588.5,
      "width": 108.0,
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
      "seed": 9948559,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "np.log(df /\ndf.shift(1))",
      "rawText": "np.log(df / df.shift(1))",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "pHGmQOi2J9y0yrCE",
      "originalText": "np.log(df /\ndf.shift(1))",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "73pkzyMt",
      "type": "arrow",
      "x": 1080.0,
      "y": 557.0,
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
      "seed": 7257177,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "Cl4QOj65QPuVfNhI",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "pHGmQOi2J9y0yrCE",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "yIGnv0cdA1Ie9vaG",
      "type": "rectangle",
      "x": 1560.0,
      "y": 572.0,
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
      "seed": 6222421,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "FTUAyUDj"
        },
        {
          "type": "arrow",
          "id": "YUcpE48v"
        },
        {
          "type": "arrow",
          "id": "CQ05hWw6"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "FTUAyUDj",
      "type": "text",
      "x": 1591.5,
      "y": 577.0,
      "width": 297.0,
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
      "seed": 9670927,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "Divides today's price by\nyesterday's price, then takes the\nnatural log.",
      "rawText": "Divides today's price by yesterday's price, then takes the natural log.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "yIGnv0cdA1Ie9vaG",
      "originalText": "Divides today's price by\nyesterday's price, then takes the\nnatural log.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "YUcpE48v",
      "type": "arrow",
      "x": 1440.0,
      "y": 611.5,
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
      "seed": 8016320,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "pHGmQOi2J9y0yrCE",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "yIGnv0cdA1Ie9vaG",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "cmN3NLKr7jIxzubg",
      "type": "rectangle",
      "x": 2060.0,
      "y": 494.5,
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
      "seed": 2763309,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "iWxtUZcD"
        },
        {
          "type": "arrow",
          "id": "tLxWniYe"
        },
        {
          "type": "arrow",
          "id": "CQ05hWw6"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "iWxtUZcD",
      "type": "text",
      "x": 2092.5,
      "y": 499.5,
      "width": 315.0,
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
      "seed": 1955365,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "Both Option A and Option B yield\nidentical mathematical results.\nOption A (np.log(df).diff()) is\ntypically preferred because .diff()\nis optimized in Cython.",
      "rawText": "Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "cmN3NLKr7jIxzubg",
      "originalText": "Both Option A and Option B yield\nidentical mathematical results.\nOption A (np.log(df).diff()) is\ntypically preferred because .diff()\nis optimized in Cython.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "tLxWniYe",
      "type": "arrow",
      "x": 1920.0,
      "y": 502.5,
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
      "seed": 7398504,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "sJhvlMC2mt3nNwKK",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "cmN3NLKr7jIxzubg",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "CQ05hWw6",
      "type": "arrow",
      "x": 1920.0,
      "y": 611.5,
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
      "seed": 4687682,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "yIGnv0cdA1Ie9vaG",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "cmN3NLKr7jIxzubg",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "mMoJ5E30605nhGT3",
      "type": "rectangle",
      "x": 880.0,
      "y": 783.0,
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
      "seed": 5869702,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "BV9OUS60"
        },
        {
          "type": "arrow",
          "id": "TV682pn1"
        },
        {
          "type": "arrow",
          "id": "BRYDg9CD"
        },
        {
          "type": "arrow",
          "id": "nOLF1Wig"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "BV9OUS60",
      "type": "text",
      "x": 912.5,
      "y": 792.0,
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
      "seed": 8828772,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "From Percentage\nChange",
      "rawText": "From Percentage Change",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "mMoJ5E30605nhGT3",
      "originalText": "From Percentage\nChange",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "TV682pn1",
      "type": "arrow",
      "x": 741.0,
      "y": 558.875,
      "width": 139.0,
      "height": 256.125,
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
      "seed": 5161637,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          139.0,
          256.125
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "9iINRm3d3rjM3Xbf",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "mMoJ5E30605nhGT3",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "TL400vJCAqSTvzjd",
      "type": "rectangle",
      "x": 1200.0,
      "y": 728.5,
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
      "seed": 7806775,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "eq66aTig"
        },
        {
          "type": "arrow",
          "id": "BRYDg9CD"
        },
        {
          "type": "arrow",
          "id": "ph3OWLB4"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "eq66aTig",
      "type": "text",
      "x": 1252.5,
      "y": 749.0,
      "width": 135.0,
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
      "seed": 2816143,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "df.pct_change()",
      "rawText": "df.pct_change()",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "TL400vJCAqSTvzjd",
      "originalText": "df.pct_change()",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "BRYDg9CD",
      "type": "arrow",
      "x": 1080.0,
      "y": 815.0,
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
      "seed": 6906168,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "mMoJ5E30605nhGT3",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "TL400vJCAqSTvzjd",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "RnGCx5cua3Iym9CC",
      "type": "rectangle",
      "x": 1560.0,
      "y": 721.0,
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
      "seed": 4763423,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "bPTPLpAJ"
        },
        {
          "type": "arrow",
          "id": "ph3OWLB4"
        }
      ],
      "updated": 1789190075505,
      "link": null,
      "locked": false
    },
    {
      "id": "bPTPLpAJ",
      "type": "text",
      "x": 1591.5,
      "y": 726.0,
      "width": 297.0,
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
      "seed": 9912365,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
      "link": null,
      "locked": false,
      "text": "Calculates simple return R =\n(Price_today - Price_yesterday) /\nPrice_yesterday.",
      "rawText": "Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "RnGCx5cua3Iym9CC",
      "originalText": "Calculates simple return R =\n(Price_today - Price_yesterday) /\nPrice_yesterday.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "ph3OWLB4",
      "type": "arrow",
      "x": 1440.0,
      "y": 760.5,
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
      "seed": 7316593,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075505,
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
        "elementId": "TL400vJCAqSTvzjd",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "RnGCx5cua3Iym9CC",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "hgjoxL3qlQ7iGUuK",
      "type": "rectangle",
      "x": 1200.0,
      "y": 837.5,
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
      "seed": 4066668,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "knbaswFU"
        },
        {
          "type": "arrow",
          "id": "nOLF1Wig"
        },
        {
          "type": "arrow",
          "id": "xoDKMw2Q"
        }
      ],
      "updated": 1789190075506,
      "link": null,
      "locked": false
    },
    {
      "id": "knbaswFU",
      "type": "text",
      "x": 1248.0,
      "y": 846.5,
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
      "seed": 7296107,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075506,
      "link": null,
      "locked": false,
      "text": "np.log1p(simple_\nreturns)",
      "rawText": "np.log1p(simple_ returns)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "hgjoxL3qlQ7iGUuK",
      "originalText": "np.log1p(simple_\nreturns)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "nOLF1Wig",
      "type": "arrow",
      "x": 1080.0,
      "y": 815.0,
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
      "seed": 1769815,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075506,
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
        "elementId": "mMoJ5E30605nhGT3",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "hgjoxL3qlQ7iGUuK",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "2Tvcrd90kcb3VKNb",
      "type": "rectangle",
      "x": 1560.0,
      "y": 830.0,
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
      "seed": 9014135,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "aBs1zQ6I"
        },
        {
          "type": "arrow",
          "id": "xoDKMw2Q"
        }
      ],
      "updated": 1789190075506,
      "link": null,
      "locked": false
    },
    {
      "id": "aBs1zQ6I",
      "type": "text",
      "x": 1596.0,
      "y": 835.0,
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
      "seed": 2524848,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075506,
      "link": null,
      "locked": false,
      "text": "Computes log(1 + R) with extra\nprecision for numbers very close\nto zero.",
      "rawText": "Computes log(1 + R) with extra precision for numbers very close to zero.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "2Tvcrd90kcb3VKNb",
      "originalText": "Computes log(1 + R) with extra\nprecision for numbers very close\nto zero.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "xoDKMw2Q",
      "type": "arrow",
      "x": 1440.0,
      "y": 869.5,
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
      "seed": 3788964,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075506,
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
        "elementId": "hgjoxL3qlQ7iGUuK",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "2Tvcrd90kcb3VKNb",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "livMubkSvQAA8R6p",
      "type": "rectangle",
      "x": 880.0,
      "y": 1179.0,
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
      "seed": 4518033,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "qnOwJqgt"
        },
        {
          "type": "arrow",
          "id": "64Y479bD"
        },
        {
          "type": "arrow",
          "id": "4oOdTXqq"
        }
      ],
      "updated": 1789190075506,
      "link": null,
      "locked": false
    },
    {
      "id": "qnOwJqgt",
      "type": "text",
      "x": 916.5,
      "y": 1188.0,
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
      "seed": 5362748,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075506,
      "link": null,
      "locked": false,
      "text": "Extract Close\nPrices",
      "rawText": "Extract Close Prices",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "livMubkSvQAA8R6p",
      "originalText": "Extract Close\nPrices",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "64Y479bD",
      "type": "arrow",
      "x": 741.0,
      "y": 1211.0,
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
      "seed": 8653040,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075506,
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
        "elementId": "5Iru8VkOg2bW1O22",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "livMubkSvQAA8R6p",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "4hKwQ8sFUYSOjhSv",
      "type": "rectangle",
      "x": 1135.0,
      "y": 1179.0,
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
      "seed": 9573116,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "3VHX0L43"
        },
        {
          "type": "arrow",
          "id": "4oOdTXqq"
        },
        {
          "type": "arrow",
          "id": "6avagHC7"
        },
        {
          "type": "arrow",
          "id": "LQWgKXUy"
        }
      ],
      "updated": 1789190075508,
      "link": null,
      "locked": false
    },
    {
      "id": "3VHX0L43",
      "type": "text",
      "x": 1167.0,
      "y": 1188.0,
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
      "seed": 4405386,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075508,
      "link": null,
      "locked": false,
      "text": "Assemble Price\nMatrix",
      "rawText": "Assemble Price Matrix",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "4hKwQ8sFUYSOjhSv",
      "originalText": "Assemble Price\nMatrix",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "4oOdTXqq",
      "type": "arrow",
      "x": 1070.0,
      "y": 1211.0,
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
      "seed": 6023640,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075508,
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
        "elementId": "livMubkSvQAA8R6p",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "4hKwQ8sFUYSOjhSv",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "hwiJzejX4o5SiKJC",
      "type": "rectangle",
      "x": 1390.0,
      "y": 1179.0,
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
      "seed": 5520147,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "40pkQ3H9"
        },
        {
          "type": "arrow",
          "id": "6avagHC7"
        },
        {
          "type": "arrow",
          "id": "FffVvF0T"
        }
      ],
      "updated": 1789190075508,
      "link": null,
      "locked": false
    },
    {
      "id": "40pkQ3H9",
      "type": "text",
      "x": 1422.0,
      "y": 1188.0,
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
      "seed": 7060622,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075508,
      "link": null,
      "locked": false,
      "text": "Apply Log\nTransformation",
      "rawText": "Apply Log Transformation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "hwiJzejX4o5SiKJC",
      "originalText": "Apply Log\nTransformation",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "6avagHC7",
      "type": "arrow",
      "x": 1325.0,
      "y": 1211.0,
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
      "seed": 9548706,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075510,
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
        "elementId": "4hKwQ8sFUYSOjhSv",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "hwiJzejX4o5SiKJC",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "qvSo4DE2gE6przA3",
      "type": "rectangle",
      "x": 1645.0,
      "y": 1179.0,
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
      "seed": 2301750,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "FIYyZeZj"
        },
        {
          "type": "arrow",
          "id": "FffVvF0T"
        }
      ],
      "updated": 1789190075511,
      "link": null,
      "locked": false
    },
    {
      "id": "FIYyZeZj",
      "type": "text",
      "x": 1686.0,
      "y": 1188.0,
      "width": 108.0,
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
      "seed": 7966409,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075511,
      "link": null,
      "locked": false,
      "text": "Clean the\nBoundary Row",
      "rawText": "Clean the Boundary Row",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "qvSo4DE2gE6przA3",
      "originalText": "Clean the\nBoundary Row",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "FffVvF0T",
      "type": "arrow",
      "x": 1580.0,
      "y": 1211.0,
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
      "seed": 7398648,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075511,
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
        "elementId": "hwiJzejX4o5SiKJC",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "qvSo4DE2gE6przA3",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "8qcM88Lz3gjwAXGt",
      "type": "rectangle",
      "x": 1135.0,
      "y": 1059.0,
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
      "seed": 4354470,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "lgOeJ5Ei"
        },
        {
          "type": "arrow",
          "id": "LQWgKXUy"
        }
      ],
      "updated": 1789190075511,
      "link": null,
      "locked": false
    },
    {
      "id": "lgOeJ5Ei",
      "type": "text",
      "x": 1158.0,
      "y": 1068.0,
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
      "seed": 3561697,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075511,
      "link": null,
      "locked": false,
      "text": "Combine into a\nsingle DataFrame",
      "rawText": "Combine into a single DataFrame",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "8qcM88Lz3gjwAXGt",
      "originalText": "Combine into a\nsingle DataFrame",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "LQWgKXUy",
      "type": "arrow",
      "x": 1230.0,
      "y": 1179.0,
      "width": 0.0,
      "height": 56.0,
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
      "seed": 5900939,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789190075511,
      "link": null,
      "locked": false,
      "points": [
        [
          0.0,
          0.0
        ],
        [
          0.0,
          -56.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "4hKwQ8sFUYSOjhSv",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "8qcM88Lz3gjwAXGt",
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
