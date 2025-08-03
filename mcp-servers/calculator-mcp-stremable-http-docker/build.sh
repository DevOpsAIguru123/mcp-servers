#!/bin/bash

# Calculator MCP Server Docker Build Script

set -e  # Exit on any error

echo "🚀 Building Calculator MCP Server Docker Image..."

# Build the Docker image
docker build -t calculator-mcp-server .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo ""
    echo "📋 Available commands:"
    echo "  docker run -p 8000:8000 calculator-mcp-server    # Run the server"
    echo "  docker-compose up                               # Run with docker-compose"
    echo "  docker-compose up -d                            # Run in background"
    echo "  docker-compose down                             # Stop the server"
    echo ""
    echo "🌐 Server will be available at: http://localhost:8000"
    echo "📚 MCP endpoint: http://localhost:8000/mcp/v1/sse"
    echo ""
    echo "🧪 Test the server with: python client.py"
else
    echo "❌ Docker build failed!"
    exit 1
fi 