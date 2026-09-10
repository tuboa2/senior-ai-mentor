"""Project and Global Initializer & Dynamic Workspace Updater for Senior AI Engineering Mentor.

Enables:
1. One-command workspace initialization across any project repository and operating system.
2. Seamless dynamic updating of existing/old initialized project scope directories (.agents/).
3. Manifest version tracking and automated sync of Tier 0 core skills and prompt directives.
"""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import sys
from typing import Any, Dict, List, Optional, Tuple
from .config import (
    BASE_DIR,
    GLOBAL_CONFIG_DIR,
    GLOBAL_DATA_DIR,
    GLOBAL_RULES_PATH,
    GLOBAL_SKILLS_DIR,
    SKILLS_TIER0_DIR,
    ensure_directories
)

CURRENT_FRAMEWORK_VERSION = "1.1.1"
MANIFEST_FILE_NAME = "manifest.json"

CORE_MENTOR_SKILLS = [
    "council",
    "mentor",
    "solve",
    "interview",
    "status",
    "hint",
    "challenge",
    "refine",
    "update",
    "changelog",
    "context",
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

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

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

def get_workspace_manifest(target_dir: Path) -> Optional[Dict[str, Any]]:
    """Reads the installed mentor manifest from the target workspace, if present."""
    manifest_path = target_dir / ".agents" / MANIFEST_FILE_NAME
    if manifest_path.exists():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
    return None

def write_workspace_manifest(
    target_dir: Path,
    synced_skills: List[str],
    version: str = CURRENT_FRAMEWORK_VERSION,
    initial_time: Optional[str] = None
) -> Path:
    """Writes or updates .agents/manifest.json with version and sync metadata."""
    agents_dir = target_dir / ".agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = agents_dir / MANIFEST_FILE_NAME

    existing = get_workspace_manifest(target_dir)
    init_at = initial_time or (existing.get("initialized_at") if existing else now_iso())

    manifest_data = {
        "framework_version": version,
        "initialized_at": init_at,
        "last_updated_at": now_iso(),
        "synced_skills": sorted(list(set(synced_skills))),
        "core_skills_count": len(synced_skills),
        "status": "up_to_date"
    }

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    return manifest_path

def check_workspace_update_available(target_dir: Path) -> Tuple[bool, str, Dict[str, Any]]:
    """Inspects a target workspace to determine if updates are available.
    
    Returns:
        (needs_update, reason, details)
    """
    target_dir = target_dir.resolve()
    agents_dir = target_dir / ".agents"
    if not agents_dir.exists():
        return True, "Workspace is not yet initialized for Senior AI Engineering Mentor.", {"installed_version": None}

    manifest = get_workspace_manifest(target_dir)
    installed_ver = manifest.get("framework_version") if manifest else "1.0.0"

    # Version mismatch
    if installed_ver != CURRENT_FRAMEWORK_VERSION:
        return True, f"Workspace framework version (v{installed_ver}) is behind latest release (v{CURRENT_FRAMEWORK_VERSION}).", {
            "installed_version": installed_ver,
            "target_version": CURRENT_FRAMEWORK_VERSION
        }

    # Check for missing core skills
    agents_skills_dir = agents_dir / "skills"
    missing_skills = []
    if SKILLS_TIER0_DIR.exists():
        for skill_dir in SKILLS_TIER0_DIR.iterdir():
            if skill_dir.is_dir() and not (agents_skills_dir / skill_dir.name).exists():
                missing_skills.append(skill_dir.name)

    if missing_skills:
        return True, f"Workspace is missing {len(missing_skills)} core skills: {', '.join(missing_skills)}", {
            "installed_version": installed_ver,
            "missing_skills": missing_skills
        }

    return False, "Workspace is up to date.", {"installed_version": installed_ver}

def update_workspace(
    target_dir: Path,
    force: bool = False,
    enable_global: bool = True
) -> Dict[str, Any]:
    """Dynamically updates an existing initialized project scope directory to the latest release.
    
    1. Synchronizes Tier 0 skills (installs newly added skills, updates modified skills, preserves custom user skills).
    2. Refreshes .agents/skills.json with current discovery configuration.
    3. Synchronizes GEMINI.md and AGENTS.md directives with latest framework specifications.
    4. Updates .agents/manifest.json recording framework version and sync timestamp.
    5. Refreshes global Antigravity CLI discovery paths.
    """
    target_dir = target_dir.resolve()
    agents_dir = target_dir / ".agents"
    agents_skills_dir = agents_dir / "skills"
    agents_skills_dir.mkdir(parents=True, exist_ok=True)

    updated_files: List[str] = []
    new_skills: List[str] = []
    updated_skills: List[str] = []
    messages: List[str] = []

    # 1. Synchronize Tier 0 Core Skills
    synced_skill_names: List[str] = []
    if SKILLS_TIER0_DIR.exists():
        for skill_dir in SKILLS_TIER0_DIR.iterdir():
            if skill_dir.is_dir():
                skill_name = skill_dir.name
                synced_skill_names.append(skill_name)
                dest = agents_skills_dir / skill_name

                if skill_dir.resolve() != dest.resolve():
                    if not dest.exists():
                        shutil.copytree(skill_dir, dest)
                        new_skills.append(skill_name)
                        updated_files.append(str(dest))
                    else:
                        src_skill_md = skill_dir / "SKILL.md"
                        dest_skill_md = dest / "SKILL.md"
                        # Compare content
                        if src_skill_md.exists():
                            src_content = src_skill_md.read_text(encoding="utf-8")
                            dest_content = dest_skill_md.read_text(encoding="utf-8") if dest_skill_md.exists() else ""
                            if src_content != dest_content or force:
                                shutil.copytree(skill_dir, dest, dirs_exist_ok=True)
                                updated_skills.append(skill_name)
                                updated_files.append(str(dest))

    # Also include any custom skills found in the project's .agents/skills/
    if agents_skills_dir.exists():
        for custom_skill in agents_skills_dir.iterdir():
            if custom_skill.is_dir() and custom_skill.name not in synced_skill_names:
                synced_skill_names.append(custom_skill.name)

    # 2. Refresh .agents/skills.json
    skills_json_path = agents_dir / "skills.json"
    skills_config = {
        "entries": [
            {
                "path": ".agents/skills"
            },
            {
                "path": str(Path.home() / ".gemini" / "antigravity-cli" / "skills"),
                "include_only": CORE_MENTOR_SKILLS
            }
        ]
    }
    with open(skills_json_path, "w", encoding="utf-8") as f:
        json.dump(skills_config, f, indent=2)
    updated_files.append(str(skills_json_path))

    # 3. Synchronize GEMINI.md and AGENTS.md
    proj_gemini = target_dir / "GEMINI.md"
    gemini_template = get_gemini_template()
    src_gemini = (BASE_DIR / "GEMINI.md").resolve()
    if src_gemini != proj_gemini.resolve():
        if not proj_gemini.exists() or proj_gemini.read_text(encoding="utf-8") != gemini_template or force:
            proj_gemini.write_text(gemini_template, encoding="utf-8")
            updated_files.append(str(proj_gemini))
            messages.append("Synchronized GEMINI.md directives with latest Scope Guard and Council rules.")

    proj_agents = target_dir / "AGENTS.md"
    agents_template = get_agents_template()
    src_agents = (BASE_DIR / "AGENTS.md").resolve()
    if src_agents != proj_agents.resolve():
        if not proj_agents.exists() or proj_agents.read_text(encoding="utf-8") != agents_template or force:
            proj_agents.write_text(agents_template, encoding="utf-8")
            updated_files.append(str(proj_agents))
            messages.append("Synchronized AGENTS.md specification.")

    # 4. Write/update .agents/manifest.json
    manifest_path = write_workspace_manifest(target_dir, synced_skill_names)
    updated_files.append(str(manifest_path))

    # 5. Global discovery refresh
    if enable_global:
        ensure_directories()
        GLOBAL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        global_skills_json = GLOBAL_CONFIG_DIR / "skills.json"

        global_cfg = {
            "entries": [
                {
                    "path": str(SKILLS_TIER0_DIR)
                },
                {
                    "path": str(Path.home() / ".gemini" / "antigravity-cli" / "skills"),
                    "include_only": CORE_MENTOR_SKILLS
                }
            ]
        }
        with open(global_skills_json, "w", encoding="utf-8") as f:
            json.dump(global_cfg, f, indent=2)

        # Mirror Tier 0 skills in ~/.gemini/antigravity-cli/skills/
        if GLOBAL_SKILLS_DIR.exists() and SKILLS_TIER0_DIR.exists():
            for skill_dir in SKILLS_TIER0_DIR.iterdir():
                if skill_dir.is_dir():
                    gdest = GLOBAL_SKILLS_DIR / skill_dir.name
                    if skill_dir.resolve() != gdest.resolve():
                        shutil.copytree(skill_dir, gdest, dirs_exist_ok=True)

        if not GLOBAL_RULES_PATH.exists() or force:
            GLOBAL_RULES_PATH.write_text(gemini_template, encoding="utf-8")

        messages.append(f"Global Antigravity discovery refreshed at: {global_skills_json}")

    return {
        "status": "success",
        "version": CURRENT_FRAMEWORK_VERSION,
        "target_dir": str(target_dir),
        "updated_files": updated_files,
        "new_skills": new_skills,
        "updated_skills": updated_skills,
        "messages": messages
    }

def initialize_workspace(
    target_dir: Path,
    enable_global: bool = True,
    copy_core_skills: bool = True
) -> Dict[str, List[str]]:
    """Initializes a repository or workspace to run the Senior Engineering Mentor."""
    target_dir = target_dir.resolve()
    res = update_workspace(target_dir, force=True, enable_global=enable_global)
    return {
        "created_files": res["updated_files"],
        "messages": res["messages"]
    }
