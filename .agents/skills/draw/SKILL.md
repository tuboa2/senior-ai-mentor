---
name: draw
description: >-
  Generate serene, beautiful Excalidraw architectural and mathematical diagrams (.excalidraw.md and .excalidraw) with full KaTeX/LaTeX formulas, harmonious pastel visual hierarchy, and cognitive comfort.
---

# Visual Architecture & Excalidraw Diagramming (/draw)

When invoked via `/draw <concept>` or `/diagram <concept>`, activate the Visual Architecture Engine to render high-fidelity, aesthetically calming diagrams for machine learning, data engineering, and system design concepts.

## 1. Aesthetic Directives ("Serene, Monochromatic & Non-Overwhelming")

- **Benchmark Reference Standard:** Modeled directly after production Obsidian-Excalidraw technical mind maps (e.g. `Log-Return Transformation.excalidraw.md`).
- **Dark Monochromatic Canvas:** Dark canvas (`theme: "dark"`, `#121212` background, `#1e1e1e` borders rendering crisp white in dark mode, `backgroundColor: "transparent"`). No distracting rainbow card fills.
- **Flawlessly Centered Text:** All container text is mathematically centered horizontally and vertically:
  - `containerId` binding between container rectangles and text elements.
  - `textAlign: "center"` and `verticalAlign: "middle"`.
  - `autoResize: true` with strict line-wrapping (`\n`) matching column character budgets (14–16 for nodes, 22 for code, 34–36 for explanations/callouts).
  - Punctuation-aware word splitting (`.`, `-`, `:`, `_`, `=`, `/`, `(`, `)`) ensuring zero text clipping or border overflow.
- **Symmetrical 6-Column Hierarchical Mind Map Tree:**
  - Col 1: Root Concept Node (220×75px).
  - Col 2: Major Branches (`Libraries`, `Methods`, `Architecture` - 181×64px).
  - Col 3: Sub-Sections & Library Items (200×64px).
  - Col 4: Code Operations (240×64px+).
  - Col 5: Technical Explanations (360×75px+).
  - Col 6: Synthesis Callouts (380×102px+).
- **Collision-Free Architecture Pipeline:** Guaranteed 140px+ vertical clearance separating methods from the architecture pipeline and vertical branches.
- **Bold Hierarchical Connection Lines:** Symmetrical routing with `strokeWidth: 4` arrows and rounded corners (`roundness: {"type": 2}`).

## 2. Mathematical Rigor & Text-Based Canvas Math

- **Text-Based Canvas Math:** Inside the Excalidraw drawing boxes, all mathematical formulas and identities are written in clean, legible, text-based notation (e.g. `x_t = sqrt(alpha)*x_0 + sqrt(1-alpha)*eps`, `Score = -eps_pred / sqrt(1 - alpha)`). Never embed unrendered raw LaTeX tokens like `\nabla_{x_t}` or `\mathcal{L}` inside canvas boxes.
- **Full KaTeX / LaTeX Markdown Rigor:** In the Markdown section of `.excalidraw.md` (`## 2. Mathematical Foundations (KaTeX / LaTeX)`), provide complete, publication-grade LaTeX equations (`$$ ... $$`) with full derivations, tensor shapes, and boundary conditions.

## 3. Dual-Format Artifact Generation

Every `/draw` execution generates two files inside the active project's `diagrams/` folder:
1. **`.excalidraw.md` (Obsidian Excalidraw Plugin):**
   - Full Markdown documentation with overview, KaTeX math derivations, and embedded Excalidraw JSON block.
   - Interactively editable in Obsidian or readable as clean Markdown anywhere.
2. **`.excalidraw` (Standard Excalidraw JSON):**
   - Pure Excalidraw scene file for 1-click opening at [excalidraw.com](https://excalidraw.com) or in the VS Code / Antigravity IDE Excalidraw extension.

## 4. Automation Helper

To generate or inspect a diagram from the terminal:
```bash
# Generate diagram and print Markdown with KaTeX math
python3 -m senior_mentor.cli --draw "transformer attention"

# Machine-readable JSON output for subagent workflows
python3 -m senior_mentor.cli --draw "diffusion models" --json
```
