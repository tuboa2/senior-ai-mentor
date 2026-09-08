"""Evaluation Rubric for Senior Engineering Competency.

Implements multi-dimensional rubric evaluation based on Microsoft's LLM-Rubric standard:
1. Technical Correctness & Mathematical Soundness (30%)
2. Architectural Design & Scalability (20%)
3. Statistical Validity & Leakage Resistance (20%)
4. Defensive Programming & Security (15%)
5. Clear Trade-Off Communication & Justification (15%)
"""

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class DimensionScore:
    name: str
    weight: float
    score: float  # 0.0 to 10.0
    feedback: str

@dataclass
class EvaluationReport:
    overall_score: float  # 0.0 to 10.0
    competency_tier: str  # "Junior Engineer", "Mid-Level Engineer", "Senior Engineer", "Staff Engineer", "Principal Engineer"
    dimension_scores: List[DimensionScore]
    strengths: List[str]
    areas_for_growth: List[str]
    recommended_learning_plan: List[str]

class CompetencyRubric:
    DIMENSIONS = [
        ("Technical Correctness & Mathematical Soundness", 0.30),
        ("Architectural Design & Scalability", 0.20),
        ("Statistical Validity & Leakage Resistance", 0.20),
        ("Defensive Programming & Security", 0.15),
        ("Trade-Off Communication & Justification", 0.15)
    ]

    def evaluate(self, dimension_ratings: Dict[str, float], custom_notes: Dict[str, str] = None) -> EvaluationReport:
        notes = custom_notes or {}
        dim_scores = []
        weighted_sum = 0.0

        for dim_name, weight in self.DIMENSIONS:
            score = max(0.0, min(10.0, dimension_ratings.get(dim_name, 6.0)))
            weighted_sum += score * weight
            feedback = notes.get(dim_name, f"Demonstrated score of {score:.1f}/10 on {dim_name}.")
            dim_scores.append(DimensionScore(name=dim_name, weight=weight, score=score, feedback=feedback))

        # Map overall score to career competency tier
        if weighted_sum >= 9.0:
            tier = "Principal Engineer"
        elif weighted_sum >= 8.0:
            tier = "Staff Engineer"
        elif weighted_sum >= 6.5:
            tier = "Senior Engineer"
        elif weighted_sum >= 4.5:
            tier = "Mid-Level Engineer"
        else:
            tier = "Junior Engineer"

        strengths = [d.name for d in dim_scores if d.score >= 7.5]
        weaknesses = [d.name for d in dim_scores if d.score < 6.5]

        learning_plan = []
        if "Statistical Validity & Leakage Resistance" in weaknesses:
            learning_plan.append("Deep dive into out-of-fold temporal cross-validation and multiple testing corrections.")
        if "Architectural Design & Scalability" in weaknesses:
            learning_plan.append("Study distributed ML systems, latency budgets, and asynchronous pipeline design.")
        if "Defensive Programming & Security" in weaknesses:
            learning_plan.append("Practice input sanitization, prompt injection defense, and automated invariant tests.")
        if not learning_plan:
            learning_plan.append("Advance to system design reviews and novel research paper reproductions.")

        return EvaluationReport(
            overall_score=round(weighted_sum, 2),
            competency_tier=tier,
            dimension_scores=dim_scores,
            strengths=strengths or ["Foundational coding competence"],
            areas_for_growth=weaknesses or ["Continue honing Principal-level trade-off synthesis"],
            recommended_learning_plan=learning_plan
        )
