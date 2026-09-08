"""Learner Model and Zone of Proximal Development (ZPD) Engine.

Maintains proficiency state, tracks anti-dependency ratios, and determines
optimal pedagogical assistance levels based on cognitive readiness.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from ..memory.store import MemoryStore, KnowledgeRecord
from ..knowledge.graph import KnowledgeGraph, ConceptNode

@dataclass
class ZPDStatus:
    concept_name: str
    proficiency: float
    confidence: float
    zone: str  # "Frustration" (<0.3), "Proximal" (0.3-0.75), "Mastery" (>0.75)
    recommended_level: int
    unmet_prerequisites: List[str]

class LearnerModel:
    def __init__(self, memory_store: MemoryStore, knowledge_graph: KnowledgeGraph):
        self.store = memory_store
        self.graph = knowledge_graph

    def get_proficiency_map(self) -> Dict[str, float]:
        records = self.store.get_knowledge_state()
        return {r.microskill.lower(): r.proficiency for r in records}

    def assess_concept_zpd(self, concept_name: str) -> ZPDStatus:
        """Determines whether a concept is in the user's Zone of Proximal Development."""
        node = self.graph.get_concept(concept_name)
        prof_map = self.get_proficiency_map()
        
        # Concept proficiency
        prof = prof_map.get(concept_name.lower(), 0.2)
        
        # Check prerequisites
        unmet = []
        if node:
            for prereq in node.prerequisites:
                p_prof = prof_map.get(prereq.lower(), 0.0)
                if p_prof < 0.5:
                    unmet.append(f"{prereq} (proficiency: {p_prof:.2f})")

        # Determine Zone
        if unmet:
            zone = "Frustration (Prerequisites Unmet)"
            rec_level = 0  # Needs direct instruction (L0/L1) on missing prereqs
        elif prof < 0.3:
            zone = "Novice / Direct Guidance"
            rec_level = 1  # L1: First principles
        elif 0.3 <= prof <= 0.75:
            zone = "Proximal (ZPD: Prime for Socratic Scaffolding)"
            rec_level = 4  # L3-L5 Socratic hints and dialogue
        else:
            zone = "Mastery (Ready for Independent Challenge)"
            rec_level = 6  # L6-L7 Transfer challenges and adversarial critique

        confidence = 0.5
        records = self.store.get_knowledge_state()
        for r in records:
            if r.microskill.lower() == concept_name.lower():
                confidence = r.confidence
                break

        return ZPDStatus(
            concept_name=concept_name,
            proficiency=prof,
            confidence=confidence,
            zone=zone,
            recommended_level=rec_level,
            unmet_prerequisites=unmet
        )

    def record_attempt(self, domain: str, microskill: str, success: bool) -> KnowledgeRecord:
        return self.store.record_knowledge_assessment(domain, microskill, success)

    def check_anti_dependency_warning(self) -> Optional[str]:
        """Checks if the user has become overly reliant on direct answers."""
        ratio = self.store.get_anti_dependency_ratio(last_n=15)
        if ratio > 0.65:
            return (
                f"⚠️ ANTI-DEPENDENCY ALERT: Direct-solve ratio is {ratio:.0%}. "
                "As your Senior Mentor, I strongly encourage switching to Socratic mode (/mentor or /hint) "
                "to ensure you develop independent problem-solving skills."
            )
        return None
