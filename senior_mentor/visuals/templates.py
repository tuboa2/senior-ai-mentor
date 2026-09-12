"""Hierarchical Mind Map Templates for Senior AI Engineering Mentor.

Every diagram is built as an Obsidian-compatible Excalidraw concept decomposition
mind map (Libraries -> Methods & Code & Explanations & Synthesis -> Architecture Pipeline),
accompanied by rigorous LaTeX / KaTeX mathematical foundations.
"""

from typing import Dict, List, Optional
import re

from .excalidraw import (
    MindmapExcalidrawBuilder,
    MindmapMethod,
    MindmapOperation,
    MindmapTreeData
)


def get_log_return_transformation_diagram() -> MindmapExcalidrawBuilder:
    """Financial Data Science & Log-Return Transformation Mind Map."""
    data = MindmapTreeData(
        root_title="Log-Returns\nTransformation",
        libraries=["pandas", "numpy"],
        methods=[
            MindmapMethod(
                name="Natural Log Differencing",
                operations=[
                    MindmapOperation(
                        code="np.log(df)",
                        explanation="Computes the natural logarithm of every price value."
                    ),
                    MindmapOperation(
                        code="df.diff(1)",
                        explanation="Computes the difference between the current row and the previous row (row[t] - row[t-1])"
                    )
                ],
                synthesis_callout=(
                    "Since log(A / B) = log(A) - log(B), you can take the natural log of all prices first, "
                    "then take the first difference:\n  log_returns = np.log(prices_df).diff()"
                )
            ),
            MindmapMethod(
                name="Ratio with Lag Shift",
                operations=[
                    MindmapOperation(
                        code="df.shift(1)",
                        explanation="Moves every row down by 1 position (bringing yesterday's price into today's row)."
                    ),
                    MindmapOperation(
                        code="np.log(df / df.shift(1))",
                        explanation="Divides today's price by yesterday's price, then takes the natural log."
                    )
                ],
                synthesis_callout=(
                    "Both Option A and Option B yield identical mathematical results. Option A (np.log(df).diff()) "
                    "is typically preferred because .diff() is optimized in Cython."
                )
            ),
            MindmapMethod(
                name="From Percentage Change",
                operations=[
                    MindmapOperation(
                        code="df.pct_change()",
                        explanation="Calculates simple return R = (Price_today - Price_yesterday) / Price_yesterday."
                    ),
                    MindmapOperation(
                        code="np.log1p(simple_returns)",
                        explanation="Computes log(1 + R) with extra precision for numbers very close to zero."
                    )
                ]
            )
        ],
        pipeline_steps=[
            "Extract Close Prices",
            "Assemble Price Matrix",
            "Apply Log Transformation",
            "Clean the Boundary Row"
        ],
        pipeline_branch=("Assemble Price Matrix", "Combine into a single DataFrame"),
        intuition_markdown=(
            "Log returns (continuously compounded returns) offer several decisive mathematical advantages over simple percentage changes:\n"
            "- **Time Additivity:** Multi-period compounding is linear: $r_{0 \\to T} = \\sum_{t=1}^T r_t$.\n"
            "- **Symmetry:** Equal percentage upward and downward shocks are represented symmetrically.\n"
            "- **Statistical Tractability:** Prices are bounded below by zero, whereas log-prices and log-returns map smoothly to $(-\\infty, +\\infty)$."
        ),
        math_katex_markdown=(
            "### Mathematical Equivalence Formulation\n\n"
            "$$r_t = \\ln\\left(\\frac{P_t}{P_{t-1}}\\right) = \\ln(P_t) - \\ln(P_{t-1})$$\n\n"
            "Relation to simple returns $R_t = \\frac{P_t - P_{t-1}}{P_{t-1}}$:\n"
            "$$1 + R_t = \\frac{P_t}{P_{t-1}} \\implies r_t = \\ln(1 + R_t)$$\n\n"
            "First-order Taylor expansion around $R_t \\approx 0$:\n"
            "$$\\ln(1 + R_t) = R_t - \\frac{R_t^2}{2} + \\frac{R_t^3}{3} - \\dots \\approx R_t$$\n\n"
            "For small daily returns ($|R_t| < 0.05$), simple and log returns are almost indistinguishable, "
            "but over multi-day horizons additivity makes log returns vastly superior."
        ),
        engineering_insights_markdown=(
            "- **Boundary Condition Trap:** The first row after `.diff(1)` or `.shift(1)` evaluates to `NaN`. Always drop or handle row $t=0$ using `.dropna()` before feeding downstream models.\n"
            "- **Performance (Cython Vectorization):** `np.log(df).diff()` is significantly faster than `np.log(df / df.shift(1))` because `DataFrame.diff()` executes vectorized in Cython without allocating intermediate shifted arrays."
        )
    )
    builder = MindmapExcalidrawBuilder(data)
    builder.build_scene()
    return builder


def get_diffusion_model_diagram() -> MindmapExcalidrawBuilder:
    """Denoising Diffusion Probabilistic Models (DDPM) Mind Map."""
    data = MindmapTreeData(
        root_title="Denoising Diffusion\nProbabilistic Models",
        libraries=["torch", "diffusers", "einops"],
        methods=[
            MindmapMethod(
                name="Forward Noise Perturbation",
                operations=[
                    MindmapOperation(
                        code="torch.randn_like(x_0)",
                        explanation="Samples standard normal isotropic Gaussian noise vector epsilon ~ N(0, I)."
                    ),
                    MindmapOperation(
                        code="x_t = sqrt(alpha_bar)*x_0 + sqrt(1-alpha_bar)*eps",
                        explanation="Computes marginal noisy state directly at arbitrary timestep t in O(1)."
                    )
                ],
                synthesis_callout=(
                    "Reparameterization property: q(x_t | x_0) = N(x_t; sqrt(alpha_bar_t)*x_0, (1-alpha_bar_t)*I). "
                    "This eliminates sequential Markov simulation during training, allowing parallel loss evaluation at random timesteps."
                )
            ),
            MindmapMethod(
                name="Reverse Noise Estimator",
                operations=[
                    MindmapOperation(
                        code="eps_pred = unet(x_t, t)",
                        explanation="U-Net with cross-attention predicts the exact injected noise vector epsilon."
                    ),
                    MindmapOperation(
                        code="loss = F.mse_loss(eps_pred, eps)",
                        explanation="Calculates simplified variational bound loss ||eps - eps_pred||^2."
                    )
                ],
                synthesis_callout=(
                    "Optimizing MSE on predicted noise matches denoising score matching: "
                    "nabla_{x_t} log q(x_t) = -eps_theta(x_t, t) / sqrt(1 - alpha_bar_t). "
                    "The neural network directly learns the score function of data distribution."
                )
            ),
            MindmapMethod(
                name="Inference Denoising Loop",
                operations=[
                    MindmapOperation(
                        code="scheduler.step(eps_pred, t, x_t)",
                        explanation="Subtracts estimated noise and injects scaled variance sigma_t * z."
                    ),
                    MindmapOperation(
                        code="torch.clamp(x_pred, -1.0, 1.0)",
                        explanation="Restricts reconstructed latent coordinates to valid physical tensor range."
                    )
                ],
                synthesis_callout=(
                    "DDIM (Denoising Diffusion Implicit Models) enables non-Markovian deterministic sampling trajectories, "
                    "reducing inference latency from 1,000 steps to 20-50 steps without retraining."
                )
            )
        ],
        pipeline_steps=[
            "Clean Data Ingress x_0",
            "Noise Schedule beta_t",
            "U-Net Score Prediction",
            "Reverse Langevin Step",
            "Denoised Output x_0"
        ],
        pipeline_branch=("U-Net Score Prediction", "Conditioning Prompt Embeddings"),
        intuition_markdown=(
            "Diffusion models generate complex probability distributions through learned thermodynamic reversal:\n"
            "- **Forward Markov Process ($q$):** Pure information $\\mathbf{x}_0$ is systematically corrupted with Gaussian perturbation over $T$ steps until matching isotropic noise $\\mathcal{N}(0, \\mathbf{I})$.\n"
            "- **Reverse Denoising ($p_\\theta$):** A neural network learns the local vector field pointing back toward regions of high probability density (the score function)."
        ),
        math_katex_markdown=(
            "### Forward Transition Dynamics\n\n"
            "$$q(\\mathbf{x}_t \\mid \\mathbf{x}_{t-1}) = \\mathcal{N}\\left(\\mathbf{x}_t; \\sqrt{1 - \\beta_t}\\mathbf{x}_{t-1}, \\beta_t \\mathbf{I}\\right)$$\n\n"
            "Marginal closed-form distribution jumping directly from $t=0$ to $t$:\n"
            "$$q(\\mathbf{x}_t \\mid \\mathbf{x}_0) = \\mathcal{N}\\left(\\mathbf{x}_t; \\sqrt{\\bar{\\alpha}_t}\\mathbf{x}_0, (1 - \\bar{\\alpha}_t)\\mathbf{I}\\right)$$\n\n"
            "Where $\\alpha_t = 1 - \\beta_t$ and $\\bar{\\alpha}_t = \\prod_{s=1}^t \\alpha_s$.\n\n"
            "### Simplified Training Objective\n\n"
            "$$\\mathcal{L}_{\\text{simple}}(\\theta) = \\mathbb{E}_{t, \\mathbf{x}_0, \\boldsymbol{\\epsilon}}\\left[ "
            "\\left\\| \\boldsymbol{\\epsilon} - \\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, t) \\right\\|^2 \\right]$$\n\n"
            "### Reverse Denoising Transition\n\n"
            "$$p_\\theta(\\mathbf{x}_{t-1} \\mid \\mathbf{x}_t) = \\mathcal{N}\\left(\\mathbf{x}_{t-1}; \\boldsymbol{\\mu}_\\theta(\\mathbf{x}_t, t), \\sigma_t^2 \\mathbf{I}\\right)$$\n\n"
            "$$\\boldsymbol{\\mu}_\\theta(\\mathbf{x}_t, t) = \\frac{1}{\\sqrt{\\alpha_t}}\\left(\\mathbf{x}_t - \\frac{\\beta_t}{\\sqrt{1 - \\bar{\\alpha}_t}}\\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, t)\\right)$$"
        ),
        engineering_insights_markdown=(
            "- **Latent Space Compression:** Running diffusion in raw pixel space ($3 \\times 512 \\times 512 = 786{,}432$ dimensions) is computationally prohibitive. A VAE compresses images into latent space ($4 \\times 64 \\times 64 = 16{,}384$ dimensions), accelerating training by $48\\times$.\n"
            "- **Classifier-Free Guidance (CFG):** Interpolating between unconditional and conditional noise estimates $\\tilde{\\epsilon} = \\epsilon_\\emptyset + s \\cdot (\\epsilon_c - \\epsilon_\\emptyset)$ with scale $s \\in [5, 8]$ improves prompt adherence at the cost of sample diversity."
        )
    )
    builder = MindmapExcalidrawBuilder(data)
    builder.build_scene()
    return builder


def get_transformer_attention_diagram() -> MindmapExcalidrawBuilder:
    """Scaled Dot-Product & Multi-Head Attention Mind Map."""
    data = MindmapTreeData(
        root_title="Transformer Attention\nMechanism",
        libraries=["torch", "torch.nn.functional", "einops"],
        methods=[
            MindmapMethod(
                name="Scaled Dot-Product",
                operations=[
                    MindmapOperation(
                        code="scores = (Q @ K.mT) / math.sqrt(d_k)",
                        explanation="Computes pairwise alignment energy between all query-key token pairs."
                    ),
                    MindmapOperation(
                        code="attn = F.softmax(scores, dim=-1)",
                        explanation="Normalizes raw compatibility logits across context dimension into probability simplex."
                    )
                ],
                synthesis_callout=(
                    "Since Var(Q·K) = d_k, dividing by sqrt(d_k) preserves unit variance Var(scores) = 1. "
                    "Without scaling, large dot-product magnitudes push softmax into vanishing gradient saturation regions."
                )
            ),
            MindmapMethod(
                name="FlashAttention Kernel",
                operations=[
                    MindmapOperation(
                        code="flash_attn_func(q, k, v)",
                        explanation="Fuses QK^T MatMul, Softmax, and Value reduction into a single GPU SRAM kernel."
                    ),
                    MindmapOperation(
                        code="recompute_grad_in_backward()",
                        explanation="Recomputes attention matrix during backward pass instead of caching in VRAM."
                    )
                ],
                synthesis_callout=(
                    "FlashAttention reduces memory complexity from O(N^2) to O(N) by tiling inputs in GPU SRAM "
                    "and computing softmax running normalizers online without materializing the N x N matrix in HBM."
                )
            ),
            MindmapMethod(
                name="Causal Autoregressive Mask",
                operations=[
                    MindmapOperation(
                        code="scores.masked_fill_(mask == 0, -1e9)",
                        explanation="Masks upper-triangular future token positions with negative infinity before softmax."
                    ),
                    MindmapOperation(
                        code="out = torch.matmul(attn, V)",
                        explanation="Computes contextual representations as weighted combinations of Value feature vectors."
                    )
                ]
            )
        ],
        pipeline_steps=[
            "Token Ingress",
            "Linear Projections QKV",
            "Scaled MatMul QK^T",
            "Softmax Simplex",
            "Value Aggregation",
            "Output Projection W_o"
        ],
        pipeline_branch=("Scaled MatMul QK^T", "Apply Causal Mask (-inf)"),
        intuition_markdown=(
            "Attention operates as a high-dimensional soft content-addressable memory:\n"
            "- **Query ($Q$):** Specifies the information need of the target token.\n"
            "- **Key ($K$):** Acts as descriptive indexing tags on context tokens.\n"
            "- **Value ($V$):** Contains the retrieved feature payload.\n\n"
            "Pairwise inner products evaluate geometric alignment, normalized by Softmax to compute expectation weights over $V$."
        ),
        math_katex_markdown=(
            "### Scaled Dot-Product Attention Equation\n\n"
            "$$\\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = "
            "\\text{softmax}\\left(\\frac{\\mathbf{Q}\\mathbf{K}^T}{\\sqrt{d_k}} + \\mathbf{M}\\right) \\mathbf{V}$$\n\n"
            "Where:\n"
            "- $\\mathbf{Q} \\in \\mathbb{R}^{n \\times d_k}, \\quad \\mathbf{K} \\in \\mathbb{R}^{m \\times d_k}, \\quad \\mathbf{V} \\in \\mathbb{R}^{m \\times d_v}$\n"
            "- Causal mask $\\mathbf{M}_{ij} = 0$ for $j \\le i$ and $-\\infty$ for $j > i$.\n\n"
            "### Multi-Head Decomposition\n\n"
            "$$\\text{MultiHead}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = \\text{Concat}(\\text{head}_1, \\dots, \\text{head}_h) \\mathbf{W}^O$$\n\n"
            "$$\\text{head}_i = \\text{Attention}(\\mathbf{Q}\\mathbf{W}_i^Q, \\mathbf{K}\\mathbf{W}_i^K, \\mathbf{V}\\mathbf{W}_i^V)$$"
        ),
        engineering_insights_markdown=(
            "- **KV Cache in Serving:** During autoregressive token generation, past $K$ and $V$ vectors are cached in GPU VRAM, converting per-step generation cost from $O(n^2)$ to $O(n)$.\n"
            "- **Rotary Position Embeddings (RoPE):** Multiplies query and key vectors by complex rotation matrices $R_{\\Theta, m}^d$, injecting relative distance directly into the dot-product: $\\langle R_m q, R_n k \\rangle = g(q, k, m-n)$."
        )
    )
    builder = MindmapExcalidrawBuilder(data)
    builder.build_scene()
    return builder


def get_backpropagation_diagram() -> MindmapExcalidrawBuilder:
    """Computational Graph & Backpropagation Mind Map."""
    data = MindmapTreeData(
        root_title="Computational Graph\n& Backpropagation",
        libraries=["torch.autograd", "torch.nn"],
        methods=[
            MindmapMethod(
                name="Forward Activation Pass",
                operations=[
                    MindmapOperation(
                        code="z = torch.matmul(W, a_prev) + b",
                        explanation="Computes affine linear weighted combination of upstream layer activations."
                    ),
                    MindmapOperation(
                        code="a = torch.relu(z)",
                        explanation="Applies non-linear activation gate producing layer output representations."
                    )
                ],
                synthesis_callout=(
                    "In the forward pass, intermediate tensors a_prev and z must be retained in memory (activation caching) "
                    "because they are required to compute parameter gradients during the backward pass."
                )
            ),
            MindmapMethod(
                name="Reverse Adjoint Chain Rule",
                operations=[
                    MindmapOperation(
                        code="delta = torch.matmul(W_next.T, delta_next) * relu_prime(z)",
                        explanation="Computes upstream error vector delta via transposed downstream weights and local derivative."
                    ),
                    MindmapOperation(
                        code="grad_W = torch.outer(delta, a_prev)",
                        explanation="Calculates exact parameter gradient as outer product of error and activations."
                    )
                ],
                synthesis_callout=(
                    "Multivariable chain rule: partial L / partial W^[l] = delta^[l] (a^[l-1])^T. "
                    "Adjoint error vectors propagate perturbation signals backward in reverse topological order in O(1) pass."
                )
            ),
            MindmapMethod(
                name="Optimizer Update Step",
                operations=[
                    MindmapOperation(
                        code="W.data.add_(-lr * grad_W)",
                        explanation="Adjusts weights against the direction of steepest loss ascent."
                    ),
                    MindmapOperation(
                        code="optimizer.zero_grad(set_to_none=True)",
                        explanation="Frees accumulated gradient buffers to prevent gradient leakage across training iterations."
                    )
                ]
            )
        ],
        pipeline_steps=[
            "Input Tensor a_0",
            "Affine Linear Sum Wx+b",
            "Activation Gate sigma(z)",
            "Loss Criterion L(y, y_hat)",
            "Accumulate Gradients"
        ],
        pipeline_branch=("Loss Criterion L(y, y_hat)", "Compute Loss Adjoint dL/dy_hat"),
        intuition_markdown=(
            "Backpropagation is reverse-mode automatic differentiation applied to an acyclic computation graph:\n"
            "- **Forward:** Information cascades from input variables to compute objective scalar loss $\\mathcal{L}$.\n"
            "- **Backward:** A scalar perturbation of 1.0 at $\\mathcal{L}$ propagates upstream, calculating sensitivity derivatives $\\frac{\\partial \\mathcal{L}}{\\partial \\theta}$ for every parameter."
        ),
        math_katex_markdown=(
            "### Forward Equations\n\n"
            "$$\\mathbf{z}^{[l]} = \\mathbf{W}^{[l]} \\mathbf{a}^{[l-1]} + \\mathbf{b}^{[l]}, \\quad \\mathbf{a}^{[l]} = \\sigma(\\mathbf{z}^{[l]})$$\n\n"
            "### Backward Adjoint Error Vector\n\n"
            "$$\\boldsymbol{\\delta}^{[l]} \\equiv \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{z}^{[l]}} = "
            "\\left( (\\mathbf{W}^{[l+1]})^T \\boldsymbol{\\delta}^{[l+1]} \\right) \\odot \\sigma'(\\mathbf{z}^{[l]})$$\n\n"
            "### Parameter Gradient Outer Products\n\n"
            "$$\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{W}^{[l]}} = \\boldsymbol{\\delta}^{[l]} (\\mathbf{a}^{[l-1]})^T, "
            "\\quad \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{b}^{[l]}} = \\sum_{\\text{batch}} \\boldsymbol{\\delta}^{[l]}$$"
        ),
        engineering_insights_markdown=(
            "- **Gradient Saturation Trap:** If sigmoid or tanh activations are used, saturation occurs when $|z| \\gg 1$, driving $\\sigma'(z) \\to 0$ and killing gradient flow. ReLU, GELU, and SwiGLU avoid negative saturation.\n"
            "- **Gradient Checkpointing:** Recomputes activations dynamically in the backward pass rather than caching all layer outputs, reducing peak activation VRAM by $4\\times$."
        )
    )
    builder = MindmapExcalidrawBuilder(data)
    builder.build_scene()
    return builder


def get_rag_architecture_diagram() -> MindmapExcalidrawBuilder:
    """Production Retrieval-Augmented Generation (RAG) Mind Map."""
    data = MindmapTreeData(
        root_title="Retrieval-Augmented\nGeneration (RAG)",
        libraries=["faiss", "sentence-transformers", "langchain"],
        methods=[
            MindmapMethod(
                name="Dense Semantic Retrieval",
                operations=[
                    MindmapOperation(
                        code="q_emb = encoder.encode(query)",
                        explanation="Maps user query into dense high-dimensional semantic embedding space."
                    ),
                    MindmapOperation(
                        code="D, I = index.search(q_emb, k=5)",
                        explanation="Conducts approximate nearest neighbor search over HNSW vector index."
                    )
                ],
                synthesis_callout=(
                    "Dense cosine similarity captures semantic intent and synonymy that lexical keyword matching misses: "
                    "sim(q, d) = (e_q · e_d) / (||e_q|| ||e_d||)."
                )
            ),
            MindmapMethod(
                name="BM25 Sparse Retrieval",
                operations=[
                    MindmapOperation(
                        code="bm25.get_scores(tokenized_query)",
                        explanation="Scores term frequency and inverse document frequency for exact keyword hits."
                    ),
                    MindmapOperation(
                        code="reciprocal_rank_fusion(dense, sparse)",
                        explanation="Merges ranking positions from dense and sparse retrieval to mitigate blind spots."
                    )
                ],
                synthesis_callout=(
                    "Hybrid Retrieval combines dense cosine similarity with BM25 keyword matching via Reciprocal Rank Fusion (RRF), "
                    "preventing hallucinations on acronyms, IDs, and domain-specific terminology."
                )
            ),
            MindmapMethod(
                name="Cross-Encoder Reranking",
                operations=[
                    MindmapOperation(
                        code="reranker.predict([[q, doc] for doc in cand])",
                        explanation="Jointly attends across full query-document pairs to produce calibrated relevance scores."
                    ),
                    MindmapOperation(
                        code="assemble_prompt(top_k_docs, query)",
                        explanation="Constructs structured context window with citation bounds for generation."
                    )
                ]
            )
        ],
        pipeline_steps=[
            "Document Ingestion",
            "Recursive Chunking",
            "Vector Graph Indexing",
            "Hybrid Retrieval & Rerank",
            "Grounded LLM Output"
        ],
        pipeline_branch=("Vector Graph Indexing", "Store Document Metadata"),
        intuition_markdown=(
            "RAG provides language models with verified open-book external memory:\n"
            "- **Ingestion:** Enterprise corpora are chunked, embedded, and structured in high-dimensional vector space.\n"
            "- **Retrieval:** User queries retrieve relevant grounding passages via hybrid semantic + lexical search.\n"
            "- **Synthesis:** The LLM generates factual responses grounded directly in cited evidence."
        ),
        math_katex_markdown=(
            "### Cosine Distance Metric\n\n"
            "$$\\text{sim}(\\mathbf{q}, \\mathbf{d}_i) = \\frac{\\mathbf{e}_q \\cdot \\mathbf{e}_{d_i}}{\\|\\mathbf{e}_q\\| \\|\\mathbf{e}_{d_i}\\|} = \\cos(\\theta)$$\n\n"
            "### Reciprocal Rank Fusion (RRF)\n\n"
            "$$\\text{RRF\\_Score}(d \\in \\mathcal{D}) = \\sum_{m \\in \\{\\text{dense}, \\text{sparse}\\}} \\frac{1}{k + r_m(d)}$$\n\n"
            "Where $r_m(d)$ is the rank position of passage $d$ in retrieval system $m$, and $k \\approx 60$ is a smoothing constant."
        ),
        engineering_insights_markdown=(
            "- **Chunk Size Boundary Dilemma:** Chunks smaller than 200 tokens lose context; chunks larger than 800 tokens dilute vector representations. 300-500 tokens with 10% overlap is standard.\n"
            "- **Lost-in-the-Middle Phenomenon:** Attention sinks prioritize tokens at prompt boundaries. Place the most critical retrieved evidence at the start and end of the context prompt."
        )
    )
    builder = MindmapExcalidrawBuilder(data)
    builder.build_scene()
    return builder


def get_dynamic_diagram(concept: str, query: str) -> MindmapExcalidrawBuilder:
    """Universal Dynamic Mind Map Synthesizer for arbitrary technical queries."""
    clean_name = concept.replace("/draw", "").replace("/diagram", "").strip() if concept else "System Architecture"
    words = [w.capitalize() for w in clean_name.split()]
    title_display = "\n".join(words[:2]) if len(words) >= 2 else words[0]

    data = MindmapTreeData(
        root_title=title_display,
        libraries=["torch", "numpy", "scipy"],
        methods=[
            MindmapMethod(
                name="Primary Formulation",
                operations=[
                    MindmapOperation(
                        code="state = transform(inputs)",
                        explanation="Transforms raw input signals into normalized representation space."
                    ),
                    MindmapOperation(
                        code="loss = criterion(state, targets)",
                        explanation="Evaluates objective divergence and computes numerical optimization loss."
                    )
                ],
                synthesis_callout=(
                    f"Core mathematical invariant for {clean_name}: "
                    "minimizing risk objective min_theta E[L(y, f(x; theta))] while maintaining numerical stability."
                )
            ),
            MindmapMethod(
                name="Optimized Implementation",
                operations=[
                    MindmapOperation(
                        code="optimized_kernel(inputs)",
                        explanation="Executes vectorized compute path minimizing memory allocation overhead."
                    ),
                    MindmapOperation(
                        code="validate_bounds(outputs)",
                        explanation="Performs defensive assertions checking for NaN, Inf, and boundary anomalies."
                    )
                ],
                synthesis_callout=(
                    "Vectorized operations reduce runtime complexity and prevent CPU-GPU synchronization bottlenecks."
                )
            )
        ],
        pipeline_steps=[
            "Data Ingress",
            "Feature Engineering",
            "State Transformation",
            "Loss Optimization",
            "Verified Output"
        ],
        pipeline_branch=("State Transformation", "Cache Intermediate State"),
        intuition_markdown=(
            f"The **{clean_name}** framework structures transformations through modular, decoupled stages:\n"
            "- **Ingress & Parsing:** Inputs are validated against schema boundaries.\n"
            "- **Core Dynamics:** Mathematical operators transform feature representations.\n"
            "- **Egress:** Predictions are verified for stability and emitted downstream."
        ),
        math_katex_markdown=(
            f"### Mathematical Dynamics for {clean_name}\n\n"
            "$$\\mathbf{h}_{t} = \\mathcal{T}\\left(\\mathbf{h}_{t-1}, \\mathbf{x}_t; \\boldsymbol{\\theta}\\right)$$\n\n"
            "Optimization objective across parameter space:\n"
            "$$\\boldsymbol{\\theta}^* = \\operatorname{arg\\,min}_{\\boldsymbol{\\theta}} \\mathbb{E}_{(\\mathbf{x}, \\mathbf{y})}\\left[ \\mathcal{L}\\left(\\mathbf{y}, f(\\mathbf{x}; \\boldsymbol{\\theta})\\right) \\right]$$"
        ),
        engineering_insights_markdown=(
            "- **Defensive Programming:** Add runtime assertions verifying tensor shapes and non-NaN values before state mutation.\n"
            "- **Decoupled Architecture:** Separate pure algorithmic computations from I/O boundaries to enable independent unit testing."
        )
    )
    builder = MindmapExcalidrawBuilder(data)
    builder.build_scene()
    return builder


class DiagramTemplateRegistry:
    """Registry routing concepts to specialized or dynamic mind map generators."""

    TEMPLATES = {
        "log return": get_log_return_transformation_diagram,
        "log-return": get_log_return_transformation_diagram,
        "log_return": get_log_return_transformation_diagram,
        "returns": get_log_return_transformation_diagram,
        "diffusion": get_diffusion_model_diagram,
        "diffusion models": get_diffusion_model_diagram,
        "ddpm": get_diffusion_model_diagram,
        "denoising": get_diffusion_model_diagram,
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
        "rag": get_rag_architecture_diagram,
        "retrieval": get_rag_architecture_diagram,
        "retrieval-augmented generation": get_rag_architecture_diagram
    }

    @classmethod
    def get_diagram(cls, query: str, concept_name: Optional[str] = None) -> MindmapExcalidrawBuilder:
        lookup_str = f"{concept_name or ''} {query}".lower()
        for key, builder in cls.TEMPLATES.items():
            if re.search(rf"\b{re.escape(key)}\b", lookup_str):
                return builder()
        return get_dynamic_diagram(concept_name or query, query)


def get_diagram_for_concept(query: str, concept_name: Optional[str] = None) -> MindmapExcalidrawBuilder:
    return DiagramTemplateRegistry.get_diagram(query, concept_name)
