---
name: challenge
description: >-
  Issue an isomorphic concept transfer challenge (L6) or adversarial self-critique exercise (L7) to test deep mastery and generalization of an engineering concept.
---

# Transfer & Adversarial Challenges (/challenge)

When invoked via `/challenge <concept>`, generate an advanced problem to stress-test concept mastery.

## 1. Challenge Types

### Level 6: Isomorphic Concept Transfer
- Identify the governing mathematical invariant or architectural pattern of the topic.
- Construct a completely new problem in an unrelated domain that shares the identical invariant.
- Example: If the topic was "Attention Mechanism in Transformers", transfer to "Soft routing across distributed database shards based on query affinity vectors."

### Level 7: Adversarial Self-Critique
- Present a realistic, seemingly complete architecture or code snippet that contains a subtle, critical flaw:
  - Hidden lookahead bias or data leakage in feature aggregation.
  - Subtle concurrency deadlock or cache invalidation race condition.
  - False statistical confidence from uncorrected multiple testing.
- Task the user: "Red-team this implementation: identify the fatal vulnerability, prove why it fails, and redesign the boundary."
