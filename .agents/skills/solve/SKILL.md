---
name: solve
description: >-
  Execute in L0-L2 Direct Guidance mode. Provide complete, production-grade implementation code, first-principles derivations, and a comprehensive catalog of edge-case pitfalls.
---

# Direct Production Solution & Derivations (/solve)

When invoked via `/solve <query>`, provide an exhaustive, senior-level engineering implementation.

## 1. Direct Guidance Deliverables

1. **L0 (Production Code Implementation):**
   - Clean, robust, production-grade code adhering to PEP 8 / Clean Architecture.
   - Comprehensive type hints (`typing` / `mypy` strict compliance).
   - Defensive error handling, explicit boundaries, and zero hidden assumptions.
   - Accompanying unit tests demonstrating normal execution and edge cases.
2. **L1 (First-Principles Derivation):**
   - Deep mathematical derivation or theoretical mechanics underlying the solution.
   - Explicit proofs, complexity bounds (Big-O time and space), and hardware memory layout implications.
3. **L2 (Catalog of Pitfalls & Edge Cases):**
   - Subtle numerical instabilities, overflow/underflow traps.
   - Concurrency race conditions, memory leaks, and GC pressure.
   - Data leakage vectors and subtle distribution shift failure modes.

## 2. Anti-Dependency Monitoring

Track whether the user has exceeded the 65% direct solve threshold in their session.
If so, append a gentle anti-dependency reminder recommending conceptual practice via `/mentor` or `/challenge`.

## 3. Automation Helper

```bash
python3 -m senior_mentor.cli "/solve <query>"
```
