"""Visual Architecture & Excalidraw Diagramming Engine for Senior AI Mentor.

Generates serene, beautiful, hierarchical Excalidraw concept mind maps with
full Markdown formatting, KaTeX/LaTeX mathematical formulas, and cognitive ease.
"""

from .excalidraw import (
    ExcalidrawDiagram,
    MindmapExcalidrawBuilder,
    MindmapTreeData,
    MindmapMethod,
    MindmapOperation,
    gen_excalidraw_id
)
from .templates import (
    DiagramTemplateRegistry,
    get_diagram_for_concept
)
from .generator import (
    VisualMentor,
    VisualDiagramResult
)

__all__ = [
    "ExcalidrawDiagram",
    "MindmapExcalidrawBuilder",
    "MindmapTreeData",
    "MindmapMethod",
    "MindmapOperation",
    "gen_excalidraw_id",
    "DiagramTemplateRegistry",
    "get_diagram_for_concept",
    "VisualMentor",
    "VisualDiagramResult"
]
