"""Unit tests for the pedagogical engine, learner model, and scaffolding."""

import unittest
from pathlib import Path
import tempfile
from senior_mentor.memory.store import MemoryStore
from senior_mentor.knowledge.graph import KnowledgeGraph
from senior_mentor.pedagogy.learner_model import LearnerModel
from senior_mentor.pedagogy.scaffolding import ScaffoldingEngine

class TestPedagogy(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_memory.db"
        self.store = MemoryStore(self.db_path)
        self.graph = KnowledgeGraph()
        self.model = LearnerModel(self.store, self.graph)
        self.engine = ScaffoldingEngine(self.model, self.graph)

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_zpd_assessment_unmet_prerequisites(self):
        # Concept with prerequisites where user has no history
        status = self.model.assess_concept_zpd("Principal Component Analysis")
        self.assertIn("Prerequisites Unmet", status.zone)
        self.assertEqual(status.recommended_level, 0)
        self.assertTrue(len(status.unmet_prerequisites) > 0)

    def test_zpd_assessment_mastery(self):
        # Satisfy prereqs and high proficiency
        self.store.record_knowledge_assessment("Mathematics", "Linear Algebra: Eigenvectors & SVD", success=True)
        # Multiple successes to raise proficiency
        for _ in range(5):
            self.store.record_knowledge_assessment("Machine Learning", "Principal Component Analysis", success=True)

        status = self.model.assess_concept_zpd("Principal Component Analysis")
        self.assertEqual(status.zone, "Mastery (Ready for Independent Challenge)")
        self.assertIn(status.recommended_level, [6, 7])

    def test_explicit_override_solve(self):
        resp = self.engine.generate_scaffold(
            query="Implement PCA in Python",
            concept_name="Principal Component Analysis",
            override_mode="solve"
        )
        self.assertEqual(resp.level, 0)
        self.assertEqual(resp.tier, "Direct Guidance")
        self.assertIn("Direct Solution", resp.content)

    def test_explicit_override_mentor(self):
        resp = self.engine.generate_scaffold(
            query="How does self-attention work?",
            concept_name="Transformer Architecture & Attention",
            override_mode="mentor"
        )
        self.assertEqual(resp.level, 5)
        self.assertEqual(resp.tier, "Socratic Scaffolding")

    def test_anti_dependency_alert_trigger(self):
        # Flood with direct solve queries
        for i in range(12):
            self.engine.generate_scaffold(f"query {i}", override_mode="solve")

        warning = self.model.check_anti_dependency_warning()
        self.assertIsNotNone(warning)
        self.assertIn("ANTI-DEPENDENCY ALERT", warning)

if __name__ == "__main__":
    unittest.main()
