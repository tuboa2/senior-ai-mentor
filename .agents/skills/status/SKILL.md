---
name: status
description: >-
  Display learner profile, competency ratings across 5 core engineering dimensions, anti-dependency metrics, tracked misconceptions, and personalized learning roadmap.
---

# Learner Status & Competency Evaluation (/status)

When invoked via `/status`, inspect and report the learner's longitudinal profile and competency evaluation.

## 1. Execution Procedure

Execute the CLI status reporter using `run_command`:
```bash
python3 -m senior_mentor.cli --status
```

## 2. Reporting Breakdown

Present the output clearly formatted:
1. **Learner Profile:** Target Role, Current Assessed Level, Overall Score (out of 10.0).
2. **5 Core Competency Dimensions:**
   - Technical Correctness & Mathematical Soundness
   - Architectural Design & Scalability
   - Statistical Validity & Leakage Resistance
   - Defensive Programming & Security
   - Trade-Off Communication & Justification
3. **Anti-Dependency Health:** Direct Solve vs. Socratic Ratio (Threshold: <= 65%).
4. **Active Misconceptions:** Unresolved conceptual gaps and recurring bugs tracked across sessions.
5. **Actionable Roadmap:** Targeted learning recommendations and suggested next challenges.
