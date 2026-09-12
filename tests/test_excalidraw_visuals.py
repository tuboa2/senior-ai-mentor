"""Comprehensive test suite for the Excalidraw Visual Mind Map & Architecture Engine."""

import json
from pathlib import Path
import tempfile
import unittest

from senior_mentor.visuals.excalidraw import (
    MindmapExcalidrawBuilder,
    MindmapTreeData,
    MindmapMethod,
    MindmapOperation
)
from senior_mentor.visuals.templates import (
    DiagramTemplateRegistry,
    get_log_return_transformation_diagram,
    get_transformer_attention_diagram,
    get_backpropagation_diagram,
    get_diffusion_model_diagram,
    get_rag_architecture_diagram,
    get_dynamic_diagram
)
from senior_mentor.visuals.generator import VisualMentor
from senior_mentor.orchestrator import Orchestrator
from senior_mentor.pedagogy.scope_guard import ScopeGuard


class TestExcalidrawVisuals(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_log_return_mindmap_structure_and_json_validity(self):
        builder = get_log_return_transformation_diagram()
        raw_json = builder.to_json()
        parsed = json.loads(raw_json)

        self.assertEqual(parsed["type"], "excalidraw")
        self.assertEqual(parsed["version"], 2)
        self.assertEqual(parsed["appState"]["theme"], "dark")
        self.assertIn("elements", parsed)

        # Verify elements have containerId and proper text binding
        rectangles = [e for e in parsed["elements"] if e["type"] == "rectangle"]
        texts = [e for e in parsed["elements"] if e["type"] == "text"]
        arrows = [e for e in parsed["elements"] if e["type"] == "arrow"]

        self.assertGreater(len(rectangles), 15)
        self.assertGreater(len(texts), 15)
        self.assertGreater(len(arrows), 15)

        # Check containerId binding
        for t in texts:
            self.assertIsNotNone(t.get("containerId"))
            # Confirm container exists
            matching_rect = [r for r in rectangles if r["id"] == t["containerId"]]
            self.assertEqual(len(matching_rect), 1)
            # Confirm matching rect binds the text
            bound_types = [b["type"] for b in matching_rect[0]["boundElements"]]
            self.assertIn("text", bound_types)

    def test_obsidian_markdown_formatting_with_katex(self):
        builder = get_transformer_attention_diagram()
        md_text = builder.to_obsidian_markdown()

        # Check Obsidian frontmatter & warning
        self.assertIn("excalidraw-plugin: parsed", md_text)
        self.assertIn("==⚠  Switch to EXCALIDRAW VIEW", md_text)

        # Check KaTeX mathematical equations
        self.assertIn("$$\\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V})", md_text)
        self.assertIn("\\text{softmax}", md_text)
        self.assertIn("\\sqrt{d_k}", md_text)

        # Check Excalidraw Data and Text Elements
        self.assertIn("# Excalidraw Data", md_text)
        self.assertIn("## Text Elements", md_text)
        self.assertIn("^", md_text)  # Block IDs

        # Check embedded drawing block
        self.assertIn("%%", md_text)
        self.assertIn("## Drawing", md_text)
        self.assertIn('"type": "excalidraw"', md_text)

    def test_dual_file_persistence(self):
        builder = get_diffusion_model_diagram()
        out_dir = self.temp_path / "diagrams"
        md_file, raw_file = builder.save(out_dir, "test_diffusion")

        self.assertTrue(md_file.exists())
        self.assertTrue(raw_file.exists())
        self.assertTrue(md_file.name.endswith(".excalidraw.md"))
        self.assertTrue(raw_file.name.endswith(".excalidraw"))

        # Verify raw file is valid Excalidraw JSON
        content_json = json.loads(raw_file.read_text(encoding="utf-8"))
        self.assertEqual(content_json["type"], "excalidraw")
        self.assertIn("elements", content_json)

    def test_template_registry_routing(self):
        diag_log = DiagramTemplateRegistry.get_diagram("log returns transformation")
        self.assertIn("Log-Returns", diag_log.data.root_title)

        diag_attn = DiagramTemplateRegistry.get_diagram("transformer attention")
        self.assertIn("Transformer Attention", diag_attn.data.root_title)

        diag_bp = DiagramTemplateRegistry.get_diagram("backpropagation computational graph")
        self.assertIn("Backpropagation", diag_bp.data.root_title)

        diag_diff = DiagramTemplateRegistry.get_diagram("diffusion models")
        self.assertIn("Diffusion", diag_diff.data.root_title)

        diag_custom = DiagramTemplateRegistry.get_diagram("causal inference DAG")
        self.assertIsNotNone(diag_custom.data.root_title)

    def test_visual_mentor_generator(self):
        vm = VisualMentor(workspace_dir=self.temp_path)
        res = vm.generate("log returns")

        self.assertIsNotNone(res)
        self.assertIn("Log-Returns", res.title)
        self.assertTrue(res.md_path.exists())
        self.assertTrue(res.raw_path.exists())
        self.assertIn("file://", res.summary_markdown)
        self.assertIn("Mathematical Foundations", res.summary_markdown)
        self.assertIn("End-to-End Pipeline", res.summary_markdown)

    def test_orchestrator_draw_command(self):
        orch = Orchestrator(workspace_dir=self.temp_path)
        response = orch.process_query("/draw log returns transformation")

        self.assertEqual(response.command_mode, "draw")
        self.assertFalse(response.is_rejected)
        self.assertIn("Excalidraw", response.scaffold.content)
        self.assertIn("Log-Returns", response.scaffold.content)
        self.assertIn(".excalidraw.md", response.scaffold.content)

    def test_orchestrator_conversational_visual_query(self):
        orch = Orchestrator(workspace_dir=self.temp_path)
        response = orch.process_query("can you draw an excalidraw diagram for diffusion models")

        self.assertEqual(response.command_mode, "draw")
        self.assertFalse(response.is_rejected)
        self.assertIn("Diffusion", response.scaffold.content)

    def test_scope_guard_with_visual_queries(self):
        guard = ScopeGuard()

        # Legitimate technical drawing queries should be in scope
        res_tech1 = guard.check_scope("/draw transformer attention")
        self.assertTrue(res_tech1.is_in_scope)

        res_tech2 = guard.check_scope("/diagram backpropagation computational graph")
        self.assertTrue(res_tech2.is_in_scope)

        res_tech3 = guard.check_scope("draw an excalidraw diagram for RAG architecture")
        self.assertTrue(res_tech3.is_in_scope)

        # Non-technical out-of-scope query should still be rejected!
        res_food = guard.check_scope("/draw a delicious chocolate cake recipe")
        self.assertFalse(res_food.is_in_scope)
        self.assertIn("Culinary", res_food.rejection_message)


if __name__ == "__main__":
    unittest.main()
