"""Unit tests for Phase 7 Self-Improvement, Technical Interviews, and Advanced Governance."""

import unittest
from pathlib import Path
import tempfile
import json
from senior_mentor.config import MentorConfig
from senior_mentor.memory.store import MemoryStore
from senior_mentor.knowledge.graph import KnowledgeGraph
from senior_mentor.self_improvement.feedback import AutonomousSelfImprovementEngine
from senior_mentor.council.interview import InterviewSimulator
from senior_mentor.council.debate import DebateEngine
from senior_mentor.skills.sandbox import ExecutionSandbox
from senior_mentor.skills.manager import SkillManager

class TestAdvancedFeatures(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "adv_test.db"
        self.audit_log = Path(self.temp_dir.name) / "audit_otel.jsonl"
        self.cfg = MentorConfig(db_path=self.db_path, audit_log_path=self.audit_log)
        self.store = MemoryStore(self.db_path)
        self.graph = KnowledgeGraph()
        self.self_improvement = AutonomousSelfImprovementEngine(self.store)
        self.interviewer = InterviewSimulator(self.store)
        self.debate_engine = DebateEngine()
        self.sandbox = ExecutionSandbox(self.cfg)
        self.skill_manager = SkillManager(self.cfg)

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_self_improvement_feedback_and_refinement(self):
        # 1. Log two user corrections
        self.self_improvement.capture_correction(
            context="Explanation of SVD sign ambiguity",
            user_correction="Make sure to mention that singular vectors can differ in sign across numpy and scipy."
        )
        self.self_improvement.capture_correction(
            context="Explanation of SVD truncation",
            user_correction="Clarify that singular values are non-negative and sorted in descending order."
        )
        # 2. Record recurring misconception
        self.store.record_misconception("Principal Component Analysis", "Forgot to center data before computing covariance matrix")
        self.store.record_misconception("Principal Component Analysis", "Forgot to center data before computing covariance matrix")

        # 3. Analyze proposals
        proposals = self.self_improvement.analyze_improvement_opportunities()
        self.assertGreaterEqual(len(proposals), 2)
        prop_targets = [p.target_component for p in proposals]
        self.assertIn("Orchestrator System Prompt", prop_targets)
        self.assertIn("Skill: Principal Component Analysis", prop_targets)

        # 4. Stage a version
        ver_rec = self.self_improvement.stage_component_version(
            component_type="system_prompt",
            component_name="Orchestrator System Prompt",
            version="1.0.1",
            content="Updated system prompt with SVD precision clause.",
            changelog="Added sign ambiguity clarification from user feedback."
        )
        self.assertEqual(ver_rec.version, "1.0.1")
        self.assertIsNotNone(ver_rec.content_hash)

    def test_technical_interview_flow_and_evaluation(self):
        # 1. Start system design interview
        q = self.interviewer.start_interview("system_design")
        self.assertEqual(q.domain, "system_design")
        self.assertIn("Recommendation", q.title)

        # 2. Submit candidate answer
        good_response = (
            "We split candidate generation from ranking using a two-tower bi-encoder and ScaNN vector search for ANN. "
            "For ranking, we optimize multi-task loss with position bias correction. "
            "The primary trade-off is inference latency vs ranking accuracy, respecting a 60ms p99 SLA with fallback cache."
        )
        eval_result = self.interviewer.evaluate_candidate_response(q, good_response)
        self.assertGreaterEqual(eval_result["overall_score"], 7.0)
        self.assertIn(eval_result["evaluated_level"], ["Senior Engineer", "Staff Engineer", "Principal Engineer"])

        # 3. Check that knowledge record was updated
        records = self.store.get_knowledge_state()
        self.assertTrue(any(q.title in r.microskill for r in records))

    def test_user_decision_rationale_evaluation(self):
        synth = self.debate_engine.deliberate("XGBoost vs Deep Learning", force_disagreement=True)
        eval_result = self.debate_engine.evaluate_user_decision_rationale(
            user_choice="XGBoost",
            user_rationale="I choose XGBoost because tabular data lacks spatial invariance, and our latency SLA is 20ms. "
                           "The trade-off is sacrificing multi-modal integration for lower operational cost and verified benchmark metrics.",
            debate_synthesis=synth
        )
        self.assertGreaterEqual(eval_result["judgment_score"], 7.5)
        self.assertTrue(len(eval_result["strengths"]) > 0)

    def test_knowledge_graph_concept_linking(self):
        # Log a project using PCA
        self.store.log_project(
            name="Customer Segmentation Platform",
            tech_stack="Python, scikit-learn, PCA, DuckDB",
            architecture_notes="Used Principal Component Analysis to reduce 200 customer features to 15 orthogonal components.",
            key_decisions="Chose PCA over t-SNE to maintain linear interpretability.",
            lessons_learned="Must normalize variances before decomposition."
        )
        # Log a misconception
        self.store.record_misconception("Principal Component Analysis", "Interpreted PCA components as causal features")

        # Query concept context from KnowledgeGraph
        ctx = self.graph.get_concept_context("Principal Component Analysis", self.store)
        self.assertIn("Customer Segmentation Platform", ctx["applied_in_projects"])
        self.assertIn("Linear Algebra: Eigenvectors & SVD", ctx["prerequisites"])
        self.assertTrue(len(ctx["past_misconceptions"]) > 0)

    def test_opentelemetry_audit_logging(self):
        script = Path(self.temp_dir.name) / "test_exec.py"
        script.write_text("print('Executing under OpenTelemetry SemConv')", encoding="utf-8")

        res = self.sandbox.run_script(script)
        self.assertTrue(res.success)

        # Inspect audit trail
        self.assertTrue(self.audit_log.exists())
        lines = self.audit_log.read_text(encoding="utf-8").strip().splitlines()
        self.assertGreater(len(lines), 0)
        entry = json.loads(lines[-1])
        self.assertIn("trace_id", entry)
        self.assertIn("span_id", entry)
        self.assertEqual(entry["attributes"]["gen_ai.system"], "senior_ai_mentor")
        self.assertEqual(entry["attributes"]["gen_ai.operation.name"], "sandboxed_skill_execution")

    def test_tier2_dynamic_skill_discovery(self):
        # Run dynamic discovery for a task
        results = self.skill_manager.discover_skills_for_task("Run security audit and red team attack", max_candidates=3)
        self.assertIsInstance(results, list)

if __name__ == "__main__":
    unittest.main()
