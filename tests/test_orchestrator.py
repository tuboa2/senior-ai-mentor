"""Unit tests for the end-to-end Orchestrator engine."""

import unittest
from pathlib import Path
import tempfile
from senior_mentor.config import MentorConfig
from senior_mentor.orchestrator import Orchestrator

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "orchestrator_test.db"
        self.log_path = Path(self.temp_dir.name) / "audit.jsonl"
        self.cfg = MentorConfig(db_path=self.db_path, audit_log_path=self.log_path)
        self.orchestrator = Orchestrator(self.cfg)

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_parse_slash_commands(self):
        cmd, clean = self.orchestrator.parse_command("/solve implement flash attention")
        self.assertEqual(cmd, "solve")
        self.assertEqual(clean, "implement flash attention")

        cmd2, clean2 = self.orchestrator.parse_command("regular query without slash")
        self.assertIsNone(cmd2)
        self.assertEqual(clean2, "regular query without slash")

    def test_end_to_end_solve_query(self):
        resp = self.orchestrator.process_query("/solve How to calculate eigenvalues?")
        self.assertEqual(resp.command_mode, "solve")
        self.assertEqual(resp.scaffold.level, 0)
        self.assertEqual(resp.scaffold.tier, "Direct Guidance")

    def test_end_to_end_council_tradeoff(self):
        resp = self.orchestrator.process_query("/council Should we use Spark or DuckDB for 50GB analytics?")
        self.assertIsNotNone(resp.debate_synthesis)
        self.assertTrue(resp.debate_synthesis.has_unresolved_disagreement)
        self.assertIn("DuckDB", str(resp.debate_synthesis.positions))

    def test_learner_status_generation(self):
        status = self.orchestrator.get_learner_status()
        self.assertIn("profile", status)
        self.assertIn("overall_score", status)
        self.assertIn("competency_tier", status)
        self.assertGreater(len(status["dimension_scores"]), 0)

if __name__ == "__main__":
    unittest.main()
