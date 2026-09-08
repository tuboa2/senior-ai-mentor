"""Unit tests for Expert Council deliberation and the Disagreement Protocol."""

import unittest
from senior_mentor.council.experts import PERMANENT_EXPERTS, spawn_dynamic_specialist
from senior_mentor.council.debate import DebateEngine

class TestCouncilDebate(unittest.TestCase):
    def setUp(self):
        self.engine = DebateEngine()

    def test_expert_selection_heuristics(self):
        experts = self.engine.select_relevant_experts("How to detect temporal data leakage in cross-validation splits?")
        names = [e.role_id for e in experts]
        self.assertIn("statistician", names)
        self.assertIn("red_team_adversary", names)

    def test_performance_query_expert_selection(self):
        experts = self.engine.select_relevant_experts("Optimizing GPU CUDA kernels and tensor memory bandwidth")
        names = [e.role_id for e in experts]
        self.assertIn("performance_engineer", names)

    def test_disagreement_protocol_on_tradeoff(self):
        # Query with competing trade-offs
        synthesis = self.engine.deliberate("Should we use XGBoost vs Deep Neural Nets for tabular click-through rate prediction?")
        self.assertTrue(synthesis.has_unresolved_disagreement)
        self.assertIsNotNone(synthesis.conflict_statement)
        self.assertIsNotNone(synthesis.uncertainty_statement)
        self.assertIsNotNone(synthesis.experiment_design)
        self.assertIn("which architecture would you choose", synthesis.escalation_question)
        self.assertIsNone(synthesis.consensus_summary)

    def test_consensus_on_clear_implementation(self):
        synthesis = self.engine.deliberate("Refactor this python function to include typing annotations and remove bare excepts.")
        self.assertFalse(synthesis.has_unresolved_disagreement)
        self.assertIsNotNone(synthesis.consensus_summary)

    def test_dynamic_specialist_spawning(self):
        specialist = spawn_dynamic_specialist("Graph ML", "Graph Convolutional Networks and Message Passing")
        self.assertEqual(specialist.name, "Graph ML Specialist")
        self.assertIn("specialist_graph_ml", specialist.role_id)
        self.assertIn("Message Passing", specialist.focus_domain)

if __name__ == "__main__":
    unittest.main()
