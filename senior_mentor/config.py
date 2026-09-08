"""Configuration and path management for Senior AI Engineering Mentor.

Supports both global cross-project persistence across all antigravity-cli workspaces
and optional project-local isolation.
"""

from dataclasses import dataclass
from pathlib import Path
import os
import sys

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Machine-wide global persistence locations (antigravity-cli integration)
GLOBAL_BASE_DIR = Path.home() / ".gemini"
GLOBAL_CLI_DIR = GLOBAL_BASE_DIR / "antigravity-cli"
GLOBAL_DATA_DIR = GLOBAL_CLI_DIR / "mentor_data"
GLOBAL_CONFIG_DIR = GLOBAL_BASE_DIR / "config"
GLOBAL_SKILLS_DIR = GLOBAL_CLI_DIR / "skills"
GLOBAL_RULES_PATH = GLOBAL_BASE_DIR / "GEMINI.md"

# Project-local fallback locations
LOCAL_DATA_DIR = BASE_DIR / ".mentor_data"
SKILLS_TIER0_DIR = BASE_DIR / ".agents" / "skills"

# Determine active persistence directory
# Default to machine-wide global persistence so all projects share state
_env_data_dir = os.environ.get("MENTOR_DATA_DIR")
_env_persistence = os.environ.get("MENTOR_PERSISTENCE", "global").lower()

if _env_data_dir:
    ACTIVE_DATA_DIR = Path(_env_data_dir)
elif _env_persistence == "local":
    ACTIVE_DATA_DIR = LOCAL_DATA_DIR
else:
    ACTIVE_DATA_DIR = GLOBAL_DATA_DIR

DB_PATH = ACTIVE_DATA_DIR / "mentor_memory.db"
AUDIT_LOG_PATH = ACTIVE_DATA_DIR / "audit_trail.jsonl"

@dataclass(frozen=True)
class MentorConfig:
    db_path: Path = DB_PATH
    audit_log_path: Path = AUDIT_LOG_PATH
    skills_tier0_dir: Path = SKILLS_TIER0_DIR
    global_skills_dir: Path = GLOBAL_SKILLS_DIR
    global_config_dir: Path = GLOBAL_CONFIG_DIR
    global_rules_path: Path = GLOBAL_RULES_PATH
    default_alpha: float = 0.05
    anti_dependency_threshold: float = 0.65  # Ratio above which direct solve is throttled
    max_execution_timeout_sec: int = 10
    is_global_persistence: bool = (_env_persistence == "global")

def ensure_directories(data_dir: Path = ACTIVE_DATA_DIR) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    GLOBAL_DATA_DIR.mkdir(parents=True, exist_ok=True)

def is_antigravity_cli(strict_test_bypass: bool = False) -> bool:
    """Checks whether the current execution is within the Google Antigravity CLI ('agy') environment.

    Args:
        strict_test_bypass: If True, ignores test/CI bypass flags (used to test the security guard).

    Returns:
        True if running inside Antigravity CLI or test environment, False otherwise.
    """
    if not strict_test_bypass:
        if (
            os.environ.get("MENTOR_ALLOW_TESTS") == "1"
            or os.environ.get("CI") == "true"
            or os.environ.get("TESTING") == "1"
            or "unittest" in sys.modules
            or "pytest" in sys.modules
        ):
            return True

    return bool(
        os.environ.get("ANTIGRAVITY_AGENT") == "1"
        or os.environ.get("AI_AGENT") == "antigravity"
        or os.environ.get("ANTIGRAVITY_CONVERSATION_ID")
        or os.environ.get("ANTIGRAVITY_LS_ADDRESS")
        or os.environ.get("ANTIGRAVITY_AGENTAPI_EXE")
        or "antigravity-cli" in os.environ.get("JETSKI_APP_DATA_DIR", "")
        or os.environ.get("ANTIGRAVITY_CLI") == "1"
    )

def enforce_antigravity_cli(strict_test_bypass: bool = False) -> None:
    """Enforces that execution is strictly contained within Antigravity CLI.

    Raises:
        RuntimeError: If executed in an independent terminal outside Antigravity CLI.
    """
    if not is_antigravity_cli(strict_test_bypass=strict_test_bypass):
        raise RuntimeError(
            "Senior AI Engineering Mentor is strictly configured for use within "
            "the Google Antigravity CLI ('agy') environment only. "
            "Independent terminal execution is disabled. "
            "Please launch 'agy' to interact with the mentor."
        )

