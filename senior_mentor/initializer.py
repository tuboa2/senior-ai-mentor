"""Project and Global Initializer for Senior AI Engineering Mentor.

Enables one-command initialization across any project repository and operating system
(Linux, macOS, Windows) with cross-project memory persistence.
"""

from pathlib import Path
import json
import os
import shutil
import sys
from typing import Dict, List, Optional
from .config import (
    BASE_DIR,
    GLOBAL_CONFIG_DIR,
    GLOBAL_DATA_DIR,
    GLOBAL_RULES_PATH,
    SKILLS_TIER0_DIR,
    ensure_directories
)

def get_gemini_template() -> str:
    gemini_path = BASE_DIR / "GEMINI.md"
    if gemini_path.exists():
        return gemini_path.read_text(encoding="utf-8")
    return "# Workspace Directives: Senior AI Engineering Mentor\n"

def get_agents_template() -> str:
    agents_path = BASE_DIR / "AGENTS.md"
    if agents_path.exists():
        return agents_path.read_text(encoding="utf-8")
    return "# Multi-Agent Senior Engineering Mentor Specification\n"

def initialize_workspace(
    target_dir: Path,
    enable_global: bool = True,
    copy_core_skills: bool = True
) -> Dict[str, List[str]]:
    """Initializes a repository or workspace to run the Senior Engineering Mentor."""
    target_dir = target_dir.resolve()
    created_files: List[str] = []
    messages: List[str] = []

    # 1. Ensure global persistence directory exists
    ensure_directories()
    messages.append(f"Connected to persistent global memory at: {GLOBAL_DATA_DIR}")

    # 2. Setup project .agents directory
    agents_dir = target_dir / ".agents"
    agents_skills_dir = agents_dir / "skills"
    agents_skills_dir.mkdir(parents=True, exist_ok=True)

    # 3. Copy Tier 0 Core Skills into project if requested (ensures repository is self-contained for GitHub)
    if copy_core_skills and SKILLS_TIER0_DIR.exists() and SKILLS_TIER0_DIR.resolve() != agents_skills_dir.resolve():
        for skill_dir in SKILLS_TIER0_DIR.iterdir():
            if skill_dir.is_dir():
                dest = agents_skills_dir / skill_dir.name
                if not dest.exists():
                    shutil.copytree(skill_dir, dest)
                    created_files.append(str(dest))

    # 4. Create .agents/skills.json
    skills_json_path = agents_dir / "skills.json"
    skills_config = {
        "entries": [
            {
                "path": ".agents/skills"
            },
            {
                "path": str(Path.home() / ".gemini" / "antigravity-cli" / "skills"),
                "include_only": [
                    "ab-testing",
                    "advanced-evaluation",
                    "agent-creator",
                    "ai-agents-architect",
                    "api-security-best-practices",
                    "application-performance-performance-optimization",
                    "architecture-decision-records",
                    "architecture-patterns",
                    "async-python-patterns",
                    "auto-research",
                    "code-reviewer",
                    "active-directory-attacks",
                    "accessibility-compliance-accessibility-audit"
                ]
            }
        ]
    }
    with open(skills_json_path, "w", encoding="utf-8") as f:
        json.dump(skills_config, f, indent=2)
    created_files.append(str(skills_json_path))

    # 5. Create project GEMINI.md and AGENTS.md
    proj_gemini = target_dir / "GEMINI.md"
    if not proj_gemini.exists():
        proj_gemini.write_text(get_gemini_template(), encoding="utf-8")
        created_files.append(str(proj_gemini))

    proj_agents = target_dir / "AGENTS.md"
    if not proj_agents.exists():
        proj_agents.write_text(get_agents_template(), encoding="utf-8")
        created_files.append(str(proj_agents))

    # 6. Global configuration for Antigravity-CLI across all projects
    if enable_global:
        GLOBAL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        global_skills_json = GLOBAL_CONFIG_DIR / "skills.json"
        
        # Link Tier 0 skills in global config as well
        global_cfg = {
            "entries": [
                {
                    "path": str(SKILLS_TIER0_DIR)
                },
                {
                    "path": str(Path.home() / ".gemini" / "antigravity-cli" / "skills"),
                    "include_only": skills_config["entries"][1]["include_only"]
                }
            ]
        }
        with open(global_skills_json, "w", encoding="utf-8") as f:
            json.dump(global_cfg, f, indent=2)
        messages.append(f"Configured global Antigravity discovery: {global_skills_json}")

        # Update global GEMINI.md if not already set
        if not GLOBAL_RULES_PATH.exists() or GLOBAL_RULES_PATH.stat().st_size == 0:
            GLOBAL_RULES_PATH.write_text(get_gemini_template(), encoding="utf-8")
            messages.append(f"Activated global rules: {GLOBAL_RULES_PATH}")

    return {
        "created_files": created_files,
        "messages": messages
    }
