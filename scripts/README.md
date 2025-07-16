# OpenSearchEval Publication Scripts

This directory contains scripts for publishing OpenSearchEval to GitHub and PyPI.

## Scripts Overview

### 1. `publish_complete.py` - Master Publication Script
The main script that orchestrates the complete publication process.

**Usage:**
```bash
# Complete publication (GitHub + PyPI)
python scripts/publish_complete.py

# Skip tests (faster for testing)
python scripts/publish_complete.py --skip-tests

# Skip GitHub repository creation
python scripts/publish_complete.py --skip-github

# Skip PyPI publication
python scripts/publish_complete.py --skip-pypi

# Publish to Test PyPI instead of production PyPI
python scripts/publish_complete.py --test-pypi
```

### 2. `create_github_repo.py` - GitHub Repository Setup
Creates and configures the GitHub repository with all necessary settings.

**Usage:**
```bash
# Create repository and push code
python scripts/create_github_repo.py

# Create repository without pushing code
python scripts/create_github_repo.py --skip-push

# Create repository without creating release
python scripts/create_github_repo.py --skip-release
```

### 3. `build_and_publish.py` - PyPI Package Publication
Builds and publishes the package to PyPI.

**Usage:**
```bash
# Build and publish to PyPI
python scripts/build_and_publish.py

# Build and publish to Test PyPI
python scripts/build_and_publish.py --test

# Skip running tests
python scripts/build_and_publish.py --skip-tests

# Skip cleaning build directories
python scripts/build_and_publish.py --skip-clean
```

## Prerequisites

Before running these scripts, ensure you have:

1. **Python 3.9+** installed
2. **Git** installed and configured
3. **GitHub CLI** installed and authenticated:
   ```bash
   # Install GitHub CLI (macOS)
   brew install gh
   
   # Authenticate with GitHub
   gh auth login
   ```
4. **PyPI Account** with API token configured:
   ```bash
   # Configure PyPI credentials
   pip install twine
   twine configure
   ```

## Step-by-Step Publication Process

### Option 1: Complete Automated Publication
```bash
# Run the master script for complete publication
python scripts/publish_complete.py
```

### Option 2: Manual Step-by-Step
```bash
# Step 1: Create GitHub repository
python scripts/create_github_repo.py

# Step 2: Build and publish to PyPI
python scripts/build_and_publish.py
```

## What the Scripts Do

### GitHub Repository Setup
- Creates public repository at `llamasearchai/OpenSearchEval`
- Sets up repository description and homepage
- Configures repository topics/tags
- Creates issue and PR labels
- Sets up branch protection rules
- Pushes all code to the repository
- Creates initial v1.0.0 release

### PyPI Package Publication
- Installs build dependencies
- Runs comprehensive test suite
- Cleans previous build artifacts
- Builds source distribution and wheel
- Validates package integrity
- Publishes to PyPI or Test PyPI
- Verifies successful publication

### Quality Assurance
- Validates package structure
- Checks for emojis, placeholders, and stubs
- Ensures version consistency across files
- Runs pytest test suite
- Performs code quality checks (flake8, mypy)
- Validates package metadata

## Repository Configuration

The scripts configure the repository with:

**Features:**
- Issues, Projects, Wiki, Discussions enabled
- Squash merge, merge commits, and rebase merge allowed
- Auto-delete head branches after merge
- Auto-merge and update branch features enabled

**Topics/Tags:**
- search-evaluation, machine-learning, mlx, apple-silicon
- a-b-testing, information-retrieval, search-quality
- fastapi, python, agent-architecture, llm-judge
- search-analytics, ranking-evaluation, user-behavior
- metrics, dashboard, visualization, opensearch, elasticsearch

**Branch Protection:**
- Require pull request reviews (1 approver)
- Require status checks (CI, test, build)
- Dismiss stale reviews
- Require code owner reviews
- Enforce for administrators

## Troubleshooting

### Common Issues

1. **GitHub CLI not authenticated**
   ```bash
   gh auth login
   ```

2. **PyPI credentials not configured**
   ```bash
   pip install twine
   python -m twine configure
   ```

3. **Tests failing**
   ```bash
   # Run tests manually to debug
   python -m pytest tests/ -v
   ```

4. **Package validation errors**
   - Check that all required files exist
   - Ensure no emojis in documentation
   - Verify version consistency

5. **Repository already exists**
   - The scripts handle this gracefully
   - Use `--skip-github` to skip repository creation

### Debug Mode
Add verbose logging to any script:
```bash
python scripts/publish_complete.py --verbose
```

## Security Notes

- Never commit PyPI API tokens to the repository
- Use environment variables or twine configuration for credentials
- The scripts validate package integrity before publication
- Branch protection prevents direct pushes to main branch

## Support

For issues with the publication scripts:
- Check the logs for detailed error messages
- Verify all prerequisites are installed
- Ensure you have proper permissions for the GitHub organization
- Contact: nikjois@llamasearch.ai

---

**Author**: Nik Jois <nikjois@llamasearch.ai>  
**License**: MIT 