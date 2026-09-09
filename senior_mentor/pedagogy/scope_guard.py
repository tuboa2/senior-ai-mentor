"""Scope Guard for Senior AI Engineering Mentor.

Validates that incoming queries, commands, and learner inputs fall strictly
within the technical domains of the Senior AI Engineering Mentor:
1. Machine Learning & Deep Learning
2. Data Science & Applied Statistics
3. Mathematics for ML & Optimization
4. Software Architecture & Engineering Practices
5. Data Engineering & Distributed Systems
6. MLOps & Production AI Systems
7. Technical Interviews & Pedagogical Development

Strictly rejects out-of-scope queries (e.g., culinary/recipes, creative writing,
sports/entertainment gossip, medical/legal advice, astrology/lifestyle)
and guarantees zero memory mutation (no scaffolding logs, knowledge updates,
misconceptions, decisions, or feedback records).
"""

from dataclasses import dataclass, field
import re
from typing import Dict, List, Optional, Set, Tuple

@dataclass
class ScopeCheckResult:
    is_in_scope: bool
    reason: str
    matched_domains: List[str] = field(default_factory=list)
    rejection_message: str = ""
    suggested_topics: List[str] = field(default_factory=list)

class ScopeGuard:
    """Detects and isolates out-of-scope queries from entering mentor memory."""

    ALLOWED_SLASH_COMMANDS: Set[str] = {
        "solve", "mentor", "hint", "challenge", "council",
        "interview", "status", "profile", "eval", "skills",
        "feedback", "refine", "audit", "discover", "init"
    }

    # Core technical pillars
    TECHNICAL_PATTERNS: Dict[str, str] = {
        "ml_dl": (
            r"\b(machine\s+learning|deep\s+learning|neural\s+net(work)?s?|transformer|attention|"
            r"self-attention|multi-head|cnn|rnn|lstm|gru|autoencoder|vae|gan|diffusion|"
            r"embedding|embeddings|lora|qlora|peft|rlhf|dpo|ppo|sft|fine-tun(ing|e)|pre-train(ing|ed)?|"
            r"loss\s+function|cross-entropy|mse|focal\s+loss|contrastive|adamw?|sgd|"
            r"weight\s+decay|learning\s+rate|lr\s+schedule|dropout|batchnorm|layernorm|rmsnorm|"
            r"quantiz(ation|ed)|int8|int4|fp16|bf16|classification|regression|clustering|"
            r"k-means|knn|random\s+forest|xgboost|lightgbm|catboost|decision\s+tree|svm|pca|"
            r"t-sne|umap|overfit(ting)?|underfit(ting)?|regulariz(ation|ed)|token(izer|ization)?|"
            r"bpe|kv\s+cache|temperature|top-p|top-k|beam\s+search|decoding|prompt(ing)?|"
            r"few-shot|zero-shot|rag|retrieval-augmented|vector\s+db|faiss|chroma|pinecone|"
            r"qdrant|milvus|weaviate|context\s+window|hallucinat(ion|ions)|backprop(agation)?|"
            r"gradient\s+descent|activations?|relu|gelu|swiglu|perceptron|epoch|batch\s+size|"
            r"weights|biases|loss\s+surface|hyperparameters?|grid\s+search|optuna|ray\s+tune)\b"
        ),
        "statistics_math": (
            r"\b(linear\s+algebra|matrix|matrices|vector(s)?|dot\s+product|tensor(s)?|eigenvalue(s)?|"
            r"eigenvector(s)?|svd|singular\s+value(s)?|decomposition(s)?|spectral|rank|trace|determinant(s)?|"
            r"pseudo-inverse|orthogonal|orthonormal|basis|null\s+space|column\s+space|calculus|"
            r"gradient(s)?|derivative(s)?|partial\s+derivative(s)?|chain\s+rule|jacobian(s)?|hessian(s)?|directional\s+derivative(s)?|"
            r"convex(ity)?|saddle\s+point(s)?|lagrange|kkt|objective\s+function(s)?|taylor\s+series|"
            r"information\s+theory|kl\s+divergence|entropy|mutual\s+information|statistic(s|al)?|"
            r"probability|distribution(s)?|gaussian|poisson|binomial|exponential|hypothesis\s+test(ing)?|"
            r"p-value(s)?|null\s+hypothesis|significance\s+level|type\s+[i|ii]\s+error(s)?|confidence\s+interval(s)?|"
            r"t-test(s)?|anova|chi-square|mann-whitney|bayes(ian)?|prior(s)?|posterior(s)?|likelihood|"
            r"mle|map\s+estimation|variance|covariance(s)?|standard\s+deviation|quantile(s)?|correlation(s)?|"
            r"r-squared|collinearity|homoscedasticity|heteroscedasticity|eda|data\s+leakage|"
            r"lookahead\s+bias|cross-validation|k-fold|stratified|bootstrap|permutation\s+test(s)?|"
            r"causal\s+inference|confound(er|ers|ing)?|do-calculus|propensity\s+score(s)?|a/b\s+test(ing|s)?|"
            r"sample\s+ratio\s+mismatch|power\s+analysis|normal\s+distribution|compute|calculation|derive)\b"
        ),
        "software_architecture": (
            r"\b(software\s+architecture|design\s+pattern(s)?|clean\s+architecture|hexagonal|"
            r"ports\s+and\s+adapters|domain-driven|ddd|microservice(s)?|monolith(ic)?|event-driven|cqrs|"
            r"solid\s+principles?|single\s+responsibility|dependency\s+inversion|dependency\s+injection|"
            r"factory\s+pattern|singleton|builder\s+pattern|adapter\s+pattern|strategy\s+pattern|"
            r"observer\s+pattern|decorator\s+pattern|repository\s+pattern|unit\s+of\s+work|oop|"
            r"object-oriented|functional\s+programming|refactor(ing)?|code\s+review(s)?|code\s+quality|"
            r"unit\s+test(s|ing)?|integration\s+test(s|ing)?|pytest|unittest|mock(ing|s)?|tdd|"
            r"static\s+analysis|type\s+hints?|mypy|lint(ing)?|flake8|ruff|black|git|pull\s+request(s)?|"
            r"ci/cd|docker|container(s|ization)?|kubernetes|k8s|rest\s+api(s)?|graphql|grpc|websocket(s)?|"
            r"middleware|rate\s+limit(ing|er)?|auth(entication)?|jwt|oauth|error\s+handling|"
            r"defensive\s+programming|dry\s+principle|async(io)?|concurrency|multithread(ing)?|"
            r"multiprocess(ing)?|coroutine(s)?|event\s+loop|locks?|semaphore(s)?|deadlock(s)?|race\s+condition(s)?|"
            r"thread-saf(e|ety)|caching|lru\s+cache|redis|memcached)\b"
        ),
        "data_engineering": (
            r"\b(data\s+engineering|etl|elt|pipeline(s)?|spark|pyspark|duckdb|polars|pandas|dbt|"
            r"airflow|prefect|dagster|kafka|rabbitmq|streaming|batch\s+processing|parquet|arrow|"
            r"avro|orc|delta\s+lake|iceberg|hudi|database(s)?|sql|nosql|postgres(ql)?|mysql|sqlite|"
            r"clickhouse|elasticsearch|opensearch|cassandra|dynamodb|schema(s)?|data\s+contract(s)?|"
            r"data\s+lineage|data\s+catalog|great\s+expectations|distributed\s+system(s)?|cap\s+theorem|"
            r"consensus|raft|paxos|replication|sharding|partition(ing|s)?|indexing|b-tree|lsm-tree|"
            r"write-ahead\s+log|query\s+optimiz(ation|er)|execution\s+plan)\b"
        ),
        "mlops_performance": (
            r"\b(mlops|model\s+serving|inference|triton|vllm|tgi|onnx|tensorrt|torchscript|"
            r"latency|throughput|p99|p95|sla|batching|continuous\s+batching|speculative\s+decoding|"
            r"model\s+registry|mlflow|wandb|weights\s+and\s+biases|dvc|feast|feature\s+store|"
            r"model\s+drift|data\s+drift|concept\s+drift|ks\s+test|canary\s+deployment|profil(ing|er)|"
            r"cprofile|torch\.profiler|cuda|gpu(s)?|tensor\s+core(s)?|memory\s+bandwidth|compute-bound|"
            r"memory-bound|flops|vram|oom|out\s+of\s+memory|pytorch|torch|tensorflow|jax|keras)\b"
        ),
        "algorithms_coding": (
            r"\b(algorithm(s)?|data\s+structure(s)?|time\s+complexity|space\s+complexity|big-o|"
            r"o\(n\)|o\(1\)|o\(log\s*n\)|linked\s+list(s)?|stack(s)?|queue(s)?|deque|hash\s*table(s)?|hash\s*map(s)?|"
            r"binary\s+tree(s)?|bst|balanced\s+tree|avl|red-black|heap(s)?|priority\s+queue(s)?|trie(s)?|graph(s)?|"
            r"dag|topological\s+sort|bfs|dfs|breadth\s+first|depth\s+first|dijkstra|dynamic\s+programming|"
            r"memoiz(ation|ed)|tabulation|greedy\s+algorithm|divide\s+and\s+conquer|binary\s+search|"
            r"two\s+pointers|sliding\s+window|backtracking|recursion|sorting|quicksort|mergesort|"
            r"heapsort|leetcode|coding\s+interview|system\s+design\s+interview)\b"
        ),
        "programming_languages_tools": (
            r"\b(python|rust|golang|c\+\+|java|scala|bash|shell|typescript|javascript|"
            r"numpy|scipy|scikit-learn|sklearn|matplotlib|seaborn|fastapi|flask|django|"
            r"sqlalchemy|alembic|poetry|uv|pip|conda|virtualenv|git)\b"
        )
    }

    # Prohibited non-technical domains
    OUT_OF_SCOPE_RULES: List[Tuple[str, str, str]] = [
        (
            "culinary",
            r"\b(bake|baking|recipe|recipes|ingredient|ingredients|cook|cooking|pancake|pancakes|"
            r"cake|cakes|cupcake|cupcakes|cookie|cookies|bread|pasta|pizza|soup|stew|salad|"
            r"roast|roasting|grill|grilling|fry|frying|flour|sugar|butter|delicious|tasty|"
            r"spices|kitchen|oven|microwave|sauce|dinner|lunch|breakfast|dessert|pastry|"
            r"waffle|waffles|pie|pies|marinade|simmer|steak|culinary|chef|dish|dishes)\b",
            "Culinary, cooking recipes, and food preparation queries are outside the technical scope of the Senior AI Engineering Mentor."
        ),
        (
            "creative_writing",
            r"(\b(write\s+(me\s+)?(a\s+)?(poem|song|story|novel|fairy\s+tale|rhyme|haiku|lyrics|screenplay|fanfiction|ballad|limerick))\b|"
            r"\b(lyrics\s+for|song\s+lyrics|creative\s+story|bedtime\s+story|romantic\s+poem|fictional\s+character)\b)",
            "Creative fiction, songwriting, storytelling, and poetry are outside the technical scope of the Senior AI Engineering Mentor."
        ),
        (
            "sports_entertainment",
            r"\b(world\s+cup|nba(\s+finals)?|premier\s+league|champions\s+league|super\s+bowl|"
            r"who\s+won\s+the\s+(game|match|cup|championship)|messi|ronaldo|lebron(\s+james)?|"
            r"celebrity\s+gossip|hollywood\s+gossip|box\s+office|netflix\s+movie\s+recommendation|"
            r"dating\s+history\s+of|pop\s+singer|pop\s+star|kardashian|grammys?|oscars?)\b",
            "Sports matches, celebrity gossip, and pop culture entertainment are outside the technical scope of the Senior AI Engineering Mentor."
        ),
        (
            "medical_health",
            r"(\b(diagnose\s+(me|my)|symptoms?\s+of\s+(cancer|covid|flu|cold|diabetes|depression)|"
            r"cure\s+for|medical\s+treatment\s+for|what\s+medicine\s+should\s+i\s+take|"
            r"dosage\s+of\s+(ibuprofen|paracetamol|tylenol|aspirin|antibiotic)|"
            r"home\s+remedy\s+for\s+(cough|headache|fever)|stomach\s+ache\s+cure|am\s+i\s+pregnant)\b)",
            "Medical diagnosis, clinical health recommendations, and pharmaceutical advice are strictly outside the scope of the Senior AI Engineering Mentor."
        ),
        (
            "legal_advice",
            r"(\b(how\s+to\s+sue\s+(my|a)|divorce\s+lawyer|child\s+custody\s+lawyer|"
            r"file\s+a\s+lawsuit\s+against|tenant\s+rights\s+regarding\s+eviction|draft\s+a\s+legal\s+will)\b)",
            "Personal legal counsel, litigation advice, and civil dispute assistance are outside the scope of the Senior AI Engineering Mentor."
        ),
        (
            "lifestyle_astrology",
            r"\b(horoscope|zodiac\s+sign|astrology\s+reading|tarot\s+reading|"
            r"how\s+to\s+text\s+(my\s+)?(crush|ex)|relationship\s+advice|how\s+to\s+flirt|"
            r"vacation\s+itinerary\s+for|cheap\s+flights\s+to|hotel\s+booking\s+in)\b",
            "Astrology, dating/relationship advice, and leisure travel planning are outside the technical scope of the Senior AI Engineering Mentor."
        )
    ]

    # Technical framing overrides: contexts where an out-of-scope word is allowed because it's part of software development
    TECHNICAL_CONTEXT_OVERRIDE_PATTERNS = [
        r"\b(database\s+schema|data\s+model|api|rest|endpoint|table|crud|sql|nosql|scrape|scraping|crawler)\b",
        r"\b(python\s+code|script|class|function|test|unit\s+test|mock|algorithm|backend|frontend)\b",
        r"\b(machine\s+learning|model|dataset|recommendation\s+system|predict|classifier|embeddings?)\b"
    ]

    def __init__(self):
        self._compiled_technical = {
            domain: re.compile(pattern, re.IGNORECASE)
            for domain, pattern in self.TECHNICAL_PATTERNS.items()
        }
        self._compiled_out_of_scope = [
            (category, re.compile(pattern, re.IGNORECASE), reason)
            for category, pattern, reason in self.OUT_OF_SCOPE_RULES
        ]
        self._compiled_overrides = [
            re.compile(p, re.IGNORECASE) for p in self.TECHNICAL_CONTEXT_OVERRIDE_PATTERNS
        ]

    def _extract_command_and_query(self, raw_text: str) -> Tuple[Optional[str], str]:
        text = raw_text.strip()
        if text.startswith("/"):
            parts = text[1:].split(maxsplit=1)
            cmd = parts[0].lower()
            remainder = parts[1].strip() if len(parts) > 1 else ""
            return cmd, remainder
        return None, text

    def check_scope(self, text: str) -> ScopeCheckResult:
        """Evaluates whether a user query or input is strictly within engineering mentor scope.
        
        Guarantees that out-of-scope inputs are rejected BEFORE any memory logging occurs.
        """
        cmd, query = self._extract_command_and_query(text)
        clean_text = query if query else (text if not cmd else "")
        lower_clean = clean_text.lower().strip()

        # 1. Framework control commands with empty query are valid
        if cmd in self.ALLOWED_SLASH_COMMANDS and not clean_text:
            return ScopeCheckResult(
                is_in_scope=True,
                reason=f"Framework command /{cmd} is in scope.",
                matched_domains=["framework_controls"]
            )

        # 2. If command is /interview with valid domain or empty
        if cmd == "interview" and (not clean_text or clean_text in {"system_design", "ml_theory", "statistics", "coding"}):
            return ScopeCheckResult(
                is_in_scope=True,
                reason="Interview simulation is in scope.",
                matched_domains=["algorithms_coding"]
            )

        # 3. Check for out-of-scope categories
        matched_out_of_scope: Optional[Tuple[str, str]] = None
        for category, regex, reason in self._compiled_out_of_scope:
            if regex.search(clean_text):
                matched_out_of_scope = (category, reason)
                break

        # Check matched technical domains
        matched_domains = [
            domain for domain, regex in self._compiled_technical.items()
            if regex.search(clean_text)
        ]

        # Check for technical framing override
        has_technical_override = any(r.search(clean_text) for r in self._compiled_overrides)

        if matched_out_of_scope:
            cat, reason = matched_out_of_scope

            # Check if this is an exempted technical context (e.g. "design a database schema for recipe storage")
            # But NOT if the query explicitly asks for creative writing, cooking, or medical diagnosis
            creative_or_medical = cat in {"creative_writing", "medical_health", "lifestyle_astrology"}
            if has_technical_override and not creative_or_medical and len(matched_domains) > 0:
                # Technical software task discussing a real-world domain entity
                return ScopeCheckResult(
                    is_in_scope=True,
                    reason="Technical software engineering request operating on domain entity.",
                    matched_domains=matched_domains
                )

            # Otherwise, strictly reject
            return ScopeCheckResult(
                is_in_scope=False,
                reason=reason,
                matched_domains=[],
                rejection_message=self._build_rejection_message(text, reason),
                suggested_topics=self.get_suggested_topics()
            )

        # 4. If no explicit out-of-scope matched, verify that at least one technical signal exists
        if matched_domains:
            return ScopeCheckResult(
                is_in_scope=True,
                reason="Matched authorized AI engineering technical domains.",
                matched_domains=matched_domains
            )

        # 5. Check if query is an empty or whitespace string
        if not lower_clean:
            return ScopeCheckResult(
                is_in_scope=False,
                reason="Empty query submitted.",
                rejection_message="Query is empty. Please enter a technical question or command (e.g. /council, /mentor, /solve, /interview, /status)."
            )

        # 6. Check common greetings or metadata
        if lower_clean in {"hi", "hello", "hey", "help", "who are you", "what can you do"}:
            return ScopeCheckResult(
                is_in_scope=False,
                reason="Conversational greeting or general help request outside technical problem scope.",
                rejection_message=(
                    "👋 Welcome! I am your Senior AI Engineering Mentor & Orchestrator Council.\n\n"
                    "I provide technical mentorship, architecture reviews, and adaptive scaffolding across:\n"
                    "• Machine Learning & Deep Learning (Transformers, LoRA, Attention, Training Dynamics)\n"
                    "• Mathematics for ML & Optimization (Linear Algebra, SVD, Convexity, Gradients)\n"
                    "• Software Architecture & Clean Code (DDD, Concurrency, Design Patterns, Refactoring)\n"
                    "• Data Engineering & Distributed Systems (DuckDB, Spark, Kafka, Partitioning)\n"
                    "• MLOps & Production AI (vLLM, Triton, Profiling, Model Drift, Latency)\n"
                    "• Senior Technical Interviews & Deliberations (/interview, /council)\n\n"
                    "👉 Ask a technical question or use commands: /solve, /mentor, /hint, /challenge, /council, /interview, /status."
                )
            )

        # 7. Unmatched / general trivia / unsupported domain
        return ScopeCheckResult(
            is_in_scope=False,
            reason="Query does not match any recognized Machine Learning, Data Science, Software Engineering, or Systems domain.",
            rejection_message=self._build_rejection_message(
                text,
                "Query does not belong to authorized AI Engineering, ML, Mathematics, Systems, or Software Architecture domains."
            ),
            suggested_topics=self.get_suggested_topics()
        )

    def _build_rejection_message(self, query: str, reason: str) -> str:
        return (
            "🚫 QUERY REJECTED: OUTSIDE SENIOR AI MENTOR SCOPE\n\n"
            f"Your request was identified as outside the scope of the Senior AI Engineering Mentor & Expert Council:\n"
            f"> \"{query}\"\n\n"
            f"Reason: {reason}\n\n"
            "The Senior AI Engineering Mentor strictly operates on technical topics:\n"
            "  1. Machine Learning & Deep Learning (Architectures, Training Dynamics, LoRA, Transformers)\n"
            "  2. Mathematics & Statistics (Linear Algebra, SVD, Optimization, Hypothesis Testing)\n"
            "  3. Software Architecture & Clean Code (Design Patterns, System Boundaries, Concurrency)\n"
            "  4. Data Engineering & Distributed Systems (ETL, DuckDB, Spark, Streaming, Sharding)\n"
            "  5. MLOps & Production AI (vLLM, Triton, GPU Profiling, Model Drift, Serving)\n"
            "  6. AI/LLM Systems & Multi-Agent Architecture (RAG, Evals, Tool Use, Orchestration)\n"
            "  7. Senior Technical Interviews & Code Reviews\n\n"
            "🔒 MEMORY ISOLATION ENFORCED:\n"
            "This interaction has NOT been logged to memory. Zero modifications were made to\n"
            "scaffolding logs, knowledge assessments, error patterns, or learner profile records."
        )

    @staticmethod
    def get_suggested_topics() -> List[str]:
        return [
            "Implement multi-head attention from first principles in PyTorch",
            "Derive SVD and explain sign ambiguity across NumPy and SciPy",
            "Compare DuckDB vs Apache Spark for 100GB analytical workloads",
            "Design a low-latency RAG system with hybrid vector + BM25 search",
            "Diagnose data leakage in time-series cross-validation pipelines",
            "Prepare for a Staff ML System Design technical interview (/interview system_design)"
        ]
