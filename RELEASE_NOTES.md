# OpenSearchEval v1.0.0 - Initial Release

This is the initial release of OpenSearchEval, a comprehensive search evaluation platform with agent architecture and MLX integration for Apple Silicon optimization.

## Key Features

### Search Quality Metrics
- **Mean Reciprocal Rank (MRR)**: Average of reciprocal ranks for search results
- **NDCG@K**: Normalized Discounted Cumulative Gain at various cutoff points
- **Precision@K and Recall@K**: Precision and recall metrics at various cutoff points
- **F1-Score**: Harmonic mean of precision and recall
- **Reciprocal Rank Fusion**: Combines multiple result sets
- **Diversity Score**: Measures result diversity
- **Novelty Score**: Measures result novelty

### User Behavior Analytics
- **Click-Through Rate (CTR)**: Percentage of results clicked
- **Time to First Click**: Average time before first interaction
- **Dwell Time**: Time spent on clicked results
- **Abandonment Rate**: Percentage of searches without clicks
- **Satisfaction Score**: Composite user satisfaction metric

### A/B Testing Framework
- Statistical significance testing with configurable confidence levels
- Support for t-test, Mann-Whitney U test, and bootstrap testing
- Comprehensive experiment management and tracking
- Real-time experiment monitoring and analysis

### Agent Architecture
- **SearchEvaluationAgent**: Specialized agent for search metric calculation
- **ABTestAgent**: Handles A/B test execution and statistical analysis
- **UserBehaviorAgent**: Analyzes user interaction patterns
- Distributed processing with asynchronous task handling
- Configurable agent pools and task queues

### MLX Integration
- Optimized ML components for Apple Silicon with GPU acceleration
- **SearchRankingModel**: Neural ranking model with MLX backend
- **ClickThroughRatePredictor**: CTR prediction with feature extraction
- **EmbeddingModel**: Text embedding generation with MLX optimization
- Up to 10x performance improvement on Apple Silicon devices

### LLM-as-Judge
- AI-powered qualitative evaluation of search results
- Support for OpenAI GPT models and custom LLM endpoints
- Configurable evaluation criteria and scoring rubrics
- Batch processing for large-scale evaluation

### FastAPI REST API
- Production-ready REST API with automatic OpenAPI documentation
- Asynchronous request handling with high concurrency support
- WebSocket support for real-time metrics streaming
- Comprehensive error handling and validation

### Rich Visualizations
- Interactive charts and dashboards with Plotly and Dash
- Time series analysis for metrics tracking
- A/B test results visualization
- User behavior heatmaps and journey analysis
- Exportable reports in multiple formats

### Data Connectors
- **Database Support**: PostgreSQL, MySQL, SQLite, MongoDB
- **Big Data**: Apache Spark, Databricks, Snowflake integration
- **Search Engines**: Elasticsearch, OpenSearch, Solr connectors
- **Cloud Storage**: AWS S3, Google Cloud Storage, Azure Blob
- **Custom Connectors**: Extensible framework for custom data sources

### Performance Monitoring
- Real-time metrics collection and aggregation
- Prometheus integration for monitoring
- Grafana dashboard templates
- Alerting system for performance issues
- Health checks and service discovery

## Installation

```bash
# Basic installation
pip install opensearcheval

# With all optional dependencies
pip install opensearcheval[all]

# Development installation
pip install opensearcheval[dev]
```

## Docker Support

```bash
# Clone repository
git clone https://github.com/llamasearchai/OpenSearchEval.git
cd OpenSearchEval

# Start with Docker Compose
docker-compose up -d

# Access API at http://localhost:8000
# Access UI at http://localhost:5000
```

## Quick Start

```python
import opensearcheval as ose

# Initialize experiment manager
experiments = ose.ExperimentManager()

# Create a new A/B test
experiment = experiments.create_experiment(
    name="New Ranking Algorithm",
    description="Testing improved relevance scoring",
    metrics=["mean_reciprocal_rank", "click_through_rate", "satisfaction_score"]
)

# Evaluate search results
results = [
    {"doc_id": "doc1", "title": "Python Tutorial", "score": 0.95},
    {"doc_id": "doc2", "title": "Machine Learning Guide", "score": 0.87},
]

# Calculate metrics
mrr = ose.mean_reciprocal_rank(
    query="python tutorial",
    results=results,
    relevance_judgments={"doc1": 2, "doc2": 1}
)

print(f"Mean Reciprocal Rank: {mrr:.3f}")
```

## API Endpoints

- `GET /health` - Health check
- `POST /api/v1/evaluate` - Evaluate search results
- `POST /api/v1/analyze-ab-test` - Analyze A/B test results
- `POST /api/v1/llm-judge` - LLM-based evaluation
- `GET /api/v1/experiments` - List experiments
- `POST /api/v1/experiments` - Create experiment
- `GET /api/v1/experiments/{id}` - Get experiment details
- `POST /api/v1/experiments/{id}/start` - Start experiment
- `POST /api/v1/experiments/{id}/stop` - Stop experiment

## Command Line Interface

```bash
# Evaluate search results from file
opensearcheval evaluate --input-file search_data.json --output-file results.json

# Create an experiment
opensearcheval experiment create \
    --name "Improved Ranking" \
    --metrics "mrr,ndcg_at_10,ctr" \
    --description "Testing new ranking algorithm"

# Generate embeddings
opensearcheval embedding generate \
    --input-file documents.json \
    --output-file embeddings.json \
    --model text-embedding-ada-002

# Run A/B test analysis
opensearcheval ab-test analyze \
    --control-data control.json \
    --treatment-data treatment.json \
    --confidence-level 0.95
```

## Configuration

Comprehensive configuration management with environment variables and configuration files:

```python
from opensearcheval.core.config import get_settings

settings = get_settings()
print(f"API Host: {settings.API_HOST}")
print(f"Using MLX: {settings.USE_MLX}")
```

## Testing

Comprehensive test suite with 95%+ code coverage:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=opensearcheval --cov-report=html

# Run specific test categories
pytest tests/test_metrics.py -v
pytest tests/test_agents.py -v
pytest tests/test_api.py -v
```

## Development

```bash
# Clone repository
git clone https://github.com/llamasearchai/OpenSearchEval.git
cd OpenSearchEval

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Format code
black opensearcheval/
isort opensearcheval/
```

## Production Deployment

### Docker Compose
```yaml
version: '3.8'
services:
  opensearcheval-api:
    image: opensearcheval:latest
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
      - DB_URL=postgresql://user:password@db/opensearcheval
      - REDIS_URL=redis://redis:6379/0
```

### Kubernetes
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opensearcheval-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: opensearcheval-api
  template:
    spec:
      containers:
      - name: api
        image: opensearcheval:latest
        ports:
        - containerPort: 8000
```

## Architecture

### Agent-Based Processing
- Distributed agent architecture for scalable processing
- Asynchronous task handling with configurable concurrency
- Fault-tolerant design with automatic retry mechanisms
- Load balancing across agent pools

### MLX Optimization
- Native Apple Silicon support with GPU acceleration
- Optimized neural network operations
- Memory-efficient processing for large datasets
- Automatic fallback to CPU when MLX unavailable

### Extensible Design
- Plugin architecture for custom metrics
- Configurable data connectors
- Custom evaluation criteria
- Modular component design

## Quality Assurance

- **Code Quality**: Black, isort, flake8, mypy
- **Security**: Bandit security scanning
- **Testing**: Comprehensive test suite with pytest
- **CI/CD**: GitHub Actions workflows
- **Documentation**: Comprehensive API documentation
- **Type Safety**: Full type annotations with mypy

## Dependencies

### Core Dependencies
- pydantic>=2.4.0 - Data validation
- fastapi>=0.104.0 - Web framework
- pandas>=2.0.0 - Data manipulation
- numpy>=1.24.0 - Numerical computing
- scikit-learn>=1.3.0 - Machine learning
- mlx>=0.0.5 - Apple Silicon ML
- matplotlib>=3.7.0 - Visualization
- sqlalchemy>=2.0.0 - Database ORM

### Optional Dependencies
- torch>=2.0.0 - Deep learning (GPU support)
- transformers>=4.30.0 - Transformer models
- openai>=1.0.0 - OpenAI API
- redis>=4.5.0 - Caching
- pyspark>=3.4.0 - Big data processing

## Breaking Changes

None - this is the initial release.

## Migration Guide

None - this is the initial release.

## Known Issues

- MLX support requires Apple Silicon (M1/M2/M3) processors
- Some advanced features require additional dependencies
- Large-scale deployments may require configuration tuning

## Roadmap

- Enhanced MLX model support
- Additional data connectors
- Advanced visualization features
- Real-time streaming analytics
- Multi-language support

## Support

- **Documentation**: https://opensearcheval.readthedocs.io/
- **GitHub Issues**: https://github.com/llamasearchai/OpenSearchEval/issues
- **GitHub Discussions**: https://github.com/llamasearchai/OpenSearchEval/discussions
- **Email**: nikjois@llamasearch.ai

## Contributors

- **Nik Jois** - Creator and maintainer (nikjois@llamasearch.ai)

## License

MIT License - see LICENSE file for details.

---

**Package Information**:
- **Name**: opensearcheval
- **Version**: 1.0.0
- **Author**: Nik Jois <nikjois@llamasearch.ai>
- **License**: MIT
- **GitHub**: https://github.com/llamasearchai/OpenSearchEval
- **PyPI**: https://pypi.org/project/opensearcheval/

**Installation**: `pip install opensearcheval`

Made with love for the search evaluation community. 