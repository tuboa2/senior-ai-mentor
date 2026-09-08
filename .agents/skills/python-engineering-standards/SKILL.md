---
name: python-engineering-standards
description: >-
  Use this skill whenever writing, refactoring, or reviewing Python code for machine learning,
  data engineering, and production systems to enforce senior engineering quality standards.
---

# Python Engineering Standards for Production AI/ML (Tier 0 Core Skill)

This standard establishes non-negotiable guidelines for writing robust, maintainable, performant, and type-safe Python code in AI and data systems.

## 1. Core Principles

1. **Strict Type Annotations:**
   - Every function and method signature must have full type annotations (`typing`, `collections.abc`, or Python 3.10+ native types `list[str]`, `dict[str, Any]`, `X | None`).
   - Use `TypedDict` or `@dataclass(frozen=True)` / Pydantic models for structured configurations and data payloads. Never pass untyped dictionaries across architectural boundaries.

2. **Clean Architecture & Separation of Concerns:**
   - Decouple data ingestion, preprocessing, modeling, evaluation, and serving into dedicated modules.
   - Scripts with top-level procedural code are forbidden in production. Wrap entry points inside `main()` guarded by `if __name__ == "__main__":`.

3. **Determinism and Reproducibility:**
   - Explicitly seed all pseudo-random number generators (`random.seed()`, `np.random.seed()`, `torch.manual_seed()`, `torch.cuda.manual_seed_all()`).
   - Use deterministic algorithms where available (`torch.use_deterministic_algorithms(True)`).

4. **Performance & Memory Hygiene:**
   - Never iterate row-by-row with `for index, row in df.iterrows():`. Use vectorized NumPy/Polars operations or apply with specialized routines.
   - For massive datasets or streaming pipelines, use generators or chunked iteration to maintain bounded memory footprint ($O(1)$ spatial complexity).
   - Profiling before optimization: measure with `cProfile`, `py-spy`, or `torch.profiler`.

5. **Defensive Error Handling & Logging:**
   - Never use bare `except:` or `except Exception: pass`. Catch specific exceptions.
   - Use structured logging (`logging.getLogger(__name__)`) with context dictionaries instead of `print()` statements.

## 2. Automated Code Linting Tool

Use the built-in ML code linter to identify common anti-patterns:
```bash
python3 .agents/skills/python-engineering-standards/scripts/lint_ml_code.py path/to/script.py
```
