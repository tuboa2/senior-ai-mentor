# Changelog

All notable changes to the **Senior AI Engineering Mentor & Orchestrator Council** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
