"""Changelog manager and terminal viewer for Senior AI Engineering Mentor.

Provides in-terminal rendering of release notes and version history,
integrating with CHANGELOG.md for seamless visibility.
"""

from pathlib import Path
import re
import sys
from typing import Dict, List, Optional
from .config import BASE_DIR

# ANSI escape codes
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"
RESET = "\033[0m"

EMBEDDED_CHANGELOG = """# Changelog

All notable changes to the **Senior AI Engineering Mentor & Orchestrator Council** will be documented in this file.

---

## [1.1.1] - 2026-09-10

### Added
- **Dynamic Project Context Detection & Conditional Memory Modification Protocol:**
  - Automated project context detection via ProjectContextDetector.
  - Inspects dependency manifests, model artifacts (.pt, .onnx, .safetensors), structured data (.parquet, .duckdb), and notebooks (.ipynb).
  - Conditional Memory Modification:
    - Related projects (AI, ML, Data Science, Distributed Systems): Mentor memory retrieved and progress updates authorized.
    - Unrelated projects (Non-technical, static blogs, general recipes): Mentor memory locked (read-only) with zero SQLite mutations permitted.
  - Double-layer protection: method-level checks + connection rollback guarantee.
- **New In-Session Command & CLI Flag:**
  - /context [path]: Inspect detected project context and memory lock status in session.
  - --context [path]: CLI flag to inspect workspace domain classification.
- **New Core Skill:**
  - /context skill for dynamic project context inspection.

### Changed
- Upgraded framework version to 1.1.1 across all components.
- Orchestrator automatically evaluates workspace context and enforces memory lock state.
- Welcome output and formatted responses display active project classification and memory authorization status.

---

## [1.1.0] - 2026-09-09

### Added
- **Seamless Dynamic Workspace Update:**
  - Automated detection and synchronization of outdated project scope directories (.agents/).
  - Added update_workspace() for one-command updating of skills, directives, and manifests.
  - Manifest tracking via .agents/manifest.json recording framework version and synced skills.
  - New CLI commands: mentor --update, agy-mentor update, and /update in-session command.
- **Out-of-Scope Query Rejection & Strict Memory Isolation Protocol:**
  - Real-time scope detection via ScopeGuard covering 7 core engineering pillars.
  - Explicit boundary rejection for culinary/recipes, creative writing, sports/celebrity gossip, medical, and legal advice.
  - Strict zero-mutation memory guarantee: out-of-scope requests write 0 rows to SQLite memory tables.
  - Contextual domain-entity override for software engineering tasks operating on domain entities.
- **Terminal & GitHub Changelog System:**
  - Keep a Changelog compliant CHANGELOG.md for GitHub.
  - In-terminal ANSI changelog viewer accessible via mentor --changelog [version], agy-mentor changelog, and /changelog.
- **New Tier 0 Slash Command Skills:**
  - /update: Refresh initialized project scope with latest mentor skills and directives.
  - /changelog: Inspect release notes and feature history directly inside session.

### Changed
- Upgraded package version to 1.1.0 in senior_mentor/__init__.py.
- Updated OrchestratorResponse to support rejection status and reasons.
- Enhanced MentorCLI.format_response() with high-visibility warning and rejection banners.
- Updated GEMINI.md and AGENTS.md directives to formalize Scope Guard and Memory Isolation laws.

---

## [1.0.0] - 2026-09-08

### Added
- **14 Permanent Expert Council Personas:**
  - ML Architect, ML Research Scientist, Data Scientist, Statistician, Math for ML Expert, Data Engineer, MLOps Engineer, Software Architect, Performance Engineer, AI/LLM Engineer, Code Reviewer, Red Team / Adversarial Reviewer, Pedagogical Mentor, and Technical Interviewer.
- **The Disagreement Protocol:**
  - Strict prohibition of false consensus.
  - Structured dissent exposure with experiment-first scientific validation protocols.
- **Adaptive Scaffolding Engine (L0 to L7):**
  - 8-tier scaffolding system ranging from L0 Direct Solution to L7 Adversarial Self-Critique.
  - Anti-dependency safeguard tracking direct solution ratios vs Socratic exploration.
- **Multi-Faceted Persistent Memory Store:**
  - SQLite backend implementing 8 memory stores (Profile, Knowledge, Projects, Research, Decisions, Experiments, Misconceptions, Preferences).
- **Tiered Skill Architecture & AST Security Sandbox:**
  - AST-based static security analyzer checking for unauthorized sockets, subprocesses, or filesystem access.
- **Phase 7 Autonomous Self-Improvement:**
  - Automated feedback capture loop and recurring misconception analysis.
- **Google Antigravity CLI (agy) Integration:**
  - Zero-dependency CLI interface with strict ANTIGRAVITY_CLI environment enforcement.
"""

class ChangelogManager:
    """Parses and formats CHANGELOG.md for terminal inspection and runtime access."""

    def __init__(self, changelog_path: Optional[Path] = None):
        self.changelog_path = changelog_path or (BASE_DIR / "CHANGELOG.md")
        self._raw_text: Optional[str] = None

    def get_raw_text(self) -> str:
        if self._raw_text is not None:
            return self._raw_text

        # Try designated path
        if self.changelog_path and self.changelog_path.exists():
            try:
                self._raw_text = self.changelog_path.read_text(encoding="utf-8")
                return self._raw_text
            except Exception:
                pass

        # Try current working directory
        cwd_changelog = Path.cwd() / "CHANGELOG.md"
        if cwd_changelog.exists():
            try:
                self._raw_text = cwd_changelog.read_text(encoding="utf-8")
                return self._raw_text
            except Exception:
                pass

        # Try global install directory
        global_changelog = Path.home() / ".senior-ai-mentor" / "CHANGELOG.md"
        if global_changelog.exists():
            try:
                self._raw_text = global_changelog.read_text(encoding="utf-8")
                return self._raw_text
            except Exception:
                pass

        self._raw_text = EMBEDDED_CHANGELOG
        return self._raw_text

    def list_versions(self) -> List[str]:
        """Returns all versions documented in the changelog in descending order."""
        text = self.get_raw_text()
        return re.findall(r"^##\s+\[([\d\.]+)\]", text, re.MULTILINE)

    def get_latest_version(self) -> str:
        versions = self.list_versions()
        return versions[0] if versions else "1.1.0"

    def get_version_notes(self, target_version: str) -> Optional[str]:
        """Extracts release notes for a specific version."""
        text = self.get_raw_text()
        pattern = rf"(##\s+\[{re.escape(target_version)}\][\s\S]*?)(?=(^##\s+\[|\Z))"
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None

    def format_terminal_output(self, version: Optional[str] = None, use_color: bool = True) -> str:
        """Renders formatted changelog for ANSI terminal display."""
        if version:
            content = self.get_version_notes(version)
            if not content:
                available = ", ".join(self.list_versions())
                return f"Version '{version}' not found in changelog. Available versions: {available}"
        else:
            content = self.get_raw_text()

        if not use_color:
            return content

        lines = []
        for line in content.splitlines():
            if line.startswith("# "):
                lines.append(f"\n{BOLD}{CYAN}{line}{RESET}")
            elif line.startswith("## "):
                lines.append(f"\n{BOLD}{CYAN}{line}{RESET}")
            elif line.startswith("### Added"):
                lines.append(f"{BOLD}{GREEN}{line}{RESET}")
            elif line.startswith("### Changed"):
                lines.append(f"{BOLD}{YELLOW}{line}{RESET}")
            elif line.startswith("### Fixed"):
                lines.append(f"{BOLD}{MAGENTA}{line}{RESET}")
            elif line.startswith("### Security"):
                lines.append(f"{BOLD}{RED}{line}{RESET}")
            elif line.startswith("---"):
                lines.append(f"{CYAN}{'─' * 60}{RESET}")
            elif "**" in line:
                # Highlight bold tokens
                parts = line.split("**")
                formatted_parts = []
                for i, part in enumerate(parts):
                    if i % 2 == 1:
                        formatted_parts.append(f"{BOLD}{part}{RESET}")
                    else:
                        formatted_parts.append(part)
                lines.append("".join(formatted_parts))
            else:
                lines.append(line)

        return "\n".join(lines)
