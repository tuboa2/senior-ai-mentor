"""Dynamic Project Context Detector for Senior AI Engineering Mentor.

Dynamically inspects the active project workspace directory to detect whether
it is related to:
1. Artificial Intelligence & Deep Learning
2. Data Science & Applied Statistics
3. Mathematics for ML & Optimization
4. Software Architecture & Systems Engineering
5. Data Engineering & Distributed Systems
6. MLOps & Production Infrastructure

Enforces Conditional Memory Modification:
- If RELATED: Retrieves mentor memory and progress, and authorizes active modifications.
- If UNRELATED: Locks mentor memory modification to protect the mentor's progress from corruption.
"""

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import re
from typing import Dict, List, Optional, Set, Tuple

@dataclass
class ProjectContextResult:
    is_related: bool
    confidence: float  # 0.0 to 1.0
    detected_domains: List[str] = field(default_factory=list)
    detected_frameworks: List[str] = field(default_factory=list)
    project_type: str = "Unrelated / Non-Technical"
    modification_allowed: bool = False
    evidence: List[str] = field(default_factory=list)
    summary: str = ""

class ProjectContextDetector:
    """Detects project domain and determines if mentor memory modifications are authorized."""

    # Recognized AI/ML & Data Science Frameworks & Libraries
    AI_ML_LIBRARIES: Dict[str, str] = {
        "torch": "PyTorch",
        "pytorch": "PyTorch",
        "torchvision": "TorchVision",
        "torchaudio": "TorchAudio",
        "tensorflow": "TensorFlow",
        "tf": "TensorFlow",
        "keras": "Keras",
        "jax": "JAX",
        "flax": "Flax",
        "scikit-learn": "Scikit-Learn",
        "sklearn": "Scikit-Learn",
        "xgboost": "XGBoost",
        "lightgbm": "LightGBM",
        "catboost": "CatBoost",
        "transformers": "Hugging Face Transformers",
        "huggingface": "Hugging Face",
        "datasets": "Hugging Face Datasets",
        "accelerate": "Accelerate",
        "deepspeed": "DeepSpeed",
        "peft": "PEFT (LoRA)",
        "bitsandbytes": "BitsAndBytes",
        "vllm": "vLLM",
        "triton": "Triton Inference Server",
        "timm": "PyTorch Image Models",
        "opencv-python": "OpenCV",
        "cv2": "OpenCV",
        "albumentations": "Albumentations",
        "optuna": "Optuna",
        "ray": "Ray",
        "langchain": "LangChain",
        "llama-index": "LlamaIndex",
        "chromadb": "ChromaDB",
        "faiss": "FAISS",
        "pinecone": "Pinecone",
        "qdrant": "Qdrant",
        "milvus": "Milvus",
        "weaviate": "Weaviate",
        "openai": "OpenAI SDK",
        "anthropic": "Anthropic SDK",
        "google-generativeai": "Google GenAI SDK"
    }

    DATA_SCIENCE_LIBRARIES: Dict[str, str] = {
        "pandas": "Pandas",
        "numpy": "NumPy",
        "scipy": "SciPy",
        "polars": "Polars",
        "duckdb": "DuckDB",
        "pyspark": "Apache Spark (PySpark)",
        "dbt": "dbt",
        "matplotlib": "Matplotlib",
        "seaborn": "Seaborn",
        "plotly": "Plotly",
        "statsmodels": "Statsmodels",
        "sympy": "SymPy",
        "networkx": "NetworkX",
        "graphviz": "Graphviz",
        "arrow": "Apache Arrow",
        "pyarrow": "PyArrow",
        "fastparquet": "FastParquet",
        "mlflow": "MLflow",
        "wandb": "Weights & Biases",
        "dvc": "DVC",
        "feast": "Feast Feature Store"
    }

    SOFTWARE_SYSTEMS_LIBRARIES: Dict[str, str] = {
        "fastapi": "FastAPI",
        "flask": "Flask",
        "django": "Django",
        "sqlalchemy": "SQLAlchemy",
        "alembic": "Alembic",
        "asyncio": "AsyncIO",
        "aiohttp": "AIOHTTP",
        "pydantic": "Pydantic",
        "celery": "Celery",
        "redis": "Redis",
        "psycopg2": "PostgreSQL Driver",
        "asyncpg": "AsyncPG",
        "kafka-python": "Apache Kafka",
        "aiokafka": "AIOKafka",
        "pytest": "Pytest",
        "docker": "Docker SDK",
        "grpcio": "gRPC"
    }

    MODEL_EXTENSIONS: Set[str] = {
        ".onnx", ".pt", ".pth", ".safetensors", ".bin",
        ".h5", ".tflite", ".pkl", ".joblib"
    }

    DATA_EXTENSIONS: Set[str] = {
        ".parquet", ".arrow", ".feather", ".duckdb", ".sqlite3"
    }

    AI_DIRECTORIES: Set[str] = {
        "models", "model", "checkpoints", "weights",
        "data", "dataset", "datasets", "notebooks",
        "experiments", "training", "eval", "evaluation",
        "pipelines", "features", "embeddings"
    }

    def detect(self, workspace_dir: Optional[Path] = None) -> ProjectContextResult:
        """Dynamically inspects the workspace and determines if it is related to AI/ML/Data Science."""
        root = Path(workspace_dir or Path.cwd()).resolve()
        if not root.exists() or not root.is_dir():
            return ProjectContextResult(
                is_related=False,
                confidence=0.0,
                project_type="Invalid / Non-Existent Directory",
                modification_allowed=False,
                summary="Directory does not exist. Mentor memory modifications locked."
            )

        detected_frameworks: Set[str] = set()
        detected_domains: Set[str] = set()
        evidence: List[str] = []
        score = 0.0

        # 1. Inspect Senior AI Mentor Configuration
        mentor_manifest = root / ".agents" / "manifest.json"
        if mentor_manifest.exists():
            score += 0.5
            detected_domains.add("AI Engineering Mentorship")
            evidence.append("Found Senior AI Mentor workspace manifest (.agents/manifest.json)")

        gemini_md = root / "GEMINI.md"
        if gemini_md.exists():
            try:
                content = gemini_md.read_text(encoding="utf-8", errors="ignore")
                if "Senior AI Engineering Mentor" in content or "Expert Council" in content:
                    score += 0.4
                    detected_domains.add("AI Engineering Mentorship")
                    evidence.append("Found Senior AI Mentor directives in GEMINI.md")
            except Exception:
                pass

        # 2. Inspect Dependency Manifests
        dep_files = [
            root / "requirements.txt",
            root / "pyproject.toml",
            root / "setup.py",
            root / "setup.cfg",
            root / "Pipfile",
            root / "environment.yml",
            root / "package.json"
        ]
        # Also check requirements/*.txt
        req_dir = root / "requirements"
        if req_dir.exists() and req_dir.is_dir():
            dep_files.extend(req_dir.glob("*.txt"))

        for df in dep_files:
            if df.exists() and df.is_file():
                try:
                    text = df.read_text(encoding="utf-8", errors="ignore").lower()
                    
                    # Check AI/ML libs
                    for lib, name in self.AI_ML_LIBRARIES.items():
                        if re.search(rf"\b{re.escape(lib)}\b", text):
                            detected_frameworks.add(name)
                            detected_domains.add("Machine Learning & Deep Learning")
                            score += 0.3
                            evidence.append(f"Dependency '{lib}' found in {df.name}")

                    # Check Data Science libs
                    for lib, name in self.DATA_SCIENCE_LIBRARIES.items():
                        if re.search(rf"\b{re.escape(lib)}\b", text):
                            detected_frameworks.add(name)
                            detected_domains.add("Data Science & Applied Statistics")
                            score += 0.25
                            evidence.append(f"Dependency '{lib}' found in {df.name}")

                    # Check Software Systems libs
                    for lib, name in self.SOFTWARE_SYSTEMS_LIBRARIES.items():
                        if re.search(rf"\b{re.escape(lib)}\b", text):
                            detected_frameworks.add(name)
                            detected_domains.add("Software Architecture & Distributed Systems")
                            score += 0.15
                            evidence.append(f"Dependency '{lib}' found in {df.name}")
                except Exception:
                    pass

        # 3. Inspect Directory Structure and File Types (Up to depth 2)
        notebook_count = 0
        model_file_count = 0
        data_file_count = 0
        py_file_count = 0

        try:
            for item in root.iterdir():
                if item.is_dir() and not item.name.startswith("."):
                    if item.name.lower() in self.AI_DIRECTORIES:
                        score += 0.25
                        detected_domains.add("AI/ML Project Structure")
                        evidence.append(f"Found dedicated AI/ML directory: '{item.name}/'")

                    # Shallow scan of subdirectories
                    try:
                        for sub in item.iterdir():
                            ext = sub.suffix.lower()
                            if ext == ".ipynb":
                                notebook_count += 1
                            elif ext in self.MODEL_EXTENSIONS:
                                model_file_count += 1
                            elif ext in self.DATA_EXTENSIONS:
                                data_file_count += 1
                            elif ext == ".py":
                                py_file_count += 1
                    except Exception:
                        pass
                elif item.is_file():
                    ext = item.suffix.lower()
                    if ext == ".ipynb":
                        notebook_count += 1
                    elif ext in self.MODEL_EXTENSIONS:
                        model_file_count += 1
                    elif ext in self.DATA_EXTENSIONS:
                        data_file_count += 1
                    elif ext == ".py":
                        py_file_count += 1
        except Exception:
            pass

        if notebook_count > 0:
            score += 0.3
            detected_domains.add("Data Science & Jupyter Notebooks")
            evidence.append(f"Found {notebook_count} Jupyter notebook(s) (.ipynb)")

        if model_file_count > 0:
            score += 0.4
            detected_domains.add("Trained Model Artifacts")
            evidence.append(f"Found {model_file_count} model artifact file(s)")

        if data_file_count > 0:
            score += 0.25
            detected_domains.add("Structured Data Engineering")
            evidence.append(f"Found {data_file_count} structured data file(s)")

        # 4. Code Import Scanning on top Python files
        scanned_py = 0
        try:
            for pfile in root.glob("*.py"):
                if scanned_py >= 5:
                    break
                scanned_py += 1
                try:
                    lines = pfile.read_text(encoding="utf-8", errors="ignore").splitlines()[:50]
                    for line in lines:
                        line_low = line.strip().lower()
                        if line_low.startswith(("import ", "from ")):
                            for lib, name in self.AI_ML_LIBRARIES.items():
                                if re.search(rf"\b{re.escape(lib)}\b", line_low):
                                    detected_frameworks.add(name)
                                    detected_domains.add("Machine Learning & Deep Learning")
                                    score += 0.2
                            for lib, name in self.DATA_SCIENCE_LIBRARIES.items():
                                if re.search(rf"\b{re.escape(lib)}\b", line_low):
                                    detected_frameworks.add(name)
                                    detected_domains.add("Data Science & Applied Statistics")
                                    score += 0.15
                except Exception:
                    pass
        except Exception:
            pass

        # 5. Determine Final Classification & Confidence
        confidence = min(1.0, round(score, 2))
        is_related = (confidence >= 0.25) or (len(detected_frameworks) > 0) or ("AI Engineering Mentorship" in detected_domains)

        if is_related:
            if "Machine Learning & Deep Learning" in detected_domains or model_file_count > 0:
                proj_type = "AI & Machine Learning System"
            elif "Data Science & Applied Statistics" in detected_domains or notebook_count > 0:
                proj_type = "Data Science & Statistical Analytics"
            elif "Software Architecture & Distributed Systems" in detected_domains:
                proj_type = "Software Systems & Backend Architecture"
            elif "AI Engineering Mentorship" in detected_domains:
                proj_type = "AI Engineering Mentorship Environment"
            else:
                proj_type = "AI / Technical Computing Project"

            fw_list = sorted(list(detected_frameworks))
            fw_str = f" ({', '.join(fw_list[:4])})" if fw_list else ""
            summary = (
                f"Active workspace is recognized as an {proj_type}{fw_str}. "
                f"Senior AI Mentor memory retrieved; progress updates and modifications AUTHORIZED."
            )
            modification_allowed = True
        else:
            proj_type = "Unrelated / Non-Technical Project"
            summary = (
                "Active workspace is NOT related to AI, Machine Learning, Data Science, or Software Engineering. "
                "Senior AI Mentor memory modifications are LOCKED to prevent progress corruption."
            )
            modification_allowed = False

        return ProjectContextResult(
            is_related=is_related,
            confidence=confidence,
            detected_domains=sorted(list(detected_domains)),
            detected_frameworks=sorted(list(detected_frameworks)),
            project_type=proj_type,
            modification_allowed=modification_allowed,
            evidence=evidence[:10],
            summary=summary
        )
