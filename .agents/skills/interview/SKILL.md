---
name: interview
description: >-
  Launch a realistic senior/staff mock technical interview across System Design, ML Theory, Statistics, or Coding, and provide rigorous senior-level candidate evaluation.
---

# Senior Technical Mock Interview (/interview)

When invoked via `/interview [domain]` (domains: `system_design`, `ml_theory`, `statistics`, `coding`):

## 1. Interview Initiation

1. Retrieve or formulate an authentic senior/staff engineering interview scenario.
   Helper script command:
   ```bash
   python3 -m senior_mentor.cli --interview [domain]
   ```
2. Present the scenario with:
   - **Context & Scale:** Explicit user base, traffic volume (e.g. 100M DAU), latency SLA (e.g. p99 < 60ms).
   - **Key Constraints:** Hardware budget, data freshness, partition skew.
   - **Probing Dimensions:** 3 architectural and algorithmic questions to explore.

## 2. Candidate Evaluation Rubric

When the user submits their architectural response, evaluate them strictly across 4 senior dimensions:
- **Architectural Depth & Modularity (1-10):** Clean separation of concerns, scalability boundaries, failure isolation.
- **Trade-Off Justification (1-10):** Deep mechanical sympathy, explicit latency vs accuracy balancing.
- **Defensive Engineering & Edge Cases (1-10):** Handling cold-starts, drift, data corruption, network partitions.
- **Communication & Leadership (1-10):** Structural clarity, precision, avoiding hand-waving.

Assign an overall score and seniority classification:
- **Junior / Associate (< 5.0)**
- **Mid-Level (5.0 - 6.9)**
- **Senior Engineer (7.0 - 8.4)**
- **Staff / Principal Engineer (>= 8.5)**
