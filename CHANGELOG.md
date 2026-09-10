# Changelog

All notable changes to the **Senior AI Engineering Mentor & Orchestrator Council** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.1] - 2026-09-10

### Added
- **Dynamic Project Context Detection & Conditional Memory Modification Protocol:**
  - Automated project context detection via `senior_mentor.project_detector.ProjectContextDetector`.
  - Comprehensive workspace inspection analyzing:
    - Dependency manifests (`requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile`, `environment.yml`, `package.json`).
    - Dedicated AI/ML directory trees (`models/`, `data/`, `notebooks/`, `pipelines/`, `experiments/`).
    - Model artifact files (`.pt`, `.onnx`, `.safetensors`, `.h5`, `.tflite`, `.pkl`).
    - Structured data storage (`.parquet`, `.arrow`, `.feather`, `.duckdb`, `.sqlite3`).
    - Jupyter notebooks (`.ipynb`) and AST code import scanning.
  - **Conditional Memory Modification Enforcement:**
    - **Related Projects (AI, ML, Data Science, Distributed Systems):** Senior AI Mentor retrieves memory and learner progress. Live updates to knowledge state, misconception memory, decision memory, and project memory are **AUTHORIZED**.
    - **Unrelated Projects (Non-Technical, Static Blogs, Recipes, General Docs):** Senior AI Mentor memory is **LOCKED (READ-ONLY)**. Modifications to SQLite memory tables are strictly blocked to prevent corruption of the mentor's progress records.
  - **Double-Layer Mutation Protection in `MemoryStore`:**
    - Layer 1: Individual write methods check `mutation_allowed` and return early without mutating state.
    - Layer 2: Connection-level rollback in `_get_conn(for_write=True)` ensures 0 commits if writes are attempted while locked.
- **New In-Session Command & CLI Flag:**
  - `/context [path]`: Inspect the detected project classification, confidence, frameworks, and memory status directly inside Antigravity CLI.
  - `--context [path]` flag on `mentor` and `agy-mentor` CLI for standalone workspace inspection.
- **New Core Skill:**
  - `/context` skill added to `.agents/skills/context/SKILL.md` and registered in `CORE_MENTOR_SKILLS`.

### Changed
- Upgraded package version to `1.1.1` across `senior_mentor/__init__.py`, `pyproject.toml`, `setup.py`, and `senior_mentor/initializer.py`.
- Updated `Orchestrator` to automatically evaluate active workspace context upon initialization and conditionalize `MemoryStore.set_mutation_allowed()`.
- Updated `MentorCLI` welcome message and response formatting to display active project context classification and memory authorization status.
- Updated `GEMINI.md` and `AGENTS.md` with Section 6: Dynamic Project Context Detection & Conditional Memory Modification Protocol.

---

## [1.1.0] - 2026-09-09

### Added
- **Seamless Dynamic Workspace Update:**
  - Automated detection and synchronization of outdated project scope directories (`.agents/`).
  - Added `senior_mentor.initializer.update_workspace()` for one-command updating of skills, directives, configurations, and global discovery.
  - Project manifest tracking via `.agents/manifest.json` recording framework version, initialization timestamp, last updated timestamp, and synced skill inventory.
  - New CLI commands: `mentor --update [path]`, `agy-mentor update [path]`.
  - New in-session slash command: `/update` to refresh the active workspace directly inside Antigravity CLI.
- **Out-of-Scope Query Rejection & Strict Memory Isolation Protocol:**
  - Real-time scope detection via `senior_mentor.pedagogy.scope_guard.ScopeGuard`.
  - Comprehensive classification covering the 7 engineering pillars (ML/DL, Mathematics for ML, Software Architecture, Data Engineering, MLOps, Algorithms/Interviews, Programming Tools).
  - Explicit boundary enforcement rejecting culinary/recipes, creative fiction, sports/celebrity gossip, clinical medical advice, legal litigation, and astrology/lifestyle queries.
  - Strict zero-mutation memory guarantee: out-of-scope requests write 0 rows to SQLite tables (`scaffolding_log`, `knowledge_state`, `decision_memory`, `misconception_memory`, `feedback_log`, `user_profile`).
  - Contextual domain-entity override permitting engineering tasks that operate on real-world entities (e.g., database schema for recipe storage, scraper scripts).
- **Terminal & GitHub Changelog System:**
  - Markdown changelog adhering to Keep a Changelog standards (`CHANGELOG.md`).
  - In-terminal ANSI-formatted changelog viewer accessible via `mentor --changelog [version]`, `agy-mentor changelog`, and the `/changelog` slash command.
  - Formatted terminal rendering with distinct color highlights for additions, modifications, and fixes.
- **New Tier 0 Slash Command Skills:**
  - `/update`: Check and perform dynamic workspace synchronization.
  - `/changelog`: Inspect version history and release notes in-session.

### Changed
- Upgraded package version to `1.1.0` in `senior_mentor/__init__.py`.
- Updated `OrchestratorResponse` to support rejection status and reasons (`is_rejected`, `rejection_reason`).
- Enhanced `MentorCLI.format_response()` with high-visibility warning and rejection banners.
- Updated `GEMINI.md` and `AGENTS.md` workspace directives to formalize Scope Guard and Memory Isolation laws.

---

## [1.0.0] - 2026-09-08

### Added
- **14 Permanent Expert Council Personas:**
  - ML Architect, ML Research Scientist, Data Scientist, Statistician, Math for ML Expert, Data Engineer, MLOps Engineer, Software Architect, Performance Engineer, AI/LLM Engineer, Code Reviewer, Red Team / Adversarial Reviewer, Pedagogical Mentor, and Technical Interviewer.
  - Dynamic Specialist Spawner for niche domains (Graph ML, Causal Inference, Speech/Audio, RL, Robotics).
- **The Disagreement Protocol:**
  - Strict prohibition of false consensus.
  - Structured dissent exposure with experiment-first scientific validation protocols.
- **Adaptive Scaffolding Engine (L0 to L7):**
  - 8-tier scaffolding system ranging from L0 Direct Solution to L7 Adversarial Self-Critique.
  - Anti-dependency safeguard tracking direct solution ratios vs Socratic exploration.
- **Multi-Faceted Persistent Memory Store:**
  - SQLite backend implementing 8 memory stores: User Profile, Knowledge State, Project Memory, Research Memory, Decision Memory, Experiment Memory, Error/Misconception Memory, and Technical Preferences.
- **Knowledge Graph:**
  - Prerequisite dependency modeling, topological sorting, and automated knowledge gap detection.
- **Tiered Skill Architecture & Security Sandbox:**
  - AST-based static security analyzer checking for unauthorized socket, subprocess, or filesystem access.
  - Isolation sandbox enforcing timeout and memory boundaries.
- **Phase 7 Autonomous Self-Improvement:**
  - Automated feedback capture loop and recurring misconception analysis.
  - Staged component versioning and refinement proposal generator.
- **Google Antigravity CLI (agy) Integration:**
  - Zero-dependency CLI interface with strict `ANTIGRAVITY_CLI` environment enforcement.
  - Automated workspace initialization via `mentor --init` and `agy-mentor init`.
