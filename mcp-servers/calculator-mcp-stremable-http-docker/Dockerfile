FROM python:3.11-slim

WORKDIR /app

# Install uv for faster dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY server.py client.py ./

# Expose port for HTTP interface
EXPOSE 8000

# Set environment variables for the MCP server
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000

# Run the MCP server with streamable HTTP
CMD ["uv", "run", "python", "server.py"] 