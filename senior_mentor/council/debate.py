"""Expert Council Multi-Agent Debate Engine & Disagreement Protocol.

Simulates collaborative engineering deliberation, identifies genuine disagreements,
enforces the Experiment-First principle, and structures unresolved dissent
without manufacturing artificial consensus.
"""

import re
from dataclasses import dataclass
from typing import Dict, List, Optional
from .experts import ExpertPersona, PERMANENT_EXPERTS

@dataclass
class ExpertPerspective:
    expert: ExpertPersona
    stance: str
    rationale: str
    key_trade_off: str
    suggested_check: str

@dataclass
class ControlledExperimentDesign:
    title: str
    hypothesis: str
    baseline: str
    independent_variables: List[str]
    evaluation_metrics: List[str]
    expected_outcomes: str

@dataclass
class DebateSynthesis:
    query: str
    participating_experts: List[str]
    has_unresolved_disagreement: bool
    positions: List[Dict[str, str]]
    conflict_statement: Optional[str]
    uncertainty_statement: Optional[str]
    pathways_forward: List[str]
    experiment_design: Optional[ControlledExperimentDesign]
    escalation_question: str
    consensus_summary: Optional[str]

class DebateEngine:
    def __init__(self):
        self.experts = PERMANENT_EXPERTS
        self.tradeoff_pattern = re.compile(
            r"\b(vs|or|trade-off|tradeoff|choice|which|compare|better|best|alternative)\b",
            re.IGNORECASE
        )

    def select_relevant_experts(self, query: str) -> List[ExpertPersona]:
        """Selects the 3 to 5 most relevant experts for a given technical query."""
        q = query.lower()
        selected: List[str] = []

        if any(w in q for w in ["stat", "p-value", "significan", "leakage", "split", "cross-val", "hypothesis"]):
            selected.extend(["statistician", "data_scientist"])
        if any(w in q for w in ["model", "xgboost", "neural", "train", "loss", "architecture", "pipeline", "cluster", "system"]):
            selected.extend(["ml_architect", "ml_research_scientist"])
        if any(w in q for w in ["math", "linear algebra", "eigen", "matrix", "calculus", "gradient", "svd"]):
            selected.append("math_for_ml_expert")
        if any(w in q for w in ["perf", "memory", "cuda", "gpu", "latency", "vectoriz", "bottleneck", "profile", "h100", "a100", "vram", "ttft", "throughput", "cache", "quantiz", "int4", "int8", "fp16", "kernel"]):
            selected.append("performance_engineer")
        if any(w in q for w in ["llm", "rag", "agent", "prompt", "mcp", "transformer", "attention", "flashattention", "context", "token"]):
            selected.append("ai_llm_engineer")
        if any(w in q for w in ["data", "etl", "spark", "duckdb", "stream", "table"]):
            selected.append("data_engineer")
        if any(w in q for w in ["deploy", "ci/cd", "drift", "mlops", "serving", "kubernetes"]):
            selected.append("mlops_engineer")
        if any(w in q for w in ["code", "refactor", "bug", "clean", "type"]):
            selected.append("code_reviewer")

        # Always ensure Red Team is represented to probe edge cases
        if "red_team_adversary" not in selected:
            selected.append("red_team_adversary")

        # Fallback default council
        if len(selected) < 3:
            selected.extend(["ml_architect", "statistician", "performance_engineer"])

        # Deduplicate preserving order
        seen = set()
        result = []
        for role in selected:
            if role not in seen and role in self.experts:
                seen.add(role)
                result.append(self.experts[role])
        return result[:5]

    def deliberate(self, query: str, force_disagreement: bool = False) -> DebateSynthesis:
        """Conducts a deliberation among selected experts and synthesizes findings."""
        experts = self.select_relevant_experts(query)
        q = query.lower()

        # Assess if query inherently contains competing trade-offs
        is_tradeoff_query = force_disagreement or bool(self.tradeoff_pattern.search(q))

        positions = []
        for exp in experts:
            if exp.role_id == "statistician":
                positions.append({
                    "role": exp.name,
                    "title": exp.title,
                    "position": f"Rigorous statistical validation and assumption verification on '{query}'.",
                    "rationale": "Empirical metrics can be misleading without testing for leakage, i.i.d. violations, and multiple hypothesis corrections."
                })
            elif exp.role_id == "ml_architect":
                positions.append({
                    "role": exp.name,
                    "title": exp.title,
                    "position": f"End-to-end system scalability, latency budget, and operational simplicity for '{query}'.",
                    "rationale": "The most mathematically elegant model is worthless if it introduces insurmountable serving latency or retraining fragility."
                })
            elif exp.role_id == "performance_engineer":
                positions.append({
                    "role": exp.name,
                    "title": exp.title,
                    "position": f"Vectorization, memory bandwidth, and GPU kernel throughput for '{query}'.",
                    "rationale": "Algorithmic complexity must match modern hardware topology (SIMD/tensor cores) to remain cost-effective."
                })
            elif exp.role_id == "red_team_adversary":
                positions.append({
                    "role": exp.name,
                    "title": exp.title,
                    "position": f"Active vulnerability probing, edge cases, and distribution shifts for '{query}'.",
                    "rationale": "Models consistently break on unseen edge cases, corrupt inputs, or adversarial perturbations."
                })
            else:
                positions.append({
                    "role": exp.name,
                    "title": exp.title,
                    "position": f"Specialized focus on {exp.focus_domain} regarding '{query}'.",
                    "rationale": f"Ensures standards of {', '.join(exp.core_values)} are preserved."
                })

        if is_tradeoff_query:
            conflict = (
                "The core conflict centers on the tension between rigorous theoretical validity / sample efficiency "
                "versus real-world operational scalability, inference latency, and hardware constraints."
            )
            uncertainty = (
                "Current theoretical analysis cannot predict whether the incremental accuracy gains justify the "
                "additional operational complexity without empirical data on live traffic distributions."
            )
            pathways = [
                "Benchmark inference latency and memory footprint under realistic batch sizes.",
                "Execute an out-of-time (OOT) validation split to test generalization under temporal distribution shift.",
                "Run a statistical equivalence test (TOST) or Welch's t-test with bootstrap confidence intervals."
            ]
            experiment = ControlledExperimentDesign(
                title="A/B Benchmark & Statistical Validation Experiment",
                hypothesis="The proposed architecture provides a statistically significant metric improvement without exceeding the 50ms latency ceiling.",
                baseline="Current production baseline with standard feature transformations.",
                independent_variables=["Model architecture variant", "Input batch size [1, 8, 32]", "Quantization level (FP16 vs INT8)"],
                evaluation_metrics=["ROC-AUC / Log-Loss with 95% bootstrap CI", "p99 Inference Latency (ms)", "Peak GPU Memory (VRAM)"],
                expected_outcomes="Validate whether delta AUC > +0.015 at p < 0.01 while p99 latency <= 45ms."
            )
            escalation = (
                "Based on this conflict between operational simplicity and marginal statistical gain, "
                "which architecture would you choose for production, and what failure mode are you willing to accept?"
            )
            return DebateSynthesis(
                query=query,
                participating_experts=[e.name for e in experts],
                has_unresolved_disagreement=True,
                positions=positions,
                conflict_statement=conflict,
                uncertainty_statement=uncertainty,
                pathways_forward=pathways,
                experiment_design=experiment,
                escalation_question=escalation,
                consensus_summary=None
            )
        else:
            return DebateSynthesis(
                query=query,
                participating_experts=[e.name for e in experts],
                has_unresolved_disagreement=False,
                positions=positions,
                conflict_statement=None,
                uncertainty_statement=None,
                pathways_forward=["Proceed to implementation with unit tests and leakage audits."],
                experiment_design=None,
                escalation_question="What unit test will you write first to verify the edge cases flagged by the Red Team?",
                consensus_summary="The Council agrees on the core implementation path, subject to the safety and verification checks outlined above."
            )

    def evaluate_user_decision_rationale(
        self,
        user_choice: str,
        user_rationale: str,
        debate_synthesis: DebateSynthesis
    ) -> Dict:
        """Evaluates user's engineering judgment when responding to an escalated council disagreement."""
        rat_lower = user_rationale.lower()
        strengths = []
        unstated_assumptions = []
        score = 6.0

        # Check for trade-off recognition
        if any(w in rat_lower for w in ["trade-off", "tradeoff", "compromise", "versus", "vs", "sacrifice", "cost"]):
            strengths.append("Demonstrated explicit trade-off awareness rather than seeking a silver bullet.")
            score += 1.5

        # Check for empirical validation reference
        if any(w in rat_lower for w in ["experiment", "benchmark", "test", "metric", "profile", "validation"]):
            strengths.append("Anchored decision in empirical verification / Experiment-First principle.")
            score += 1.5

        # Check for unstated assumptions
        if "latency" not in rat_lower and "speed" not in rat_lower:
            unstated_assumptions.append("Assumes serving latency SLA will not be breached under high concurrency.")
        if "cost" not in rat_lower and "resource" not in rat_lower:
            unstated_assumptions.append("Assumes infrastructure budget accommodates increased compute/VRAM.")
        if "drift" not in rat_lower and "maintenance" not in rat_lower:
            unstated_assumptions.append("Assumes feature distributions remain stationary without active retraining.")

        score = min(10.0, max(1.0, score))

        return {
            "chosen_option": user_choice,
            "rationale": user_rationale,
            "judgment_score": score,
            "strengths": strengths or ["Formulated a decisive engineering position"],
            "unstated_assumptions": unstated_assumptions,
            "mentor_verdict": (
                "Solid engineering judgment! You clearly weighed competing trade-offs."
                if score >= 7.5 else
                "Reasonable start, but consider the unstated operational assumptions highlighted above."
            )
        }
