"""Engineering and AI Knowledge Graph.

Models concepts, mathematical foundations, prerequisites, failure modes,
and gap-identification algorithms for adaptive learning.
"""

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

@dataclass
class ConceptNode:
    name: str
    domain: str
    difficulty: str  # "Foundational", "Intermediate", "Advanced", "Staff/Principal"
    prerequisites: List[str] = field(default_factory=list)
    leads_to: List[str] = field(default_factory=list)
    common_pitfalls: List[str] = field(default_factory=list)
    aliases: List[str] = field(default_factory=list)
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
        """Finds concepts matching the query based on exact match, aliases, pitfalls, and token overlap."""
        q = query.lower().strip()
        if not q:
            return []

        tokens = set(re.findall(r"\b[a-zA-Z0-9_\-]{3,}\b", q))
        stop_words = {
            "what", "when", "where", "which", "with", "from", "that", "this", "about",
            "should", "could", "would", "how", "why", "the", "and", "for", "give", "please",
            "want", "need", "using", "into", "onto", "over"
        }
        meaningful_tokens = tokens - stop_words

        scored_results: List[Tuple[float, ConceptNode]] = []
        for node in self.nodes.values():
            score = 0.0
            node_name_lower = node.name.lower()
            node_domain_lower = node.domain.lower()

            # 1. Exact or substring match in name
            if node_name_lower in q:
                score += 20.0
            elif q in node_name_lower:
                score += 15.0

            # 2. Alias match
            for alias in getattr(node, "aliases", []):
                alias_lower = alias.lower()
                if alias_lower in q:
                    score += 14.0
                elif q in alias_lower:
                    score += 9.0

            # 3. Pitfall keyword match
            for pitfall in node.common_pitfalls:
                pit_lower = pitfall.lower()
                if any(phrase in q for phrase in [pit_lower[:25]]):
                    score += 8.0

            # 4. Token overlap
            all_node_text = f"{node_name_lower} {' '.join(getattr(node, 'aliases', []))}"
            node_tokens = set(re.findall(r"\b[a-zA-Z0-9_\-]{3,}\b", all_node_text)) - stop_words
            overlap = meaningful_tokens.intersection(node_tokens)
            if overlap:
                score += len(overlap) * 3.5

            # 5. Domain match
            if node_domain_lower in q:
                score += 2.0

            if score > 0:
                scored_results.append((score, node))

        # Sort descending by score
        scored_results.sort(key=lambda x: x[0], reverse=True)
        return [node for _, node in scored_results]

    def get_concept_context(self, concept_name: str, memory_store: Any) -> Dict[str, Any]:
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
            aliases=["svd", "singular value decomposition", "eigenvector", "eigenvalue", "eigenvalues", "matrix decomposition", "linear algebra", "null space", "spectral"],
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
            aliases=["gradient descent", "convex optimization", "learning rate", "loss landscape", "optimizer", "sgd", "adam", "convexity", "saddle point"],
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
            aliases=["hypothesis testing", "p-value", "p-hacking", "multiple testing", "bonferroni", "benjamini-hochberg", "t-test", "fdr", "significance test"],
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
            aliases=["data leakage", "leakage", "cross-validation", "cross validation", "k-fold", "kfold", "lookahead bias", "temporal split", "time-series split", "train test split", "validation split", "folds"],
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
            aliases=["pca", "principal component analysis", "dimensionality reduction", "variance ratio"],
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
            aliases=["xgboost", "lightgbm", "catboost", "gbdt", "gradient boosting", "decision tree", "random forest", "tabular"],
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
            aliases=["backpropagation", "backprop", "autograd", "computational graph", "backward pass", "zero_grad", "chain rule"],
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
            aliases=["transformer", "attention mechanism", "self-attention", "flashattention", "multi-head attention", "rope", "causal mask", "kv cache", "llm"],
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
            aliases=["rag", "retrieval-augmented generation", "vector db", "embeddings", "hybrid search", "bm25", "reranking", "chunking", "semantic search"],
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
            aliases=["multi-agent", "agentic", "tool use", "mcp", "orchestrator", "subagent", "autonomous agent", "model context protocol"],
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
            aliases=["lora", "qlora", "peft", "parameter-efficient", "adapter", "rank r", "fine-tuning"],
            first_principles_formulation="W' = W_0 + ΔW = W_0 + (α/r) B A, where B ∈ R^{d×r}, A ∈ R^{r×k}, r ≪ min(d, k).",
            practical_implementation_notes="Use HuggingFace peft library with QLoRA 4-bit base weights for memory efficiency."
        ))

        # Data Engineering & Modern Analytical Engines
        self.add_node(ConceptNode(
            name="Data Engineering & Analytical Engines (DuckDB/Spark/Polars)",
            domain="Data Engineering",
            difficulty="Intermediate",
            prerequisites=[],
            leads_to=["Production ML Pipelines"],
            common_pitfalls=[
                "Pulling entire large datasets into single-node Pandas memory instead of using streaming or pushdown filters.",
                "Selecting distributed Spark over in-process DuckDB for sub-100GB datasets incurring massive JVM overhead.",
                "Missing partition pruning keys on Parquet lakehouse storage."
            ],
            aliases=["duckdb", "spark", "pyspark", "polars", "data engineering", "etl", "elt", "parquet", "lakehouse", "arrow", "sql pipeline"],
            first_principles_formulation="Vectorized columnar execution engine with predicate pushdown and chunked memory processing: O(N) vectorized scan.",
            practical_implementation_notes="Use DuckDB for single-node sub-100GB out-of-core analytics; use PySpark for multi-node PB-scale clusters."
        ))

        # Software Architecture & Clean Design
        self.add_node(ConceptNode(
            name="Software Architecture: Clean Design & Modularity",
            domain="Software Architecture",
            difficulty="Intermediate",
            prerequisites=[],
            leads_to=["Production ML Pipelines", "Multi-Agent Architectures & Tool Use"],
            common_pitfalls=[
                "Coupling domain business logic directly to frameworks or database clients.",
                "Creating God classes or monolithic functions with hidden side-effects.",
                "Neglecting defensive programming, error boundaries, and static type safety."
            ],
            aliases=["clean architecture", "hexagonal architecture", "design patterns", "solid principles", "refactor", "modularity", "clean code", "dry principle"],
            first_principles_formulation="Dependency Inversion: High-level policy modules must depend on abstractions, never on low-level implementation details.",
            practical_implementation_notes="Separate Domain Entities, Use Cases (Interactors), and Infrastructure Adapters with explicit interfaces."
        ))

        # MLOps & High-Throughput Serving
        self.add_node(ConceptNode(
            name="MLOps & Model Serving (vLLM/Triton/CUDA)",
            domain="MLOps",
            difficulty="Advanced",
            prerequisites=["Transformer Architecture & Attention"],
            leads_to=["Production ML Pipelines"],
            common_pitfalls=[
                "Serving LLMs with naive sequential request processing instead of continuous dynamic batching.",
                "Failing to profile GPU memory bottlenecks (VRAM fragmentation, KV cache allocation).",
                "Deploying models without automated drift detection (KS test, PSI) and latency SLAs."
            ],
            aliases=["mlops", "vllm", "triton", "model serving", "continuous batching", "pagedattention", "inference latency", "profiling", "cuda", "vram", "model drift"],
            first_principles_formulation="Throughput / Latency Pareto curve: T = (B * L) / (t_compute + t_memory_io).",
            practical_implementation_notes="Deploy with vLLM PagedAttention or NVIDIA Triton Inference Server; profile with PyTorch Profiler."
        ))

        # Exploratory Data Analysis & Feature Engineering
        self.add_node(ConceptNode(
            name="Exploratory Data Analysis & Feature Engineering",
            domain="Data Science",
            difficulty="Foundational",
            prerequisites=[],
            leads_to=["Data Leakage & Cross-Validation Strategy", "Gradient Boosted Decision Trees (XGBoost/LightGBM)"],
            common_pitfalls=[
                "Dropping missing values (NaNs) blindly without assessing missingness mechanism (MCAR vs MAR vs MNAR).",
                "Applying global imputation on the full dataset before splitting train/test sets.",
                "Creating redundant collinear features without inspecting correlation matrices."
            ],
            aliases=["eda", "feature engineering", "missing values", "nulls", "nans", "data cleaning", "imputation", "outliers", "collinearity", "data exploration"],
            first_principles_formulation="Information extraction: Mutual Information I(X; Y) = H(Y) - H(Y | X).",
            practical_implementation_notes="Analyze missingness patterns with missingno/pandas before imputing; inspect distributions with IQR and z-scores."
        ))

        # Time-Series Modeling & Temporal Validation
        self.add_node(ConceptNode(
            name="Time-Series Modeling & Temporal Validation",
            domain="Statistics",
            difficulty="Intermediate",
            prerequisites=["Data Leakage & Cross-Validation Strategy"],
            leads_to=["Production ML Pipelines"],
            common_pitfalls=[
                "Using standard random K-Fold on sequential data causing severe future lookahead leakage.",
                "Failing to lag target and features correctly when computing rolling window aggregations.",
                "Ignoring survivorship bias and non-stationarity in financial market data."
            ],
            aliases=["time-series", "time series", "financial data", "temporal split", "lookahead", "rolling window", "spy", "returns", "stationarity", "autocorrelation"],
            first_principles_formulation="Temporal causality invariant: P(Y_t | X_{<=t}) must only condition on past observations t' <= t.",
            practical_implementation_notes="Use TimeSeriesSplit or PurgedGroupTimeSeriesSplit with an embargo period between train and test windows."
        ))
