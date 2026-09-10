"""The Orchestrator (Principal AI Engineer & Mentor Lead).

Acts as the cognitive bottleneck, decision-maker, and pedagogical synthesizer.
Coordinates the Expert Council, Learner Model, Knowledge Graph, and Scaffolding Engine.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from .config import MentorConfig
from .memory.store import MemoryStore, UserProfile
from .knowledge.graph import KnowledgeGraph, ConceptNode
from .pedagogy.learner_model import LearnerModel, ZPDStatus
from .pedagogy.scaffolding import ScaffoldingEngine, ScaffoldedResponse
from .pedagogy.scope_guard import ScopeGuard, ScopeCheckResult
from .council.experts import PERMANENT_EXPERTS, spawn_dynamic_specialist
from .council.debate import DebateEngine, DebateSynthesis
from .council.interview import InterviewSimulator, InterviewQuestion
from .skills.manager import SkillManager
from .evaluation.tracker import CompetencyTracker, EvaluationReport
from .self_improvement.feedback import AutonomousSelfImprovementEngine, RefinementProposal
from .project_detector import ProjectContextDetector, ProjectContextResult

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
    is_rejected: bool = False
    rejection_reason: Optional[str] = None
    project_context: Optional[ProjectContextResult] = None
    retrieved_progress: Optional[Dict] = None

class Orchestrator:
    def __init__(self, config: Optional[MentorConfig] = None, workspace_dir: Optional[Path] = None):
        self.config = config or MentorConfig()
        self.workspace_dir = Path(workspace_dir or Path.cwd()).resolve()
        self.context_detector = ProjectContextDetector()
        self.project_context = self.context_detector.detect(self.workspace_dir)

        # Initialize Memory Store with conditional mutation authorization
        self.store = MemoryStore(self.config.db_path, mutation_allowed=self.project_context.is_related)
        self.graph = KnowledgeGraph()
        self.learner_model = LearnerModel(self.store, self.graph)
        self.scaffolding_engine = ScaffoldingEngine(self.learner_model, self.graph)
        self.debate_engine = DebateEngine()
        self.interviewer = InterviewSimulator(self.store)
        self.skill_manager = SkillManager(self.config)
        self.tracker = CompetencyTracker(self.store)
        self.self_improvement = AutonomousSelfImprovementEngine(self.store)
        self.scope_guard = ScopeGuard()

        # If project is related to AI/ML/Data Science, retrieve progress and link project
        self.retrieved_progress: Optional[Dict] = None
        if self.project_context.is_related:
            self.retrieved_progress = self.get_learner_status()
            self._sync_project_memory()

    def _sync_project_memory(self) -> None:
        """Links active technical project to project memory if modification is authorized."""
        if not self.project_context.is_related:
            return
        proj_name = self.workspace_dir.name
        existing = [p for p in self.store.get_projects(limit=20) if p.name == proj_name]
        if not existing:
            stack = ", ".join(self.project_context.detected_frameworks) or self.project_context.project_type
            notes = f"Detected domains: {', '.join(self.project_context.detected_domains)}"
            self.store.log_project(
                name=proj_name,
                tech_stack=stack,
                architecture_notes=notes,
                key_decisions="Project dynamically linked by Senior AI Mentor Orchestrator",
                lessons_learned="Active development underway"
            )

    def set_workspace(self, workspace_dir: Path) -> ProjectContextResult:
        """Dynamically switches workspace context and updates memory mutation lock."""
        self.workspace_dir = Path(workspace_dir).resolve()
        self.project_context = self.context_detector.detect(self.workspace_dir)
        self.store.set_mutation_allowed(self.project_context.is_related)
        if self.project_context.is_related:
            self.retrieved_progress = self.get_learner_status()
            self._sync_project_memory()
        else:
            self.retrieved_progress = None
        return self.project_context

    def parse_command(self, raw_text: str) -> Tuple[Optional[str], str]:
        """Extracts slash commands like /solve, /mentor, /hint, /challenge, /council, /interview, /context."""
        text = raw_text.strip()
        if text.startswith("/"):
            parts = text[1:].split(maxsplit=1)
            cmd = parts[0].lower()
            remainder = parts[1].strip() if len(parts) > 1 else ""
            if cmd in ("solve", "mentor", "hint", "challenge", "council", "interview", "status", "profile", "eval", "skills", "feedback", "refine", "update", "changelog", "context"):
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

        # Scope Guard: Reject queries outside AI engineering scope and guarantee zero memory mutation
        scope_result = self.scope_guard.check_scope(user_input)
        if not scope_result.is_in_scope:
            return OrchestratorResponse(
                query=user_input,
                command_mode=cmd,
                scaffold=ScaffoldedResponse(
                    level=-1,
                    level_name="Rejected (Out of Scope)",
                    tier="Scope Guard",
                    content=scope_result.rejection_message,
                    anti_dependency_alert=None,
                    next_action_prompt="Submit a technical query in Machine Learning, Systems, Software Architecture, or Data Science."
                ),
                debate_synthesis=None,
                matched_concept=None,
                zpd_status=None,
                anti_dependency_warning=None,
                interview_question=None,
                is_rejected=True,
                rejection_reason=scope_result.reason
            )

        # Handle changelog command
        if cmd == "changelog":
            from .changelog import ChangelogManager
            cm = ChangelogManager()
            target_ver = clean_query if clean_query else None
            text_out = cm.format_terminal_output(target_ver, use_color=False)
            return OrchestratorResponse(
                query=user_input,
                command_mode="changelog",
                scaffold=ScaffoldedResponse(
                    level=3,
                    level_name="Changelog & Release Notes",
                    tier="System Release Notes",
                    content=text_out,
                    anti_dependency_alert=None,
                    next_action_prompt="Use /status to inspect your current profile or /update to sync the latest framework features."
                ),
                debate_synthesis=None,
                matched_concept=None,
                zpd_status=None,
                anti_dependency_warning=None,
                project_context=self.project_context,
                retrieved_progress=self.retrieved_progress
            )

        # Handle context command
        if cmd == "context":
            target_dir = Path(clean_query).resolve() if clean_query else self.workspace_dir
            ctx_res = self.context_detector.detect(target_dir)
            ctx_lines = [
                f"### [Senior AI Engineering Mentor: Project Context Inspection]",
                "",
                f"**Workspace Path:** `{target_dir}`",
                f"**Related to AI/ML/Data Science:** {'YES (Active Domain)' if ctx_res.is_related else 'NO (Unrelated / Non-Technical)'}",
                f"**Project Classification:** {ctx_res.project_type}",
                f"**Detection Confidence:** {ctx_res.confidence * 100:.0f}%",
                f"**Detected Domains:** {', '.join(ctx_res.detected_domains) if ctx_res.detected_domains else 'None'}",
                f"**Detected Frameworks:** {', '.join(ctx_res.detected_frameworks) if ctx_res.detected_frameworks else 'None'}",
                "",
                f"**Mentor Memory Status:** {'🔓 RETRIEVED & MODIFICATIONS AUTHORIZED' if ctx_res.modification_allowed else '🔒 LOCKED (READ-ONLY) - ZERO MUTATIONS PERMITTED'}",
                ""
            ]
            if ctx_res.evidence:
                ctx_lines.append("**Detection Evidence:**")
                for ev in ctx_res.evidence:
                    ctx_lines.append(f"- {ev}")
                ctx_lines.append("")
            ctx_lines.append(f"*{ctx_res.summary}*")

            return OrchestratorResponse(
                query=user_input,
                command_mode="context",
                scaffold=ScaffoldedResponse(
                    level=3,
                    level_name="Project Context Inspection",
                    tier="Context Detector",
                    content="\n".join(ctx_lines),
                    anti_dependency_alert=None,
                    next_action_prompt="Ask a technical ML/engineering question or use /council to deliberate technical decisions."
                ),
                debate_synthesis=None,
                matched_concept=None,
                zpd_status=None,
                anti_dependency_warning=None,
                project_context=ctx_res,
                retrieved_progress=self.retrieved_progress
            )

        # Handle update command
        if cmd == "update":
            from .initializer import update_workspace
            target_path = Path(clean_query).resolve() if clean_query else Path.cwd()
            res = update_workspace(target_path)
            report_lines = [
                f"### [Senior AI Engineering Mentor: Workspace Synchronized to v{res.get('version', '1.1.1')}]",
                "",
                f"**Target Workspace:** `{target_path}`",
                f"**Status:** {res.get('status', 'success').upper()}",
                ""
            ]
            if res.get("new_skills"):
                report_lines.append("**New Skills Installed:**")
                for s in res["new_skills"]:
                    report_lines.append(f"- `/{s}`")
                report_lines.append("")
            if res.get("updated_skills"):
                report_lines.append("**Skills Refreshed:**")
                for s in res["updated_skills"]:
                    report_lines.append(f"- `/{s}`")
                report_lines.append("")
            if res.get("updated_files"):
                report_lines.append(f"**Updated {len(res['updated_files'])} Configuration & Directive Files.**")
            for m in res.get("messages", []):
                report_lines.append(f"• {m}")

            return OrchestratorResponse(
                query=user_input,
                command_mode="update",
                scaffold=ScaffoldedResponse(
                    level=3,
                    level_name="Dynamic Workspace Update",
                    tier="System Synchronizer",
                    content="\n".join(report_lines),
                    anti_dependency_alert=None,
                    next_action_prompt="Your workspace is fully updated. Use /changelog to view release details or /council to deliberate technical decisions."
                ),
                debate_synthesis=None,
                matched_concept=None,
                zpd_status=None,
                anti_dependency_warning=None,
                project_context=self.project_context,
                retrieved_progress=self.retrieved_progress
            )

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
            interview_question=interview_q,
            project_context=self.project_context,
            retrieved_progress=self.retrieved_progress
        )

    def record_user_decision(self, context: str, options: List[str], chosen: str, rationale: str) -> Dict:
        """Evaluates and persists the user's decision rationale when resolving an escalated trade-off."""
        scope_check = self.scope_guard.check_scope(context)
        if not scope_check.is_in_scope:
            return {
                "judgment_score": 0.0,
                "mentor_verdict": f"Rejected: context '{context}' is outside technical scope.",
                "strengths": [],
                "blind_spots": [scope_check.reason],
                "calibrated_guidance": "Decisions can only be recorded for in-scope technical engineering trade-offs."
            }

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
