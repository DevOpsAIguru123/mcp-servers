import asyncio
import os
from mcp.server.fastmcp import FastMCP

# Get host and port from environment variables with defaults
host = os.getenv("MCP_HOST", "localhost")
port = int(os.getenv("MCP_PORT", "8000"))

mcp = FastMCP(
    name="calculator-mcp",
    host=host,
    port=port
)
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

async def main():
    await mcp.run_streamable_http_async()

if __name__ == "__main__":
    asyncio.run(main())