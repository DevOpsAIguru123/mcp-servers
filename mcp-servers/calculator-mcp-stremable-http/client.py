import asyncio
import aiohttp
import json

async def call_mcp_tool(session, tool_name, arguments):
    """Call an MCP tool via HTTP"""
    url = "http://localhost:8000/mcp/v1/sse"  # Adjust endpoint if needed
    
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    
    async with session.post(url, json=request) as response:
        if response.status == 200:
            result = await response.json()
            return result
        else:
            return {"error": f"HTTP {response.status}: {await response.text()}"}

async def list_tools(session):
    """List available MCP tools"""
    url = "http://localhost:8000/mcp"  # Adjust endpoint if needed
    
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list"
    }
    
    async with session.post(url, json=request) as response:
        if response.status == 200:
            result = await response.json()
            return result
        else:
            return {"error": f"HTTP {response.status}: {await response.text()}"}

async def test_calculator():
    """Test the calculator MCP server"""
    async with aiohttp.ClientSession() as session:
        # List available tools
        print("Available tools:")
        tools_response = await list_tools(session)
        if "result" in tools_response:
            for tool in tools_response["result"].get("tools", []):
                print(f"  - {tool['name']}: {tool.get('description', 'No description')}")
        print()
        
        # Test calculations
        tests = [
            ("add", {"a": 10, "b": 5}, "10 + 5"),
            ("subtract", {"a": 20, "b": 8}, "20 - 8"),
            ("multiply", {"a": 4, "b": 7}, "4 * 7"),
            ("divide", {"a": 100, "b": 4}, "100 / 4"),
            ("power", {"base": 2, "exponent": 8}, "2 ^ 8"),
            ("calculate_percentage", {"value": 200, "percentage": 15}, "15% of 200"),
        ]
        
        for tool_name, args, description in tests:
            print(f"Testing {description}:")
            result = await call_mcp_tool(session, tool_name, args)
            
            if "result" in result:
                content = result["result"].get("content", [])
                if content and content[0].get("type") == "text":
                    print(f"  Result: {content[0]['text']}")
            elif "error" in result:
                print(f"  Error: {result['error']}")
            print()

if __name__ == "__main__":
    print("Testing Calculator MCP Server...\n")
    asyncio.run(test_calculator())