---
name: statistical-validation
description: >-
  Use this skill whenever evaluating model metrics, testing hypotheses, validating experimental results,
  checking statistical assumptions (normality, independence, homoscedasticity), or detecting p-hacking.
---

# Statistical Validation Protocol (Tier 0 Core Skill)

This skill provides rigorous statistical procedures to ensure that empirical machine learning and data science results are statistically sound, reproducible, and resistant to false discovery.

## 1. Assumption Verification Checklist

Before reporting metrics or statistical significance, verify the following:

1. **Independence of Observations:**
   - Are samples independent and identically distributed (i.i.d.)?
   - In time-series or hierarchical/clustered data, standard t-tests and random cross-validation are strictly invalid.
   - *Action:* Check for temporal autocorrelation (Durbin-Watson) or intra-cluster correlation.

2. **Distributional Assumptions:**
   - For parametric tests (t-test, ANOVA), test for normality (Shapiro-Wilk for $N < 5000$, D'Agostino-Pearson for larger $N$) or rely on the Central Limit Theorem only when $N \gg 30$ and distributions are not heavily skewed.
   - If distributions are heavy-tailed or skewed, apply non-parametric equivalents (Mann-Whitney U, Wilcoxon signed-rank, Kruskal-Wallis, or bootstrap resampling).

3. **Homoscedasticity (Equal Variance):**
   - Verify variance homogeneity with Levene's test or Bartlett's test. If violated, use Welch's t-test instead of Student's t-test.

## 2. Model Comparison and Evaluation Standards

When comparing Model A vs Model B:

1. **Avoid Point Estimates:** Never declare a model superior based solely on point differences (e.g., "0.842 vs 0.839 accuracy"). Always report confidence intervals (95% bootstrap CI or empirical Bayesian intervals).
2. **Multiple Comparison Corrections:**
   - When testing $k$ hypotheses or evaluating multiple hyperparameters, control Family-Wise Error Rate (FWER) or False Discovery Rate (FDR):
     - **Bonferroni Correction:** $\alpha_{adjusted} = \alpha / k$ (conservative, controls FWER).
     - **Benjamini-Hochberg (BH) Procedure:** Rank p-values $p_{(1)} \le \dots \le p_{(k)}$, find largest $i$ where $p_{(i)} \le \frac{i}{k} Q$, reject $H_{(1)} \dots H_{(i)}$ (controls FDR).
3. **Statistical Power & Sample Size:**
   - Calculate minimum detectable effect size (MDE) and statistical power ($1 - \beta \ge 0.80$) before declaring "no significant difference". Absence of evidence is not evidence of absence.

## 3. Automation Helper Script

Use the helper script to run fast automated validation:
```bash
python3 .agents/skills/statistical-validation/scripts/validate_stats.py --sample-a 0.82,0.85,0.83 --sample-b 0.81,0.84,0.80
```
