"""Visual Mentor Generator: Orchestrates beautiful Excalidraw creation.

Combines LaTeX/KaTeX mathematics, visual design, file persistence,
and serene Markdown responses.
"""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Optional, Tuple

from .excalidraw import ExcalidrawDiagram
from .templates import get_diagram_for_concept


@dataclass
class VisualDiagramResult:
    concept: str
    title: str
    diagram: ExcalidrawDiagram
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
        base_slug = self._slugify(diagram.concept or effective_concept)

        md_path, raw_path = diagram.save(out_dir, base_slug)
        md_text = diagram.to_markdown()
        json_text = diagram.to_json(indent=2)

        # Construct serene, welcoming chat/terminal presentation
        summary_lines = [
            f"### 🎨 [Excalidraw Visual Architecture: {diagram.title}]",
            f"*{diagram.subtitle}*",
            "",
            "---",
            "",
            "#### 🌿 Intuition & Mental Model",
            diagram.intuition,
            "",
            "---",
            "",
            "#### 📐 Mathematical Foundations (KaTeX / LaTeX)",
            diagram.math_katex,
            "",
            "---",
            "",
            "#### 🗺️ Visual Architecture Map",
            "\n".join(f"{i+1}. {step}" for i, step in enumerate(diagram.walkthrough_steps)),
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
            "#### 💡 Senior Engineering Takeaways",
            "\n".join(f"- {tip}" for tip in diagram.engineering_insights)
        ]

        summary_md = "\n".join(summary_lines)

        return VisualDiagramResult(
            concept=effective_concept,
            title=diagram.title,
            diagram=diagram,
            markdown_content=md_text,
            json_content=json_text,
            md_path=md_path,
            raw_path=raw_path,
            summary_markdown=summary_md
        )
