"""Comprehensive test suite for the Excalidraw Visual Diagramming Engine."""

import json
from pathlib import Path
import tempfile
import unittest

from senior_mentor.visuals.excalidraw import (
    ExcalidrawDiagram,
    ExcalidrawElement,
    ZenPalette
)
from senior_mentor.visuals.templates import (
    DiagramTemplateRegistry,
    get_transformer_attention_diagram,
    get_backpropagation_diagram,
    get_diffusion_model_diagram,
    get_rag_architecture_diagram,
    get_resnet_residual_block_diagram,
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

    def test_element_serialization_and_json_validity(self):
        diag = ExcalidrawDiagram(
            title="Unit Test Architecture",
            concept="Testing Concept",
            intuition="Mental model intuition.",
            math_katex="$$f(x) = W x + b$$"
        )
        c1 = diag.add_zen_card(
            x=100, y=100, width=200, height=120,
            title="Component 1",
            subtitle="Test Sub",
            latex_formula="z = W a + b",
            step_badge="Stage 1",
            theme="azure"
        )
        c2 = diag.add_zen_card(
            x=350, y=100, width=200, height=120,
            title="Component 2",
            subtitle="Output",
            latex_formula="a = \\sigma(z)",
            step_badge="Stage 2",
            theme="sage"
        )
        diag.add_flow_arrow(c1, c2, label="Activations")

        raw_json = diag.to_json()
        parsed = json.loads(raw_json)

        self.assertEqual(parsed["type"], "excalidraw")
        self.assertEqual(parsed["version"], 2)
        self.assertIn("elements", parsed)
        self.assertGreater(len(parsed["elements"]), 4)
        self.assertEqual(parsed["appState"]["viewBackgroundColor"], ZenPalette.CANVAS_BG)

    def test_obsidian_markdown_formatting_with_katex(self):
        diag = get_transformer_attention_diagram()
        md_text = diag.to_markdown()

        # Check Obsidian frontmatter
        self.assertIn("excalidraw-plugin: parsed", md_text)
        self.assertIn("tags: [excalidraw, senior-ai-mentor, architecture]", md_text)

        # Check KaTeX mathematical equations
        self.assertIn("$$\\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V})", md_text)
        self.assertIn("\\text{softmax}", md_text)
        self.assertIn("\\sqrt{d_k}", md_text)

        # Check drawing block embedding
        self.assertIn("%%", md_text)
        self.assertIn("# Drawing", md_text)
        self.assertIn('"type": "excalidraw"', md_text)

    def test_dual_file_persistence(self):
        diag = get_rag_architecture_diagram()
        out_dir = self.temp_path / "diagrams"
        md_file, raw_file = diag.save(out_dir, "test_rag")

        self.assertTrue(md_file.exists())
        self.assertTrue(raw_file.exists())
        self.assertTrue(md_file.name.endswith(".excalidraw.md"))
        self.assertTrue(raw_file.name.endswith(".excalidraw"))

        # Verify raw file is valid Excalidraw JSON
        content_json = json.loads(raw_file.read_text(encoding="utf-8"))
        self.assertEqual(content_json["type"], "excalidraw")
        self.assertIn("elements", content_json)

    def test_template_registry_routing(self):
        diag_attn = DiagramTemplateRegistry.get_diagram("transformer attention")
        self.assertIn("Attention", diag_attn.title)

        diag_bp = DiagramTemplateRegistry.get_diagram("backpropagation chain rule")
        self.assertIn("Backpropagation", diag_bp.title)

        diag_diff = DiagramTemplateRegistry.get_diagram("diffusion models")
        self.assertIn("Diffusion", diag_diff.title)

        diag_res = DiagramTemplateRegistry.get_diagram("residual skip connection")
        self.assertIn("Residual", diag_res.title)

        diag_custom = DiagramTemplateRegistry.get_diagram("graph neural network message passing")
        self.assertIn("Architecture", diag_custom.title)

    def test_visual_mentor_generator(self):
        vm = VisualMentor(workspace_dir=self.temp_path)
        res = vm.generate("backpropagation")

        self.assertIsNotNone(res)
        self.assertIn("Backpropagation", res.title)
        self.assertTrue(res.md_path.exists())
        self.assertTrue(res.raw_path.exists())
        self.assertIn("file://", res.summary_markdown)
        self.assertIn("Mathematical Foundations", res.summary_markdown)

    def test_orchestrator_draw_command(self):
        orch = Orchestrator(workspace_dir=self.temp_path)
        response = orch.process_query("/draw transformer attention")

        self.assertEqual(response.command_mode, "draw")
        self.assertFalse(response.is_rejected)
        self.assertIn("Excalidraw", response.scaffold.content)
        self.assertIn("Attention", response.scaffold.content)
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
