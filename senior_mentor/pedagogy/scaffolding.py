"""Pedagogical Scaffolding Engine (L0 through L7).

Translates technical concepts and queries into calibrated pedagogical interventions
tailored to the user's proficiency level or explicit mode override.
"""

from dataclasses import dataclass
from typing import Optional
from .learner_model import LearnerModel, ZPDStatus
from ..knowledge.graph import KnowledgeGraph, ConceptNode

@dataclass
class ScaffoldedResponse:
    level: int
    level_name: str
    tier: str  # Direct Guidance, Socratic Scaffolding, Independent Problem-Solving
    content: str
    anti_dependency_alert: Optional[str] = None
    next_action_prompt: str = ""

class ScaffoldingEngine:
    def __init__(self, learner_model: LearnerModel, knowledge_graph: KnowledgeGraph):
        self.learner_model = learner_model
        self.graph = knowledge_graph

    def resolve_target_level(self, query: str, override_mode: Optional[str] = None, matched_concept: Optional[str] = None) -> int:
        """Determines the exact scaffolding level to apply."""
        if override_mode == "solve":
            return 0
        if override_mode == "mentor":
            return 5
        if override_mode == "hint":
            return 3
        if override_mode == "challenge":
            return 6
        if override_mode == "interview":
            return 5

        # Adaptive routing via ZPD
        if matched_concept:
            zpd = self.learner_model.assess_concept_zpd(matched_concept)
            return zpd.recommended_level

        # Default pedagogical baseline: Socratic level 3 (High-level hint)
        return 3

    def generate_scaffold(
        self,
        query: str,
        concept_name: Optional[str] = None,
        override_mode: Optional[str] = None
    ) -> ScaffoldedResponse:
        level = self.resolve_target_level(query, override_mode, concept_name)
        concept = self.graph.get_concept(concept_name) if concept_name else None
        anti_dep = self.learner_model.check_anti_dependency_warning()

        # Record this scaffolding interaction for anti-dependency tracking
        self.learner_model.store.log_scaffolding_interaction(query, level, override_mode is not None)

        if level == 0:
            return self._build_l0(query, concept, anti_dep)
        elif level == 1:
            return self._build_l1(query, concept, anti_dep)
        elif level == 2:
            return self._build_l2(query, concept, anti_dep)
        elif level == 3:
            return self._build_l3(query, concept, anti_dep)
        elif level == 4:
            return self._build_l4(query, concept, anti_dep)
        elif level == 5:
            return self._build_l5(query, concept, anti_dep)
        elif level == 6:
            return self._build_l6(query, concept, anti_dep)
        else:
            return self._build_l7(query, concept, anti_dep)

    def _build_l0(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = (
            "### [L0: Direct Solution & Implementation]\n\n"
            "Here is the complete, production-grade implementation and direct solution for your task:\n\n"
        )
        if concept:
            content += (
                f"**Domain:** {concept.domain} | **Concept:** {concept.name}\n\n"
                f"**Implementation Architecture:**\n{concept.practical_implementation_notes}\n\n"
                f"**Mathematical Formulation:**\n`{concept.first_principles_formulation}`\n"
            )
        else:
            content += f"Addressing query: *{query}*\n(See complete code structure provided by the Orchestrator).\n"

        return ScaffoldedResponse(
            level=0,
            level_name="Direct Solution",
            tier="Direct Guidance",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Review the code. Try modifying the inputs or running the test suite to verify behavior."
        )

    def _build_l1(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = (
            "### [L1: First Principles & Foundations]\n\n"
            "Before jumping to code, let us understand the underlying mechanics:\n\n"
        )
        if concept:
            content += (
                f"**Core Principle:** {concept.name}\n"
                f"**Mathematical Core:** `{concept.first_principles_formulation}`\n\n"
                f"**Why this works:** Rather than treating this as a black box, notice how the objective function "
                "or mathematical structure guarantees convergence and stability."
            )
        else:
            content += f"Analyzing principles behind: *{query}*.\n"

        return ScaffoldedResponse(
            level=1,
            level_name="First Principles",
            tier="Direct Guidance",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Can you explain in your own words how the objective function penalizes errors here?"
        )

    def _build_l2(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = "### [L2: Pitfall Catalog & Failure Modes]\n\n"
        if concept and concept.common_pitfalls:
            content += "**Senior Engineer Warning Checklist:**\n"
            for pit in concept.common_pitfalls:
                content += f"- ⚠️ **Common Trap:** {pit}\n"
        else:
            content += "- ⚠️ Watch for silent data leakage, memory retention across iterations, and unverified assumptions.\n"

        return ScaffoldedResponse(
            level=2,
            level_name="Pitfall Warning",
            tier="Direct Guidance",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="How would you design an automated test to catch this specific pitfall?"
        )

    def _build_l3(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        hint = f"Look at the mathematical formulation: `{concept.first_principles_formulation}`" if concept else "Think about how data flows between training and test boundaries."
        content = (
            "### [L3: High-Level Socratic Hint]\n\n"
            "💡 **Mentor's Clue:** Rather than giving you the exact line of code, consider the invariant:\n"
            f"> {hint}\n\n"
            "What assumption about your data or model structure needs to hold true here?"
        )
        return ScaffoldedResponse(
            level=3,
            level_name="High-Level Hint",
            tier="Socratic Scaffolding",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Give it a try or type `/hint` for an architectural clue."
        )

    def _build_l4(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = (
            "### [L4: Architectural Clue & Interface Scaffold]\n\n"
            "Here is the high-level interface contract. Your goal is to implement the internal logic:\n\n"
            "```python\n"
            "def solve_engineering_task(inputs: Tensor) -> Result:\n"
            "    # Step 1: Validate input bounds & sanitize\n"
            "    # Step 2: Compute core transformation (apply first-principles formulation)\n"
            "    # Step 3: Enforce dimensional invariance\n"
            "    ...\n"
            "```\n"
        )
        return ScaffoldedResponse(
            level=4,
            level_name="Architectural Clue",
            tier="Socratic Scaffolding",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Fill in Step 2. What vectorized operation would you use?"
        )

    def _build_l5(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = (
            "### [L5: Guided Socratic Dialogue]\n\n"
            "Let's reason through this step-by-step like a Senior Staff Engineer:\n\n"
            "1. If you run this transformation on the entire dataset at once, what hidden information does the validation set receive?\n"
            "2. How does that change the statistical distribution of your out-of-fold metrics compared to actual production inference?\n"
        )
        return ScaffoldedResponse(
            level=5,
            level_name="Guided Dialogue",
            tier="Socratic Scaffolding",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Post your answer to question 1 to proceed to the next step."
        )

    def _build_l6(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = (
            "### [L6: Isomorphic Transfer Challenge]\n\n"
            "🎯 **Transfer Exercise:** You have mastered the base concept. Now let's test transfer to a realistic system:\n\n"
            "Suppose instead of a single tabular dataset, you are building an online fraud detection model with 10M daily events "
            "where fraudulent patterns evolve every 48 hours. How do you structure your cross-validation and feature store window "
            "to guarantee zero temporal leakage without degrading training throughput?"
        )
        return ScaffoldedResponse(
            level=6,
            level_name="Transfer Challenge",
            tier="Independent Problem-Solving",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Draft your architecture proposal. The Council will evaluate your design."
        )

    def _build_l7(self, query: str, concept: Optional[ConceptNode], anti_dep: Optional[str]) -> ScaffoldedResponse:
        content = (
            "### [L7: Adversarial Self-Critique Challenge]\n\n"
            "🛡️ **Red Team Attack:** Assume your proposed design is deployed in production tomorrow.\n\n"
            "1. Where will it break first under a 10x traffic spike?\n"
            "2. How could an adversarial actor craft an input to bypass your statistical assumption?\n"
            "3. What silent failure mode would your existing metrics completely miss?"
        )
        return ScaffoldedResponse(
            level=7,
            level_name="Adversarial Critique",
            tier="Independent Problem-Solving",
            content=content,
            anti_dependency_alert=anti_dep,
            next_action_prompt="Defend your architecture against these three attack vectors."
        )
