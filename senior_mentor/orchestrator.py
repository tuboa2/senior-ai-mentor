"""The Orchestrator (Principal AI Engineer & Mentor Lead).

Acts as the cognitive bottleneck, decision-maker, and pedagogical synthesizer.
Coordinates the Expert Council, Learner Model, Knowledge Graph, and Scaffolding Engine.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from .config import MentorConfig
from .memory.store import MemoryStore, UserProfile
from .knowledge.graph import KnowledgeGraph, ConceptNode
from .pedagogy.learner_model import LearnerModel, ZPDStatus
from .pedagogy.scaffolding import ScaffoldingEngine, ScaffoldedResponse
from .council.experts import PERMANENT_EXPERTS, spawn_dynamic_specialist
from .council.debate import DebateEngine, DebateSynthesis
from .council.interview import InterviewSimulator, InterviewQuestion
from .skills.manager import SkillManager
from .evaluation.tracker import CompetencyTracker, EvaluationReport
from .self_improvement.feedback import AutonomousSelfImprovementEngine, RefinementProposal

@dataclass
class OrchestratorResponse:
    query: str
    command_mode: Optional[str]
    scaffold: ScaffoldedResponse
    debate_synthesis: Optional[DebateSynthesis]
    matched_concept: Optional[str]
    zpd_status: Optional[ZPDStatus]
    anti_dependency_warning: Optional[str]
    interview_question: Optional[InterviewQuestion] = None
    interview_feedback: Optional[Dict] = None

class Orchestrator:
    def __init__(self, config: Optional[MentorConfig] = None):
        self.config = config or MentorConfig()
        self.store = MemoryStore(self.config.db_path)
        self.graph = KnowledgeGraph()
        self.learner_model = LearnerModel(self.store, self.graph)
        self.scaffolding_engine = ScaffoldingEngine(self.learner_model, self.graph)
        self.debate_engine = DebateEngine()
        self.interviewer = InterviewSimulator(self.store)
        self.skill_manager = SkillManager(self.config)
        self.tracker = CompetencyTracker(self.store)
        self.self_improvement = AutonomousSelfImprovementEngine(self.store)

    def parse_command(self, raw_text: str) -> Tuple[Optional[str], str]:
        """Extracts slash commands like /solve, /mentor, /hint, /challenge, /council, /interview."""
        text = raw_text.strip()
        if text.startswith("/"):
            parts = text[1:].split(maxsplit=1)
            cmd = parts[0].lower()
            remainder = parts[1].strip() if len(parts) > 1 else ""
            if cmd in ("solve", "mentor", "hint", "challenge", "council", "interview", "status", "profile", "eval", "skills", "feedback", "refine"):
                return cmd, remainder
        return None, text

    def match_concept(self, text: str) -> Optional[str]:
        """Finds closest matching concept in knowledge graph."""
        matches = self.graph.search(text)
        if matches:
            return matches[0].name
        return None

    def process_query(self, user_input: str) -> OrchestratorResponse:
        cmd, clean_query = self.parse_command(user_input)
        active_query = clean_query if clean_query else user_input

        # Handle interview command
        interview_q = None
        if cmd == "interview":
            domain = clean_query if clean_query else "system_design"
            interview_q = self.interviewer.start_interview(domain)

        # Match relevant concept in knowledge graph
        matched_concept = self.match_concept(active_query)
        zpd_info = self.learner_model.assess_concept_zpd(matched_concept) if matched_concept else None

        # Check if Expert Council debate should be triggered
        should_debate = (cmd == "council") or any(
            t in active_query.lower() for t in ["trade-off", "vs", "or", "compare", "which is better", "should i use"]
        )

        debate_result = None
        if should_debate:
            debate_result = self.debate_engine.deliberate(active_query, force_disagreement=(cmd == "council"))

        # Generate Scaffolding
        scaffold = self.scaffolding_engine.generate_scaffold(
            query=active_query,
            concept_name=matched_concept,
            override_mode=cmd
        )

        anti_warning = self.learner_model.check_anti_dependency_warning()

        return OrchestratorResponse(
            query=user_input,
            command_mode=cmd,
            scaffold=scaffold,
            debate_synthesis=debate_result,
            matched_concept=matched_concept,
            zpd_status=zpd_info,
            anti_dependency_warning=anti_warning,
            interview_question=interview_q
        )

    def record_user_decision(self, context: str, options: List[str], chosen: str, rationale: str) -> Dict:
        """Evaluates and persists the user's decision rationale when resolving an escalated trade-off."""
        if not hasattr(self, "_last_debate") or not self._last_debate:
            dummy_synth = self.debate_engine.deliberate(context, force_disagreement=True)
        else:
            dummy_synth = self._last_debate

        evaluation = self.debate_engine.evaluate_user_decision_rationale(chosen, rationale, dummy_synth)
        self.store.log_decision(context, options, chosen, rationale, outcome=evaluation["mentor_verdict"])
        return evaluation

    def get_learner_status(self) -> Dict:
        """Returns comprehensive diagnostic on learner profile and competency."""
        profile = self.store.get_or_create_profile()
        eval_report = self.tracker.generate_current_assessment()
        anti_ratio = self.store.get_anti_dependency_ratio()
        unresolved_errs = self.store.get_unresolved_misconceptions()
        recent_decisions = self.store.get_recent_decisions(limit=5)
        knowledge_records = self.store.get_knowledge_state()

        return {
            "profile": profile,
            "competency_tier": eval_report.competency_tier,
            "overall_score": eval_report.overall_score,
            "dimension_scores": eval_report.dimension_scores,
            "anti_dependency_ratio": anti_ratio,
            "unresolved_misconceptions": unresolved_errs,
            "recent_decisions": recent_decisions,
            "knowledge_count": len(knowledge_records),
            "recommended_learning_plan": eval_report.recommended_learning_plan
        }
