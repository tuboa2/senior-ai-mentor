"""Visual Architecture & Excalidraw Diagramming Engine for Senior AI Mentor.

Generates serene, beautiful, harmonious Excalidraw visual diagrams with
full Markdown formatting, KaTeX/LaTeX mathematical formulas, and cognitive ease.
"""

from .excalidraw import (
    ExcalidrawDiagram,
    ExcalidrawElement,
    ZenPalette,
    ExcalidrawTheme
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
    "ExcalidrawElement",
    "ZenPalette",
    "ExcalidrawTheme",
    "DiagramTemplateRegistry",
    "get_diagram_for_concept",
    "VisualMentor",
    "VisualDiagramResult"
]
