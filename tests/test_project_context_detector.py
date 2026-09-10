"""Tests for Dynamic Project Context Detection and Conditional Memory Modification (v1.1.1)."""

from pathlib import Path
import shutil
import tempfile
import unittest
import sqlite3

from senior_mentor.project_detector import ProjectContextDetector, ProjectContextResult
from senior_mentor.memory.store import MemoryStore, UserProfile
from senior_mentor.orchestrator import Orchestrator
from senior_mentor.config import MentorConfig


class TestProjectContextDetector(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.detector = ProjectContextDetector()

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_ai_ml_workspace_from_requirements(self):
        req_file = self.temp_dir / "requirements.txt"
        req_file.write_text("torch>=2.1.0\ntransformers==4.35.0\naccelerate\n", encoding="utf-8")

        res = self.detector.detect(self.temp_dir)
        self.assertTrue(res.is_related)
        self.assertTrue(res.modification_allowed)
        self.assertIn("PyTorch", res.detected_frameworks)
        self.assertIn("Hugging Face Transformers", res.detected_frameworks)
        self.assertIn("Machine Learning & Deep Learning", res.detected_domains)
        self.assertGreaterEqual(res.confidence, 0.5)

    def test_detect_data_science_workspace_from_notebooks_and_pyproject(self):
        pyproject = self.temp_dir / "pyproject.toml"
        pyproject.write_text('[project]\ndependencies = ["pandas>=2.0.0", "polars", "duckdb"]\n', encoding="utf-8")
        nb = self.temp_dir / "eda_exploration.ipynb"
        nb.write_text('{"cells": []}', encoding="utf-8")

        res = self.detector.detect(self.temp_dir)
        self.assertTrue(res.is_related)
        self.assertTrue(res.modification_allowed)
        self.assertIn("Pandas", res.detected_frameworks)
        self.assertIn("Data Science & Applied Statistics", res.detected_domains)

    def test_detect_model_artifacts_and_dedicated_dirs(self):
        models_dir = self.temp_dir / "models"
        models_dir.mkdir(parents=True)
        (models_dir / "resnet50.onnx").write_bytes(b"dummy_weights")
        (models_dir / "config.json").write_text("{}", encoding="utf-8")

        res = self.detector.detect(self.temp_dir)
        self.assertTrue(res.is_related)
        self.assertTrue(res.modification_allowed)
        self.assertIn("Trained Model Artifacts", res.detected_domains)

    def test_detect_unrelated_workspace_locks_memory(self):
        # Create an unrelated static blog or recipe project
        (self.temp_dir / "index.html").write_text("<h1>My Personal Blog</h1>", encoding="utf-8")
        (self.temp_dir / "style.css").write_text("body { color: red; }", encoding="utf-8")
        (self.temp_dir / "recipes.md").write_text("# Chocolate Cake Recipe", encoding="utf-8")

        res = self.detector.detect(self.temp_dir)
        self.assertFalse(res.is_related)
        self.assertFalse(res.modification_allowed)
        self.assertEqual(res.confidence, 0.0)
        self.assertEqual(res.project_type, "Unrelated / Non-Technical Project")
        self.assertIn("LOCKED", res.summary)


class TestConditionalMemoryModification(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.db_path = self.temp_dir / "test_mentor.db"

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _get_row_count(self, table_name: str) -> int:
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cur.fetchone()[0]
        conn.close()
        return count

    def test_memory_store_mutation_locked_blocks_all_writes(self):
        store = MemoryStore(self.db_path, mutation_allowed=False)
        self.assertFalse(store.is_mutation_allowed())

        # Attempt to write to all tables
        store.update_profile(UserProfile("u1", "Test Learner"))
        store.record_knowledge_assessment("ML", "Backpropagation", True)
        store.record_misconception("Overfitting", "High bias instead of variance")
        store.log_decision("Architecture choice", ["A", "B"], "A", "Rationale")
        store.log_experiment("Exp1", "Hypo", "Base", "Var", "Met")
        store.log_scaffolding_interaction("Explain LoRA", 3, False)
        store.log_project("Vision Transformer", "PyTorch", "ViT arch", "AdamW", "Good lr")
        store.log_feedback("Context", "Feedback", "prompt")
        store.record_component_version("prompt", "ML_Architect", "1.1.0", "hash123", "Bump")

        # Verify 0 rows written across all tables
        self.assertEqual(self._get_row_count("user_profile"), 0)
        self.assertEqual(self._get_row_count("knowledge_state"), 0)
        self.assertEqual(self._get_row_count("misconception_memory"), 0)
        self.assertEqual(self._get_row_count("decision_memory"), 0)
        self.assertEqual(self._get_row_count("experiment_memory"), 0)
        self.assertEqual(self._get_row_count("scaffolding_log"), 0)
        self.assertEqual(self._get_row_count("project_memory"), 0)
        self.assertEqual(self._get_row_count("feedback_log"), 0)
        self.assertEqual(self._get_row_count("component_versions"), 0)

    def test_memory_store_mutation_allowed_persists_writes(self):
        store = MemoryStore(self.db_path, mutation_allowed=True)
        self.assertTrue(store.is_mutation_allowed())

        store.get_or_create_profile("learner_1", "Senior AI Engineer")
        store.record_knowledge_assessment("Machine Learning", "Backpropagation", True)
        store.log_decision("Model Choice", ["CNN", "ViT"], "ViT", "Self-attention benefits")

        self.assertGreaterEqual(self._get_row_count("user_profile"), 1)
        self.assertGreaterEqual(self._get_row_count("knowledge_state"), 1)
        self.assertGreaterEqual(self._get_row_count("decision_memory"), 1)


class TestOrchestratorProjectContextIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.ai_workspace = self.temp_dir / "ai_project"
        self.ai_workspace.mkdir()
        (self.ai_workspace / "requirements.txt").write_text("torch\ntransformers\n", encoding="utf-8")

        self.unrelated_workspace = self.temp_dir / "recipe_blog"
        self.unrelated_workspace.mkdir()
        (self.unrelated_workspace / "index.html").write_text("<h1>Recipes</h1>", encoding="utf-8")

        self.mentor_config = MentorConfig(db_path=self.temp_dir / "mentor_memory.db")

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_orchestrator_in_ai_workspace(self):
        orch = Orchestrator(config=self.mentor_config, workspace_dir=self.ai_workspace)
        self.assertTrue(orch.project_context.is_related)
        self.assertTrue(orch.store.is_mutation_allowed())
        self.assertIsNotNone(orch.retrieved_progress)

        # Query process logs interaction
        resp = orch.process_query("How does gradient checkpointing reduce VRAM in PyTorch?")
        self.assertFalse(resp.is_rejected)
        self.assertIsNotNone(resp.project_context)
        self.assertTrue(resp.project_context.is_related)

        # Scaffolding interaction was written to memory
        conn = sqlite3.connect(str(self.mentor_config.db_path))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM scaffolding_log")
        self.assertGreaterEqual(cur.fetchone()[0], 1)
        conn.close()

    def test_orchestrator_in_unrelated_workspace(self):
        # Create a clean DB for unrelated workspace test
        clean_db = self.temp_dir / "unrelated_mentor.db"
        orch = Orchestrator(config=MentorConfig(db_path=clean_db), workspace_dir=self.unrelated_workspace)
        self.assertFalse(orch.project_context.is_related)
        self.assertFalse(orch.store.is_mutation_allowed())
        self.assertIsNone(orch.retrieved_progress)

        # Query process answers query but DOES NOT write to scaffolding_log
        resp = orch.process_query("What is backpropagation in neural networks?")
        self.assertFalse(resp.is_rejected)
        self.assertIsNotNone(resp.project_context)
        self.assertFalse(resp.project_context.is_related)

        # Verify zero rows written to scaffolding_log or any memory table
        conn = sqlite3.connect(str(clean_db))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM scaffolding_log")
        self.assertEqual(cur.fetchone()[0], 0)
        cur.execute("SELECT COUNT(*) FROM user_profile")
        self.assertEqual(cur.fetchone()[0], 0)
        conn.close()

    def test_context_command(self):
        orch = Orchestrator(config=self.mentor_config, workspace_dir=self.ai_workspace)
        resp = orch.process_query("/context")
        self.assertEqual(resp.command_mode, "context")
        self.assertIn("Project Context Inspection", resp.scaffold.content)
        self.assertIn("RETRIEVED & MODIFICATIONS AUTHORIZED", resp.scaffold.content)
        self.assertTrue(resp.project_context.is_related)


if __name__ == "__main__":
    unittest.main()
