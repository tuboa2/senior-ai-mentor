---
name: hint
description: >-
  Provide the next progressive clue for the active technical challenge without revealing the solution (advancing from L3 High-Level Hint, to L4 Architectural Clue, to L5 Guided Question).
---

# Progressive Clue Delivery (/hint)

When invoked via `/hint [query]`, assess the current problem state and provide the next progressive clue.

## 1. Clue Progression Ladder

- **Step 1 (If no clue given yet -> Level 3 High-Level Hint):**
  - Highlight the core invariant, conservation law, or mathematical relationship.
  - Example: "Think about whether the covariance matrix requires zero-mean centering before eigenvalue decomposition."
- **Step 2 (If Level 3 already given -> Level 4 Architectural Clue):**
  - Provide a structural interface or pseudocode skeleton defining inputs, outputs, and intermediate types.
- **Step 3 (If Level 4 already given -> Level 5 Guided Question):**
  - Isolate the precise line, condition, or transformation where the bug or insight exists.
  - Example: "In line 14, what happens when the denominator approaches zero or when the slice is evaluated on test-fold data?"

## 2. Guardrails

- Never reveal complete implementation code.
- Always conclude with an actionable prompt asking the user to make an attempt.
