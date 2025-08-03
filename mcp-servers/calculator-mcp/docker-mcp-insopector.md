To access the MCP server running in Docker:

  1. MCP Inspector with Docker
  Add server config:
  {
    "command": "docker",
    "args": ["run", "-i", "--rm", "calculator-mcp"]
  }

  2. Claude Desktop with Docker
  Add to ~/Library/Application Support/Claude/claude_desktop_config.json:
  {
    "mcpServers": {
      "calculator": {
        "command": "docker",
        "args": ["run", "-i", "--rm", "calculator-mcp"]
      }
    }
  }

  3. MCP CLI with Docker
  mcp-cli -s "docker run -i --rm calculator-mcp"

  Key points:
  - Use -i flag for interactive stdin/stdout communication
  - Use --rm to auto-remove container after exit
  - MCP servers communicate via stdio, not HTTP, so no port mapping needed
  - The container will start fresh for each MCP client connection

  The Docker approach works but is less efficient than running locally since it creates a new container for each client connection.


  echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | docker run -i --rm calculator-mcp

  ### working docker inspector 

  (
  echo '{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"cli","version":"1.0"}}}'
  echo '{"jsonrpc":"2.0","method":"notifications/initialized"}'
  echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
) | docker run -i --rm calculator-mcp