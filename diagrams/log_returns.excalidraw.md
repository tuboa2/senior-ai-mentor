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
Libraries ^iEf8jfP4

pandas ^6Q2fJO5P

numpy ^pE4FkZ8c

Methods ^GDNS31eC

Architecture ^SQ0NIY2i

Log-Returns Transformation ^jr2g0w90

Natural Log Differencing ^pRMN5CoJ

np.log(df) ^ZAgvisYI

Computes the natural logarithm of every price value. ^pjLyvufR

df.diff(1) ^nwLCOhUh

Computes the difference between the current row and the previous row (row[t] - row[t-1]) ^ZjktjABk

Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference: log_returns = np.log(prices_df).diff() ^6sRmQQdP

Ratio with Lag Shift ^bcTdE7Yh

df.shift(1) ^Cs9VvO46

Moves every row down by 1 position (bringing yesterday's price into today's row). ^dIEgwDYa

np.log(df / df.shift(1)) ^WnKoHPrf

Divides today's price by yesterday's price, then takes the natural log. ^3wSBI97s

Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython. ^U3NoSWeV

From Percentage Change ^YO5irFKX

df.pct_change() ^eaGqFBk3

Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday. ^mwlARuXG

np.log1p(simple_ returns) ^Zhe8EStQ

Computes log(1 + R) with extra precision for numbers very close to zero. ^k4naGNGC

Extract Close Prices ^sXysy4HA

Assemble Price Matrix ^8pahPLgD

Apply Log Transformation ^lbilhNqp

Clean the Boundary Row ^A5yazSP1

Combine into a single DataFrame ^hS7QhXPa

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "2BrEyDNUMWbTKHJ3",
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
      "seed": 8944993,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "iEf8jfP4"
        },
        {
          "type": "arrow",
          "id": "pJgMRrSY"
        },
        {
          "type": "arrow",
          "id": "GW95WXA6"
        },
        {
          "type": "arrow",
          "id": "OTHMfPBj"
        }
      ],
      "updated": 1789189620812,
      "link": null,
      "locked": false
    },
    {
      "id": "iEf8jfP4",
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
      "seed": 587074,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620812,
      "link": null,
      "locked": false,
      "text": "Libraries",
      "rawText": "Libraries",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "2BrEyDNUMWbTKHJ3",
      "originalText": "Libraries",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "xtq3Qly1yUz4q6m7",
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
      "seed": 1797929,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "6Q2fJO5P"
        },
        {
          "type": "arrow",
          "id": "pJgMRrSY"
        }
      ],
      "updated": 1789189620812,
      "link": null,
      "locked": false
    },
    {
      "id": "6Q2fJO5P",
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
      "seed": 7390594,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620812,
      "link": null,
      "locked": false,
      "text": "pandas",
      "rawText": "pandas",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "xtq3Qly1yUz4q6m7",
      "originalText": "pandas",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "pJgMRrSY",
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
      "seed": 4630580,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620812,
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
        "elementId": "2BrEyDNUMWbTKHJ3",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "xtq3Qly1yUz4q6m7",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "AQoLYQuojEMAxzOd",
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
      "seed": 5807784,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "pE4FkZ8c"
        },
        {
          "type": "arrow",
          "id": "GW95WXA6"
        }
      ],
      "updated": 1789189620813,
      "link": null,
      "locked": false
    },
    {
      "id": "pE4FkZ8c",
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
      "seed": 8347509,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
      "link": null,
      "locked": false,
      "text": "numpy",
      "rawText": "numpy",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "AQoLYQuojEMAxzOd",
      "originalText": "numpy",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "GW95WXA6",
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
      "seed": 2450035,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
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
        "elementId": "2BrEyDNUMWbTKHJ3",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "AQoLYQuojEMAxzOd",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "6EbnaaNimIc57jDo",
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
      "seed": 5536804,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "GDNS31eC"
        },
        {
          "type": "arrow",
          "id": "SZOR2Y2E"
        },
        {
          "type": "arrow",
          "id": "af4yp88n"
        },
        {
          "type": "arrow",
          "id": "eja5Jlxc"
        },
        {
          "type": "arrow",
          "id": "dMV8yEUz"
        }
      ],
      "updated": 1789189620813,
      "link": null,
      "locked": false
    },
    {
      "id": "GDNS31eC",
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
      "seed": 4513165,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
      "link": null,
      "locked": false,
      "text": "Methods",
      "rawText": "Methods",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "6EbnaaNimIc57jDo",
      "originalText": "Methods",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "5VEozoNtf3tBIdvz",
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
      "seed": 6933110,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "SQ0NIY2i"
        },
        {
          "type": "arrow",
          "id": "MKkS5U5Z"
        },
        {
          "type": "arrow",
          "id": "P1sGeNac"
        }
      ],
      "updated": 1789189620813,
      "link": null,
      "locked": false
    },
    {
      "id": "SQ0NIY2i",
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
      "seed": 7145258,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
      "link": null,
      "locked": false,
      "text": "Architecture",
      "rawText": "Architecture",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "5VEozoNtf3tBIdvz",
      "originalText": "Architecture",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "9DkWEXQKimXQmP3A",
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
      "seed": 6867110,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "jr2g0w90"
        },
        {
          "type": "arrow",
          "id": "OTHMfPBj"
        },
        {
          "type": "arrow",
          "id": "SZOR2Y2E"
        },
        {
          "type": "arrow",
          "id": "MKkS5U5Z"
        }
      ],
      "updated": 1789189620813,
      "link": null,
      "locked": false
    },
    {
      "id": "jr2g0w90",
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
      "seed": 9448966,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
      "link": null,
      "locked": false,
      "text": "Log-Returns\nTransformation",
      "rawText": "Log-Returns Transformation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "9DkWEXQKimXQmP3A",
      "originalText": "Log-Returns\nTransformation",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "OTHMfPBj",
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
      "seed": 7614364,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
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
        "elementId": "9DkWEXQKimXQmP3A",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "2BrEyDNUMWbTKHJ3",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "SZOR2Y2E",
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
      "seed": 2660586,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
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
        "elementId": "9DkWEXQKimXQmP3A",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "6EbnaaNimIc57jDo",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "MKkS5U5Z",
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
      "seed": 826210,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
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
        "elementId": "9DkWEXQKimXQmP3A",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "5VEozoNtf3tBIdvz",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "vUfEnn2Au1N4ehnu",
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
      "seed": 8811705,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "pRMN5CoJ"
        },
        {
          "type": "arrow",
          "id": "af4yp88n"
        },
        {
          "type": "arrow",
          "id": "MQtGXBp0"
        },
        {
          "type": "arrow",
          "id": "vaLcZPND"
        }
      ],
      "updated": 1789189620813,
      "link": null,
      "locked": false
    },
    {
      "id": "pRMN5CoJ",
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
      "seed": 4575690,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
      "link": null,
      "locked": false,
      "text": "Natural Log\nDifferencing",
      "rawText": "Natural Log Differencing",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "vUfEnn2Au1N4ehnu",
      "originalText": "Natural Log\nDifferencing",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "af4yp88n",
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
      "seed": 7074648,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620813,
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
        "elementId": "6EbnaaNimIc57jDo",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "vUfEnn2Au1N4ehnu",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "0CiWuIRsqZh4j9E9",
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
      "seed": 5905328,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "ZAgvisYI"
        },
        {
          "type": "arrow",
          "id": "MQtGXBp0"
        },
        {
          "type": "arrow",
          "id": "d63gSkCe"
        }
      ],
      "updated": 1789189620814,
      "link": null,
      "locked": false
    },
    {
      "id": "ZAgvisYI",
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
      "seed": 9013757,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620814,
      "link": null,
      "locked": false,
      "text": "np.log(df)",
      "rawText": "np.log(df)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "0CiWuIRsqZh4j9E9",
      "originalText": "np.log(df)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "MQtGXBp0",
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
      "seed": 9806870,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620814,
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
        "elementId": "vUfEnn2Au1N4ehnu",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "0CiWuIRsqZh4j9E9",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "AJB4v6b0ZsdVd7Ej",
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
      "seed": 3226641,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "pjLyvufR"
        },
        {
          "type": "arrow",
          "id": "d63gSkCe"
        },
        {
          "type": "arrow",
          "id": "guzrRXFp"
        }
      ],
      "updated": 1789189620818,
      "link": null,
      "locked": false
    },
    {
      "id": "pjLyvufR",
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
      "seed": 6683091,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620818,
      "link": null,
      "locked": false,
      "text": "Computes the natural logarithm of\nevery price value.",
      "rawText": "Computes the natural logarithm of every price value.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "AJB4v6b0ZsdVd7Ej",
      "originalText": "Computes the natural logarithm of\nevery price value.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "d63gSkCe",
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
      "seed": 9100419,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620818,
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
        "elementId": "0CiWuIRsqZh4j9E9",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "AJB4v6b0ZsdVd7Ej",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "iR5ySrex3yDIdV6c",
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
      "seed": 2460504,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "nwLCOhUh"
        },
        {
          "type": "arrow",
          "id": "vaLcZPND"
        },
        {
          "type": "arrow",
          "id": "Oi2fjw3V"
        }
      ],
      "updated": 1789189620818,
      "link": null,
      "locked": false
    },
    {
      "id": "nwLCOhUh",
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
      "seed": 6115002,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620818,
      "link": null,
      "locked": false,
      "text": "df.diff(1)",
      "rawText": "df.diff(1)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "iR5ySrex3yDIdV6c",
      "originalText": "df.diff(1)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "vaLcZPND",
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
      "seed": 9919257,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620818,
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
        "elementId": "vUfEnn2Au1N4ehnu",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "iR5ySrex3yDIdV6c",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "RdBWKvVkvc2AXqR8",
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
      "seed": 8332907,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "ZjktjABk"
        },
        {
          "type": "arrow",
          "id": "Oi2fjw3V"
        },
        {
          "type": "arrow",
          "id": "m2yQOEiM"
        }
      ],
      "updated": 1789189620818,
      "link": null,
      "locked": false
    },
    {
      "id": "ZjktjABk",
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
      "seed": 683087,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620818,
      "link": null,
      "locked": false,
      "text": "Computes the difference between\nthe current row and the previous\nrow (row[t] - row[t-1])",
      "rawText": "Computes the difference between the current row and the previous row (row[t] - row[t-1])",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "RdBWKvVkvc2AXqR8",
      "originalText": "Computes the difference between\nthe current row and the previous\nrow (row[t] - row[t-1])",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Oi2fjw3V",
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
      "seed": 1527114,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "iR5ySrex3yDIdV6c",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "RdBWKvVkvc2AXqR8",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "SBAb2OXK8Ggdte53",
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
      "seed": 6775258,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "6sRmQQdP"
        },
        {
          "type": "arrow",
          "id": "guzrRXFp"
        },
        {
          "type": "arrow",
          "id": "m2yQOEiM"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "6sRmQQdP",
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
      "seed": 4960112,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "Since log(A / B) = log(A) - log(B),\nyou can take the natural log of all\nprices first, then take the first\ndifference:\nlog_returns =\nnp.log(prices_df).diff()",
      "rawText": "Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, then take the first difference: log_returns = np.log(prices_df).diff()",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "SBAb2OXK8Ggdte53",
      "originalText": "Since log(A / B) = log(A) - log(B),\nyou can take the natural log of all\nprices first, then take the first\ndifference:\nlog_returns =\nnp.log(prices_df).diff()",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "guzrRXFp",
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
      "seed": 4415718,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "AJB4v6b0ZsdVd7Ej",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "SBAb2OXK8Ggdte53",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "m2yQOEiM",
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
      "seed": 5544284,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "RdBWKvVkvc2AXqR8",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "SBAb2OXK8Ggdte53",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "YIcfNKa9kahFdVRW",
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
      "seed": 9707920,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "bcTdE7Yh"
        },
        {
          "type": "arrow",
          "id": "eja5Jlxc"
        },
        {
          "type": "arrow",
          "id": "mlNqdcbm"
        },
        {
          "type": "arrow",
          "id": "a7bgN3XK"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "bcTdE7Yh",
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
      "seed": 9051034,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "Ratio with Lag\nShift",
      "rawText": "Ratio with Lag Shift",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "YIcfNKa9kahFdVRW",
      "originalText": "Ratio with Lag\nShift",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "eja5Jlxc",
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
      "seed": 8577471,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "6EbnaaNimIc57jDo",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "YIcfNKa9kahFdVRW",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "QxdyUC2OJDPuMyVV",
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
      "seed": 6489130,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Cs9VvO46"
        },
        {
          "type": "arrow",
          "id": "mlNqdcbm"
        },
        {
          "type": "arrow",
          "id": "Tmqt0aFR"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "Cs9VvO46",
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
      "seed": 5301580,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "df.shift(1)",
      "rawText": "df.shift(1)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "QxdyUC2OJDPuMyVV",
      "originalText": "df.shift(1)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "mlNqdcbm",
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
      "seed": 3587379,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "YIcfNKa9kahFdVRW",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "QxdyUC2OJDPuMyVV",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "TgLB9XjzZ2hpjNQ5",
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
      "seed": 1283732,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "dIEgwDYa"
        },
        {
          "type": "arrow",
          "id": "Tmqt0aFR"
        },
        {
          "type": "arrow",
          "id": "BoQeRbiI"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "dIEgwDYa",
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
      "seed": 6652266,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "Moves every row down by 1 position\n(bringing yesterday's price into\ntoday's row).",
      "rawText": "Moves every row down by 1 position (bringing yesterday's price into today's row).",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "TgLB9XjzZ2hpjNQ5",
      "originalText": "Moves every row down by 1 position\n(bringing yesterday's price into\ntoday's row).",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "Tmqt0aFR",
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
      "seed": 6431159,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "QxdyUC2OJDPuMyVV",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "TgLB9XjzZ2hpjNQ5",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "tQtk2EH6H34B6qAq",
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
      "seed": 3615087,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "WnKoHPrf"
        },
        {
          "type": "arrow",
          "id": "a7bgN3XK"
        },
        {
          "type": "arrow",
          "id": "N4IcIYOM"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "WnKoHPrf",
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
      "seed": 2727907,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "np.log(df /\ndf.shift(1))",
      "rawText": "np.log(df / df.shift(1))",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "tQtk2EH6H34B6qAq",
      "originalText": "np.log(df /\ndf.shift(1))",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "a7bgN3XK",
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
      "seed": 6596808,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "YIcfNKa9kahFdVRW",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "tQtk2EH6H34B6qAq",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "qGJORtiml3jlFeyM",
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
      "seed": 154267,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "3wSBI97s"
        },
        {
          "type": "arrow",
          "id": "N4IcIYOM"
        },
        {
          "type": "arrow",
          "id": "ljkpLXzp"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "3wSBI97s",
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
      "seed": 8221716,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "Divides today's price by\nyesterday's price, then takes the\nnatural log.",
      "rawText": "Divides today's price by yesterday's price, then takes the natural log.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "qGJORtiml3jlFeyM",
      "originalText": "Divides today's price by\nyesterday's price, then takes the\nnatural log.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "N4IcIYOM",
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
      "seed": 7386097,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "tQtk2EH6H34B6qAq",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "qGJORtiml3jlFeyM",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "yyqTLCyQFobfJc42",
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
      "seed": 9177670,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "U3NoSWeV"
        },
        {
          "type": "arrow",
          "id": "BoQeRbiI"
        },
        {
          "type": "arrow",
          "id": "ljkpLXzp"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "U3NoSWeV",
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
      "seed": 6409475,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "Both Option A and Option B yield\nidentical mathematical results.\nOption A (np.log(df).diff()) is\ntypically preferred because .diff()\nis optimized in Cython.",
      "rawText": "Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) is typically preferred because .diff() is optimized in Cython.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "yyqTLCyQFobfJc42",
      "originalText": "Both Option A and Option B yield\nidentical mathematical results.\nOption A (np.log(df).diff()) is\ntypically preferred because .diff()\nis optimized in Cython.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "BoQeRbiI",
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
      "seed": 1575182,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "TgLB9XjzZ2hpjNQ5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "yyqTLCyQFobfJc42",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "ljkpLXzp",
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
      "seed": 8437301,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
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
        "elementId": "qGJORtiml3jlFeyM",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "yyqTLCyQFobfJc42",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "QZc36RIY8DAMMA22",
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
      "seed": 1405967,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "YO5irFKX"
        },
        {
          "type": "arrow",
          "id": "dMV8yEUz"
        },
        {
          "type": "arrow",
          "id": "oJyXlV9j"
        },
        {
          "type": "arrow",
          "id": "DEDnUWbw"
        }
      ],
      "updated": 1789189620819,
      "link": null,
      "locked": false
    },
    {
      "id": "YO5irFKX",
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
      "seed": 1095634,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620819,
      "link": null,
      "locked": false,
      "text": "From Percentage\nChange",
      "rawText": "From Percentage Change",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "QZc36RIY8DAMMA22",
      "originalText": "From Percentage\nChange",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "dMV8yEUz",
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
      "seed": 667879,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "6EbnaaNimIc57jDo",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "QZc36RIY8DAMMA22",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "No8w9XkqU5Z4bvWJ",
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
      "seed": 9832588,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "eaGqFBk3"
        },
        {
          "type": "arrow",
          "id": "oJyXlV9j"
        },
        {
          "type": "arrow",
          "id": "dlGjjdTq"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "eaGqFBk3",
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
      "seed": 8763597,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "df.pct_change()",
      "rawText": "df.pct_change()",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "No8w9XkqU5Z4bvWJ",
      "originalText": "df.pct_change()",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "oJyXlV9j",
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
      "seed": 2982532,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "QZc36RIY8DAMMA22",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "No8w9XkqU5Z4bvWJ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "9qqL6BsEfFCtkELJ",
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
      "seed": 5881118,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "mwlARuXG"
        },
        {
          "type": "arrow",
          "id": "dlGjjdTq"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "mwlARuXG",
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
      "seed": 2704164,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "Calculates simple return R =\n(Price_today - Price_yesterday) /\nPrice_yesterday.",
      "rawText": "Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "9qqL6BsEfFCtkELJ",
      "originalText": "Calculates simple return R =\n(Price_today - Price_yesterday) /\nPrice_yesterday.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "dlGjjdTq",
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
      "seed": 5047566,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "No8w9XkqU5Z4bvWJ",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "9qqL6BsEfFCtkELJ",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "w9AeHzdOscQy1yQE",
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
      "seed": 5080400,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "Zhe8EStQ"
        },
        {
          "type": "arrow",
          "id": "DEDnUWbw"
        },
        {
          "type": "arrow",
          "id": "3ijOkm6K"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "Zhe8EStQ",
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
      "seed": 7098890,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "np.log1p(simple_\nreturns)",
      "rawText": "np.log1p(simple_ returns)",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "w9AeHzdOscQy1yQE",
      "originalText": "np.log1p(simple_\nreturns)",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "DEDnUWbw",
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
      "seed": 112109,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "QZc36RIY8DAMMA22",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "w9AeHzdOscQy1yQE",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "TCSbeDjkqnw7h9oT",
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
      "seed": 4269650,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "k4naGNGC"
        },
        {
          "type": "arrow",
          "id": "3ijOkm6K"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "k4naGNGC",
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
      "seed": 7410407,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "Computes log(1 + R) with extra\nprecision for numbers very close\nto zero.",
      "rawText": "Computes log(1 + R) with extra precision for numbers very close to zero.",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "TCSbeDjkqnw7h9oT",
      "originalText": "Computes log(1 + R) with extra\nprecision for numbers very close\nto zero.",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "3ijOkm6K",
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
      "seed": 7914008,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "w9AeHzdOscQy1yQE",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "TCSbeDjkqnw7h9oT",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "QZi3CD0vBFA3gr9K",
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
      "seed": 2471474,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "sXysy4HA"
        },
        {
          "type": "arrow",
          "id": "P1sGeNac"
        },
        {
          "type": "arrow",
          "id": "VNqBsWqN"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "sXysy4HA",
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
      "seed": 9347569,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "Extract Close\nPrices",
      "rawText": "Extract Close Prices",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "QZi3CD0vBFA3gr9K",
      "originalText": "Extract Close\nPrices",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "P1sGeNac",
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
      "seed": 2535729,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "5VEozoNtf3tBIdvz",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "QZi3CD0vBFA3gr9K",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "EBmJVvy2EFHmFHp5",
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
      "seed": 1565466,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "8pahPLgD"
        },
        {
          "type": "arrow",
          "id": "VNqBsWqN"
        },
        {
          "type": "arrow",
          "id": "YNAIfUzm"
        },
        {
          "type": "arrow",
          "id": "6js2q2jA"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "8pahPLgD",
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
      "seed": 8219812,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "Assemble Price\nMatrix",
      "rawText": "Assemble Price Matrix",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "EBmJVvy2EFHmFHp5",
      "originalText": "Assemble Price\nMatrix",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "VNqBsWqN",
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
      "seed": 8609761,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "QZi3CD0vBFA3gr9K",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "EBmJVvy2EFHmFHp5",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "5DVTs1s7rBGUoiRP",
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
      "seed": 3245898,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "lbilhNqp"
        },
        {
          "type": "arrow",
          "id": "YNAIfUzm"
        },
        {
          "type": "arrow",
          "id": "K8fP25Sy"
        }
      ],
      "updated": 1789189620820,
      "link": null,
      "locked": false
    },
    {
      "id": "lbilhNqp",
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
      "seed": 7096715,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
      "link": null,
      "locked": false,
      "text": "Apply Log\nTransformation",
      "rawText": "Apply Log Transformation",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "5DVTs1s7rBGUoiRP",
      "originalText": "Apply Log\nTransformation",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "YNAIfUzm",
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
      "seed": 5298809,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620820,
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
        "elementId": "EBmJVvy2EFHmFHp5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "5DVTs1s7rBGUoiRP",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "kyAK5UDSDmywHxi5",
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
      "seed": 9777463,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "A5yazSP1"
        },
        {
          "type": "arrow",
          "id": "K8fP25Sy"
        }
      ],
      "updated": 1789189620827,
      "link": null,
      "locked": false
    },
    {
      "id": "A5yazSP1",
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
      "seed": 6571777,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620827,
      "link": null,
      "locked": false,
      "text": "Clean the\nBoundary Row",
      "rawText": "Clean the Boundary Row",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "kyAK5UDSDmywHxi5",
      "originalText": "Clean the\nBoundary Row",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "K8fP25Sy",
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
      "seed": 6067918,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620827,
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
        "elementId": "5DVTs1s7rBGUoiRP",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "kyAK5UDSDmywHxi5",
        "focus": 0,
        "gap": 1
      },
      "startArrowhead": null,
      "endArrowhead": "arrow"
    },
    {
      "id": "bA7rUSis5Syjdw1Q",
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
      "seed": 675179,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": [
        {
          "type": "text",
          "id": "hS7QhXPa"
        },
        {
          "type": "arrow",
          "id": "6js2q2jA"
        }
      ],
      "updated": 1789189620827,
      "link": null,
      "locked": false
    },
    {
      "id": "hS7QhXPa",
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
      "seed": 2961031,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620827,
      "link": null,
      "locked": false,
      "text": "Combine into a\nsingle DataFrame",
      "rawText": "Combine into a single DataFrame",
      "fontSize": 20,
      "fontFamily": 7,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "bA7rUSis5Syjdw1Q",
      "originalText": "Combine into a\nsingle DataFrame",
      "hasTextLink": false,
      "autoResize": true,
      "lineHeight": 1.15
    },
    {
      "id": "6js2q2jA",
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
      "seed": 377219,
      "version": 1,
      "versionNonce": 1,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1789189620827,
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
        "elementId": "EBmJVvy2EFHmFHp5",
        "focus": 0,
        "gap": 1
      },
      "endBinding": {
        "elementId": "bA7rUSis5Syjdw1Q",
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
