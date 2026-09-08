---
name: data-leakage-detection
description: >-
  Use this skill whenever building ML pipelines, engineering features, partitioning datasets,
  performing cross-validation, or auditing training code for subtle data leakage and lookahead bias.
---

# Data Leakage Detection Protocol (Tier 0 Core Skill)

Data leakage occurs when information from outside the training dataset (such as target values or future events) is inadvertently used to create the model, leading to overly optimistic evaluation and catastrophic production failure.

## 1. The Four Primary Leakage Vectors

1. **Target Leakage:**
   - Features included in the model that are proxies for the target or only available *after* the target event occurs (e.g., `account_closed_reason` in a churn prediction model).
   - *Audit Rule:* Check feature timestamps vs event timestamps. Every feature value must have been finalized strictly prior to the prediction horizon $T_0$.

2. **Train-Test Contamination (Pipeline Leakage):**
   - Performing transformations (imputation, scaling, normalization, feature selection, target encoding) *before* splitting the dataset into train/test folds.
   - *Audit Rule:* Fits (`fit`, `fit_transform`) must strictly execute on training folds only. Evaluation/test folds must only ever receive `transform`.

3. **Temporal Lookahead Bias:**
   - In time-series or sequential data, using random K-Fold cross-validation or future observations to predict past states.
   - *Audit Rule:* Always use forward-chaining splits (`TimeSeriesSplit` or expanding/rolling windows) where train timestamps $< \min(\text{test timestamps})$.

4. **Group / Identity Leakage:**
   - Samples from the same patient, user, device, or document appearing in both train and test splits (e.g., multiple ECG segments of the same patient).
   - *Audit Rule:* Enforce `GroupKFold` or hierarchical grouping on the entity identifier.

## 2. Leakage Audit Checklist

- [ ] Are any feature correlations with the target suspicious ($|r| > 0.95$ without domain justification)?
- [ ] Is `fit_transform` called on the entire dataset prior to splitting?
- [ ] Are duplicate or near-duplicate rows present across splits?
- [ ] Are window functions (e.g., rolling means) computed over the entire series without shifting by 1 step ($t-1$)?
- [ ] In target encoding, is out-of-fold target encoding or additive smoothing properly applied?

## 3. Automated Inspection Tool

Run the leakage checker on CSV files:
```bash
python3 .agents/skills/data-leakage-detection/scripts/leakage_checker.py --train train.csv --test test.csv --target label --id-col user_id --time-col timestamp
```
