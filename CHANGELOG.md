# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Real-time metrics streaming via WebSocket
- Grafana dashboard templates
- Advanced alerting system
- Custom connector framework

### Changed
- Improved MLX performance on Apple Silicon
- Enhanced API rate limiting
- Better error handling and logging

### Fixed
- Memory leak in long-running experiments
- Race condition in agent task processing
- Incorrect NDCG calculation for edge cases

## [1.0.0] - 2024-01-15

### Added
- Initial release of OpenSearchEval
- Core search evaluation metrics (MRR, NDCG, Precision@K, Recall@K)
- User behavior analytics (CTR, dwell time, abandonment rate)
- A/B testing framework with statistical significance testing
- Agent-based architecture for distributed processing
- MLX integration for Apple Silicon optimization
- LLM-as-Judge evaluation capabilities
- FastAPI-based REST API with automatic documentation
- Rich visualization tools and dashboards
- Command-line interface for batch processing
- Docker containerization support
- Comprehensive test suite with 95%+ coverage
- Production-ready configuration management
- Database connectivity (PostgreSQL, MySQL, SQLite)
- Redis caching support
- Prometheus metrics integration
- Comprehensive documentation and examples

### Metrics
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG@K)
- Precision@K and Recall@K
- Click-Through Rate (CTR)
- Time to First Click
- Average Dwell Time
- Abandoned Search Rate
- Satisfaction Score
- Reciprocal Rank Fusion
- Diversity Score

### API Endpoints
- `GET /health` - Health check
- `POST /api/v1/evaluate` - Evaluate search results
- `POST /api/v1/analyze-ab-test` - Analyze A/B test results
- `POST /api/v1/llm-judge` - LLM-based evaluation
- `GET /api/v1/experiments` - List experiments
- `POST /api/v1/experiments` - Create experiment
- `GET /api/v1/experiments/{id}` - Get experiment details
- `POST /api/v1/experiments/{id}/start` - Start experiment
- `POST /api/v1/experiments/{id}/stop` - Stop experiment

### Agent Types
- SearchEvaluationAgent - Processes search quality metrics
- ABTestAgent - Handles A/B test analysis
- UserBehaviorAgent - Analyzes user interaction patterns

### Data Connectors
- SQL databases (PostgreSQL, MySQL, SQLite)
- Apache Spark integration
- Databricks connector
- REST API connector

### ML Components
- SearchRankingModel - Neural ranking model using MLX
- ClickThroughRatePredictor - CTR prediction model
- EmbeddingModel - Text embedding generation
- LLMJudge - LLM-based relevance evaluation

### Visualization Tools
- Time series plots for metrics
- A/B test comparison charts
- User behavior heatmaps
- Radar charts for metric comparison
- Interactive dashboards

### CLI Commands
- `opensearcheval evaluate` - Evaluate search results
- `opensearcheval experiment create` - Create new experiment
- `opensearcheval embedding generate` - Generate embeddings
- `opensearcheval ab-test analyze` - Analyze A/B test results

### Configuration
- Environment-based configuration
- YAML/JSON configuration files
- Docker Compose setup
- Kubernetes deployment templates

### Security
- API key authentication
- Rate limiting
- Input validation
- SQL injection prevention
- XSS protection

### Performance
- Async processing with asyncio
- Connection pooling
- Result caching with Redis
- Batch processing capabilities
- Memory optimization

### Monitoring
- Prometheus metrics collection
- Structured logging
- Health check endpoints
- Performance monitoring
- Error tracking

### Testing
- Unit tests with pytest
- Integration tests
- Performance tests
- Mock data generation
- Test fixtures

### Documentation
- Comprehensive README
- API documentation
- User guides
- Development setup guide
- Deployment instructions
- Architecture overview

### Dependencies
- Python 3.9+ support
- FastAPI for web framework
- MLX for Apple Silicon ML
- Pydantic for data validation
- SQLAlchemy for database ORM
- Redis for caching
- Prometheus for metrics
- Docker for containerization

## [0.9.0] - 2023-12-01

### Added
- Beta release with core functionality
- Basic search evaluation metrics
- Simple A/B testing framework
- Initial API implementation
- Docker support

### Known Issues
- Limited MLX optimization
- Basic error handling
- No production deployment guide

## [0.8.0] - 2023-11-15

### Added
- Alpha release for testing
- Core metric calculations
- Basic agent framework
- SQLite database support

### Known Issues
- No web UI
- Limited documentation
- Basic test coverage

## [0.7.0] - 2023-11-01

### Added
- Initial development version
- Basic project structure
- Core metric implementations
- Simple CLI interface

### Known Issues
- Development-only release
- No production features
- Limited functionality

---

## Release Notes

### Version 1.0.0 Release Notes

This is the first stable release of OpenSearchEval, a comprehensive search evaluation platform. This release includes:

**Production-Ready Features:**
- Complete search evaluation metrics suite
- Statistical A/B testing framework
- Real-time user behavior analytics
- Agent-based distributed processing
- MLX-optimized ML components

**Performance Improvements:**
- Up to 10x faster evaluation on Apple Silicon with MLX
- Async processing with high concurrency
- Efficient caching with Redis
- Optimized database queries

**Rich Analytics:**
- Interactive dashboards
- Real-time metrics streaming
- Custom visualization tools
- Comprehensive reporting

**Developer Experience:**
- Intuitive Python API
- Comprehensive CLI tools
- Docker containerization
- Extensive documentation

**Production Security:**
- API authentication
- Rate limiting
- Input validation
- Security best practices

**Scalability:**
- Distributed agent architecture
- Database connection pooling
- Horizontal scaling support
- Load balancing ready

### Migration Guide

This is the initial release, so no migration is required.

### Breaking Changes

None in this initial release.

### Deprecations

None in this initial release.

### Security Updates

- Implemented comprehensive security measures
- Added rate limiting and authentication
- Input validation and sanitization
- SQL injection prevention

### Bug Fixes

None in this initial release.

---

## Contributing

We welcome contributions to OpenSearchEval! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to contribute.

### Reporting Issues

If you encounter any issues, please report them on our [GitHub Issues](https://github.com/llamasearchai/OpenSearchEval/issues) page.

### Feature Requests

Feature requests are welcome! Please use our [GitHub Discussions](https://github.com/llamasearchai/OpenSearchEval/discussions) to propose new features.

---

## Support

- **Documentation**: [https://opensearcheval.readthedocs.io/](https://opensearcheval.readthedocs.io/)
- **Issues**: [GitHub Issues](https://github.com/llamasearchai/OpenSearchEval/issues)
- **Discussions**: [GitHub Discussions](https://github.com/llamasearchai/OpenSearchEval/discussions)
- **Email**: nikjois@llamasearch.ai 