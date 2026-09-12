"""Pre-configured Architectural Templates and Dynamic Visual Synthesizer.

Provides high-fidelity, aesthetically calming Excalidraw diagrams for key AI/ML
architectures, complete with rigorous KaTeX mathematical formulations.
"""

from typing import Dict, List, Optional, Tuple
import re

from .excalidraw import (
    ExcalidrawDiagram,
    ZenPalette
)


def get_transformer_attention_diagram() -> ExcalidrawDiagram:
    """Scaled Dot-Product & Multi-Head Attention Architecture."""
    diag = ExcalidrawDiagram(
        title="Scaled Dot-Product Attention Architecture",
        concept="Transformer Attention Mechanism",
        subtitle="Dynamic Associative Retrieval & Routing in High-Dimensional Space",
        intuition=(
            "Attention can be understood intuitively as a **soft database query**:\n"
            "- The **Query (Q)** represents what a token is actively looking for.\n"
            "- The **Key (K)** represents the indexing metadata of other tokens.\n"
            "- The **Value (V)** represents the content payload retrieved.\n\n"
            "By taking the scaled inner product $\\frac{Q K^T}{\\sqrt{d_k}}$, we compute pairwise alignment scores, "
            "normalize them with Softmax into a probability simplex, and take the expected value across $V$."
        ),
        math_katex=(
            "### Scaled Dot-Product Attention Formulation\n\n"
            "$$\\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = "
            "\\text{softmax}\\left(\\frac{\\mathbf{Q}\\mathbf{K}^T}{\\sqrt{d_k}} + \\mathbf{M}\\right) \\mathbf{V}$$\n\n"
            "Where:\n"
            "- $\\mathbf{Q} \\in \\mathbb{R}^{n \\times d_k}$ (Sequence length $n$, projection dimension $d_k$)\n"
            "- $\\mathbf{K} \\in \\mathbb{R}^{m \\times d_k}$ (Context memory length $m$)\n"
            "- $\\mathbf{V} \\in \\mathbb{R}^{m \\times d_v}$ (Value feature space $d_v$)\n"
            "- $\\mathbf{M}$ is the optional causal autoregressive mask ($-\\infty$ for future tokens)\n"
            "- The scaling factor $\\frac{1}{\\sqrt{d_k}}$ counteracts variance growth: if components of $q, k$ are i.i.d. with variance 1, "
            "their dot product has variance $d_k$. Without scaling, large magnitudes push Softmax into vanishing gradient saturation regions.\n\n"
            "### Multi-Head Attention Expansion\n\n"
            "$$\\text{MultiHead}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = "
            "\\text{Concat}(\\text{head}_1, \\dots, \\text{head}_h) \\mathbf{W}^O$$\n\n"
            "$$\\text{head}_i = \\text{Attention}(\\mathbf{Q}\\mathbf{W}_i^Q, \\mathbf{K}\\mathbf{W}_i^K, \\mathbf{V}\\mathbf{W}_i^V)$$"
        ),
        walkthrough_steps=[
            "Input tokens are linearly projected through learned matrices $W_Q, W_K, W_V$ into subspace representations.",
            "Queries and Keys undergo parallel matrix multiplication $Q K^T$ producing pairwise compatibility logits.",
            "Logits are scaled by $1 / \\sqrt{d_k}$ to stabilize softmax gradient propagation.",
            "Softmax normalizes raw attention energy into a probability distribution over context tokens.",
            "Attention probabilities weight the Value vectors $V$, producing the contextualized output representation."
        ],
        engineering_insights=[
            "**Memory Bound:** Attention matrix has space complexity $O(n^2)$. For long contexts ($n > 4096$), employ FlashAttention to fuse Softmax and avoid materialize $QK^T$ in HBM.",
            "**KV Caching in Inference:** During auto-regressive decoding, Key and Value vectors for past tokens are cached, reducing step complexity from $O(n^2)$ to $O(n)$."
        ]
    )

    # 1. Outer Surrounding Container
    diag.add_canvas_container(
        x=60,
        y=40,
        width=1020,
        height=320,
        title="Transformer Scaled Dot-Product Attention Pipeline"
    )

    # 2. Sequential Cards
    c1 = diag.add_zen_card(
        x=90, y=90, width=190, height=180,
        title="Input Projections",
        subtitle="Linear Mappings",
        latex_formula="Q, K, V = X W_{Q,K,V}",
        step_badge="Step 1",
        theme="azure"
    )

    c2 = diag.add_zen_card(
        x=330, y=90, width=190, height=180,
        title="Pairwise MatMul",
        subtitle="Compatibility Logits",
        latex_formula="S = Q K^T / \\sqrt{d_k}",
        step_badge="Step 2",
        theme="amber"
    )

    c3 = diag.add_zen_card(
        x=570, y=90, width=190, height=180,
        title="Softmax Normalizer",
        subtitle="Attention Weights",
        latex_formula="A = \\text{softmax}(S)",
        step_badge="Step 3",
        theme="sage"
    )

    c4 = diag.add_zen_card(
        x=810, y=90, width=220, height=180,
        title="Value Weighting",
        subtitle="Contextualized Output",
        latex_formula="\\text{Out} = A \\times V",
        step_badge="Step 4",
        theme="lavender"
    )

    # 3. Connecting Flow Arrows
    diag.add_flow_arrow(c1, c2, label="Q, K vectors")
    diag.add_flow_arrow(c2, c3, label="Scaled Logits")
    diag.add_flow_arrow(c3, c4, label="Probabilities & V")

    return diag


def get_backpropagation_diagram() -> ExcalidrawDiagram:
    """Computational Graph & Backpropagation Gradient Flow."""
    diag = ExcalidrawDiagram(
        title="Backpropagation Computational Graph",
        concept="Chain Rule Gradient Flow",
        subtitle="Reverse-Mode Automatic Differentiation Across Layer Boundaries",
        intuition=(
            "Backpropagation is simply the **multivariable chain rule** executed backward:\n"
            "- In the **Forward Pass**, input activations cascade through weights and activation functions to compute the scalar loss $\\mathcal{L}$.\n"
            "- In the **Backward Pass**, the scalar loss acts as a perturbation source, propagating upstream adjoint gradients $\\frac{\\partial \\mathcal{L}}{\\partial z}$ to adjust weights."
        ),
        math_katex=(
            "### Forward Equations\n\n"
            "$$\\mathbf{z}^{[l]} = \\mathbf{W}^{[l]} \\mathbf{a}^{[l-1]} + \\mathbf{b}^{[l]}$$\n"
            "$$\\mathbf{a}^{[l]} = \\sigma\\left(\\mathbf{z}^{[l]}\\right)$$\n\n"
            "### Backward Error Adjoint (The Chain Rule)\n\n"
            "$$\\boldsymbol{\\delta}^{[l]} \\equiv \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{z}^{[l]}} = "
            "\\left( (\\mathbf{W}^{[l+1]})^T \\boldsymbol{\\delta}^{[l+1]} \\right) \\odot \\sigma'\\left(\\mathbf{z}^{[l]}\\right)$$\n\n"
            "### Parameter Gradients for Optimization\n\n"
            "$$\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{W}^{[l]}} = \\boldsymbol{\\delta}^{[l]} (\\mathbf{a}^{[l-1]})^T, "
            "\\quad \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{b}^{[l]}} = \\sum_{\\text{batch}} \\boldsymbol{\\delta}^{[l]}$$\n\n"
            "Where $\\odot$ represents the Hadamard element-wise product."
        ),
        walkthrough_steps=[
            "Activation $a^{[l-1]}$ from preceding layer undergoes affine transformation producing pre-activation $z^{[l]}$.",
            "Non-linear activation $\\sigma(z)$ squashes pre-activation into layer output $a^{[l]}$.",
            "Loss function $\\mathcal{L}(y, \\hat{y})$ compares network prediction to ground-truth target.",
            "Backward error vector $\\delta^{[l]}$ propagates upstream via transposed weight matrix $(W^{[l+1]})^T$.",
            "Local gradient $\\frac{\\partial \\mathcal{L}}{\\partial W^{[l]}}$ is accumulated as the outer product of error and input activation."
        ],
        engineering_insights=[
            "**Gradient Vanishing / Exploding Trap:** If $|\\sigma'(z)| < 1$ (e.g. sigmoid saturation $\\sigma'(z) \\le 0.25$), deep cascades multiply fractions, extinguishing gradient flow.",
            "**Memory Activation Stashing:** During the forward pass, intermediate activations $a^{[l-1]}$ must be retained in VRAM to compute parameter gradients later."
        ]
    )

    diag.add_canvas_container(
        x=60,
        y=40,
        width=1020,
        height=340,
        title="Layer Boundary Computational Graph (Forward & Reverse Adjoints)"
    )

    c1 = diag.add_zen_card(
        x=90, y=90, width=190, height=190,
        title="Layer Input",
        subtitle="Activation State",
        latex_formula="a^{[l-1]} \\in \\mathbb{R}^{d_{in}}",
        step_badge="State",
        theme="azure"
    )

    c2 = diag.add_zen_card(
        x=330, y=90, width=200, height=190,
        title="Affine Transformation",
        subtitle="Linear Weighted Sum",
        latex_formula="z^{[l]} = W^{[l]} a + b",
        step_badge="Affine",
        theme="lavender"
    )

    c3 = diag.add_zen_card(
        x=580, y=90, width=190, height=190,
        title="Activation Gate",
        subtitle="Non-linear Mapping",
        latex_formula="a^{[l]} = \\sigma(z^{[l]})",
        step_badge="Non-Linear",
        theme="sage"
    )

    c4 = diag.add_zen_card(
        x=820, y=90, width=210, height=190,
        title="Objective Loss",
        subtitle="Error Criterion",
        latex_formula="\\mathcal{L}(y, \\hat{y})",
        step_badge="Criterion",
        theme="amber"
    )

    # Forward arrows
    diag.add_flow_arrow(c1, c2, label="Forward Pass")
    diag.add_flow_arrow(c2, c3, label="z values")
    diag.add_flow_arrow(c3, c4, label="Predictions")

    # Reverse backward gradient arrow
    diag.add_flow_arrow(c4, c3, label="\\partial L / \\partial a", style="dashed", color=ZenPalette.ARROW_REVERSE)
    diag.add_flow_arrow(c3, c2, label="\\delta^{[l]} \\odot \\sigma'", style="dashed", color=ZenPalette.ARROW_REVERSE)

    return diag


def get_diffusion_model_diagram() -> ExcalidrawDiagram:
    """Denoising Diffusion Probabilistic Models (DDPM)."""
    diag = ExcalidrawDiagram(
        title="Denoising Diffusion Probabilistic Architecture (DDPM)",
        concept="Diffusion Generative Modeling",
        subtitle="Forward Thermodynamic Entropy & Learned Reverse Denoising Dynamics",
        intuition=(
            "Diffusion models generate data by learning to reverse a gradual destruction process:\n"
            "- **Forward Process ($q$):** Pure data $\\mathbf{x}_0$ is systematically corrupted with Gaussian noise over $T$ steps until it matches white noise $\\mathcal{N}(0, \\mathbf{I})$.\n"
            "- **Reverse Process ($p_\\theta$):** A neural network (typically a U-Net or DiT) predicts the noise injected at each step, progressively uncorrupted back to clean data."
        ),
        math_katex=(
            "### Forward Process Jump Formulation\n\n"
            "$$q(\\mathbf{x}_t \\mid \\mathbf{x}_0) = \\mathcal{N}\\left(\\mathbf{x}_t; \\sqrt{\\bar{\\alpha}_t}\\mathbf{x}_0, (1 - \\bar{\\alpha}_t)\\mathbf{I}\\right)$$\n\n"
            "Where $\\alpha_t = 1 - \\beta_t$ and $\\bar{\\alpha}_t = \\prod_{s=1}^t \\alpha_s$.\n\n"
            "Reparameterization trick allows jumping directly to timestep $t$ in $O(1)$ without simulating intermediate steps:\n"
            "$$\\mathbf{x}_t = \\sqrt{\\bar{\\alpha}_t} \\mathbf{x}_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\boldsymbol{\\epsilon}, "
            "\\quad \\boldsymbol{\\epsilon} \\sim \\mathcal{N}(\\mathbf{0}, \\mathbf{I})$$\n\n"
            "### Simplified Training Objective\n\n"
            "$$\\mathcal{L}_{\\text{simple}}(\\theta) = \\mathbb{E}_{t, \\mathbf{x}_0, \\boldsymbol{\\epsilon}}\\left[ "
            "\\left\\| \\boldsymbol{\\epsilon} - \\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, t) \\right\\|^2 \\right]$$"
        ),
        walkthrough_steps=[
            "Clean data tensor $\\mathbf{x}_0$ is sampled from empirical training dataset.",
            "Variance schedule $\\beta_1, \\dots, \\beta_T$ systematically injects Gaussian perturbation.",
            "Reparameterized noisy state $\\mathbf{x}_t$ is computed directly for sampled timestep $t$.",
            "U-Net / Diffusion Transformer predicts the exact noise vector $\\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, t)$.",
            "Mean Squared Error loss supervises the noise estimator, enabling step-by-step reverse sampling."
        ],
        engineering_insights=[
            "**Latent Diffusion:** Running diffusion in raw pixel space is computationally prohibitive. Compressing images into latent space via a VAE reduces spatial resolution by $8\\times$ with negligible perceptual loss.",
            "**Classifier-Free Guidance (CFG):** Interpolating between conditional and unconditional score estimates $\\tilde{\\epsilon}_\\theta = \\epsilon_\\theta(x_t, \\emptyset) + s \\cdot (\\epsilon_\\theta(x_t, c) - \\epsilon_\\theta(x_t, \\emptyset))$ trades sample diversity for adherence."
        ]
    )

    diag.add_canvas_container(
        x=60,
        y=40,
        width=1020,
        height=320,
        title="Forward Perturbation & Learned Reverse Sampling Pipeline"
    )

    c1 = diag.add_zen_card(
        x=90, y=90, width=190, height=180,
        title="Clean Data",
        subtitle="Empirical Distribution",
        latex_formula="x_0 \\sim q(x)",
        step_badge="t = 0",
        theme="azure"
    )

    c2 = diag.add_zen_card(
        x=330, y=90, width=190, height=180,
        title="Noise Schedule",
        subtitle="Forward Markov Chain",
        latex_formula="x_t = \\sqrt{\\bar{\\alpha}_t} x_0 + \\sigma_t \\epsilon",
        step_badge="t = t",
        theme="amber"
    )

    c3 = diag.add_zen_card(
        x=570, y=90, width=200, height=180,
        title="Noise Estimator",
        subtitle="U-Net / Transformer",
        latex_formula="\\epsilon_\\theta(x_t, t)",
        step_badge="Model",
        theme="lavender"
    )

    c4 = diag.add_zen_card(
        x=820, y=90, width=210, height=180,
        title="Reverse Step",
        subtitle="Denoised Trajectory",
        latex_formula="p_\\theta(x_{t-1} \\mid x_t)",
        step_badge="Sample",
        theme="sage"
    )

    diag.add_flow_arrow(c1, c2, label="Add Noise q")
    diag.add_flow_arrow(c2, c3, label="Noisy Latent x_t")
    diag.add_flow_arrow(c3, c4, label="Denoise p_\\theta")

    return diag


def get_rag_architecture_diagram() -> ExcalidrawDiagram:
    """Retrieval-Augmented Generation Architecture."""
    diag = ExcalidrawDiagram(
        title="Production Retrieval-Augmented Generation (RAG)",
        concept="Hybrid Semantic Retrieval & Knowledge Grounding",
        subtitle="Bridging Parametric Memory and Dynamic Verifiable Knowledge Stores",
        intuition=(
            "RAG mitigates hallucinations and stale training data by treating retrieval as an **open-book lookup**:\n"
            "- Unstructured documents are chunked and converted to high-dimensional embeddings.\n"
            "- A user's query is mapped into the same geometric space to find relevant context passages.\n"
            "- Retrieved context passages are assembled into an augmented prompt for synthesis."
        ),
        math_katex=(
            "### Cosine Similarity in Dual-Encoder Space\n\n"
            "$$\\text{sim}(\\mathbf{q}, \\mathbf{d}_i) = "
            "\\frac{\\mathbf{e}_q \\cdot \\mathbf{e}_{d_i}}{\\|\\mathbf{e}_q\\| \\|\\mathbf{e}_{d_i}\\|} = \\cos(\\theta)$$\n\n"
            "### Top-K Context Set Selection\n\n"
            "$$\\mathcal{D}^* = \\operatorname{arg\\,top-}k_{d \\in \\mathcal{C}}\\left( "
            "\\alpha \\cdot \\text{sim}_{\\text{dense}}(q, d) + (1 - \\alpha) \\cdot \\text{score}_{\\text{BM25}}(q, d) \\right)$$\n\n"
            "### Conditional Autoregressive Generation\n\n"
            "$$P(y \\mid q, \\mathcal{D}^*) = \\prod_{t=1}^T P_{\\text{LLM}}\\left(y_t \\mid y_{<t}, [q; \\mathcal{D}^*]\\right)$$"
        ),
        walkthrough_steps=[
            "Ingestion pipeline chunks raw enterprise documents and generates dense vector embeddings.",
            "Embeddings are indexed in approximate nearest neighbor graph (e.g. HNSW).",
            "User query is embedded and paired with sparse BM25 indices for hybrid retrieval.",
            "Cross-encoder reranker scores candidate passages to select optimal top-k context.",
            "Context-augmented prompt is presented to LLM for factual, grounded answer generation."
        ],
        engineering_insights=[
            "**Lost in the Middle Trap:** LLMs prioritize information at the extreme start and end of prompt context. Place the most vital chunks at the top/bottom rather than center.",
            "**Chunk Size Trade-Off:** Chunks that are too small lack context; chunks that are too large dilute embedding cosine similarity. 300-500 tokens with 10% overlap is standard."
        ]
    )

    diag.add_canvas_container(
        x=60,
        y=40,
        width=1020,
        height=320,
        title="End-to-End Enterprise RAG System Architecture"
    )

    c1 = diag.add_zen_card(
        x=90, y=90, width=190, height=180,
        title="Document Ingestion",
        subtitle="Chunking & Parser",
        latex_formula="d_i \\in \\text{Chunks}(\\mathcal{C})",
        step_badge="Ingest",
        theme="slate"
    )

    c2 = diag.add_zen_card(
        x=330, y=90, width=190, height=180,
        title="Vector Index",
        subtitle="HNSW / Dense Store",
        latex_formula="\\mathbf{e}_d = E_\\phi(d)",
        step_badge="Index",
        theme="amber"
    )

    c3 = diag.add_zen_card(
        x=570, y=90, width=200, height=180,
        title="Hybrid Retriever",
        subtitle="Dense + BM25 Reranker",
        latex_formula="\\text{Top-}k(\\text{sim}_{dense} + \\text{sparse})",
        step_badge="Retrieve",
        theme="azure"
    )

    c4 = diag.add_zen_card(
        x=820, y=90, width=210, height=180,
        title="LLM Synthesis",
        subtitle="Grounded Generation",
        latex_formula="P(y \\mid [q; \\mathcal{D}^*])",
        step_badge="Generate",
        theme="sage"
    )

    diag.add_flow_arrow(c1, c2, label="Embeddings")
    diag.add_flow_arrow(c2, c3, label="Vector Search")
    diag.add_flow_arrow(c3, c4, label="Context Prompt")

    return diag


def get_resnet_residual_block_diagram() -> ExcalidrawDiagram:
    """Residual Block & Skip Connection Architecture."""
    diag = ExcalidrawDiagram(
        title="Residual Block & Skip Connection Flow",
        concept="Residual Network Skip Connections",
        subtitle="Identity Mapping Creating Unimpeded Gradient Highways",
        intuition=(
            "Deep networks traditionally suffer from gradient degradation as depth increases.\n"
            "ResNet reformulates layers to learn an **additive residual perturbation** $\\mathcal{F}(\\mathbf{x}) = \\mathcal{H}(\\mathbf{x}) - \\mathbf{x}$.\n"
            "If an identity mapping is optimal, weights can easily decay toward zero rather than learning an identity map from scratch."
        ),
        math_katex=(
            "### Forward Identity Bypass\n\n"
            "$$\\mathbf{x}_{l+1} = \\mathbf{x}_l + \\mathcal{F}(\\mathbf{x}_l, \\mathcal{W}_l)$$\n\n"
            "Where $\\mathcal{F}(\\mathbf{x}_l, \\mathcal{W}_l) = \\mathbf{W}_2 \\sigma(\\mathbf{W}_1 \\mathbf{x}_l)$.\n\n"
            "### The Gradient Highway Proof\n\n"
            "By recursively expanding the forward pass to any downstream layer $L > l$:\n"
            "$$\\mathbf{x}_L = \\mathbf{x}_l + \\sum_{i=l}^{L-1} \\mathcal{F}(\\mathbf{x}_i, \\mathcal{W}_i)$$\n\n"
            "Taking the gradient with respect to input $\\mathbf{x}_l$:\n"
            "$$\\frac{\\partial \\mathcal{E}}{\\partial \\mathbf{x}_l} = "
            "\\frac{\\partial \\mathcal{E}}{\\partial \\mathbf{x}_L} "
            "\\left( \\mathbf{I} + \\frac{\\partial}{\\partial \\mathbf{x}_l} \\sum_{i=l}^{L-1} \\mathcal{F}(\\mathbf{x}_i, \\mathcal{W}_i) \\right)$$\n\n"
            "Notice the identity term $\\mathbf{I}$: even if the path gradients approach zero, the error signal propagates directly backward through the identity shortcut!"
        ),
        walkthrough_steps=[
            "Input feature tensor $\\mathbf{x}_l$ splits into two parallel streams: the residual function path and identity shortcut.",
            "Residual stream undergoes sequential convolution, normalization, and non-linear activation.",
            "Identity stream bypasses computation completely with zero parameter overhead.",
            "Element-wise addition node sums residual features and original input $\\mathcal{F}(\\mathbf{x}_l) + \\mathbf{x}_l$.",
            "Output features $\\mathbf{x}_{l+1}$ continue to subsequent network layers."
        ],
        engineering_insights=[
            "**Pre-LN vs Post-LN:** Modern Transformers place LayerNorm on the residual branch *before* transformation (Pre-LN), which allows training 100B+ parameter models without learning rate warmup instability."
        ]
    )

    diag.add_canvas_container(
        x=60,
        y=40,
        width=1020,
        height=320,
        title="Residual Block: Additive Identity Bypass Architecture"
    )

    c1 = diag.add_zen_card(
        x=90, y=90, width=190, height=180,
        title="Input State",
        subtitle="Identity Tensor",
        latex_formula="x_l \\in \\mathbb{R}^{C \\times H \\times W}",
        step_badge="Input",
        theme="azure"
    )

    c2 = diag.add_zen_card(
        x=340, y=90, width=200, height=180,
        title="Residual Stream",
        subtitle="Weight Layers",
        latex_formula="\\mathcal{F}(x_l, \\mathcal{W}_l)",
        step_badge="Residual",
        theme="lavender"
    )

    c3 = diag.add_zen_card(
        x=590, y=90, width=180, height=180,
        title="Summation Gate",
        subtitle="Additive Merge",
        latex_formula="x_l + \\mathcal{F}(x_l)",
        step_badge="Add",
        theme="amber"
    )

    c4 = diag.add_zen_card(
        x=820, y=90, width=210, height=180,
        title="Output State",
        subtitle="Next Layer Feed",
        latex_formula="x_{l+1} = \\sigma(x_l + \\mathcal{F})",
        step_badge="Output",
        theme="sage"
    )

    diag.add_flow_arrow(c1, c2, label="Residual Path")
    diag.add_flow_arrow(c2, c3, label="Features")
    diag.add_flow_arrow(c3, c4, label="Combined")
    # Identity skip arrow directly from c1 to c3
    diag.add_flow_arrow(c1, c3, label="Identity Shortcut (+x_l)", style="dashed", color=ZenPalette.ARROW_ACCENT)

    return diag


def get_dynamic_diagram(concept: str, query: str) -> ExcalidrawDiagram:
    """Dynamically synthesizes a serene, mathematically grounded diagram for any custom topic."""
    clean_name = concept if concept else "System Architecture"
    title_text = f"{clean_name.title()} Architecture"

    diag = ExcalidrawDiagram(
        title=title_text,
        concept=clean_name,
        subtitle="Component Flow & Mathematical Dynamics",
        intuition=(
            f"The **{clean_name}** architecture orchestrates information flow through modular, decoupled stages.\n"
            "Each transition transforms input representations while preserving necessary mathematical invariants."
        ),
        math_katex=(
            f"### Mathematical Invariants for {clean_name}\n\n"
            "$$\\mathbf{h}_{t} = \\mathcal{T}\\left(\\mathbf{h}_{t-1}, \\mathbf{x}_t; \\boldsymbol{\\theta}\\right)$$\n\n"
            "Where:\n"
            "- $\\mathbf{x}_t$ represents input signals or observations\n"
            "- $\\mathbf{h}_t$ represents internal state embeddings\n"
            "- $\\mathcal{T}$ denotes the parameterized functional transformation\n"
            "- Objective is optimized over parameter space $\\min_\\theta \\mathbb{E}[\\mathcal{L}(\\mathbf{y}, \\hat{\\mathbf{y}})]$"
        ),
        walkthrough_steps=[
            f"Ingress signal is parsed and mapped into canonical representation space.",
            f"Core computational module applies parameterized transformation rules.",
            f"Intermediate state validation checks numerical stability and bounds.",
            f"Egress layer emits formatted output representation."
        ],
        engineering_insights=[
            "Maintain decoupled modular boundaries to allow independent unit testing and component benchmarking.",
            "Profile latency and memory footprint to identify bottlenecks early in development."
        ]
    )

    diag.add_canvas_container(
        x=60,
        y=40,
        width=1020,
        height=320,
        title=f"{clean_name.title()} Visual Flow & Architecture"
    )

    c1 = diag.add_zen_card(
        x=90, y=90, width=190, height=180,
        title="Ingress Signal",
        subtitle="Input & Schema",
        latex_formula="x \\in \\mathcal{X}",
        step_badge="Stage 1",
        theme="azure"
    )

    c2 = diag.add_zen_card(
        x=330, y=90, width=190, height=180,
        title="Core Engine",
        subtitle="Transformation",
        latex_formula="h = f(x; \\theta)",
        step_badge="Stage 2",
        theme="lavender"
    )

    c3 = diag.add_zen_card(
        x=570, y=90, width=190, height=180,
        title="State Evaluator",
        subtitle="Loss & Metrics",
        latex_formula="\\mathcal{L}(y, \\hat{y})",
        step_badge="Stage 3",
        theme="amber"
    )

    c4 = diag.add_zen_card(
        x=810, y=90, width=220, height=180,
        title="Egress Serving",
        subtitle="Verified Output",
        latex_formula="\\hat{y} = g(h)",
        step_badge="Stage 4",
        theme="sage"
    )

    diag.add_flow_arrow(c1, c2, label="Signals")
    diag.add_flow_arrow(c2, c3, label="State h")
    diag.add_flow_arrow(c3, c4, label="Outputs")

    return diag


class DiagramTemplateRegistry:
    """Registry routing concepts to specialized or dynamic diagram generators."""

    TEMPLATES = {
        "attention": get_transformer_attention_diagram,
        "transformer": get_transformer_attention_diagram,
        "self-attention": get_transformer_attention_diagram,
        "scaled dot-product": get_transformer_attention_diagram,
        "multi-head attention": get_transformer_attention_diagram,
        "backprop": get_backpropagation_diagram,
        "backpropagation": get_backpropagation_diagram,
        "gradient descent": get_backpropagation_diagram,
        "chain rule": get_backpropagation_diagram,
        "computational graph": get_backpropagation_diagram,
        "diffusion": get_diffusion_model_diagram,
        "diffusion models": get_diffusion_model_diagram,
        "ddpm": get_diffusion_model_diagram,
        "denoising": get_diffusion_model_diagram,
        "rag": get_rag_architecture_diagram,
        "retrieval": get_rag_architecture_diagram,
        "retrieval-augmented generation": get_rag_architecture_diagram,
        "vector search": get_rag_architecture_diagram,
        "resnet": get_resnet_residual_block_diagram,
        "residual": get_resnet_residual_block_diagram,
        "skip connection": get_resnet_residual_block_diagram,
        "residual connections": get_resnet_residual_block_diagram
    }

    @classmethod
    def get_diagram(cls, query: str, concept_name: Optional[str] = None) -> ExcalidrawDiagram:
        lookup_str = f"{concept_name or ''} {query}".lower()
        for key, builder in cls.TEMPLATES.items():
            if re.search(rf"\b{re.escape(key)}\b", lookup_str):
                return builder()

        # Fallback to universal dynamic synthesizer
        best_name = concept_name or query.replace("/draw", "").replace("/diagram", "").strip()
        return get_dynamic_diagram(best_name, query)


def get_diagram_for_concept(query: str, concept_name: Optional[str] = None) -> ExcalidrawDiagram:
    return DiagramTemplateRegistry.get_diagram(query, concept_name)
