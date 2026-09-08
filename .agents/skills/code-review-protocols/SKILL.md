---
name: code-review-protocols
description: >-
  Use this skill whenever conducting formal code reviews, grading architectural designs,
  verifying test suites, checking security boundaries, or auditing PRs across engineering disciplines.
---

# Senior Engineering Code Review Protocols (Tier 0 Core Skill)

This protocol establishes the multi-perspective criteria employed by a Principal Engineer / Senior Staff Reviewer when auditing code.

## 1. The 6-Dimension Review Framework

Every pull request or implementation proposal must be evaluated against these six dimensions:

1. **Algorithmic Correctness & Mathematical Soundness:**
   - Are edge cases handled (empty batches, single-sample inference, NaN/Inf gradients, division by zero)?
   - Are matrix operations dimension-compatible with proper broadcasting behavior?
   - Do loss functions properly account for label imbalance or numerical instability (`log_sum_exp`)?

2. **Data & Pipeline Integrity:**
   - Is there any risk of train/test data leakage?
   - Are transformations deterministic? Are random seeds propagated?
   - Are schemas and data contracts verified upon ingestion?

3. **Performance & Resource Scalability:**
   - What are the asymptotic time ($O(T)$) and space ($O(S)$) complexities?
   - Are there hidden CPU-GPU memory bottlenecks (excessive `.cpu()`, `.item()`, or `.numpy()` inside training loops)?
   - Is memory explicitly freed or are tensor graphs inadvertently retained across iterations?

4. **Robustness & Defensive Engineering:**
   - Are exceptions typed, informative, and handled gracefully?
   - Are external I/O operations wrapped with retry logic, timeouts, and circuit breakers?
   - Is logging structured and contextual rather than unstructured standard output?

5. **Security & Threat Surface:**
   - Are user inputs sanitized to prevent code injection, SQL injection, or prompt injection?
   - Are credentials, tokens, or API keys isolated in environment configurations?
   - Are permissions adhering strictly to the principle of least privilege?

6. **Testability & Observability:**
   - Are pure functions decoupled from side-effects to enable fast unit testing?
   - Are mocks used judiciously without mocking away the core failure modes?
   - Are metrics exported to telemetry (OpenTelemetry, Prometheus, TensorBoard, WandB)?

## 2. Review Classification Standard

Review comments must be categorized with clear severity tags:
- `[BLOCKER]`: Must fix before merge. Threat to correctness, data integrity, or security.
- `[PERF]`: Significant performance or scalability bottleneck.
- `[ARCH]`: Architectural concern, violation of separation of concerns, or modularity issue.
- `[NIT]`: Minor style, naming, or readability suggestion. Non-blocking.
- `[QUESTION]`: Socratic inquiry asking the author to justify a specific design trade-off.
