"""Autonomous Self-Improvement and Feedback Refinement Engine (Phase 7).

Implements:
1. Feedback capture loop for user corrections and failed problem attempts.
2. Refinement analysis identifying recurring misconceptions and routing failures.
3. Versioning and staged review for core components (prompts, skills, rubrics).
"""

from dataclasses import dataclass
import hashlib
from typing import Dict, List, Optional
from ..memory.store import MemoryStore, FeedbackRecord, ComponentVersionRecord
from ..pedagogy.scope_guard import ScopeGuard

@dataclass
class RefinementProposal:
    target_component: str
    component_type: str
    current_version: str
    proposed_version: str
    rationale: str
    suggested_changes: str
    evidence_count: int

class AutonomousSelfImprovementEngine:
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
        self.scope_guard = ScopeGuard()

    def capture_correction(self, context: str, user_correction: str, target: str = "prompt") -> bool:
        """Captures user corrections when model output was flawed or uncalibrated.
        
        Rejects out-of-scope feedback to prevent non-engineering corruption of the feedback log.
        """
        context_check = self.scope_guard.check_scope(context)
        correction_check = self.scope_guard.check_scope(user_correction)
        if not context_check.is_in_scope and not correction_check.is_in_scope:
            return False

        self.store.log_feedback(context=context, user_feedback=user_correction, system_target=target)
        return True

    def analyze_improvement_opportunities(self) -> List[RefinementProposal]:
        """Analyzes feedback logs and misconception patterns to generate concrete refinement proposals."""
        feedbacks = self.store.get_feedback_logs(status="logged")
        misconceptions = self.store.get_unresolved_misconceptions()
        proposals: List[RefinementProposal] = []

        # 1. Analyze prompt feedbacks
        prompt_fb = [f for f in feedbacks if f.system_target == "prompt"]
        if len(prompt_fb) >= 2:
            reasons = "; ".join(f.user_feedback for f in prompt_fb[:3])
            proposals.append(RefinementProposal(
                target_component="Orchestrator System Prompt",
                component_type="system_prompt",
                current_version="1.0.0",
                proposed_version="1.0.1",
                rationale=f"Accumulated {len(prompt_fb)} user corrections on response tone or accuracy.",
                suggested_changes=f"Incorporate defensive clauses addressing: {reasons}",
                evidence_count=len(prompt_fb)
            ))

        # 2. Analyze recurring misconceptions for skill refinements
        for misc in misconceptions:
            if misc.frequency >= 2:
                proposals.append(RefinementProposal(
                    target_component=f"Skill: {misc.concept}",
                    component_type="skill",
                    current_version="1.0.0",
                    proposed_version="1.1.0",
                    rationale=f"Learner encountered recurring trap {misc.frequency}x: '{misc.pattern_description}'",
                    suggested_changes=f"Add explicit L2 Pitfall warning and unit test invariant for '{misc.pattern_description}'",
                    evidence_count=misc.frequency
                ))

        return proposals

    def stage_component_version(
        self,
        component_type: str,
        component_name: str,
        version: str,
        content: str,
        changelog: str
    ) -> ComponentVersionRecord:
        """Stages and records a new versioned snapshot of a system component."""
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]
        self.store.record_component_version(
            component_type=component_type,
            component_name=component_name,
            version=version,
            content_hash=content_hash,
            changelog=changelog
        )
        versions = self.store.get_component_versions(component_name)
        return versions[0]
