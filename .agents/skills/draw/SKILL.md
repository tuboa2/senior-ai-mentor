---
name: draw
description: >-
  Generate serene, beautiful Excalidraw architectural and mathematical diagrams (.excalidraw.md and .excalidraw) with full KaTeX/LaTeX formulas, harmonious pastel visual hierarchy, and cognitive comfort.
---

# Visual Architecture & Excalidraw Diagramming (/draw)

When invoked via `/draw <concept>` or `/diagram <concept>`, activate the Visual Architecture Engine to render high-fidelity, aesthetically calming diagrams for machine learning, data engineering, and system design concepts.

## 1. Aesthetic Directives ("Serene & Non-Overwhelming")

- **Harmonious Pastel Palette (Zen Palette):**
  - **Azure (`#e8f0fe`):** Input tensors, queries, initial representations.
  - **Amber (`#fef7e0`):** Weights, attention scores, latent distributions.
  - **Sage (`#e6f4ea`):** Transformations, activations, normalized states, verified outputs.
  - **Lavender (`#f3e8fd`):** Projections, multi-head subspaces, non-linear mappings.
  - **Coral (`#fce8e6`):** Losses, reverse gradients, residual error signals.
  - **Slate (`#f1f3f4`):** Memory caches, vector stores, registries, infrastructure.
- **Generous Breathing Room:** Spacing of 80–120px between sequential components. No cramped or overlapping nodes.
- **Gentle Rounded Corners:** Container and card elements use smooth curved radii (`roundness: {"type": 3}`).
- **Organic Hand-Drawn Warmth:** Low roughness (`roughness: 1`) provides an organic, approachable feel that reduces learner anxiety.
- **Cognitive Chunking:** Deconstruct complex systems into 4–5 digestible visual stages with clear step badges (`[1]`, `[2]`, `[3]`).

## 2. Mathematical Rigor (KaTeX / LaTeX Integration)

Every diagram document must feature complete mathematical foundations:
- **Block Formulations:** Use standard `$$ ... $$` syntax for derivations, loss functions, and tensor transitions.
- **Variable Clarity:** Explicitly document tensor dimensions ($n \times d_k$, $B \times L \times D$) and scalar invariants.
- **Visual Canvas Labels:** The Excalidraw drawing embeds mathematical notation in card labels (e.g. `softmax(QK^T / \sqrt{d_k}) V`), natively renderable by Obsidian Excalidraw.

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
