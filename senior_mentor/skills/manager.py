"""Skill Lifecycle and Tier Management.

Coordinates:
- Tier 0: Trusted Core (hand-curated, local)
- Tier 1: Curated External (audited, approved)
- Tier 2: Dynamic Discovery (automated search, audit-on-demand)
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from ..config import MentorConfig, SKILLS_TIER0_DIR, GLOBAL_SKILLS_DIR
from .auditor import SkillSecurityAuditor, SkillAuditReport

@dataclass
class SkillInfo:
    name: str
    tier: str  # "Tier 0 (Trusted Core)", "Tier 1 (Curated External)", "Tier 2 (Dynamic)"
    path: Path
    description: str
    is_audited: bool
    risk_level: str

class SkillManager:
    def __init__(self, config: Optional[MentorConfig] = None):
        self.config = config or MentorConfig()
        self.auditor = SkillSecurityAuditor()

    def list_tier0_skills(self) -> List[SkillInfo]:
        """Lists all hand-curated Tier 0 skills in .agents/skills/."""
        skills = []
        if not self.config.skills_tier0_dir.exists():
            return []
        for d in self.config.skills_tier0_dir.iterdir():
            if d.is_dir():
                skill_md = d / "SKILL.md"
                desc = self._extract_description(skill_md) if skill_md.exists() else "No description"
                skills.append(SkillInfo(
                    name=d.name,
                    tier="Tier 0 (Trusted Core)",
                    path=d,
                    description=desc,
                    is_audited=True,
                    risk_level="TRUSTED"
                ))
        return skills

    def list_curated_external_skills(self, limit: int = 20) -> List[SkillInfo]:
        """Lists candidate external skills from the global pool."""
        skills = []
        if not self.config.global_skills_dir.exists():
            return []
        count = 0
        for d in sorted(self.config.global_skills_dir.iterdir()):
            if d.is_dir() and count < limit:
                skill_md = d / "SKILL.md"
                if skill_md.exists():
                    desc = self._extract_description(skill_md)
                    skills.append(SkillInfo(
                        name=d.name,
                        tier="Tier 1 (Curated External Pool)",
                        path=d,
                        description=desc,
                        is_audited=False,
                        risk_level="UNAUDITED"
                    ))
                    count += 1
        return skills

    def audit_skill(self, skill_name_or_path: str) -> SkillAuditReport:
        p = Path(skill_name_or_path)
        if not p.is_dir():
            # Check tier 0
            tier0_cand = self.config.skills_tier0_dir / skill_name_or_path
            if tier0_cand.is_dir():
                p = tier0_cand
            else:
                # Check global
                global_cand = self.config.global_skills_dir / skill_name_or_path
                if global_cand.is_dir():
                    p = global_cand
        return self.auditor.audit_skill_directory(p)

    def discover_skills_for_task(self, task_query: str, max_candidates: int = 5) -> List[Dict]:
        """Tier 2 Dynamic Discovery: Searches external skills, analyzes capability match, and executes security audit."""
        keywords = [w.lower() for w in task_query.split() if len(w) > 3]
        matches = []

        # Check global repository if available
        if self.config.global_skills_dir.exists():
            for d in self.config.global_skills_dir.iterdir():
                if not d.is_dir():
                    continue
                name_match = any(k in d.name.lower() for k in keywords)
                skill_md = d / "SKILL.md"
                desc = self._extract_description(skill_md) if skill_md.exists() else ""
                desc_match = any(k in desc.lower() for k in keywords)

                if name_match or desc_match:
                    audit_rep = self.auditor.audit_skill_directory(d)
                    matches.append({
                        "name": d.name,
                        "tier": "Tier 2 (Dynamic Discovery)",
                        "path": str(d),
                        "description": desc,
                        "is_safe": audit_rep.is_safe,
                        "risk_level": audit_rep.risk_level,
                        "audit_findings_count": len(audit_rep.findings)
                    })
                    if len(matches) >= max_candidates:
                        break

        return matches

    def _extract_description(self, skill_md: Path) -> str:
        try:
            content = skill_md.read_text(encoding="utf-8", errors="replace")
            lines = content.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("description:"):
                    desc = line.split(":", 1)[1].strip()
                    if desc in (">-", ">", "|"):
                        # Multi-line description
                        desc = " ".join(l.strip() for l in lines[i+1:i+4] if l.startswith("  "))
                    return desc.strip("\"'")
        except Exception as e:
            _ = e
        return "Standard Agent Skill"
