"""Unit tests for the persistent structured memory store."""

import unittest
from pathlib import Path
import tempfile
from senior_mentor.memory.store import MemoryStore, UserProfile

class TestMemoryStore(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_memory.db"
        self.store = MemoryStore(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_profile_creation_and_update(self):
        prof = self.store.get_or_create_profile("user1", "Alice")
        self.assertEqual(prof.name, "Alice")
        self.assertEqual(prof.target_role, "Senior AI Engineer")

        prof.target_role = "Principal ML Architect"
        self.store.update_profile(prof)

        updated = self.store.get_or_create_profile("user1")
        self.assertEqual(updated.target_role, "Principal ML Architect")

    def test_knowledge_assessment_and_ema(self):
        # First assessment
        rec1 = self.store.record_knowledge_assessment("Statistics", "Hypothesis Testing", success=True)
        self.assertGreater(rec1.proficiency, 0.5)
        self.assertEqual(rec1.attempts, 1)
        self.assertEqual(rec1.successes, 1)

        # Second assessment failure
        rec2 = self.store.record_knowledge_assessment("Statistics", "Hypothesis Testing", success=False)
        self.assertLess(rec2.proficiency, rec1.proficiency)
        self.assertEqual(rec2.attempts, 2)
        self.assertEqual(rec2.successes, 1)

    def test_misconception_lifecycle(self):
        self.store.record_misconception("Cross-Validation", "Random split on time-series data")
        errs = self.store.get_unresolved_misconceptions()
        self.assertEqual(len(errs), 1)
        self.assertEqual(errs[0].frequency, 1)

        # Record again -> frequency increases
        self.store.record_misconception("Cross-Validation", "Random split on time-series data")
        errs = self.store.get_unresolved_misconceptions()
        self.assertEqual(errs[0].frequency, 2)

        # Resolve
        self.store.resolve_misconception(errs[0].id)
        self.assertEqual(len(self.store.get_unresolved_misconceptions()), 0)

    def test_decision_and_experiment_logging(self):
        self.store.log_decision(
            context="Choosing vector search engine",
            options=["Faiss", "Qdrant", "Chroma"],
            chosen="Qdrant",
            rationale="Need distributed filtering with metadata payloads."
        )
        decisions = self.store.get_recent_decisions()
        self.assertEqual(len(decisions), 1)
        self.assertEqual(decisions[0].chosen_option, "Qdrant")

        self.store.log_experiment(
            name="LoRA rank ablation",
            hypothesis="r=16 matches full fine-tuning with 90% memory savings",
            baseline="Full fine-tuning",
            variables="r=[4, 8, 16, 32]",
            metrics="Perplexity, VRAM"
        )
        exps = self.store.get_experiments()
        self.assertEqual(len(exps), 1)
        self.assertEqual(exps[0].name, "LoRA rank ablation")

    def test_anti_dependency_ratio(self):
        # Log 3 direct solves (L0) and 1 Socratic (L4)
        self.store.log_scaffolding_interaction("test 1", level=0, explicit_override=True)
        self.store.log_scaffolding_interaction("test 2", level=1, explicit_override=True)
        self.store.log_scaffolding_interaction("test 3", level=2, explicit_override=True)
        self.store.log_scaffolding_interaction("test 4", level=4, explicit_override=False)

        ratio = self.store.get_anti_dependency_ratio()
        self.assertEqual(ratio, 0.75)

if __name__ == "__main__":
    unittest.main()
