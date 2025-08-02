# Calculator MCP Server

A Model Context Protocol (MCP) server that provides basic arithmetic operations. This server exposes mathematical calculation tools that can be used by MCP clients to perform addition, subtraction, multiplication, and division operations.

## Features

The calculator MCP server provides the following tools:

- **add(a, b)** - Add two numbers
- **subtract(a, b)** - Subtract two numbers  
- **multiply(a, b)** - Multiply two numbers
- **divide(a, b)** - Divide two numbers (with zero division protection)

All operations support floating-point numbers and return floating-point results.

## Requirements

- Python 3.11 or higher
- MCP library (>=1.12.3)

## Installation

1. Clone or download this repository
2. Install dependencies using uv (recommended) or pip:

```bash
# Using uv
uv sync

# Or using pip
pip install mcp mcp-cli
```

## Running the Server

### Method 1: Direct execution
```bash
python server.py
```

### Method 2: Using uv
```bash
uv run server.py
```

### Method 3: Using MCP development mode
```bash
uv run mcp dev server.py
```

The server runs in stdio mode and communicates via standard input/output streams following the MCP protocol.

## Usage with MCP Clients

To use this server with an MCP client, you'll need to configure the client to connect to this server. The server communicates over stdio.

Example client configuration:
```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["/path/to/calculator-mcp/server.py"]
    }
  }
}
```

## Inspecting the Server

### 1. Using MCP CLI Inspector

Install the MCP CLI tools and use the inspector:

```bash
# Install MCP CLI
pip install mcp-cli

# Inspect the server
mcp-inspector python server.py
```

This will show you:
- Available tools and their schemas
- Server capabilities
- Tool descriptions and parameters

### 2. Manual Testing

You can test individual tools by creating a simple client script:

```python
import asyncio
from mcp.client.stdio import stdio_client

async def test_calculator():
    async with stdio_client("python", ["server.py"]) as (read, write):
        # Test addition
        result = await read.call_tool("add", {"a": 5, "b": 3})
        print(f"5 + 3 = {result}")
        
        # Test division
        result = await read.call_tool("divide", {"a": 10, "b": 2})
        print(f"10 / 2 = {result}")

asyncio.run(test_calculator())
```

### 3. Checking Server Health

To verify the server starts correctly:

```bash
# Test server startup
python server.py &lt;&lt;EOF
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}}
EOF
```

## Error Handling

The server includes proper error handling:
- Division by zero returns a `ValueError` with message "Cannot divide by zero"
- Invalid parameters will return appropriate MCP error responses
- All operations validate input types (expects float/numeric values)

## Development

The server is built using FastMCP, which provides a simplified way to create MCP servers. The code structure is:

- `server.py` - Main server implementation with tool definitions
- `pyproject.toml` - Project configuration and dependencies
- `README.md` - This documentation

To modify or extend the calculator:
1. Add new tool functions decorated with `@mcp.tool()`
2. Ensure proper type hints and docstrings
3. Test using the inspection methods above

## License

This project is provided as-is for educational and development purposes.