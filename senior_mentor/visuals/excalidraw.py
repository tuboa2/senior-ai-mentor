"""Excalidraw Visual Diagram Engine for Senior AI Engineering Mentor.

Produces harmonious, serene Excalidraw diagrams with generous whitespace,
soft pastel palettes, clean typographic hierarchy, and full Obsidian/Markdown
KaTeX mathematical interoperability.
"""

from dataclasses import dataclass, field
import json
from pathlib import Path
import random
import time
from typing import Any, Dict, List, Optional, Tuple
import uuid


class ZenPalette:
    """A calming, harmonious, non-overwhelming color palette for technical architecture."""
    CANVAS_BG = "#fafbfc"
    CANVAS_CONTAINER_BG = "#f8fafd"
    CANVAS_CONTAINER_BORDER = "#cfd8dc"

    # Soft Theme Cards
    AZURE = {
        "name": "azure",
        "bg": "#e8f0fe",
        "stroke": "#1a73e8",
        "text": "#174ea6",
        "label": "Input / Representation"
    }
    SAGE = {
        "name": "sage",
        "bg": "#e6f4ea",
        "stroke": "#1e8e3e",
        "text": "#137333",
        "label": "Computation / Transformation"
    }
    AMBER = {
        "name": "amber",
        "bg": "#fef7e0",
        "stroke": "#f9ab00",
        "text": "#b06000",
        "label": "Weight / Attention / Latent"
    }
    LAVENDER = {
        "name": "lavender",
        "bg": "#f3e8fd",
        "stroke": "#9334e6",
        "text": "#7627bb",
        "label": "Projection / Multi-Head / State"
    }
    CORAL = {
        "name": "coral",
        "bg": "#fce8e6",
        "stroke": "#ea4335",
        "text": "#c5221f",
        "label": "Loss / Gradient / Error"
    }
    SLATE = {
        "name": "slate",
        "bg": "#f1f3f4",
        "stroke": "#80868b",
        "text": "#202124",
        "label": "Memory / Registry / Infrastructure"
    }
    WHITE = {
        "name": "white",
        "bg": "#ffffff",
        "stroke": "#dadce0",
        "text": "#3c4043",
        "label": "Neutral / Container"
    }

    THEMES = {
        "azure": AZURE,
        "blue": AZURE,
        "sage": SAGE,
        "green": SAGE,
        "amber": AMBER,
        "yellow": AMBER,
        "lavender": LAVENDER,
        "purple": LAVENDER,
        "coral": CORAL,
        "red": CORAL,
        "slate": SLATE,
        "gray": SLATE,
        "white": WHITE
    }

    ARROW_FLOW = "#5f6368"
    ARROW_REVERSE = "#ea4335"
    ARROW_ACCENT = "#1a73e8"


class ExcalidrawTheme:
    DEFAULT = "azure"


@dataclass
class ExcalidrawElement:
    """Internal representation of a single Excalidraw scene element."""
    id: str
    element_type: str
    x: float
    y: float
    width: float
    height: float
    stroke_color: str = "#1e1e1e"
    background_color: str = "transparent"
    fill_style: str = "solid"
    stroke_width: float = 1.5
    stroke_style: str = "solid"
    roughness: int = 1
    opacity: int = 100
    roundness: Optional[Dict[str, int]] = field(default_factory=lambda: {"type": 3})
    seed: int = field(default_factory=lambda: random.randint(100000, 999999))
    text: Optional[str] = None
    font_size: int = 18
    font_family: int = 1  # 1 = Virgil (hand-drawn), 2 = Helvetica, 3 = Cascadia (code)
    text_align: str = "center"
    vertical_align: str = "middle"
    points: Optional[List[List[float]]] = None
    start_binding: Optional[Dict[str, Any]] = None
    end_binding: Optional[Dict[str, Any]] = None
    end_arrowhead: Optional[str] = None
    container_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        now_ms = int(time.time() * 1000)
        base: Dict[str, Any] = {
            "id": self.id,
            "type": self.element_type,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "angle": 0,
            "strokeColor": self.stroke_color,
            "backgroundColor": self.background_color,
            "fillStyle": self.fill_style,
            "strokeWidth": self.stroke_width,
            "strokeStyle": self.stroke_style,
            "roughness": self.roughness,
            "opacity": self.opacity,
            "groupIds": [],
            "frameId": None,
            "roundness": self.roundness,
            "seed": self.seed,
            "version": 1,
            "versionNonce": 1,
            "isDeleted": False,
            "boundElements": None,
            "updated": now_ms,
            "link": None,
            "locked": False
        }

        if self.element_type == "text":
            content = self.text or ""
            base.update({
                "text": content,
                "fontSize": self.font_size,
                "fontFamily": self.font_family,
                "textAlign": self.text_align,
                "verticalAlign": self.vertical_align,
                "baseline": int(self.font_size * 0.8),
                "containerId": self.container_id,
                "originalText": content,
                "lineHeight": 1.25
            })

        if self.element_type in ("arrow", "line"):
            base.update({
                "points": self.points or [[0, 0], [self.width, self.height]],
                "lastCommittedPoint": None,
                "startBinding": self.start_binding,
                "endBinding": self.end_binding,
                "startArrowhead": None,
                "endArrowhead": self.end_arrowhead or "arrow"
            })

        return base


class ExcalidrawDiagram:
    """Encapsulates a full Excalidraw scene with Markdown and KaTeX math derivations."""

    def __init__(
        self,
        title: str,
        concept: str,
        subtitle: str = "Architectural & Mathematical Intuition",
        intuition: str = "",
        math_katex: str = "",
        walkthrough_steps: Optional[List[str]] = None,
        engineering_insights: Optional[List[str]] = None
    ):
        self.title = title
        self.concept = concept
        self.subtitle = subtitle
        self.intuition = intuition
        self.math_katex = math_katex
        self.walkthrough_steps = walkthrough_steps or []
        self.engineering_insights = engineering_insights or []
        self.elements: List[ExcalidrawElement] = []
        self._card_registry: Dict[str, Dict[str, Any]] = {}

    def _gen_id(self, prefix: str = "el") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def add_element(self, element: ExcalidrawElement) -> None:
        self.elements.append(element)

    def add_zen_card(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        title: str,
        subtitle: Optional[str] = None,
        latex_formula: Optional[str] = None,
        step_badge: Optional[str] = None,
        theme: str = "azure"
    ) -> str:
        """Adds a soothing, curved aesthetic card with title, formula, and step badge."""
        card_id = self._gen_id("card")
        palette = ZenPalette.THEMES.get(theme.lower(), ZenPalette.AZURE)

        # 1. Main Background Rectangle
        card_elem = ExcalidrawElement(
            id=card_id,
            element_type="rectangle",
            x=x,
            y=y,
            width=width,
            height=height,
            stroke_color=palette["stroke"],
            background_color=palette["bg"],
            fill_style="solid",
            stroke_width=1.5,
            stroke_style="solid",
            roughness=1,
            roundness={"type": 3}
        )
        self.elements.append(card_elem)

        # 2. Step Badge (e.g. [1], [Input], [Attention])
        if step_badge:
            badge_id = self._gen_id("badge")
            badge_w = 40 + len(step_badge) * 8
            badge_rect = ExcalidrawElement(
                id=f"{badge_id}_bg",
                element_type="rectangle",
                x=x + 12,
                y=y + 10,
                width=badge_w,
                height=22,
                stroke_color=palette["stroke"],
                background_color="#ffffff",
                fill_style="solid",
                stroke_width=1.0,
                roundness={"type": 3}
            )
            self.elements.append(badge_rect)

            badge_txt = ExcalidrawElement(
                id=f"{badge_id}_txt",
                element_type="text",
                x=x + 16,
                y=y + 12,
                width=badge_w - 8,
                height=18,
                stroke_color=palette["text"],
                text=step_badge,
                font_size=13,
                font_family=3,  # Code font
                text_align="center",
                vertical_align="middle"
            )
            self.elements.append(badge_txt)

        # 3. Card Title
        title_y = y + (36 if step_badge else 16)
        title_elem = ExcalidrawElement(
            id=self._gen_id("title"),
            element_type="text",
            x=x + 12,
            y=title_y,
            width=width - 24,
            height=26,
            stroke_color=palette["text"],
            text=title,
            font_size=18,
            font_family=1,
            text_align="center",
            vertical_align="middle"
        )
        self.elements.append(title_elem)

        # 4. Optional Subtitle
        curr_y = title_y + 28
        if subtitle:
            sub_elem = ExcalidrawElement(
                id=self._gen_id("sub"),
                element_type="text",
                x=x + 12,
                y=curr_y,
                width=width - 24,
                height=20,
                stroke_color="#5f6368",
                text=subtitle,
                font_size=14,
                font_family=1,
                text_align="center",
                vertical_align="middle"
            )
            self.elements.append(sub_elem)
            curr_y += 24

        # 5. Optional Mathematical / LaTeX Formula Pill
        if latex_formula:
            pill_w = width - 28
            pill_h = 32
            pill_x = x + 14
            pill_y = y + height - pill_h - 12

            pill_bg = ExcalidrawElement(
                id=self._gen_id("formula_bg"),
                element_type="rectangle",
                x=pill_x,
                y=pill_y,
                width=pill_w,
                height=pill_h,
                stroke_color="#dadce0",
                background_color="#ffffff",
                fill_style="solid",
                stroke_width=1.0,
                roundness={"type": 3}
            )
            self.elements.append(pill_bg)

            # KaTeX / LaTeX format representation in Excalidraw text
            formula_elem = ExcalidrawElement(
                id=self._gen_id("formula_txt"),
                element_type="text",
                x=pill_x + 6,
                y=pill_y + 6,
                width=pill_w - 12,
                height=20,
                stroke_color="#202124",
                text=latex_formula,
                font_size=13,
                font_family=3,  # Code font
                text_align="center",
                vertical_align="middle"
            )
            self.elements.append(formula_elem)

        self._card_registry[card_id] = {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "center_x": x + width / 2,
            "center_y": y + height / 2,
            "theme": theme
        }
        return card_id

    def add_flow_arrow(
        self,
        from_card_id: str,
        to_card_id: str,
        label: Optional[str] = None,
        style: str = "solid",
        color: Optional[str] = None
    ) -> str:
        """Connects two cards with a smooth, perfectly routed arrow and optional label."""
        arrow_id = self._gen_id("arrow")
        card_from = self._card_registry.get(from_card_id)
        card_to = self._card_registry.get(to_card_id)

        if not card_from or not card_to:
            return ""

        # Determine relative orientation (horizontal or vertical)
        dx = card_to["center_x"] - card_from["center_x"]
        dy = card_to["center_y"] - card_from["center_y"]

        if abs(dx) >= abs(dy):
            # Horizontal flow
            if dx > 0:
                start_x = card_from["x"] + card_from["width"]
                start_y = card_from["center_y"]
                end_x = card_to["x"]
                end_y = card_to["center_y"]
            else:
                start_x = card_from["x"]
                start_y = card_from["center_y"]
                end_x = card_to["x"] + card_to["width"]
                end_y = card_to["center_y"]
        else:
            # Vertical flow
            if dy > 0:
                start_x = card_from["center_x"]
                start_y = card_from["y"] + card_from["height"]
                end_x = card_to["center_x"]
                end_y = card_to["y"]
            else:
                start_x = card_from["center_x"]
                start_y = card_from["y"]
                end_x = card_to["center_x"]
                end_y = card_to["y"] + card_to["height"]

        arrow_color = color or (ZenPalette.ARROW_REVERSE if style == "dashed" else ZenPalette.ARROW_FLOW)

        arrow_elem = ExcalidrawElement(
            id=arrow_id,
            element_type="arrow",
            x=start_x,
            y=start_y,
            width=end_x - start_x,
            height=end_y - start_y,
            stroke_color=arrow_color,
            stroke_width=1.5,
            stroke_style=style,
            roughness=1,
            points=[[0.0, 0.0], [end_x - start_x, end_y - start_y]],
            start_binding={"elementId": from_card_id, "focus": 0, "gap": 6},
            end_binding={"elementId": to_card_id, "focus": 0, "gap": 6},
            end_arrowhead="arrow"
        )
        self.elements.append(arrow_elem)

        # Arrow text label
        if label:
            mid_x = (start_x + end_x) / 2
            mid_y = (start_y + end_y) / 2 - 16
            lbl_w = max(60, len(label) * 8)
            lbl_elem = ExcalidrawElement(
                id=self._gen_id("arrow_lbl"),
                element_type="text",
                x=mid_x - (lbl_w / 2),
                y=mid_y,
                width=lbl_w,
                height=20,
                stroke_color="#5f6368",
                text=label,
                font_size=13,
                font_family=1,
                text_align="center",
                vertical_align="middle"
            )
            self.elements.append(lbl_elem)

        return arrow_id

    def add_canvas_container(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        title: str
    ) -> None:
        """Adds a calming outer boundary container grouping related subsystems."""
        cont_id = self._gen_id("container")
        box = ExcalidrawElement(
            id=cont_id,
            element_type="rectangle",
            x=x,
            y=y,
            width=width,
            height=height,
            stroke_color=ZenPalette.CANVAS_CONTAINER_BORDER,
            background_color=ZenPalette.CANVAS_CONTAINER_BG,
            fill_style="solid",
            stroke_width=1.0,
            stroke_style="dashed",
            roughness=0,
            roundness={"type": 3}
        )
        self.elements.insert(0, box)  # Place at background layer

        title_lbl = ExcalidrawElement(
            id=self._gen_id("container_title"),
            element_type="text",
            x=x + 18,
            y=y + 14,
            width=width - 36,
            height=24,
            stroke_color="#5f6368",
            text=f"📂 {title}",
            font_size=16,
            font_family=1,
            text_align="left",
            vertical_align="middle"
        )
        self.elements.append(title_lbl)

    def to_dict(self) -> Dict[str, Any]:
        """Converts scene into standard Excalidraw JSON document format."""
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://senior-ai-mentor.antigravity",
            "elements": [elem.to_dict() for elem in self.elements],
            "appState": {
                "gridSize": None,
                "viewBackgroundColor": ZenPalette.CANVAS_BG
            },
            "files": {}
        }

    def to_json(self, indent: int = 2) -> str:
        """Outputs pure Excalidraw JSON string."""
        return json.dumps(self.to_dict(), indent=indent)

    def to_markdown(self) -> str:
        """Generates an Obsidian-compatible Excalidraw Markdown file with KaTeX math."""
        json_payload = self.to_json(indent=2)
        walkthrough_md = "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.walkthrough_steps))
        insights_md = "\n".join(f"- {tip}" for tip in self.engineering_insights)

        md_content = f"""---
excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor, architecture]
---
# 🎨 {self.title}
*{self.subtitle}*

---

## 🌿 1. Intuition & Mental Model
{self.intuition}

---

## 📐 2. Mathematical Foundations (KaTeX / LaTeX)
{self.math_katex}

---

## 🗺️ 3. Visual Architecture Walkthrough
{walkthrough_md if walkthrough_md else "Examine the flow of transformations illustrated in the Excalidraw diagram below."}

---

## 💡 4. Senior Engineering Insights & Production Traps
{insights_md if insights_md else "- Verify tensor shapes and memory footprint during forward and backward passes."}

---

## 🖼️ 5. Excalidraw Visual Scene
==To interactively view or edit: open this file in Obsidian with the Excalidraw plugin, or paste the JSON below into [excalidraw.com](https://excalidraw.com)==

%%
# Drawing
```json
{json_payload}
```
%%
"""
        return md_content.strip() + "\n"

    def save(self, target_dir: Path, base_filename: str) -> Tuple[Path, Path]:
        """Saves both the Obsidian-compatible `.excalidraw.md` and raw `.excalidraw` file."""
        target_dir = Path(target_dir).resolve()
        target_dir.mkdir(parents=True, exist_ok=True)

        md_path = target_dir / f"{base_filename}.excalidraw.md"
        raw_path = target_dir / f"{base_filename}.excalidraw"

        md_path.write_text(self.to_markdown(), encoding="utf-8")
        raw_path.write_text(self.to_json(), encoding="utf-8")

        return md_path, raw_path
