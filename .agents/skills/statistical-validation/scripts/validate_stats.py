#!/usr/bin/env python3
"""Statistical validation script for comparing model metrics and testing assumptions.

Implements:
- Welch's t-test (heteroscedastic)
- Bootstrap 95% confidence intervals
- Benjamini-Hochberg (FDR) and Bonferroni corrections
Zero external dependencies required (uses stdlib math and statistics).
"""

import argparse
import math
import random
import statistics
import sys
from typing import List, Tuple

def parse_floats(s: str) -> List[float]:
    return [float(x.strip()) for x in s.split(",") if x.strip()]

def bootstrap_ci(data: List[float], n_resamples: int = 2000, alpha: float = 0.05) -> Tuple[float, float, float]:
    """Calculate empirical bootstrap confidence interval for the mean."""
    if not data:
        return (0.0, 0.0, 0.0)
    means = []
    n = len(data)
    for _ in range(n_resamples):
        resample = [random.choice(data) for _ in range(n)]
        means.append(statistics.mean(resample))
    means.sort()
    lower_idx = int((alpha / 2.0) * n_resamples)
    upper_idx = int((1.0 - alpha / 2.0) * n_resamples)
    mean_val = statistics.mean(data)
    return mean_val, means[lower_idx], means[upper_idx]

def welch_t_test(a: List[float], b: List[float]) -> Tuple[float, float, int]:
    """Calculate Welch's t-statistic and approximate degrees of freedom."""
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        return 0.0, 1.0, 1
    m1, m2 = statistics.mean(a), statistics.mean(b)
    v1, v2 = statistics.variance(a), statistics.variance(b)
    
    se = math.sqrt(v1 / n1 + v2 / n2)
    if se == 0:
        return 0.0, 1.0, n1 + n2 - 2
    t_stat = (m1 - m2) / se
    
    # Welch-Satterthwaite equation for degrees of freedom
    df_num = (v1 / n1 + v2 / n2) ** 2
    df_den = ((v1 / n1) ** 2) / (n1 - 1) + ((v2 / n2) ** 2) / (n2 - 1)
    df = int(df_num / df_den) if df_den > 0 else (n1 + n2 - 2)
    
    # Quick two-tailed p-value approximation via standard normal for df > 30 or student t approximation
    # For robust engineering checks without scipy:
    z = abs(t_stat)
    p_approx = 2.0 * (1.0 - 0.5 * (1.0 + math.erf(z / math.sqrt(2))))
    return t_stat, max(0.0, min(1.0, p_approx)), df

def adjust_p_values(p_values: List[float], method: str = "bh", fdr: float = 0.05) -> List[Tuple[float, bool]]:
    """Adjust p-values using Benjamini-Hochberg or Bonferroni."""
    m = len(p_values)
    if method == "bonferroni":
        return [(min(1.0, p * m), min(1.0, p * m) < fdr) for p in p_values]
    
    # Benjamini-Hochberg
    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
    adjusted = [0.0] * m
    significant = [False] * m
    
    # BH critical value: p(i) <= (i / m) * Q
    max_sig_rank = -1
    for rank, (original_idx, p_val) in enumerate(indexed, 1):
        crit = (rank / m) * fdr
        if p_val <= crit:
            max_sig_rank = rank
            
    for rank, (original_idx, p_val) in enumerate(indexed, 1):
        adj_p = min(1.0, p_val * (m / rank))
        is_sig = rank <= max_sig_rank if max_sig_rank != -1 else False
        adjusted[original_idx] = adj_p
        significant[original_idx] = is_sig
        
    return list(zip(adjusted, significant))

def main():
    parser = argparse.ArgumentParser(description="Statistical metric validation utility.")
    parser.add_argument("--sample-a", required=True, help="Comma-separated metrics for Sample A (e.g. 0.82,0.85,0.83)")
    parser.add_argument("--sample-b", help="Comma-separated metrics for Sample B (optional comparison)")
    parser.add_argument("--p-values", help="Comma-separated list of p-values for multiple testing correction")
    parser.add_argument("--correction", choices=["bh", "bonferroni"], default="bh", help="Correction method")
    parser.add_argument("--alpha", type=float, default=0.05, help="Significance level alpha (default 0.05)")
    args = parser.parse_args()

    data_a = parse_floats(args.sample_a)
    mean_a, low_a, high_a = bootstrap_ci(data_a, alpha=args.alpha)
    print(f"Sample A: N={len(data_a)} | Mean={mean_a:.4f} | 95% CI=[{low_a:.4f}, {high_a:.4f}]")

    if args.sample_b:
        data_b = parse_floats(args.sample_b)
        mean_b, low_b, high_b = bootstrap_ci(data_b, alpha=args.alpha)
        print(f"Sample B: N={len(data_b)} | Mean={mean_b:.4f} | 95% CI=[{low_b:.4f}, {high_b:.4f}]")
        
        t_stat, p_val, df = welch_t_test(data_a, data_b)
        diff = mean_a - mean_b
        print("\n--- Model Comparison (Welch's Two-Sample Test) ---")
        print(f"Delta (A - B): {diff:+.4f}")
        print(f"t-statistic: {t_stat:.4f}, df: ~{df}, approximate p-value: {p_val:.5f}")
        if p_val < args.alpha:
            print(f"RESULT: Statistically significant difference at alpha={args.alpha}!")
        else:
            print(f"RESULT: INSUFFICIENT evidence to reject H0 at alpha={args.alpha}. Do NOT declare victory.")

    if args.p_values:
        p_vals = parse_floats(args.p_values)
        results = adjust_p_values(p_vals, method=args.correction, fdr=args.alpha)
        print(f"\n--- Multiple Comparison Correction ({args.correction.upper()}) ---")
        for idx, (orig, (adj, sig)) in enumerate(zip(p_vals, results)):
            print(f"Test #{idx+1}: original p={orig:.5f} -> adjusted p={adj:.5f} | Significant: {sig}")

if __name__ == "__main__":
    main()
