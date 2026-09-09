---
name: update
description: >-
  Seamlessly synchronize the active project scope directory (.agents/) with the latest Senior AI Engineering Mentor skills, directives, and manifests.
---

# Dynamic Workspace Update (/update)

When invoked via `/update`, synchronize the project directory with the latest Senior AI Engineering Mentor framework release, ensuring all core skills, prompt directives, and manifests are up to date.

## 1. Execution Procedure

Execute the workspace dynamic update using `run_command`:
```bash
python3 -m senior_mentor.cli --update
```

## 2. Dynamic Update Steps
1. **Skill Inventory Sync:** Identifies and installs new Tier 0 skills, updates modified skills, and preserves user custom skills.
2. **Directive Refresh:** Harmonizes `GEMINI.md` and `AGENTS.md` with the latest engineering directives and memory isolation protocols.
3. **Manifest Update:** Records updated version and sync timestamp in `.agents/manifest.json`.
4. **Global Discovery:** Refreshes universal Antigravity CLI discovery paths.

Report the updated files, newly installed skills, and current framework version to the user.
