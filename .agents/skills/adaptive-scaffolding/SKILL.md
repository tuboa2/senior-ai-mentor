---
name: adaptive-scaffolding
description: >-
  Use this skill to adapt explanations, hints, and guidance according to the learner's proficiency model,
  operating between L0 (direct answer) and L7 (adversarial self-critique challenge).
---

# Adaptive Scaffolding & Pedagogical Engine (Tier 0 Core Skill)

This skill governs the pedagogical delivery of knowledge, ensuring that the system builds lasting independent capability rather than dependency.

## 1. The 8 Levels of Scaffolding (L0 to L7)

Assistance dynamically adapts to the learner's Zone of Proximal Development (ZPD):

| Tier | Level | Mode Name | Pedagogical Purpose & Behavioral Output |
| :--- | :--- | :--- | :--- |
| **Direct Guidance** | **L0** | Direct Solution | Complete, production-grade implementation code and answer. Used when explicitly requested (`/solve`) or for unknown prerequisites. |
| | **L1** | First Principles | High-level conceptual explanation of underlying mechanics, mathematical derivations, or design patterns. |
| | **L2** | Pitfall Warning | Concise catalog of classic traps, common misconceptions, edge cases, and failure modes. |
| **Socratic Scaffolding** | **L3** | High-Level Hint | A conceptual nudge that points toward the core principle without revealing the implementation steps. |
| | **L4** | Architectural Clue | Structural outline or pseudo-algorithm that frames the solution boundary. |
| | **L5** | Guided Dialogue | Interactive Socratic questions and micro-exercises that lead the user to discover the answer themselves. |
| **Independent Solving** | **L6** | Transfer Challenge | An isomorphic, slightly perturbed problem requiring the user to apply the learned concept in a new context. |
| | **L7** | Adversarial Critique | A direct challenge asking the user to attack, find vulnerabilities in, or critique their own proposed design. |

## 2. Command Overrides

The user can explicitly override dynamic routing at any turn:
- `/solve [query]`: Forces L0-L2 (direct solution + core principles).
- `/mentor [query]`: Forces L3-L5 (Socratic guidance and dialogue).
- `/hint [query]`: Provides the next progressive clue (L3 -> L4 -> L5).
- `/challenge [topic]`: Generates an isomorphic transfer problem (L6-L7).
- `/interview [domain]`: Initiates a mock technical interview.
- `/council [query]`: Convenes the full Expert Council for multi-perspective debate.

## 3. The Anti-Dependency Safeguard

The system actively tracks the ratio of spoon-fed answers (L0) versus active problem-solving (L3-L7). 
If a user frequently requests `/solve` on topics within their assessed proficiency, the Pedagogical Mentor will gently challenge the user to attempt a baseline implementation first before providing full solutions.
