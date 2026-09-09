---
name: changelog
description: >-
  View the Senior AI Engineering Mentor release notes, version history, and recent updates directly in the session or terminal.
---

# Senior Mentor Changelog (/changelog)

When invoked via `/changelog`, display the version history and latest updates for the Senior AI Engineering Mentor framework.

## 1. Execution Procedure

Execute the changelog viewer using `run_command`:
```bash
python3 -m senior_mentor.cli --changelog
```
To view notes for a specific version:
```bash
python3 -m senior_mentor.cli --changelog 1.1.0
```

## 2. Reporting
Present the release notes clearly formatted with sections for:
- **Added:** New features, skills, protocols, and architectural components.
- **Changed:** Enhancements, behavioral updates, and optimizations.
- **Fixed:** Bug fixes, edge case corrections, and security hardening.
