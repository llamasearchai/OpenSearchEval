# Contributing to OpenSearchEval

We love contributions! This document outlines how to contribute to OpenSearchEval effectively.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)
- [Community](#community)

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional, for containerized development)
- Redis (optional, for caching)
- PostgreSQL (optional, for database testing)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/OpenSearchEval.git
cd OpenSearchEval
```

3. Add the original repository as upstream:

```bash
git remote add upstream https://github.com/llamasearchai/OpenSearchEval.git
```

## Development Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Development Dependencies

```bash
# Install the package in development mode
pip install -e .[dev]

# Or install all dependencies
pip install -e .[all]
```

### 3. Set Up Pre-commit Hooks

```bash
pre-commit install
```

### 4. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit configuration as needed
nano .env
```

### 5. Run Initial Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=opensearcheval --cov-report=html
```

### 6. Start Development Services (Optional)

```bash
# Start Redis and PostgreSQL with Docker
docker-compose up -d redis db

# Or start all services
docker-compose up -d
```

## Making Changes

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass

### 3. Commit Your Changes

```bash
git add .
git commit -m "Add feature: description of your changes"
```

**Commit Message Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(metrics): add reciprocal rank fusion metric

Implements RRF algorithm for combining multiple search result lists
with configurable k parameter.

Closes #123
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_metrics.py

# Run with coverage
pytest --cov=opensearcheval --cov-report=html

# Run performance tests
pytest tests/performance/ -v

# Run tests in parallel
pytest -n auto
```

### Writing Tests

1. **Unit Tests**: Test individual functions and classes
2. **Integration Tests**: Test component interactions
3. **Performance Tests**: Test performance characteristics
4. **API Tests**: Test API endpoints

**Test Structure:**
```python
import pytest
from opensearcheval.core.metrics import mean_reciprocal_rank

class TestMeanReciprocalRank:
    def test_perfect_ranking(self):
        """Test MRR with perfect ranking"""
        results = [{"doc_id": "doc1"}]
        relevance = {"doc1": 1}
        
        mrr = mean_reciprocal_rank("query", results, relevance)
        assert mrr == 1.0
    
    def test_no_relevant_results(self):
        """Test MRR with no relevant results"""
        results = [{"doc_id": "doc1"}]
        relevance = {}
        
        mrr = mean_reciprocal_rank("query", results, relevance)
        assert mrr == 0.0
    
    @pytest.mark.parametrize("position,expected", [
        (1, 1.0),
        (2, 0.5),
        (3, 0.333),
    ])
    def test_mrr_positions(self, position, expected):
        """Test MRR at different positions"""
        results = [{"doc_id": f"doc{i}"} for i in range(1, 6)]
        relevance = {f"doc{position}": 1}
        
        mrr = mean_reciprocal_rank("query", results, relevance)
        assert abs(mrr - expected) < 0.001
```

### Test Data

Use the test data utilities:

```python
from opensearcheval.testing import generate_test_data

def test_with_synthetic_data():
    test_data = generate_test_data(
        num_queries=100,
        num_results_per_query=10,
        relevance_distribution=[0.7, 0.2, 0.1]
    )
    
    # Use test_data in your tests
    assert len(test_data) == 100
```

## Submitting Changes

### 1. Push Your Changes

```bash
git push origin feature/your-feature-name
```

### 2. Create Pull Request

1. Go to the GitHub repository
2. Click "New Pull Request"
3. Select your branch
4. Fill out the PR template

### 3. Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or properly documented)
```

### 4. Code Review Process

1. Automated checks must pass
2. At least one maintainer review required
3. All conversations must be resolved
4. Tests must pass in CI/CD

## Code Style

### Python Code Style

We use the following tools:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security analysis

### Running Code Style Checks

```bash
# Format code
black opensearcheval/
isort opensearcheval/

# Check linting
flake8 opensearcheval/

# Type checking
mypy opensearcheval/

# Security check
bandit -r opensearcheval/
```

### Style Guidelines

1. **Docstrings**: Use Google-style docstrings
2. **Type Hints**: Add type hints to all functions
3. **Error Handling**: Use specific exception types
4. **Logging**: Use structured logging
5. **Constants**: Use UPPER_CASE for constants

**Example:**
```python
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

def calculate_precision_at_k(
    results: List[Dict[str, str]], 
    relevance: Dict[str, int], 
    k: int = 10
) -> float:
    """
    Calculate Precision@K for search results.
    
    Args:
        results: List of search result dictionaries
        relevance: Mapping of document IDs to relevance scores
        k: Number of results to consider
        
    Returns:
        Precision@K score between 0.0 and 1.0
        
    Raises:
        ValueError: If k is less than 1
        
    Example:
        >>> results = [{"doc_id": "doc1"}, {"doc_id": "doc2"}]
        >>> relevance = {"doc1": 1, "doc2": 0}
        >>> calculate_precision_at_k(results, relevance, k=2)
        0.5
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    
    logger.debug(f"Calculating Precision@{k} for {len(results)} results")
    
    # Implementation here
    pass
```

## Documentation

### Types of Documentation

1. **API Documentation**: Docstrings in code
2. **User Guide**: How to use the library
3. **Developer Guide**: How to contribute
4. **Architecture**: System design
5. **Examples**: Code examples and tutorials

### Building Documentation

```bash
# Install documentation dependencies
pip install -e .[dev]

# Build documentation
cd docs/
make html

# Serve documentation locally
make serve
```

### Documentation Standards

- Use clear, concise language
- Include code examples
- Keep examples up-to-date
- Use proper markdown formatting
- Include diagrams where helpful

## Issue Reporting

### Before Reporting

1. Check existing issues
2. Search documentation
3. Try latest version
4. Reproduce with minimal example

### Issue Template

```markdown
## Bug Report

**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g., macOS 12.0]
- Python: [e.g., 3.9.7]
- OpenSearchEval: [e.g., 1.0.0]
- Other relevant versions

**Additional Context:**
Any other relevant information
```

## Feature Requests

### Feature Request Template

```markdown
## Feature Request

**Is your feature request related to a problem?**
Clear description of the problem

**Describe the solution you'd like**
Clear description of desired feature

**Describe alternatives you've considered**
Alternative solutions or features

**Additional context**
Any other context about the feature request
```

### Feature Development Process

1. **Discussion**: Discuss in GitHub Discussions
2. **Proposal**: Create detailed proposal
3. **Review**: Maintainer review and feedback
4. **Implementation**: Develop feature
5. **Testing**: Comprehensive testing
6. **Documentation**: Update documentation
7. **Review**: Code review process

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General discussion and questions
- **Email**: nikjois@llamasearch.ai for direct contact

### Getting Help

1. Check the documentation
2. Search existing issues
3. Ask in GitHub Discussions
4. Contact maintainers

### Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes
- Documentation credits
- Git commit history

## Release Process

### For Maintainers

1. **Version Bump**: Update version in `__init__.py`
2. **Changelog**: Update `CHANGELOG.md`
3. **Tests**: Ensure all tests pass
4. **Documentation**: Update documentation
5. **Release**: Create GitHub release
6. **PyPI**: Publish to PyPI

### Semantic Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality, backwards compatible
- **PATCH**: Bug fixes, backwards compatible

## Questions?

If you have questions about contributing, please:

1. Check this document
2. Search existing issues and discussions
3. Create a new discussion
4. Contact the maintainers

Thank you for contributing to OpenSearchEval! 