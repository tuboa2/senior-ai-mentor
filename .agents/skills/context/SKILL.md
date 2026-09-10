---
name: context
description: >-
  Inspect dynamic project context detection and verify whether Senior AI Mentor memory modifications are authorized or locked.
---

# Project Context & Memory Inspection (/context)

When invoked via `/context` or `/context [path]`, inspect the active project workspace to determine whether it is related to AI, Machine Learning, Data Science, or Software Systems, and verify the Senior AI Mentor memory modification authorization status.

## 1. Execution Procedure

Execute the context inspector using `run_command`:
```bash
python3 -m senior_mentor.cli --context
```
Or for a specific path:
```bash
python3 -m senior_mentor.cli --context /path/to/project
```

## 2. Memory Isolation Policy
- **Related Project (AI/ML/Data Science/Distributed Systems):**
  - Senior AI Mentor memory is retrieved.
  - Live updates to knowledge state, misconception memory, decision memory, and project memory are **AUTHORIZED**.
- **Unrelated Project (Non-Technical / Non-ML):**
  - Senior AI Mentor memory is **LOCKED (READ-ONLY)**.
  - Zero modifications to SQLite memory tables are permitted to guarantee progress preservation.
