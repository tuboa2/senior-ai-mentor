"""Longitudinal Competency Tracker.

Tracks engineering progression over time, monitors knowledge state evolution,
and produces career milestone evaluations.
"""

from typing import Dict, List, Optional
from ..memory.store import MemoryStore
from .rubric import CompetencyRubric, EvaluationReport

class CompetencyTracker:
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
        self.rubric = CompetencyRubric()

    def generate_current_assessment(self) -> EvaluationReport:
        """Derives current competency ratings directly from recorded knowledge state and decisions."""
        records = self.store.get_knowledge_state()
        decisions = self.store.get_recent_decisions(limit=20)
        misconceptions = self.store.get_unresolved_misconceptions()

        if not records:
            # Baseline novice state
            ratings = {
                "Technical Correctness & Mathematical Soundness": 5.0,
                "Architectural Design & Scalability": 5.0,
                "Statistical Validity & Leakage Resistance": 5.0,
                "Defensive Programming & Security": 5.0,
                "Trade-Off Communication & Justification": 5.0
            }
        else:
            avg_prof = sum(r.proficiency for r in records) / len(records)
            base_score = avg_prof * 10.0

            # Penalize for unresolved misconceptions
            misconception_penalty = min(2.0, len(misconceptions) * 0.4)
            # Reward for documented decision rationales
            decision_bonus = min(1.5, len(decisions) * 0.2)

            stats_recs = [r.proficiency for r in records if "stat" in r.domain.lower() or "leakage" in r.microskill.lower()]
            arch_recs = [r.proficiency for r in records if "architect" in r.domain.lower() or "pipeline" in r.microskill.lower()]

            stats_score = (sum(stats_recs) / len(stats_recs) * 10.0) if stats_recs else base_score
            arch_score = (sum(arch_recs) / len(arch_recs) * 10.0) if arch_recs else base_score

            ratings = {
                "Technical Correctness & Mathematical Soundness": round(max(1.0, min(10.0, base_score - misconception_penalty)), 1),
                "Architectural Design & Scalability": round(max(1.0, min(10.0, arch_score + decision_bonus)), 1),
                "Statistical Validity & Leakage Resistance": round(max(1.0, min(10.0, stats_score - (misconception_penalty * 0.5))), 1),
                "Defensive Programming & Security": round(max(1.0, min(10.0, base_score)), 1),
                "Trade-Off Communication & Justification": round(max(1.0, min(10.0, 5.0 + decision_bonus)), 1)
            }

        report = self.rubric.evaluate(ratings)
        # Update user profile with evaluated level
        profile = self.store.get_or_create_profile()
        if profile.current_level != report.competency_tier:
            profile.current_level = report.competency_tier
            self.store.update_profile(profile)

        return report
