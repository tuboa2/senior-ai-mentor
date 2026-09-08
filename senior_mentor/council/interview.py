"""Technical Interviewer Simulation Engine.

Conducts realistic senior and staff-level technical mock interviews across:
1. ML Theory & Mathematical Foundations
2. Machine Learning System Design
3. Statistical Validity & Experimental Design
4. High-Performance Coding & Algorithmic Rigor
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from ..memory.store import MemoryStore
from ..evaluation.rubric import CompetencyRubric, EvaluationReport

@dataclass
class InterviewQuestion:
    id: str
    domain: str
    level: str  # "Senior", "Staff", "Principal"
    title: str
    scenario: str
    probing_questions: List[str]
    ideal_competencies: List[str]

INTERVIEW_QUESTION_BANK: Dict[str, List[InterviewQuestion]] = {
    "system_design": [
        InterviewQuestion(
            id="sys_01",
            domain="system_design",
            level="Senior/Staff",
            title="Real-Time Video Recommendation & Serving System",
            scenario=(
                "Design a personalized video recommendation system serving 100M Daily Active Users. "
                "The system must return top-20 recommendations with a strict p99 latency SLA of 60ms. "
                "Address candidate retrieval (bi-encoders / ANN), multi-task ranking, and real-time feature freshness."
            ),
            probing_questions=[
                "How do you handle cold-start videos and user exploration vs exploitation?",
                "What is your vector search indexing strategy (HNSW vs ScaNN), and where do you cache embeddings?",
                "How do you prevent position bias and popularity bias from corrupting the ranking loss?"
            ],
            ideal_competencies=["Candidate generation vs ranking split", "Two-tower architectures", "Approximate Nearest Neighbors", "p99 latency budgets"]
        ),
        InterviewQuestion(
            id="sys_02",
            domain="system_design",
            level="Staff/Principal",
            title="High-Throughput LLM Serving Platform with Prefix Caching",
            scenario=(
                "Architect an enterprise LLM gateway and serving cluster supporting 10,000 requests/sec. "
                "Workloads have 80% overlapping system prompts across multi-turn agent conversations. "
                "Design the memory management, batching, and KV-cache strategy."
            ),
            probing_questions=[
                "How does PagedAttention eliminate internal and external memory fragmentation?",
                "How do you implement Radix-tree prefix caching across distributed tensor-parallel replicas?",
                "Under sudden memory pressure, what is your preemptive scheduling and KV-swap policy?"
            ],
            ideal_competencies=["Continuous batching (vLLM style)", "PagedAttention", "Prefix caching", "Tensor parallelism"]
        )
    ],
    "ml_theory": [
        InterviewQuestion(
            id="theo_01",
            domain="ml_theory",
            level="Senior",
            title="Attention Scaling & Vanishing Gradients in Transformers",
            scenario=(
                "Explain from first principles why the dot-product in self-attention is scaled by 1/√d_k. "
                "What happens to the softmax gradients if this scaling factor is omitted as d_k grows large?"
            ),
            probing_questions=[
                "Can you write out the mathematical derivative of the softmax function with respect to its logits?",
                "How does FlashAttention optimize the computation without materializing the N×N attention matrix in HBM?",
                "What is the mathematical distinction between Post-LN and Pre-LN Transformer stability?"
            ],
            ideal_competencies=["Variance of sum of random variables", "Softmax saturation", "GPU memory hierarchies (SRAM vs HBM)"]
        )
    ],
    "statistics": [
        InterviewQuestion(
            id="stat_01",
            domain="statistics",
            level="Senior/Staff",
            title="A/B Testing with Network Spillover & False Discovery Control",
            scenario=(
                "You are evaluating a new social feed algorithm. Standard user-level A/B randomization suffers from "
                "social network interference (treatment users interacting with control users). How do you design "
                "the experiment and control for false discovery across 40 secondary metrics?"
            ),
            probing_questions=[
                "Why does user-level randomization violate SUTVA (Stable Unit Treatment Value Assumption)?",
                "How would cluster-based randomization or graph partitioning mitigate interference?",
                "How do you apply Benjamini-Hochberg FDR control when metrics are correlated?"
            ],
            ideal_competencies=["SUTVA violation", "Cluster randomization", "Graph partitioning", "Multiple testing FDR control"]
        )
    ],
    "coding": [
        InterviewQuestion(
            id="code_01",
            domain="coding",
            level="Senior",
            title="Vectorized Softmax with Numerical Stability & Memory Profiling",
            scenario=(
                "Write a mathematically stable, vectorized softmax function in Python for a 2D batch of logits. "
                "Explain the log-sum-exp trick and why naive exp(x) overflows into floating-point NaN."
            ),
            probing_questions=[
                "What is the asymptotic memory complexity and how do you achieve in-place subtraction?",
                "How would you implement the backward pass (Jacobian-vector product) efficiently?",
                "How does this behave under mixed-precision FP16 vs FP32?"
            ],
            ideal_competencies=["Numerical stability via max subtraction", "Vectorized array operations", "Numerical dynamic range"]
        )
    ]
}

class InterviewSimulator:
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
        self.rubric = CompetencyRubric()

    def start_interview(self, domain: str = "system_design") -> InterviewQuestion:
        dom_key = domain.lower()
        questions = INTERVIEW_QUESTION_BANK.get(dom_key) or INTERVIEW_QUESTION_BANK["system_design"]
        return questions[0]

    def evaluate_candidate_response(
        self,
        question: InterviewQuestion,
        candidate_response: str
    ) -> Dict:
        """Evaluates candidate response across senior engineering interview dimensions."""
        resp_lower = candidate_response.lower()

        # Score dimensions
        correctness_score = 7.0
        tradeoff_score = 6.0
        edge_case_score = 6.0

        for comp in question.ideal_competencies:
            if any(w in resp_lower for w in comp.lower().split()):
                correctness_score = min(10.0, correctness_score + 0.8)

        if any(w in resp_lower for w in ["trade-off", "tradeoff", "latency", "memory", "cost", "vs", "compromise"]):
            tradeoff_score = min(10.0, tradeoff_score + 2.0)

        if any(w in resp_lower for w in ["fallback", "failure", "edge case", "overflow", "bottleneck", "drift"]):
            edge_case_score = min(10.0, edge_case_score + 2.0)

        ratings = {
            "Technical Correctness & Mathematical Soundness": round(correctness_score, 1),
            "Architectural Design & Scalability": round(tradeoff_score, 1),
            "Statistical Validity & Leakage Resistance": 7.0,
            "Defensive Programming & Security": round(edge_case_score, 1),
            "Trade-Off Communication & Justification": round(tradeoff_score, 1)
        }

        eval_report = self.rubric.evaluate(ratings)

        # Update learner knowledge state based on interview performance
        is_success = eval_report.overall_score >= 7.0
        self.store.record_knowledge_assessment(
            domain=question.domain,
            microskill=f"Interview: {question.title}",
            success=is_success
        )

        return {
            "question_title": question.title,
            "domain": question.domain,
            "overall_score": eval_report.overall_score,
            "evaluated_level": eval_report.competency_tier,
            "strengths": eval_report.strengths,
            "areas_for_improvement": eval_report.areas_for_growth,
            "recommended_study": eval_report.recommended_learning_plan
        }
