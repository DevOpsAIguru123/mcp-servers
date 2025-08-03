# Calculator MCP Server - Docker Setup

This directory contains a Docker-ready implementation of a Calculator MCP (Model Context Protocol) server with streamable HTTP support.

## 🐳 Quick Start

### Option 1: Using the Build Script (Recommended)

```bash
# Make the build script executable (if not already done)
chmod +x build.sh

# Build and get instructions
./build.sh

# Run the server
docker run -p 8000:8000 calculator-mcp-server
```

### Option 2: Using Docker Compose

```bash
# Build and run in one command
docker-compose up --build

# Run in background
docker-compose up -d

# Stop the server
docker-compose down
```

### Option 3: Manual Docker Commands

```bash
# Build the image
docker build -t calculator-mcp-server .

# Run the container
docker run -p 8000:8000 calculator-mcp-server
```

## 📋 Available Tools

The server provides the following calculator tools:

- **add(a, b)**: Add two numbers
- **subtract(a, b)**: Subtract two numbers  
- **multiply(a, b)**: Multiply two numbers
- **divide(a, b)**: Divide two numbers (with zero division protection)

## 🌐 API Endpoints

- **MCP Streamable HTTP**: `http://localhost:8000/mcp`
- **Server Status**: `http://localhost:8000/health` (if implemented)

## 🧪 Testing

### Using the Python Client

```bash
# Test the server with the included client
python client.py
```

### Using curl

```bash
# List available tools
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list"
  }'

# Call a tool (Note: Requires proper MCP client for session handling)
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "add",
      "arguments": {"a": 10, "b": 5}
    }
  }'
```

## 🔧 Configuration

### Environment Variables

- `MCP_HOST`: Server host (default: `localhost`, use `0.0.0.0` for Docker)
- `MCP_PORT`: Server port (default: `8000`)

### Docker Configuration

The Docker setup includes:

- **Multi-stage build** with uv for fast dependency management
- **Health checks** for container monitoring
- **Proper port exposure** for HTTP access
- **Environment variable support** for configuration
- **Optimized .dockerignore** for faster builds

## 📁 Project Structure

```
calculator-mcp-stremable-http-docker/
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore          # Docker build exclusions
├── build.sh               # Build script
├── server.py              # MCP server implementation
├── client.py              # Test client
├── pyproject.toml         # Python dependencies
├── uv.lock               # Locked dependencies
└── README.md             # Main project documentation
```

## 🚀 Development

### Local Development

```bash
# Install dependencies
uv sync

# Run server locally
uv run python server.py

# Test with client
uv run python client.py
```

### Docker Development

```bash
# Build with no cache (for dependency changes)
docker build --no-cache -t calculator-mcp-server .

# Run with volume mount for development
docker run -p 8000:8000 -v $(pwd):/app calculator-mcp-server
```

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in docker-compose.yml or use a different port
2. **Build failures**: Ensure Docker has enough memory and disk space
3. **Connection refused**: Check if the server is running and ports are exposed

### Logs

```bash
# View container logs
docker logs <container_id>

# Follow logs in real-time
docker logs -f <container_id>

# View docker-compose logs
docker-compose logs
```

## 📚 Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/microsoft/fastmcp)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the main README.md for details. 