"""Excalidraw Visual Mind Map & Architecture Tree Engine for Senior AI Mentor.

Generates crisp, elegant, hierarchical mind map and architectural flow diagrams
modeled after production Obsidian-Excalidraw technical mind maps:
- Root Concept Node
- Libraries & Dependencies
- Methods & Alternative Approaches (Code Operations -> Technical Explanations -> Mathematical Callouts)
- End-to-End Operational Pipeline
- Full LaTeX / KaTeX mathematical foundations in Markdown
- Dark canvas, monochromatic clean styling, container-bound centered text, zero text truncation.
"""

from dataclasses import dataclass
import json
from pathlib import Path
import random
import re
import time
from typing import Any, Dict, List, Optional, Tuple


def gen_excalidraw_id(length: int = 8) -> str:
    """Generates an Excalidraw-compliant alphanumeric unique element ID."""
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(chars) for _ in range(length))


def wrap_text_to_lines(text: str, max_chars: int) -> List[str]:
    """Wraps text into clean lines respecting explicit newlines and token boundaries."""
    paragraphs = text.strip().split("\n")
    final_lines: List[str] = []

    for p in paragraphs:
        cleaned_para = p.strip()
        if not cleaned_para:
            continue
        words = cleaned_para.split(" ")
        cur = ""
        for w in words:
            if not w:
                continue
            cand = f"{cur} {w}".strip() if cur else w
            if len(cand) <= max_chars:
                cur = cand
            else:
                if cur:
                    final_lines.append(cur)
                # If a single word is longer than max_chars
                if len(w) > max_chars:
                    # Break gracefully at punctuation and operators
                    parts = [pt for pt in re.split(r"([_=@\+\*\/\(\),\.\-:])", w) if pt]
                    if len(parts) == 1:
                        # Fallback for unbroken strings longer than max_chars
                        chunk_size = max_chars - 1
                        parts = [w[i:i+chunk_size] + ("-" if i + chunk_size < len(w) else "")
                                 for i in range(0, len(w), chunk_size)]

                    sub = ""
                    for part in parts:
                        if not part:
                            continue
                        if len(sub + part) <= max_chars:
                            sub += part
                        else:
                            if sub:
                                final_lines.append(sub)
                            sub = part
                    cur = sub
                else:
                    cur = w
        if cur:
            final_lines.append(cur)

    return final_lines or [text]


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
        max_chars: int = 16,
        is_callout: bool = False
    ) -> str:
        """Creates a rectangle and container-bound text element centered mathematically."""
        rect_id = gen_excalidraw_id(16)
        text_id = gen_excalidraw_id(8)

        # 1. Wrap text into lines
        lines = wrap_text_to_lines(text, max_chars)
        wrapped_text = "\n".join(lines)
        num_lines = max(1, len(lines))
        max_line_len = max(len(l) for l in lines) if lines else 1

        # Store for Obsidian markdown reference
        clean_text_single_line = wrapped_text.replace("\n", " ")
        self.text_elements_markdown.append(f"{clean_text_single_line} ^{text_id}")

        now_ms = int(time.time() * 1000)

        # 2. Font metrics matching Obsidian Excalidraw (fontFamily 7, fontSize 20)
        char_w = 9.0
        line_h = 23.0
        text_w = min(width - 12.0, max(40.0, round(max_line_len * char_w, 1)))
        text_h = num_lines * line_h

        # Height follows benchmark reference: 64 for 1-2 lines, text_h + 10 for 3+ lines
        if num_lines <= 2:
            box_h = max(height, 64.0)
        else:
            box_h = max(height, text_h + 10.0)
        box_w = width

        # Exact mathematical centering inside container
        text_x = round(x + (box_w - text_w) / 2.0, 1)
        text_y = round(y + (box_h - text_h) / 2.0, 1)

        # Create Rectangle
        rect_elem: Dict[str, Any] = {
            "id": rect_id,
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": box_w,
            "height": box_h,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
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

        # Create Text
        text_elem: Dict[str, Any] = {
            "id": text_id,
            "type": "text",
            "x": text_x,
            "y": text_y,
            "width": text_w,
            "height": text_h,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
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
            "text": wrapped_text,
            "rawText": clean_text_single_line,
            "fontSize": 20,
            "fontFamily": 7,  # Clean monospace / technical sans font
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": rect_id,
            "originalText": wrapped_text,
            "hasTextLink": False,
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
            "width": box_w,
            "height": box_h,
            "center_x": x + box_w / 2.0,
            "center_y": y + box_h / 2.0,
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

        if abs(dx) >= abs(dy) * 0.4:
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
            "strokeWidth": 4,  # Prominent hierarchical branch arrows
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

        start_box["elem"]["boundElements"].append({"type": "arrow", "id": arrow_id})
        end_box["elem"]["boundElements"].append({"type": "arrow", "id": arrow_id})

        self.elements.append(arrow_elem)

    def build_scene(self) -> None:
        """Lays out the mindmap tree across 6 clean columns with dynamic collision avoidance."""
        col1_x = 140.0
        col2_x = 560.0
        col3_x = 880.0
        col4_x = 1200.0
        col5_x = 1560.0
        col6_x = 2060.0

        std_w = 181.0
        std_h = 64.0
        code_w = 240.0
        callout_w = 360.0
        synth_w = 380.0

        lib_start_y = 37.0
        method_base_y = 220.0

        # Pre-calculate layout of all methods to guarantee symmetrical alignment
        curr_method_y = method_base_y
        method_group_records = []
        sub_method_centers: List[float] = []

        for method in self.data.methods:
            op_records = []
            op_y = curr_method_y

            for op in method.operations:
                code_lines = wrap_text_to_lines(op.code, max_chars=22)
                code_h = 64.0 if len(code_lines) <= 2 else max(64.0, len(code_lines) * 23.0 + 10.0)

                desc_lines = wrap_text_to_lines(op.explanation, max_chars=34)
                desc_h = 64.0 if len(desc_lines) <= 2 else max(75.0, len(desc_lines) * 23.0 + 10.0)

                row_h = max(code_h, desc_h)
                row_center_y = op_y + row_h / 2.0

                code_y = row_center_y - code_h / 2.0
                desc_y = row_center_y - desc_h / 2.0

                op_records.append({
                    "op": op,
                    "code_y": code_y,
                    "code_h": code_h,
                    "desc_y": desc_y,
                    "desc_h": desc_h,
                    "row_center_y": row_center_y,
                    "row_h": row_h
                })
                op_y += row_h + 30.0

            method_center_y = (op_records[0]["row_center_y"] + op_records[-1]["row_center_y"]) / 2.0
            sub_m_y = method_center_y - std_h / 2.0

            synth_record = None
            if method.synthesis_callout:
                synth_lines = wrap_text_to_lines(method.synthesis_callout, max_chars=36)
                synth_h = max(102.0, len(synth_lines) * 23.0 + 10.0)
                synth_y = method_center_y - synth_h / 2.0
                synth_record = {
                    "text": method.synthesis_callout,
                    "synth_y": synth_y,
                    "synth_h": synth_h
                }

            method_bottom_y = max(op_y, (synth_record["synth_y"] + synth_record["synth_h"]) if synth_record else op_y)

            method_group_records.append({
                "method": method,
                "sub_m_y": sub_m_y,
                "method_center_y": method_center_y,
                "op_records": op_records,
                "synth_record": synth_record,
                "bottom_y": method_bottom_y
            })
            sub_method_centers.append(method_center_y)
            curr_method_y = method_bottom_y + 40.0

        # Dynamic architecture row with generous vertical clearance
        arch_y = max(1150.0, curr_method_y + 200.0)

        # Libraries layout
        lib_box_id = self._add_box_with_text(col2_x, lib_start_y, std_w, std_h, "Libraries", max_chars=16)

        lib_count = len(self.data.libraries)
        lib_start_offset = lib_start_y - ((lib_count - 1) * 85.0) / 2.0
        lib_y = lib_start_offset
        for lib_name in self.data.libraries:
            l_id = self._add_box_with_text(col3_x, lib_y, std_w, std_h, lib_name, max_chars=16)
            self._add_arrow(lib_box_id, l_id)
            lib_y += 85.0

        # Centered Methods Root Node
        if sub_method_centers:
            methods_root_y = (sub_method_centers[0] + sub_method_centers[-1]) / 2.0 - std_h / 2.0
        else:
            methods_root_y = method_base_y
        methods_root_id = self._add_box_with_text(col2_x, methods_root_y, std_w, std_h, "Methods", max_chars=16)

        # Architecture Node
        arch_box_id = self._add_box_with_text(col2_x, arch_y, std_w, std_h, "Architecture", max_chars=16)

        # Centered Root Concept Node across Libraries, Methods, and Architecture
        root_center_y = (lib_start_y + std_h / 2.0 + arch_y + std_h / 2.0) / 2.0
        root_y = root_center_y - 37.5
        root_id = self._add_box_with_text(col1_x, root_y, 220.0, 75.0, self.data.root_title, max_chars=20)

        # Connect Root to major branches
        self._add_arrow(root_id, lib_box_id)
        self._add_arrow(root_id, methods_root_id)
        self._add_arrow(root_id, arch_box_id)

        # Render Methods Branch
        for m_rec in method_group_records:
            method = m_rec["method"]
            sub_m_id = self._add_box_with_text(col3_x, m_rec["sub_m_y"], 200.0, std_h, method.name, max_chars=18)
            self._add_arrow(methods_root_id, sub_m_id)

            desc_ids: List[str] = []
            for op_rec in m_rec["op_records"]:
                op = op_rec["op"]
                op_id = self._add_box_with_text(
                    col4_x, op_rec["code_y"], code_w, op_rec["code_h"], op.code, max_chars=22
                )
                self._add_arrow(sub_m_id, op_id)

                desc_id = self._add_box_with_text(
                    col5_x, op_rec["desc_y"], callout_w, op_rec["desc_h"], op.explanation, max_chars=34, is_callout=True
                )
                self._add_arrow(op_id, desc_id)
                desc_ids.append(desc_id)

            if m_rec["synth_record"]:
                s_rec = m_rec["synth_record"]
                synth_id = self._add_box_with_text(
                    col6_x, s_rec["synth_y"], synth_w, s_rec["synth_h"], s_rec["text"], max_chars=36, is_callout=True
                )
                for d_id in desc_ids:
                    self._add_arrow(d_id, synth_id)

        # Render Architecture Pipeline
        pipe_x = col3_x
        prev_pipe_id = arch_box_id
        step_id_map: Dict[str, str] = {}

        for step in self.data.pipeline_steps:
            p_id = self._add_box_with_text(pipe_x, arch_y, 190.0, std_h, step, max_chars=16)
            self._add_arrow(prev_pipe_id, p_id)
            prev_pipe_id = p_id
            step_id_map[step] = p_id
            pipe_x += 255.0

        # Optional vertical branch off pipeline
        if self.data.pipeline_branch:
            from_step_name, branch_text = self.data.pipeline_branch
            from_pipe_id = step_id_map.get(from_step_name)
            if from_pipe_id:
                branch_box = self._rect_map[from_pipe_id]
                branch_y = arch_y - 120.0
                branch_id = self._add_box_with_text(
                    branch_box["x"], branch_y, 190.0, std_h, branch_text, max_chars=16
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
                "currentItemTextAlign": "center",
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
        display_title = self.data.root_title.replace("\n", " ")

        md = f"""---

excalidraw-plugin: parsed
tags: [excalidraw, senior-ai-mentor]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# {display_title}

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
