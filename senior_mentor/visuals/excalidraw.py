"""Excalidraw Visual Mind Map & Architecture Tree Engine for Senior AI Mentor.

Generates crisp, elegant, hierarchical mind map and architectural flow diagrams
modeled after production Obsidian-Excalidraw technical mind maps:
- Root Concept Node
- Libraries & Dependencies
- Methods & Alternative Approaches (Code Operations -> Technical Explanations -> Mathematical Callouts)
- End-to-End Operational Pipeline
- Full LaTeX / KaTeX mathematical foundations in Markdown
- Dark canvas, monochromatic clean styling, container-bound text, zero text truncation.
"""

from dataclasses import dataclass, field
import json
from pathlib import Path
import random
import time
from typing import Any, Dict, List, Optional, Tuple
import uuid


def gen_excalidraw_id(length: int = 8) -> str:
    """Generates an Excalidraw-compliant alphanumeric unique element ID."""
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(chars) for _ in range(length))


@dataclass
class MindmapOperation:
    code: str
    explanation: str


@dataclass
class MindmapMethod:
    name: str
    operations: List[MindmapOperation]
    synthesis_callout: Optional[str] = None


@dataclass
class MindmapTreeData:
    root_title: str
    libraries: List[str]
    methods: List[MindmapMethod]
    pipeline_steps: List[str]
    pipeline_branch: Optional[Tuple[str, str]] = None  # (from_step, branch_step)
    intuition_markdown: str = ""
    math_katex_markdown: str = ""
    engineering_insights_markdown: str = ""


class MindmapExcalidrawBuilder:
    """Builds an Excalidraw scene matching the Obsidian Mind Map standard."""

    def __init__(self, data: MindmapTreeData):
        self.data = data
        self.elements: List[Dict[str, Any]] = []
        self.text_elements_markdown: List[str] = []
        self._rect_map: Dict[str, Dict[str, Any]] = {}
        self._arrows: List[Dict[str, Any]] = []

    def _add_box_with_text(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        text: str,
        is_callout: bool = False
    ) -> str:
        """Creates a rectangle and container-bound text element."""
        rect_id = gen_excalidraw_id(16)
        text_id = gen_excalidraw_id(8)

        # Store for Obsidian markdown reference
        clean_text_single_line = text.replace("\n", " ")
        self.text_elements_markdown.append(f"{clean_text_single_line} ^{text_id}")

        now_ms = int(time.time() * 1000)

        # Create Rectangle
        rect_elem: Dict[str, Any] = {
            "id": rect_id,
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,  # Crisp sharp corners like the reference
            "seed": random.randint(100000, 9999999),
            "version": 1,
            "versionNonce": 1,
            "isDeleted": False,
            "boundElements": [
                {"type": "text", "id": text_id}
            ],
            "updated": now_ms,
            "link": None,
            "locked": False
        }

        # Calculate text position inside container
        text_w = max(width - 20, 20)
        text_h = max(height - 18, 18)

        text_elem: Dict[str, Any] = {
            "id": text_id,
            "type": "text",
            "x": x + 10,
            "y": y + 9,
            "width": text_w,
            "height": text_h,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "seed": random.randint(100000, 9999999),
            "version": 1,
            "versionNonce": 1,
            "isDeleted": False,
            "boundElements": None,
            "updated": now_ms,
            "link": None,
            "locked": False,
            "text": text,
            "fontSize": 20 if not is_callout else 18,
            "fontFamily": 7,  # Clean monospace / technical sans font
            "textAlign": "center" if not is_callout else "left",
            "verticalAlign": "middle",
            "containerId": rect_id,
            "originalText": text,
            "autoResize": True,
            "lineHeight": 1.15
        }

        self.elements.append(rect_elem)
        self.elements.append(text_elem)

        self._rect_map[rect_id] = {
            "id": rect_id,
            "text_id": text_id,
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "center_x": x + width / 2,
            "center_y": y + height / 2,
            "elem": rect_elem
        }
        return rect_id

    def _add_arrow(self, start_id: str, end_id: str) -> None:
        """Creates a direct branching arrow between two boxes."""
        start_box = self._rect_map.get(start_id)
        end_box = self._rect_map.get(end_id)
        if not start_box or not end_box:
            return

        arrow_id = gen_excalidraw_id(8)
        now_ms = int(time.time() * 1000)

        # Check relative horizontal vs vertical orientation
        dx = end_box["center_x"] - start_box["center_x"]
        dy = end_box["center_y"] - start_box["center_y"]

        if abs(dx) >= abs(dy) * 0.5:
            # Horizontal connection: right edge of start to left edge of end
            start_x = start_box["x"] + start_box["width"]
            start_y = start_box["center_y"]
            end_x = end_box["x"]
            end_y = end_box["center_y"]
        else:
            # Vertical connection (e.g. pipeline branch going up)
            if dy < 0:
                start_x = start_box["center_x"]
                start_y = start_box["y"]
                end_x = end_box["center_x"]
                end_y = end_box["y"] + end_box["height"]
            else:
                start_x = start_box["center_x"]
                start_y = start_box["y"] + start_box["height"]
                end_x = end_box["center_x"]
                end_y = end_box["y"]

        diff_x = end_x - start_x
        diff_y = end_y - start_y

        arrow_elem: Dict[str, Any] = {
            "id": arrow_id,
            "type": "arrow",
            "x": start_x,
            "y": start_y,
            "width": abs(diff_x),
            "height": abs(diff_y),
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 2},
            "seed": random.randint(100000, 9999999),
            "version": 1,
            "versionNonce": 1,
            "isDeleted": False,
            "boundElements": None,
            "updated": now_ms,
            "link": None,
            "locked": False,
            "points": [
                [0.0, 0.0],
                [diff_x, diff_y]
            ],
            "lastCommittedPoint": None,
            "startBinding": {
                "elementId": start_id,
                "focus": 0,
                "gap": 1
            },
            "endBinding": {
                "elementId": end_id,
                "focus": 0,
                "gap": 1
            },
            "startArrowhead": None,
            "endArrowhead": "arrow"
        }

        # Add arrow to boundElements of both start and end boxes
        start_box["elem"]["boundElements"].append({"type": "arrow", "id": arrow_id})
        end_box["elem"]["boundElements"].append({"type": "arrow", "id": arrow_id})

        self.elements.append(arrow_elem)

    def build_scene(self) -> None:
        """Lays out the mindmap tree across 6 clean columns."""
        # 1. Column Coordinates
        col1_x = 168.0
        col2_x = 590.0
        col3_x = 900.0
        col4_x = 1170.0
        col5_x = 1425.0
        col6_x = 1895.0

        std_w = 181.0
        std_h = 64.0
        callout_w = 347.0

        # Calculate Y layout
        # Libraries branch (top)
        lib_start_y = 37.0
        # Methods branch (middle)
        method_base_y = 220.0
        # Architecture branch (bottom)
        arch_y = 1000.0

        # Root Node in Column 1
        root_y = 490.0
        root_id = self._add_box_with_text(col1_x, root_y, std_w, std_h, self.data.root_title)

        # -------------------------------------------------------------
        # BRANCH 1: Libraries
        # -------------------------------------------------------------
        lib_box_id = self._add_box_with_text(col2_x, lib_start_y, std_w, std_h, "Libraries")
        self._add_arrow(root_id, lib_box_id)

        lib_y = lib_start_y - 60.0
        for lib_name in self.data.libraries:
            l_id = self._add_box_with_text(col3_x, lib_y, std_w, std_h, lib_name)
            self._add_arrow(lib_box_id, l_id)
            lib_y += 105.0

        # -------------------------------------------------------------
        # BRANCH 2: Methods
        # -------------------------------------------------------------
        methods_root_id = self._add_box_with_text(col2_x, 488.0, std_w, std_h, "Methods")
        self._add_arrow(root_id, methods_root_id)

        curr_method_y = method_base_y
        for method in self.data.methods:
            # Sub-method header in Col 3
            sub_method_y = curr_method_y + 60.0
            sub_m_id = self._add_box_with_text(col3_x, sub_method_y, std_w, std_h, method.name)
            self._add_arrow(methods_root_id, sub_m_id)

            op_y = curr_method_y
            desc_ids: List[str] = []

            for op in method.operations:
                # Code function in Col 4
                op_id = self._add_box_with_text(col4_x, op_y, std_w, std_h, op.code)
                self._add_arrow(sub_m_id, op_id)

                # Explanation in Col 5 (taller box)
                desc_h = 75.0 if len(op.explanation) < 70 else 88.0
                desc_id = self._add_box_with_text(col5_x, op_y, callout_w, desc_h, op.explanation, is_callout=True)
                self._add_arrow(op_id, desc_id)
                desc_ids.append(desc_id)

                op_y += 112.0

            # Synthesis callout in Col 6 (if provided)
            if method.synthesis_callout:
                callout_y = curr_method_y + 40.0
                callout_h = 105.0 if len(method.synthesis_callout) < 140 else 135.0
                synth_id = self._add_box_with_text(
                    col6_x, callout_y, callout_w, callout_h, method.synthesis_callout, is_callout=True
                )
                # Connect all operation descriptions in this method to the synthesis callout
                for d_id in desc_ids:
                    self._add_arrow(d_id, synth_id)

            curr_method_y = op_y + 20.0

        # -------------------------------------------------------------
        # BRANCH 3: Architecture Pipeline
        # -------------------------------------------------------------
        arch_box_id = self._add_box_with_text(col2_x, arch_y, std_w, std_h, "Architecture")
        self._add_arrow(root_id, arch_box_id)

        pipe_x = col3_x
        prev_pipe_id = arch_box_id
        step_id_map: Dict[str, str] = {}

        for step in self.data.pipeline_steps:
            p_id = self._add_box_with_text(pipe_x, arch_y, std_w, std_h, step)
            self._add_arrow(prev_pipe_id, p_id)
            prev_pipe_id = p_id
            step_id_map[step] = p_id
            pipe_x += 256.0

        # Optional vertical branch off pipeline
        if self.data.pipeline_branch:
            from_step_name, branch_text = self.data.pipeline_branch
            from_pipe_id = step_id_map.get(from_step_name)
            if from_pipe_id:
                branch_box = self._rect_map[from_pipe_id]
                branch_y = arch_y - 124.0
                branch_id = self._add_box_with_text(
                    branch_box["x"], branch_y, std_w, std_h, branch_text
                )
                self._add_arrow(from_pipe_id, branch_id)

    def to_dict(self) -> Dict[str, Any]:
        """Returns valid Excalidraw JSON document with dark theme."""
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "theme": "dark",
                "viewBackgroundColor": "#ffffff",
                "currentItemStrokeColor": "#1e1e1e",
                "currentItemBackgroundColor": "transparent",
                "currentItemFillStyle": "solid",
                "currentItemStrokeWidthKey": "bold",
                "currentItemStrokeStyle": "solid",
                "currentItemRoughness": 0,
                "currentItemOpacity": 100,
                "currentItemFontFamily": 7,
                "currentItemFontSize": 20,
                "currentItemTextAlign": "left",
                "currentItemEndArrowhead": "arrow",
                "gridSize": 20,
                "zoom": {"value": 0.4}
            },
            "files": {}
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def to_obsidian_markdown(self) -> str:
        """Formats the file strictly according to Obsidian Excalidraw specification with KaTeX math."""
        json_payload = self.to_json(indent=2)
        text_elements_block = "\n\n".join(self.text_elements_markdown)

        md = f"""---

excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# {self.data.root_title}

## 🌿 1. Concept Intuition & Mental Model
{self.data.intuition_markdown.strip()}

---

## 📐 2. Mathematical Foundations (KaTeX / LaTeX)
{self.data.math_katex_markdown.strip()}

---

## 💡 3. Senior Engineering & Performance Notes
{self.data.engineering_insights_markdown.strip()}

---

# Excalidraw Data

## Text Elements
{text_elements_block}

%%
## Drawing
```json
{json_payload}
```
%%
"""
        return md.strip() + "\n"

    def save(self, target_dir: Path, base_filename: str) -> Tuple[Path, Path]:
        target_dir = Path(target_dir).resolve()
        target_dir.mkdir(parents=True, exist_ok=True)

        md_path = target_dir / f"{base_filename}.excalidraw.md"
        raw_path = target_dir / f"{base_filename}.excalidraw"

        md_path.write_text(self.to_obsidian_markdown(), encoding="utf-8")
        raw_path.write_text(self.to_json(), encoding="utf-8")

        return md_path, raw_path


# Compatibility aliases
ExcalidrawDiagram = MindmapExcalidrawBuilder
