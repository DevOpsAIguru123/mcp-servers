#!/usr/bin/env python3
"""
Test script for remote MCP server using FastMCP client
"""

import asyncio
import json
from fastmcp import Client

async def test_remote_mcp():
    """Test the remote MCP server"""
    print("🧪 Testing Remote MCP Server at http://localhost:8000/mcp")
    print("=" * 60)
    
    try:
        # Connect to the remote MCP server
        async with Client("http://localhost:8000/mcp") as client:
            print("✅ Connected to remote MCP server!")
            
            # Test ping
            print("\n📡 Testing ping...")
            try:
                await client.ping()
                print("✅ Ping successful!")
            except Exception as e:
                print(f"❌ Ping failed: {e}")
            
            # List tools
            print("\n🔧 Listing available tools...")
            try:
                tools = await client.list_tools()
                print(f"✅ Found {len(tools)} tools:")
                for tool in tools:
                    print(f"  - {tool.name}: {tool.description}")
            except Exception as e:
                print(f"❌ Failed to list tools: {e}")
            
            # Test calculator tools
            print("\n🧮 Testing calculator tools...")
            test_cases = [
                ("add", {"a": 10, "b": 5}, "10 + 5"),
                ("subtract", {"a": 20, "b": 8}, "20 - 8"),
                ("multiply", {"a": 4, "b": 7}, "4 * 7"),
                ("divide", {"a": 100, "b": 4}, "100 / 4"),
            ]
            
            for tool_name, args, description in test_cases:
                try:
                    print(f"\n  Testing {description}...")
                    result = await client.call_tool(tool_name, args)
                    print(f"    ✅ Result: {result.data}")
                except Exception as e:
                    print(f"    ❌ Failed: {e}")
            
            # Test error case
            print("\n🚫 Testing error handling (divide by zero)...")
            try:
                result = await client.call_tool("divide", {"a": 10, "b": 0})
                print(f"    Result: {result.data}")
            except Exception as e:
                print(f"    ✅ Expected error caught: {e}")
                
    except Exception as e:
        print(f"❌ Failed to connect to remote MCP server: {e}")
        print("\n💡 Make sure the Docker container is running:")
        print("   docker run -d --name calculator-mcp-test -p 8000:8000 calculator-mcp-server")

if __name__ == "__main__":
    asyncio.run(test_remote_mcp()) 