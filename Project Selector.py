import random


orchestration_tools = [
    "Prefect",
    "Flyte",
    "Airflow",
    "Metaflow"
]
frameworks = [
    "PyTorch",
    "Keras",
    "Scikit Learn",
    "XGBoost",
    "H2O",
    "FastAI",
    "Apache Spark"
]
servers = [
    "Torch Serve",
    "FastAPI",
    "Flask",
    "Django",
    "BentoML",
    "TFServing",
    "Streamlit",
    "Feast",
    "ONNX Runtime",
    "Kubeflow",
    "Seldon"
]
monitors = [
    "Prometheus + Grafana",
    "InfluxDB",
    "Netdata",
    "Evidently",
    "Healthchecks",
    "MLFlow",
    "Metabase",
    "ELK Stack",
    "Zappix"
]

explainers = [
    "Apache Superset",
    "Pandas + Jupyter",
]

wildcards = [
    "Dask for distributed execution",
    "Huggingface API",
    "SpaCy for NLP",
    "Ultralytics for Image Processing",
    "Horovod for distributed training (if applicable)",
    "Mindsdb for data store enrichment",
    "Shap for model analysis"
]

datatools = [
    "PostgresQL",
    "MySQL",
    "SQL Server",
    "SQLite"
    "EdgeDB",
    "SurrealDB",
    "Firebase",
    "DVC",
    "Memgraph",
    "Dgraph",
    "ArangoDB",
    "Neo4j",

]



print(f"""
your task is to create a data project using:
    Orchestration: {random.choice(orchestration_tools)}
    Framework:     {random.choice(frameworks)}
    Server:        {random.choice(servers)}
    Monitor:       {random.choice(monitors)}
    
    Data storage:  {random.choice(datatools)}
    Data Analysis: {random.choice(explainers)}
    Wildcard:      {random.choice(wildcards)}
""")
