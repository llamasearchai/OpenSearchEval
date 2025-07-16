#!/usr/bin/env python3
"""
Build and publish script for OpenSearchEval package

This script handles building the package for PyPI and publishing it.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import argparse
import logging

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
        return False
    logger.info(f"Success: {result.stdout}")
    return True

def clean_build_dirs():
    """Clean build directories"""
    logger.info("Cleaning build directories...")
    dirs_to_clean = ['build', 'dist', 'opensearcheval.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            logger.info(f"Removed {dir_name}")

def install_build_dependencies():
    """Install build dependencies"""
    logger.info("Installing build dependencies...")
    deps = ['build', 'twine', 'wheel']
    for dep in deps:
        if not run_command(f"pip install {dep}"):
            return False
    return True

def run_tests():
    """Run the test suite"""
    logger.info("Running tests...")
    if not run_command("python -m pytest tests/ -v"):
        logger.error("Tests failed!")
        return False
    return True

def build_package():
    """Build the package"""
    logger.info("Building package...")
    if not run_command("python -m build"):
        logger.error("Package build failed!")
        return False
    return True

def check_package():
    """Check the built package"""
    logger.info("Checking package...")
    if not run_command("python -m twine check dist/*"):
        logger.error("Package check failed!")
        return False
    return True

def publish_to_test_pypi():
    """Publish to Test PyPI"""
    logger.info("Publishing to Test PyPI...")
    if not run_command("python -m twine upload --repository testpypi dist/*"):
        logger.error("Test PyPI upload failed!")
        return False
    return True

def publish_to_pypi():
    """Publish to PyPI"""
    logger.info("Publishing to PyPI...")
    if not run_command("python -m twine upload dist/*"):
        logger.error("PyPI upload failed!")
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description='Build and publish OpenSearchEval package')
    parser.add_argument('--test', action='store_true', help='Publish to Test PyPI instead of PyPI')
    parser.add_argument('--skip-tests', action='store_true', help='Skip running tests')
    parser.add_argument('--skip-clean', action='store_true', help='Skip cleaning build directories')
    
    args = parser.parse_args()
    
    # Change to project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    logger.info("Starting build and publish process...")
    
    # Clean build directories
    if not args.skip_clean:
        clean_build_dirs()
    
    # Install build dependencies
    if not install_build_dependencies():
        sys.exit(1)
    
    # Run tests
    if not args.skip_tests:
        if not run_tests():
            sys.exit(1)
    
    # Build package
    if not build_package():
        sys.exit(1)
    
    # Check package
    if not check_package():
        sys.exit(1)
    
    # Publish package
    if args.test:
        if not publish_to_test_pypi():
            sys.exit(1)
        logger.info("Package successfully published to Test PyPI!")
        logger.info("Install with: pip install -i https://test.pypi.org/simple/ opensearcheval")
    else:
        if not publish_to_pypi():
            sys.exit(1)
        logger.info("Package successfully published to PyPI!")
        logger.info("Install with: pip install opensearcheval")
    
    logger.info("Build and publish process completed successfully!")

if __name__ == "__main__":
    main() 