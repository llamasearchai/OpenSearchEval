# Multi-stage build for production OpenSearchEval
FROM python:3.9-slim as builder

# Set environment variables for build
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.6.1

# Install system dependencies for building
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Copy source code and install package
COPY . .
RUN pip install -e .

# Production stage
FROM python:3.9-slim as production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Create app directory and set permissions
RUN mkdir -p /app/data /app/logs /app/models /app/experiments \
    && chown -R appuser:appuser /app

# Copy application code
COPY --chown=appuser:appuser . /app

# Switch to non-root user
USER appuser

# Set working directory
WORKDIR /app

# Create default configuration
RUN python -c "from opensearcheval.core.config import create_default_env_file; create_default_env_file()"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Default command
CMD ["uvicorn", "opensearcheval.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

# Development stage
FROM builder as development

# Install development dependencies
RUN pip install -e .[dev]

# Copy development configuration
COPY --chown=appuser:appuser . /app
WORKDIR /app

# Create non-root user for development
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    chown -R appuser:appuser /app

USER appuser

# Development command with auto-reload
CMD ["uvicorn", "opensearcheval.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# UI stage
FROM production as ui

# Expose UI port
EXPOSE 5000

# UI command
CMD ["python", "-m", "opensearcheval.ui.app"]