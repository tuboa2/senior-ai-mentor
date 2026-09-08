"""Unit tests for the AI/ML Knowledge Graph."""

import unittest
from senior_mentor.knowledge.graph import KnowledgeGraph, ConceptNode

class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.graph = KnowledgeGraph()

    def test_node_retrieval(self):
        concept = self.graph.get_concept("Principal Component Analysis")
        self.assertIsNotNone(concept)
        self.assertEqual(concept.domain, "Machine Learning")
        self.assertIn("Linear Algebra: Eigenvectors & SVD", concept.prerequisites)

    def test_prerequisite_traversal(self):
        prereqs = self.graph.get_prerequisites_recursive("Retrieval-Augmented Generation (RAG)")
        prereq_names = [p.name for p in prereqs]
        self.assertIn("Transformer Architecture & Attention", prereq_names)
        self.assertIn("Backpropagation & Autograd Mechanics", prereq_names)
        self.assertIn("Gradient Descent & Convex Optimization", prereq_names)

    def test_gap_identification(self):
        # User has zero proficiency in Linear Algebra
        proficiencies = {
            "backpropagation & autograd mechanics": 0.8,
            "gradient descent & convex optimization": 0.8
        }
        gaps = self.graph.identify_knowledge_gaps("Transformer Architecture & Attention", proficiencies, threshold=0.6)
        gap_names = [g.name for g in gaps]
        self.assertIn("Linear Algebra: Eigenvectors & SVD", gap_names)

    def test_concept_search(self):
        results = self.graph.search("leakage")
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0].name, "Data Leakage & Cross-Validation Strategy")

if __name__ == "__main__":
    unittest.main()
