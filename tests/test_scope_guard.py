"""Unit tests for the ScopeGuard and strict memory isolation of out-of-scope queries."""

import unittest
from pathlib import Path
import sqlite3
import tempfile
from senior_mentor.config import MentorConfig
from senior_mentor.orchestrator import Orchestrator
from senior_mentor.pedagogy.scope_guard import ScopeGuard, ScopeCheckResult
from senior_mentor.self_improvement.feedback import AutonomousSelfImprovementEngine

class TestScopeGuard(unittest.TestCase):
    def setUp(self):
        self.guard = ScopeGuard()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_scope_isolation.db"
        self.cfg = MentorConfig(db_path=self.db_path)
        self.orchestrator = Orchestrator(self.cfg)

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_in_scope_technical_queries(self):
        technical_queries = [
            "How does LoRA fine-tuning reduce memory consumption?",
            "Explain multi-head attention mechanism and key-value projections",
            "What is homoscedasticity and how to test for it in regression?",
            "Derive SVD and explain eigenvectors of covariance matrices",
            "Clean architecture vs hexagonal architecture in Python services",
            "Should we use DuckDB or Apache Spark for 50GB analytical queries?",
            "How to deploy vLLM with speculative decoding on Triton inference server?",
            "Implement binary search tree traversal and evaluate time complexity",
            "/solve How to compute eigenvalues?",
            "/status",
            "/skills",
            "/refine",
            "/interview system_design"
        ]
        for q in technical_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertTrue(res.is_in_scope, f"Expected in-scope for: '{q}', got reason: {res.reason}")

    def test_in_scope_technical_queries_with_domain_entities(self):
        # Queries that mention food or recipes as software domain entities
        domain_entity_queries = [
            "Design a PostgreSQL database schema for storing recipes and ingredients",
            "Write a Python script to scrape recipe data from a culinary website",
            "Build a machine learning recommendation system for recipe suggestions",
            "Unit testing a FastAPI backend for an online restaurant menu service"
        ]
        for q in domain_entity_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertTrue(res.is_in_scope, f"Expected in-scope for technical entity query: '{q}'")

    def test_out_of_scope_culinary_queries(self):
        culinary_queries = [
            "How to bake a chocolate cake",
            "Give me a recipe for blueberry pancakes",
            "What spices go into a delicious chicken soup?",
            "How do I roast a steak in the oven?",
            "/solve how to bake bread"
        ]
        for q in culinary_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertFalse(res.is_in_scope, f"Expected out-of-scope for: '{q}'")
                self.assertIn("culinary", res.reason.lower())
                self.assertIn("MEMORY ISOLATION ENFORCED", res.rejection_message)

    def test_out_of_scope_creative_writing(self):
        creative_queries = [
            "Write me a poem about the sunrise",
            "Write a story about a magical dragon",
            "Write lyrics for a pop song",
            "Write me a poem about machine learning"
        ]
        for q in creative_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertFalse(res.is_in_scope, f"Expected out-of-scope for: '{q}'")
                self.assertIn("creative", res.reason.lower())

    def test_out_of_scope_sports_and_celebrities(self):
        sports_queries = [
            "Who won the 2022 world cup?",
            "Tell me about LeBron James NBA stats",
            "What is the latest celebrity gossip about Taylor Swift?",
            "Who will win the Super Bowl?"
        ]
        for q in sports_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertFalse(res.is_in_scope, f"Expected out-of-scope for: '{q}'")

    def test_out_of_scope_medical_and_legal(self):
        medical_legal_queries = [
            "What medicine should I take for a high fever and headache?",
            "Diagnose my stomach ache symptoms",
            "How to sue my landlord for wrongful eviction",
            "What is my horoscope for Gemini today?"
        ]
        for q in medical_legal_queries:
            with self.subTest(query=q):
                res = self.guard.check_scope(q)
                self.assertFalse(res.is_in_scope, f"Expected out-of-scope for: '{q}'")

    def test_strict_memory_isolation_on_rejected_queries(self):
        """Verifies that out-of-scope queries cause ZERO database writes."""
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()

        # Check initial counts
        def get_table_counts():
            c_scaff = cur.execute("SELECT COUNT(*) FROM scaffolding_log").fetchone()[0]
            c_know = cur.execute("SELECT COUNT(*) FROM knowledge_state").fetchone()[0]
            c_dec = cur.execute("SELECT COUNT(*) FROM decision_memory").fetchone()[0]
            c_misc = cur.execute("SELECT COUNT(*) FROM misconception_memory").fetchone()[0]
            c_feed = cur.execute("SELECT COUNT(*) FROM feedback_log").fetchone()[0]
            return c_scaff, c_know, c_dec, c_misc, c_feed

        self.assertEqual(get_table_counts(), (0, 0, 0, 0, 0))

        # Send multiple out-of-scope queries through the orchestrator
        rejected_inputs = [
            "How to bake a chocolate cake",
            "Write me a poem about flowers",
            "Who won the 2022 World Cup?",
            "What medicine should I take for a headache?",
            "/solve how to cook delicious pasta"
        ]

        for q in rejected_inputs:
            resp = self.orchestrator.process_query(q)
            self.assertTrue(resp.is_rejected, f"Query '{q}' should have been marked is_rejected=True")
            self.assertEqual(resp.scaffold.level, -1)
            self.assertIn("MEMORY ISOLATION ENFORCED", resp.scaffold.content)

        # Database tables MUST STILL HAVE ZERO ROWS!
        self.assertEqual(get_table_counts(), (0, 0, 0, 0, 0), "Out-of-scope queries caused unauthorized database writes!")

        # Verify record_user_decision rejects out-of-scope context
        dec_res = self.orchestrator.record_user_decision(
            context="Baking chocolate cake vs baking vanilla cake",
            options=["chocolate", "vanilla"],
            chosen="chocolate",
            rationale="richer flavor profile"
        )
        self.assertEqual(dec_res["judgment_score"], 0.0)
        self.assertIn("Rejected", dec_res["mentor_verdict"])
        self.assertEqual(cur.execute("SELECT COUNT(*) FROM decision_memory").fetchone()[0], 0)

        # Verify feedback engine rejects out-of-scope correction
        self_imp = AutonomousSelfImprovementEngine(self.orchestrator.store)
        success = self_imp.capture_correction(
            context="baking apple pie in the oven",
            user_correction="add cinnamon and sugar"
        )
        self.assertFalse(success)
        self.assertEqual(cur.execute("SELECT COUNT(*) FROM feedback_log").fetchone()[0], 0)

        # Now execute a legitimate in-scope query
        valid_resp = self.orchestrator.process_query("/solve How to calculate eigenvalues of a matrix?")
        self.assertFalse(valid_resp.is_rejected)
        self.assertEqual(valid_resp.scaffold.level, 0)

        # Scaffolding log should now have exactly 1 record
        c_scaff, _, _, _, _ = get_table_counts()
        self.assertEqual(c_scaff, 1)

        conn.close()

if __name__ == "__main__":
    unittest.main()
