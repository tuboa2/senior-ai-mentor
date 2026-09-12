"""Visual Mentor Generator: Orchestrates beautiful Excalidraw creation.

Combines LaTeX/KaTeX mathematics, hierarchical mind map design, file persistence,
and serene Markdown responses.
"""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Optional

from .excalidraw import MindmapExcalidrawBuilder
from .templates import get_diagram_for_concept


@dataclass
class VisualDiagramResult:
    concept: str
    title: str
    diagram: MindmapExcalidrawBuilder
    markdown_content: str
    json_content: str
    md_path: Path
    raw_path: Path
    summary_markdown: str


class VisualMentor:
    """Orchestrates creation of beautiful, serene Excalidraw files."""

    def __init__(self, workspace_dir: Optional[Path] = None):
        self.workspace_dir = Path(workspace_dir).resolve() if workspace_dir else Path.cwd()

    def _slugify(self, text: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
        return slug or "excalidraw_diagram"

    def generate(
        self,
        query: str,
        concept_name: Optional[str] = None,
        target_dir: Optional[Path] = None
    ) -> VisualDiagramResult:
        """Generates an Excalidraw diagram, writes files, and returns Markdown."""
        clean_query = query.replace("/draw", "").replace("/diagram", "").strip()
        effective_concept = concept_name or clean_query or "System Architecture"

        diagram = get_diagram_for_concept(clean_query, concept_name)

        out_dir = Path(target_dir).resolve() if target_dir else (self.workspace_dir / "diagrams")
        base_slug = self._slugify(effective_concept)

        md_path, raw_path = diagram.save(out_dir, base_slug)
        md_text = diagram.to_obsidian_markdown()
        json_text = diagram.to_json(indent=2)
        display_title = diagram.data.root_title.replace("\n", " ")

        summary_lines = [
            f"### 🎨 [Excalidraw Visual Mind Map: {display_title}]",
            "",
            "---",
            "",
            "#### 🌿 1. Concept Intuition & Mental Model",
            diagram.data.intuition_markdown.strip(),
            "",
            "---",
            "",
            "#### 📐 2. Mathematical Foundations (LaTeX / KaTeX)",
            diagram.data.math_katex_markdown.strip(),
            "",
            "---",
            "",
            "#### 🗺️ 3. Mind Map & Architecture Decomposition",
            f"**Libraries:** {', '.join(f'`{lib}`' for lib in diagram.data.libraries)}",
            "",
            "**Methods & Implementations:**",
        ]

        for m in diagram.data.methods:
            summary_lines.append(f"- **{m.name}:**")
            for op in m.operations:
                summary_lines.append(f"  • `{op.code}`: {op.explanation}")
            if m.synthesis_callout:
                summary_lines.append(f"  👉 *Synthesis:* {m.synthesis_callout}")

        summary_lines.extend([
            "",
            f"**End-to-End Pipeline:** {' ➔ '.join(f'`{s}`' for s in diagram.data.pipeline_steps)}",
            "",
            "---",
            "",
            "#### 💾 Generated Excalidraw Files",
            f"- **Obsidian-Ready Excalidraw Markdown:** [{md_path.name}](file://{md_path.as_posix()})",
            f"- **Raw Excalidraw Canvas JSON:** [{raw_path.name}](file://{raw_path.as_posix()})",
            "",
            "> 💡 **How to view:**",
            "> 1. **In Obsidian:** Open with the *Obsidian-Excalidraw plugin* for interactive visual editing.",
            "> 2. **In Browser:** Drag and drop the `.excalidraw` file directly into [excalidraw.com](https://excalidraw.com).",
            "> 3. **In VS Code / Antigravity IDE:** Open with the *Excalidraw extension* for instant rendering.",
            "",
            "---",
            "",
            "#### 💡 Senior Engineering & Performance Takeaways",
            diagram.data.engineering_insights_markdown.strip()
        ])

        summary_md = "\n".join(summary_lines)

        return VisualDiagramResult(
            concept=effective_concept,
            title=display_title,
            diagram=diagram,
            markdown_content=md_text,
            json_content=json_text,
            md_path=md_path,
            raw_path=raw_path,
            summary_markdown=summary_md
        )
