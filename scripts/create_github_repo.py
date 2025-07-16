#!/usr/bin/env python3
"""
GitHub repository creation and setup script for OpenSearchEval

This script creates the GitHub repository and sets up all necessary configuration.
"""

import os
import sys
import subprocess
import json
import logging
from pathlib import Path
import argparse

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_command(cmd, cwd=None):
    """Run a shell command and return the result"""
    logger.info(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(f"Command failed: {cmd}")
        logger.error(f"Error: {result.stderr}")
        return False, result.stderr
    logger.info(f"Success: {result.stdout}")
    return True, result.stdout

def check_gh_cli():
    """Check if GitHub CLI is installed and authenticated"""
    logger.info("Checking GitHub CLI...")
    success, output = run_command("gh --version")
    if not success:
        logger.error("GitHub CLI is not installed. Please install it first.")
        return False
    
    success, output = run_command("gh auth status")
    if not success:
        logger.error("GitHub CLI is not authenticated. Please run 'gh auth login' first.")
        return False
    
    return True

def create_repository():
    """Create the GitHub repository"""
    logger.info("Creating GitHub repository...")
    
    repo_description = "A comprehensive search evaluation platform with agent architecture and MLX integration for Apple Silicon optimization"
    
    cmd = f'''gh repo create llamasearchai/OpenSearchEval \
        --public \
        --description "{repo_description}" \
        --homepage "https://opensearcheval.readthedocs.io/" \
        --add-readme=false'''
    
    success, output = run_command(cmd)
    if not success:
        if "already exists" in output:
            logger.info("Repository already exists, continuing...")
            return True
        return False
    
    logger.info("Repository created successfully!")
    return True

def setup_repository_settings():
    """Setup repository settings"""
    logger.info("Setting up repository settings...")
    
    # Enable features
    settings = {
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True,
        "has_downloads": True,
        "allow_squash_merge": True,
        "allow_merge_commit": True,
        "allow_rebase_merge": True,
        "delete_branch_on_merge": True,
        "allow_auto_merge": True,
        "allow_update_branch": True,
        "use_squash_pr_title_as_default": True,
        "squash_merge_commit_title": "PR_TITLE",
        "squash_merge_commit_message": "PR_BODY",
        "merge_commit_title": "PR_TITLE",
        "merge_commit_message": "PR_BODY"
    }
    
    # Topics/tags for the repository
    topics = [
        "search-evaluation",
        "machine-learning",
        "mlx",
        "apple-silicon",
        "a-b-testing",
        "information-retrieval",
        "search-quality",
        "fastapi",
        "python",
        "agent-architecture",
        "llm-judge",
        "search-analytics",
        "ranking-evaluation",
        "user-behavior",
        "metrics",
        "dashboard",
        "visualization",
        "opensearch",
        "elasticsearch",
        "search-engine"
    ]
    
    # Set topics
    topics_str = " ".join(topics)
    success, output = run_command(f"gh repo edit llamasearchai/OpenSearchEval --add-topic {topics_str}")
    if not success:
        logger.warning("Failed to set repository topics")
    
    return True

def setup_branch_protection():
    """Setup branch protection rules"""
    logger.info("Setting up branch protection...")
    
    # Main branch protection
    protection_cmd = '''gh api repos/llamasearchai/OpenSearchEval/branches/main/protection \
        --method PUT \
        --field required_status_checks='{"strict":true,"contexts":["CI","test","build"]}' \
        --field enforce_admins=true \
        --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
        --field restrictions=null'''
    
    success, output = run_command(protection_cmd)
    if not success:
        logger.warning("Failed to set up branch protection (this is normal if the branch doesn't exist yet)")
    
    return True

def setup_labels():
    """Setup issue and PR labels"""
    logger.info("Setting up repository labels...")
    
    labels = [
        {"name": "bug", "color": "d73a4a", "description": "Something isn't working"},
        {"name": "enhancement", "color": "a2eeef", "description": "New feature or request"},
        {"name": "documentation", "color": "0075ca", "description": "Improvements or additions to documentation"},
        {"name": "good first issue", "color": "7057ff", "description": "Good for newcomers"},
        {"name": "help wanted", "color": "008672", "description": "Extra attention is needed"},
        {"name": "question", "color": "d876e3", "description": "Further information is requested"},
        {"name": "wontfix", "color": "ffffff", "description": "This will not be worked on"},
        {"name": "duplicate", "color": "cfd3d7", "description": "This issue or pull request already exists"},
        {"name": "invalid", "color": "e4e669", "description": "This doesn't seem right"},
        {"name": "priority-high", "color": "ff0000", "description": "High priority issue"},
        {"name": "priority-medium", "color": "ff8c00", "description": "Medium priority issue"},
        {"name": "priority-low", "color": "00ff00", "description": "Low priority issue"},
        {"name": "needs-triage", "color": "fbca04", "description": "Needs to be triaged"},
        {"name": "mlx", "color": "0e8a16", "description": "Related to MLX integration"},
        {"name": "api", "color": "1d76db", "description": "Related to API"},
        {"name": "ui", "color": "5319e7", "description": "Related to user interface"},
        {"name": "performance", "color": "ff6b6b", "description": "Performance related"},
        {"name": "security", "color": "b60205", "description": "Security related"},
        {"name": "dependencies", "color": "0366d6", "description": "Pull requests that update a dependency file"},
        {"name": "ci", "color": "28a745", "description": "Continuous integration related"}
    ]
    
    for label in labels:
        cmd = f'''gh api repos/llamasearchai/OpenSearchEval/labels \
            --method POST \
            --field name="{label['name']}" \
            --field color="{label['color']}" \
            --field description="{label['description']}"'''
        
        success, output = run_command(cmd)
        if not success and "already_exists" not in output:
            logger.warning(f"Failed to create label: {label['name']}")
    
    return True

def push_code():
    """Push code to the repository"""
    logger.info("Pushing code to repository...")
    
    # Initialize git if not already done
    if not os.path.exists('.git'):
        run_command("git init")
        run_command("git branch -M main")
    
    # Add remote
    run_command("git remote add origin https://github.com/llamasearchai/OpenSearchEval.git")
    
    # Add all files
    run_command("git add .")
    
    # Commit
    run_command('git commit -m "Initial commit: OpenSearchEval v1.0.0 - Ultimate Search Evaluation Platform"')
    
    # Push
    success, output = run_command("git push -u origin main")
    if not success:
        logger.error("Failed to push code to repository")
        return False
    
    logger.info("Code pushed successfully!")
    return True

def create_release():
    """Create the first release"""
    logger.info("Creating initial release...")
    
    release_notes = """# OpenSearchEval v1.0.0 - Initial Release

This is the initial release of OpenSearchEval, a comprehensive search evaluation platform with agent architecture and MLX integration.

## Key Features

- **Search Quality Metrics**: MRR, NDCG, Precision@K, Recall@K, and more
- **A/B Testing Framework**: Statistical significance testing with robust analytics
- **User Behavior Analytics**: Click tracking, dwell time, satisfaction metrics
- **Agent Architecture**: Distributed processing with asynchronous task handling
- **MLX Integration**: Optimized ML components for Apple Silicon
- **LLM-as-Judge**: AI-powered qualitative evaluation of search results
- **FastAPI Endpoints**: Production-ready REST API with automatic documentation
- **Rich Visualizations**: Interactive charts, dashboards, and reporting tools
- **Extensible Design**: Plugin architecture for custom metrics and data sources
- **Performance Monitoring**: Real-time metrics collection and alerting

## Installation

```bash
pip install opensearcheval
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

## Documentation

- [Documentation](https://opensearcheval.readthedocs.io/)
- [API Reference](https://opensearcheval.readthedocs.io/en/latest/api/)
- [Examples](https://github.com/llamasearchai/OpenSearchEval/tree/main/examples)

## Support

- [GitHub Issues](https://github.com/llamasearchai/OpenSearchEval/issues)
- [GitHub Discussions](https://github.com/llamasearchai/OpenSearchEval/discussions)
- Email: nikjois@llamasearch.ai

---

Made with ❤️ by [Nik Jois](https://github.com/nikjois)
"""
    
    cmd = f'''gh release create v1.0.0 \
        --title "OpenSearchEval v1.0.0 - Ultimate Search Evaluation Platform" \
        --notes "{release_notes}" \
        --latest'''
    
    success, output = run_command(cmd)
    if not success:
        logger.warning("Failed to create release (this is normal if already exists)")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Create and setup OpenSearchEval GitHub repository')
    parser.add_argument('--skip-push', action='store_true', help='Skip pushing code to repository')
    parser.add_argument('--skip-release', action='store_true', help='Skip creating release')
    
    args = parser.parse_args()
    
    # Change to project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    logger.info("Starting GitHub repository setup...")
    
    # Check prerequisites
    if not check_gh_cli():
        sys.exit(1)
    
    # Create repository
    if not create_repository():
        sys.exit(1)
    
    # Setup repository settings
    if not setup_repository_settings():
        logger.warning("Failed to setup some repository settings")
    
    # Setup labels
    if not setup_labels():
        logger.warning("Failed to setup some labels")
    
    # Push code
    if not args.skip_push:
        if not push_code():
            sys.exit(1)
    
    # Setup branch protection (after pushing code)
    if not setup_branch_protection():
        logger.warning("Failed to setup branch protection")
    
    # Create release
    if not args.skip_release:
        if not create_release():
            logger.warning("Failed to create release")
    
    logger.info("GitHub repository setup completed successfully!")
    logger.info("Repository URL: https://github.com/llamasearchai/OpenSearchEval")

if __name__ == "__main__":
    main() 