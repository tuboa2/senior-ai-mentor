"""Persistent structured memory store for Senior AI Engineering Mentor.

Implements all 8 required stores:
1. User Profile
2. Knowledge State
3. Project Memory
4. Research Memory
5. Decision Memory
6. Experiment Memory
7. Error / Misconception Memory
8. Technical Preferences
"""

from contextlib import contextmanager
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
from typing import Any, Dict, Generator, List, Optional
from ..config import DB_PATH, ensure_directories

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass
class UserProfile:
    user_id: str
    name: str
    target_role: str = "Senior AI Engineer"
    current_level: str = "Mid-Level Engineer"
    learning_goals: str = "Master distributed training, causal inference, and production LLM systems."
    created_at: str = ""
    updated_at: str = ""

@dataclass
class KnowledgeRecord:
    domain: str
    microskill: str
    proficiency: float  # 0.0 to 1.0
    confidence: float   # 0.0 to 1.0
    attempts: int
    successes: int
    last_assessed: str

@dataclass
class MisconceptionRecord:
    id: Optional[int]
    concept: str
    pattern_description: str
    frequency: int
    resolved: bool
    first_seen: str
    last_seen: str

@dataclass
class ProjectRecord:
    id: Optional[int]
    name: str
    tech_stack: str
    architecture_notes: str
    key_decisions: str
    lessons_learned: str
    created_at: str

@dataclass
class ResearchRecord:
    id: Optional[int]
    topic: str
    paper_or_source: str
    hypothesis: str
    key_findings: str
    critiques: str
    created_at: str

@dataclass
class DecisionRecord:
    id: Optional[int]
    context: str
    options_considered: str
    chosen_option: str
    rationale: str
    outcome: str
    created_at: str

@dataclass
class ExperimentRecord:
    id: Optional[int]
    name: str
    hypothesis: str
    baseline: str
    variables: str
    metrics: str
    result: str
    conclusion: str
    created_at: str

@dataclass
class FeedbackRecord:
    id: Optional[int]
    context: str
    user_feedback: str
    system_target: str  # e.g., "prompt", "skill", "routing"
    status: str         # "logged", "reviewed", "applied"
    created_at: str

@dataclass
class ComponentVersionRecord:
    id: Optional[int]
    component_type: str  # "system_prompt", "skill", "rubric"
    component_name: str
    version: str
    content_hash: str
    changelog: str
    created_at: str

@dataclass
class ScaffoldingRecord:
    id: Optional[int]
    timestamp: str
    query: str
    scaffold_level: int
    explicit_override: bool

class MemoryStore:
    def __init__(self, db_path: Path = DB_PATH, mutation_allowed: bool = True):
        self.db_path = Path(db_path)
        self.mutation_allowed = mutation_allowed
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        ensure_directories(self.db_path.parent)
        self._init_db()

    def set_mutation_allowed(self, allowed: bool) -> None:
        """Dynamically enable or disable writes to the mentor memory database."""
        self.mutation_allowed = bool(allowed)

    def is_mutation_allowed(self) -> bool:
        """Returns True if memory modifications are currently permitted."""
        return self.mutation_allowed

    @contextmanager
    def _get_conn(self, for_write: bool = False) -> Generator[sqlite3.Connection, None, None]:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            if for_write and not self.mutation_allowed:
                conn.rollback()
            else:
                conn.commit()
        finally:
            conn.close()

    def _init_db(self) -> None:
        with self._get_conn() as conn:
            cur = conn.cursor()
            # 1. User Profile
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_profile (
                    user_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    target_role TEXT,
                    current_level TEXT,
                    learning_goals TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            """)
            # 2. Knowledge State
            cur.execute("""
                CREATE TABLE IF NOT EXISTS knowledge_state (
                    domain TEXT NOT NULL,
                    microskill TEXT NOT NULL,
                    proficiency REAL NOT NULL,
                    confidence REAL NOT NULL,
                    attempts INTEGER NOT NULL,
                    successes INTEGER NOT NULL,
                    last_assessed TEXT,
                    PRIMARY KEY (domain, microskill)
                )
            """)
            # 3. Misconception / Error Memory
            cur.execute("""
                CREATE TABLE IF NOT EXISTS misconception_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    concept TEXT NOT NULL,
                    pattern_description TEXT NOT NULL,
                    frequency INTEGER DEFAULT 1,
                    resolved BOOLEAN DEFAULT 0,
                    first_seen TEXT,
                    last_seen TEXT
                )
            """)
            # 4. Project Memory
            cur.execute("""
                CREATE TABLE IF NOT EXISTS project_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    tech_stack TEXT,
                    architecture_notes TEXT,
                    key_decisions TEXT,
                    lessons_learned TEXT,
                    created_at TEXT
                )
            """)
            # 5. Research Memory
            cur.execute("""
                CREATE TABLE IF NOT EXISTS research_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    topic TEXT NOT NULL,
                    paper_or_source TEXT,
                    hypothesis TEXT,
                    key_findings TEXT,
                    critiques TEXT,
                    created_at TEXT
                )
            """)
            # 6. Decision Memory
            cur.execute("""
                CREATE TABLE IF NOT EXISTS decision_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    context TEXT NOT NULL,
                    options_considered TEXT,
                    chosen_option TEXT,
                    rationale TEXT,
                    outcome TEXT,
                    created_at TEXT
                )
            """)
            # 7. Experiment Memory
            cur.execute("""
                CREATE TABLE IF NOT EXISTS experiment_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    hypothesis TEXT,
                    baseline TEXT,
                    variables TEXT,
                    metrics TEXT,
                    result TEXT,
                    conclusion TEXT,
                    created_at TEXT
                )
            """)
            # 8. Technical Preferences
            cur.execute("""
                CREATE TABLE IF NOT EXISTS technical_preferences (
                    category TEXT NOT NULL,
                    preference_key TEXT NOT NULL,
                    preference_value TEXT NOT NULL,
                    notes TEXT,
                    updated_at TEXT,
                    PRIMARY KEY (category, preference_key)
                )
            """)
            # 9. Scaffolding interaction history for anti-dependency tracking
            cur.execute("""
                CREATE TABLE IF NOT EXISTS scaffolding_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    query TEXT,
                    scaffold_level INTEGER,
                    explicit_override BOOLEAN
                )
            """)
            # 10. Feedback Log for Phase 7 Self-Improvement
            cur.execute("""
                CREATE TABLE IF NOT EXISTS feedback_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    context TEXT NOT NULL,
                    user_feedback TEXT NOT NULL,
                    system_target TEXT NOT NULL,
                    status TEXT DEFAULT 'logged',
                    created_at TEXT
                )
            """)
            # 11. Component Versioning for Phase 7
            cur.execute("""
                CREATE TABLE IF NOT EXISTS component_versions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    component_type TEXT NOT NULL,
                    component_name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    content_hash TEXT NOT NULL,
                    changelog TEXT,
                    created_at TEXT
                )
            """)
            conn.commit()

    # --- Profile Methods ---
    def get_or_create_profile(self, user_id: str = "default_user", name: str = "Senior AI Engineer Learner") -> UserProfile:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM user_profile WHERE user_id = ?", (user_id,))
            row = cur.fetchone()
            if row:
                return UserProfile(**dict(row))
            t = now_iso()
            profile = UserProfile(user_id=user_id, name=name, created_at=t, updated_at=t)
            if not self.mutation_allowed:
                return profile
            cur.execute("""
                INSERT INTO user_profile (user_id, name, target_role, current_level, learning_goals, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (profile.user_id, profile.name, profile.target_role, profile.current_level, profile.learning_goals, profile.created_at, profile.updated_at))
            conn.commit()
            return profile

    def update_profile(self, profile: UserProfile) -> None:
        if not self.mutation_allowed:
            return
        profile.updated_at = now_iso()
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE user_profile
                SET name=?, target_role=?, current_level=?, learning_goals=?, updated_at=?
                WHERE user_id=?
            """, (profile.name, profile.target_role, profile.current_level, profile.learning_goals, profile.updated_at, profile.user_id))
            conn.commit()

    # --- Knowledge State Methods ---
    def get_knowledge_state(self, domain: Optional[str] = None) -> List[KnowledgeRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            if domain:
                cur.execute("SELECT * FROM knowledge_state WHERE domain = ?", (domain,))
            else:
                cur.execute("SELECT * FROM knowledge_state ORDER BY domain, microskill")
            return [KnowledgeRecord(**dict(row)) for row in cur.fetchall()]

    def record_knowledge_assessment(self, domain: str, microskill: str, success: bool, delta_weight: float = 0.15) -> KnowledgeRecord:
        t = now_iso()
        if not self.mutation_allowed:
            existing = [r for r in self.get_knowledge_state(domain) if r.microskill == microskill]
            if existing:
                return existing[0]
            return KnowledgeRecord(domain, microskill, 0.0, 0.0, 0, 0, t)

        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM knowledge_state WHERE domain = ? AND microskill = ?", (domain, microskill))
            row = cur.fetchone()
            if row:
                rec = KnowledgeRecord(**dict(row))
                new_attempts = rec.attempts + 1
                new_successes = rec.successes + (1 if success else 0)
                # Exponential moving average update
                target_score = 1.0 if success else 0.0
                new_prof = (1 - delta_weight) * rec.proficiency + delta_weight * target_score
                new_conf = min(1.0, rec.confidence + 0.1)
                cur.execute("""
                    UPDATE knowledge_state
                    SET proficiency=?, confidence=?, attempts=?, successes=?, last_assessed=?
                    WHERE domain=? AND microskill=?
                """, (round(new_prof, 3), round(new_conf, 3), new_attempts, new_successes, t, domain, microskill))
                conn.commit()
                return KnowledgeRecord(domain, microskill, round(new_prof, 3), round(new_conf, 3), new_attempts, new_successes, t)
            else:
                initial_prof = 0.8 if success else 0.3
                initial_conf = 0.4
                cur.execute("""
                    INSERT INTO knowledge_state (domain, microskill, proficiency, confidence, attempts, successes, last_assessed)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (domain, microskill, initial_prof, initial_conf, 1, 1 if success else 0, t))
                conn.commit()
                return KnowledgeRecord(domain, microskill, initial_prof, initial_conf, 1, 1 if success else 0, t)

    # --- Misconception Methods ---
    def record_misconception(self, concept: str, pattern: str) -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, frequency FROM misconception_memory WHERE concept=? AND pattern_description=?", (concept, pattern))
            row = cur.fetchone()
            t = now_iso()
            if row:
                cur.execute("""
                    UPDATE misconception_memory
                    SET frequency = frequency + 1, resolved = 0, last_seen = ?
                    WHERE id = ?
                """, (t, row["id"]))
            else:
                cur.execute("""
                    INSERT INTO misconception_memory (concept, pattern_description, frequency, resolved, first_seen, last_seen)
                    VALUES (?, ?, 1, 0, ?, ?)
                """, (concept, pattern, t, t))
            conn.commit()

    def get_unresolved_misconceptions(self) -> List[MisconceptionRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM misconception_memory WHERE resolved = 0 ORDER BY frequency DESC")
            return [MisconceptionRecord(**dict(row)) for row in cur.fetchall()]

    def resolve_misconception(self, misconception_id: int) -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE misconception_memory SET resolved = 1 WHERE id = ?", (misconception_id,))
            conn.commit()

    # --- Decision & Experiment Methods ---
    def log_decision(self, context: str, options: List[str], chosen: str, rationale: str, outcome: str = "Pending evaluation") -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO decision_memory (context, options_considered, chosen_option, rationale, outcome, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (context, json.dumps(options), chosen, rationale, outcome, now_iso()))
            conn.commit()

    def get_recent_decisions(self, limit: int = 10) -> List[DecisionRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM decision_memory ORDER BY id DESC LIMIT ?", (limit,))
            return [DecisionRecord(**dict(row)) for row in cur.fetchall()]

    def log_experiment(self, name: str, hypothesis: str, baseline: str, variables: str, metrics: str, result: str = "Ongoing", conclusion: str = "") -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO experiment_memory (name, hypothesis, baseline, variables, metrics, result, conclusion, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, hypothesis, baseline, variables, metrics, result, conclusion, now_iso()))
            conn.commit()

    def get_experiments(self, limit: int = 10) -> List[ExperimentRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM experiment_memory ORDER BY id DESC LIMIT ?", (limit,))
            return [ExperimentRecord(**dict(row)) for row in cur.fetchall()]

    # --- Scaffolding & Anti-Dependency Log ---
    def log_scaffolding_interaction(self, query: str, level: int, explicit_override: bool) -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO scaffolding_log (timestamp, query, scaffold_level, explicit_override)
                VALUES (?, ?, ?, ?)
            """, (now_iso(), query, level, 1 if explicit_override else 0))
            conn.commit()

    def get_anti_dependency_ratio(self, last_n: int = 20) -> float:
        """Returns the ratio of spoon-fed responses (L0-L2) vs active Socratic interactions (L3-L7)."""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT scaffold_level FROM scaffolding_log ORDER BY id DESC LIMIT ?", (last_n,))
            rows = cur.fetchall()
            if not rows:
                return 0.0
            direct_count = sum(1 for r in rows if r["scaffold_level"] <= 2)
            return round(direct_count / len(rows), 2)

    def get_scaffolding_history(self, limit: int = 200) -> List[ScaffoldingRecord]:
        """Retrieves recent scaffolding interactions in chronological order."""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM scaffolding_log ORDER BY id ASC LIMIT ?", (limit,))
            return [ScaffoldingRecord(**dict(row)) for row in cur.fetchall()]

    # --- Project Memory Methods ---
    def log_project(self, name: str, tech_stack: str, architecture_notes: str, key_decisions: str, lessons_learned: str) -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO project_memory (name, tech_stack, architecture_notes, key_decisions, lessons_learned, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, tech_stack, architecture_notes, key_decisions, lessons_learned, now_iso()))
            conn.commit()

    def get_projects(self, limit: int = 10) -> List[ProjectRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM project_memory ORDER BY id DESC LIMIT ?", (limit,))
            return [ProjectRecord(**dict(row)) for row in cur.fetchall()]

    def get_projects_for_concept(self, concept_name: str) -> List[ProjectRecord]:
        """Finds projects where a specific concept was applied."""
        with self._get_conn() as conn:
            cur = conn.cursor()
            like_pat = f"%{concept_name}%"
            cur.execute("""
                SELECT * FROM project_memory
                WHERE name LIKE ? OR tech_stack LIKE ? OR architecture_notes LIKE ? OR key_decisions LIKE ?
                ORDER BY id DESC
            """, (like_pat, like_pat, like_pat, like_pat))
            return [ProjectRecord(**dict(row)) for row in cur.fetchall()]

    def get_misconceptions_for_concept(self, concept_name: str) -> List[MisconceptionRecord]:
        """Finds recorded misconceptions for a specific concept."""
        with self._get_conn() as conn:
            cur = conn.cursor()
            like_pat = f"%{concept_name}%"
            cur.execute("SELECT * FROM misconception_memory WHERE concept LIKE ? ORDER BY frequency DESC", (like_pat,))
            return [MisconceptionRecord(**dict(row)) for row in cur.fetchall()]

    # --- Phase 7 Self-Improvement: Feedback & Versioning Methods ---
    def log_feedback(self, context: str, user_feedback: str, system_target: str = "prompt") -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO feedback_log (context, user_feedback, system_target, status, created_at)
                VALUES (?, ?, ?, 'logged', ?)
            """, (context, user_feedback, system_target, now_iso()))
            conn.commit()

    def get_feedback_logs(self, status: Optional[str] = None) -> List[FeedbackRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            if status:
                cur.execute("SELECT * FROM feedback_log WHERE status = ? ORDER BY id DESC", (status,))
            else:
                cur.execute("SELECT * FROM feedback_log ORDER BY id DESC")
            return [FeedbackRecord(**dict(row)) for row in cur.fetchall()]

    def record_component_version(self, component_type: str, component_name: str, version: str, content_hash: str, changelog: str) -> None:
        if not self.mutation_allowed:
            return
        with self._get_conn(for_write=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO component_versions (component_type, component_name, version, content_hash, changelog, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (component_type, component_name, version, content_hash, changelog, now_iso()))
            conn.commit()

    def get_component_versions(self, component_name: str) -> List[ComponentVersionRecord]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM component_versions WHERE component_name = ? ORDER BY id DESC", (component_name,))
            return [ComponentVersionRecord(**dict(row)) for row in cur.fetchall()]
