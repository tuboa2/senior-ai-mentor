"""Engineering and AI Knowledge Graph.

Models concepts, mathematical foundations, prerequisites, failure modes,
and gap-identification algorithms for adaptive learning.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

@dataclass
class ConceptNode:
    name: str
    domain: str
    difficulty: str  # "Foundational", "Intermediate", "Advanced", "Staff/Principal"
    prerequisites: List[str] = field(default_factory=list)
    leads_to: List[str] = field(default_factory=list)
    common_pitfalls: List[str] = field(default_factory=list)
    first_principles_formulation: str = ""
    practical_implementation_notes: str = ""

class KnowledgeGraph:
    def __init__(self):
        self.nodes: Dict[str, ConceptNode] = {}
        self._populate_core_graph()

    def add_node(self, node: ConceptNode) -> None:
        self.nodes[node.name.lower()] = node

    def get_concept(self, name: str) -> Optional[ConceptNode]:
        return self.nodes.get(name.lower())

    def get_prerequisites_recursive(self, name: str, visited: Optional[Set[str]] = None) -> List[ConceptNode]:
        """Returns all transitive prerequisites in topological dependency order."""
        if visited is None:
            visited = set()
        node = self.get_concept(name)
        if not node:
            return []
        prereqs: List[ConceptNode] = []
        for p_name in node.prerequisites:
            p_key = p_name.lower()
            if p_key not in visited:
                visited.add(p_key)
                p_node = self.get_concept(p_key)
                if p_node:
                    prereqs.extend(self.get_prerequisites_recursive(p_key, visited))
                    prereqs.append(p_node)
        return prereqs

    def identify_knowledge_gaps(self, target_concept: str, proficiencies: Dict[str, float], threshold: float = 0.6) -> List[ConceptNode]:
        """Identifies any prerequisites of the target concept where proficiency is below threshold."""
        prereqs = self.get_prerequisites_recursive(target_concept)
        gaps = []
        for p in prereqs:
            prof = proficiencies.get(p.name.lower(), 0.0)
            if prof < threshold:
                gaps.append(p)
        return gaps

    def search(self, query: str) -> List[ConceptNode]:
        q = query.lower()
        results = []
        for node in self.nodes.values():
            if q in node.name.lower() or q in node.domain.lower() or any(q in p.lower() for p in node.common_pitfalls):
                results.append(node)
        return results

    def get_concept_context(self, concept_name: str, memory_store) -> Dict:
        """Links the concept node to project memory, past misconceptions, and prerequisites."""
        node = self.get_concept(concept_name)
        if not node:
            return {}
        prereqs = self.get_prerequisites_recursive(concept_name)
        projects = memory_store.get_projects_for_concept(concept_name)
        misconceptions = memory_store.get_misconceptions_for_concept(concept_name)
        return {
            "concept": node,
            "prerequisites": [p.name for p in prereqs],
            "applied_in_projects": [p.name for p in projects],
            "past_misconceptions": [m.pattern_description for m in misconceptions]
        }

    def _populate_core_graph(self) -> None:
        # Mathematics & Foundations
        self.add_node(ConceptNode(
            name="Linear Algebra: Eigenvectors & SVD",
            domain="Mathematics",
            difficulty="Foundational",
            prerequisites=[],
            leads_to=["Principal Component Analysis", "Low-Rank Adaptation (LoRA)"],
            common_pitfalls=[
                "Confusing eigenvectors with singular vectors in non-square matrices.",
                "Forgetting that covariance matrix must be symmetric and positive semi-definite."
            ],
            first_principles_formulation="Av = λv. SVD decomposes any A ∈ R^{m×n} into U Σ V^T.",
            practical_implementation_notes="Use scipy.linalg.svd or torch.linalg.svd. Watch for sign ambiguity across implementations."
        ))

        self.add_node(ConceptNode(
            name="Gradient Descent & Convex Optimization",
            domain="Mathematics",
            difficulty="Foundational",
            prerequisites=[],
            leads_to=["Backpropagation", "Adam & Adaptive Optimizers"],
            common_pitfalls=[
                "Choosing learning rate too high causing loss explosion or NaN gradients.",
                "Assuming non-convex neural net loss landscapes have severe local minima rather than saddle points."
            ],
            first_principles_formulation="θ_{t+1} = θ_t - η ∇_θ L(θ).",
            practical_implementation_notes="Always clip gradients (torch.nn.utils.clip_grad_norm_) in deep networks."
        ))

        # Core Statistics & Data Science
        self.add_node(ConceptNode(
            name="Hypothesis Testing & Multiple Comparisons",
            domain="Statistics",
            difficulty="Intermediate",
            prerequisites=[],
            leads_to=["A/B Testing & Causal Inference", "Offline Model Evaluation"],
            common_pitfalls=[
                "Treating p > 0.05 as proof of the null hypothesis.",
                "Evaluating 50 features or model variants without Benjamini-Hochberg or Bonferroni correction (p-hacking).",
                "Failing to verify variance homogeneity before running Student's t-test."
            ],
            first_principles_formulation="FWER = 1 - (1 - α)^k. False Discovery Rate (FDR) = E[V / R].",
            practical_implementation_notes="Use statsmodels.stats.multitest.multipletests or validate_stats.py."
        ))

        self.add_node(ConceptNode(
            name="Data Leakage & Cross-Validation Strategy",
            domain="Statistics",
            difficulty="Intermediate",
            prerequisites=["Hypothesis Testing & Multiple Comparisons"],
            leads_to=["Production ML Pipelines"],
            common_pitfalls=[
                "Fitting scalers or imputers before splitting folds.",
                "Random K-Fold on time-series data introducing future lookahead bias.",
                "Target leakage through proxy columns generated downstream."
            ],
            first_principles_formulation="Information flow P(X_test | X_train) must be strictly zero prior to model evaluation.",
            practical_implementation_notes="Wrap transformations in sklearn Pipeline or ColumnTransformer."
        ))

        # Classical Machine Learning
        self.add_node(ConceptNode(
            name="Principal Component Analysis",
            domain="Machine Learning",
            difficulty="Intermediate",
            prerequisites=["Linear Algebra: Eigenvectors & SVD"],
            leads_to=["Dimensionality Reduction", "Feature Embeddings"],
            common_pitfalls=[
                "Failing to center (subtract mean) and standardize data before PCA.",
                "Interpreting principal components as causal latent factors."
            ],
            first_principles_formulation="Maximizes variance: max w^T S w subject to ||w||_2 = 1.",
            practical_implementation_notes="sklearn.decomposition.PCA automatically centers data; check explained_variance_ratio_."
        ))

        self.add_node(ConceptNode(
            name="Gradient Boosted Decision Trees (XGBoost/LightGBM)",
            domain="Machine Learning",
            difficulty="Intermediate",
            prerequisites=["Gradient Descent & Convex Optimization", "Data Leakage & Cross-Validation Strategy"],
            leads_to=["Production ML Pipelines", "Ranking Systems"],
            common_pitfalls=[
                "Overfitting depth on noisy tabular data.",
                "Failing to tune subsample and colsample_bytree.",
                "Neglecting monotonic constraints on domain-critical features."
            ],
            first_principles_formulation="Additive model: f_m(x) = f_{m-1}(x) + η h_m(x), fitting pseudo-residuals via second-order Taylor expansion.",
            practical_implementation_notes="LightGBM histogram binning is faster; monitor out-of-fold validation."
        ))

        # Deep Learning & Transformers
        self.add_node(ConceptNode(
            name="Backpropagation & Autograd Mechanics",
            domain="Deep Learning",
            difficulty="Intermediate",
            prerequisites=["Gradient Descent & Convex Optimization"],
            leads_to=["Transformer Architecture & Attention", "Distributed Training (DDP/FSDP)"],
            common_pitfalls=[
                "Retaining computation graph accidentally (storing tensor instead of tensor.item() in loss tracker).",
                "Calling loss.backward() without zeroing gradients (optimizer.zero_grad())."
            ],
            first_principles_formulation="Reverse-mode automatic differentiation via multivariate chain rule: ∂L/∂x_i = ∑_j (∂L/∂y_j)(∂y_j/∂x_i).",
            practical_implementation_notes="Inspect with torch.autograd.set_detect_anomaly(True) when debugging NaNs."
        ))

        self.add_node(ConceptNode(
            name="Transformer Architecture & Attention",
            domain="Deep Learning",
            difficulty="Advanced",
            prerequisites=["Backpropagation & Autograd Mechanics", "Linear Algebra: Eigenvectors & SVD"],
            leads_to=["LLM Pretraining & Fine-Tuning", "Retrieval-Augmented Generation (RAG)"],
            common_pitfalls=[
                "Quadratic O(N^2) memory scaling in standard self-attention without FlashAttention.",
                "Causal masking omissions in autoregressive decoders allowing lookahead.",
                "Misunderstanding rotary position embeddings (RoPE) relative rotation vs absolute positional embeddings."
            ],
            first_principles_formulation="Attention(Q, K, V) = softmax(Q K^T / √d_k) V.",
            practical_implementation_notes="Use FlashAttention-2 / SDPA kernels (torch.nn.functional.scaled_dot_product_attention)."
        ))

        # Modern LLM Systems & AI Engineering
        self.add_node(ConceptNode(
            name="Retrieval-Augmented Generation (RAG)",
            domain="AI Engineering",
            difficulty="Advanced",
            prerequisites=["Transformer Architecture & Attention", "Data Leakage & Cross-Validation Strategy"],
            leads_to=["Multi-Agent Architectures & Tool Use"],
            common_pitfalls=[
                "Naive cosine similarity retrieval on mismatched semantic chunks.",
                "Ignoring chunk boundary context splitting sentences awkwardly.",
                "Lack of reranking (cross-encoders) and synthetic query expansion (HyDE)."
            ],
            first_principles_formulation="p(y | x) = ∑_z p(y | x, z) p(z | x), where z are retrieved chunks.",
            practical_implementation_notes="Implement hybrid search (BM25 + dense vector embeddings) + cross-encoder reranker."
        ))

        self.add_node(ConceptNode(
            name="Multi-Agent Architectures & Tool Use",
            domain="AI Engineering",
            difficulty="Staff/Principal",
            prerequisites=["Retrieval-Augmented Generation (RAG)"],
            leads_to=["Autonomous Self-Improvement"],
            common_pitfalls=[
                "Agent proliferation without clear separation of responsibilities.",
                "Manufacturing artificial consensus instead of exposing structural trade-offs.",
                "Lack of bounded execution sandboxes and prompt injection defense."
            ],
            first_principles_formulation="Distributed state machine with progressive disclosure, role-bounded cognition, and sandboxed execution.",
            practical_implementation_notes="Adopt Model Context Protocol (MCP) and principle of least privilege."
        ))

        self.add_node(ConceptNode(
            name="Low-Rank Adaptation (LoRA) & Parameter-Efficient Tuning",
            domain="Deep Learning",
            difficulty="Advanced",
            prerequisites=["Transformer Architecture & Attention", "Linear Algebra: Eigenvectors & SVD"],
            leads_to=["Production ML Pipelines"],
            common_pitfalls=[
                "Only adapting query/value matrices when MLP projection weights contain substantial task knowledge.",
                "Selecting rank r too high without stabilizing scaling factor α."
            ],
            first_principles_formulation="W' = W_0 + ΔW = W_0 + (α/r) B A, where B ∈ R^{d×r}, A ∈ R^{r×k}, r ≪ min(d, k).",
            practical_implementation_notes="Use HuggingFace peft library with QLoRA 4-bit base weights for memory efficiency."
        ))
