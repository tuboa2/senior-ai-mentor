"""Unit tests validating fixes for real user conversation flaws discovered in Antigravity transcripts.

Covers:
1. ScopeGuard false positive eradication (greetings, confusion, next steps, /mentor queries).
2. Debate trigger fix (eradicating raw "or" substring matching).
3. Concept matching, dynamic knowledge state progression, and competency score growth.
4. Actionable micro-task scaffolding on cognitive overload / confusion.
5. CLI --json programmatic consumption support.
"""

import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from senior_mentor.config import MentorConfig
from senior_mentor.knowledge.graph import KnowledgeGraph
from senior_mentor.orchestrator import Orchestrator
from senior_mentor.pedagogy.scope_guard import ScopeGuard
from senior_mentor.pedagogy.scaffolding import ScaffoldingEngine
from senior_mentor.cli import MentorCLI

class TestRealConversationsFixes(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_mentor.db"
        self.cfg = MentorConfig(db_path=self.db_path)
        self.orchestrator = Orchestrator(self.cfg)
        # Ensure mutations are permitted for tests
        self.orchestrator.project_context.is_related = True
        self.orchestrator.store.set_mutation_allowed(True)
        self.guard = ScopeGuard()
        self.graph = KnowledgeGraph()

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    # --- Test Flaw 1: ScopeGuard False Positives ---
    def test_scope_guard_conversational_and_workflow_queries(self):
        """Verify that real workflow queries from users are NOT falsely rejected."""
        valid_workflow_queries = [
            "/mentor I am now confused, give me the very first task to do.",
            "/mentor Hello!",
            "/mentor where do I start with this project?",
            "/mentor What is my first step?",
            "Where do I begin with data preprocessing?",
            "I am now confused, what should I do first?",
            "Can you review my script and give me feedback?",
            "How should we structure the training pipeline?",
            "Also if there is nulls, should we drop it or investigate it if signals persists?",
            "What about missing values in tabular features?",
            "Hello mentor",
            "Hi"
        ]
        for q in valid_workflow_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertTrue(res.is_in_scope, f"Query falsely rejected: '{q}', reason: {res.reason}")

    def test_scope_guard_still_rejects_genuine_out_of_scope(self):
        """Verify that genuine out-of-scope non-engineering queries are still strictly isolated."""
        bad_queries = [
            "How to bake a chocolate cake",
            "Write me a bedtime poem about dragons",
            "Who won the Super Bowl?",
            "Diagnose my fever and prescribe antibiotics",
            "/solve how to cook delicious pasta"
        ]
        for q in bad_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertFalse(res.is_in_scope, f"Should reject out-of-scope query: '{q}'")

    # --- Test Flaw 2: Accidental Debate Triggering ("or" substring bug) ---
    def test_accidental_debate_not_triggered_by_or_substrings(self):
        """Words containing 'or' or non-comparative sentences must NOT trigger unsolicited debates."""
        queries_with_or_substrings = [
            "How to use torch DataLoader for batches?",
            "What is the best error handling pattern in Python?",
            "How does vector store indexing work?",
            "Explain forward pass in transformers",
            "/mentor What should we do about nulls or missing data?"
        ]
        for q in queries_with_or_substrings:
            with self.subTest(query=q):
                resp = self.orchestrator.process_query(q)
                self.assertIsNone(resp.debate_synthesis, f"Unsolicited debate triggered for: '{q}'")

    def test_debate_still_triggers_on_explicit_council_or_comparisons(self):
        """Explicit /council or comparative queries must still trigger debate."""
        comp_queries = [
            "/council DuckDB vs Apache Spark",
            "Clean Architecture vs Hexagonal Architecture for microservices",
            "Which is better LoRA or full fine-tuning for 7B models?"
        ]
        for q in comp_queries:
            with self.subTest(query=q):
                resp = self.orchestrator.process_query(q)
                self.assertIsNotNone(resp.debate_synthesis, f"Debate should have triggered for: '{q}'")

    # --- Test Flaw 3: Concept Matching & Dynamic Knowledge State Updates ---
    def test_natural_language_concept_matching(self):
        """Knowledge graph search matches concepts from natural language sentences."""
        matches_leakage = self.graph.search("How do I split SPY data without temporal leakage?")
        self.assertTrue(len(matches_leakage) > 0)
        self.assertIn("Data Leakage", matches_leakage[0].name)

        matches_duckdb = self.graph.search("DuckDB vs Spark for analytical workloads")
        self.assertTrue(len(matches_duckdb) > 0)
        self.assertIn("DuckDB", matches_duckdb[0].name)

        matches_eda = self.graph.search("Should I drop nulls or investigate if signal persists?")
        self.assertTrue(len(matches_eda) > 0)
        self.assertIn("Exploratory Data Analysis", matches_eda[0].name)

    def test_knowledge_state_and_competency_growth(self):
        """Interacting with concepts dynamically logs attempts and increases competency score."""
        initial_status = self.orchestrator.get_learner_status()
        self.assertEqual(initial_status["knowledge_count"], 0)
        self.assertEqual(initial_status["overall_score"], 5.0)

        # Process a query that engages with data leakage
        self.orchestrator.process_query("How to implement time-series cross-validation without data leakage?")

        updated_status = self.orchestrator.get_learner_status()
        self.assertGreater(updated_status["knowledge_count"], 0, "Knowledge concept should be tracked!")
        self.assertGreater(updated_status["overall_score"], 5.0, "Competency score should have increased!")

    # --- Test Flaw 4: Actionable Micro-Tasks on Confusion ---
    def test_cognitive_deescalation_on_confusion(self):
        """Queries expressing confusion or asking for first steps receive an Actionable Micro-Task."""
        resp = self.orchestrator.process_query("/mentor I am now confused, give me the very first task to do.")
        self.assertEqual(resp.scaffold.level, 4)
        self.assertEqual(resp.scaffold.level_name, "Actionable Micro-Task")
        self.assertIn("Concrete Step 1 of 1", resp.scaffold.content)
        self.assertIn("Step 1 Focus", resp.scaffold.content)

    def test_greeting_orientation_scaffold(self):
        """Greetings yield welcoming mentor orientation rather than errors."""
        resp = self.orchestrator.process_query("/mentor Hello!")
        self.assertEqual(resp.scaffold.level_name, "Mentor Orientation")
        self.assertIn("Online and ready to pair program", resp.scaffold.content)

    # --- Test Flaw 5: CLI JSON output serialization ---
    def test_cli_json_status_output(self):
        """CLI status format supports clean JSON without serialization crashes."""
        st = self.orchestrator.get_learner_status()
        json_obj = {
            "user_id": st["profile"].user_id,
            "overall_score": st["overall_score"],
            "dimension_scores": [{"name": ds.name, "score": ds.score} for ds in st["dimension_scores"]],
            "knowledge_concepts_tracked": st["knowledge_count"]
        }
        serialized = json.dumps(json_obj)
        deserialized = json.loads(serialized)
        self.assertEqual(deserialized["user_id"], "default_user")

if __name__ == "__main__":
    unittest.main()
