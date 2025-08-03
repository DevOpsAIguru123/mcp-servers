FROM python:3.11-slim

WORKDIR /app

# Install uv for faster dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY server.py ./

# Expose port (if needed for future HTTP interface)
EXPOSE 8000

# Run the MCP server
CMD ["uv", "run", "python", "server.py"]