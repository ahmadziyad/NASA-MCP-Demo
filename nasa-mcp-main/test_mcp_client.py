#!/usr/bin/env python3
"""
MCP Client Test Script - Tests the NASA MCP server by acting as an MCP client
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the NASA MCP server using MCP protocol"""
    
    print("🧪 Testing NASA MCP Server as MCP Client...")
    
    # Server parameters - runs the server as subprocess
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "nasa_mcp_server.py"],
        env=None
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                print("✅ Connected to MCP server!")
                
                # Initialize the session
                await session.initialize()
                print("✅ Session initialized!")
                
                # List available tools
                print("\n📋 Available tools:")
                tools = await session.list_tools()
                for tool in tools.tools:
                    print(f"   - {tool.name}: {tool.description}")
                
                # Test 1: Search NASA images
                print("\n🔍 Test 1: Searching for Mars rover images...")
                try:
                    result = await session.call_tool("search_images_data", {
                        "q": "Mars rover",
                        "size": 2
                    })
                    
                    if result.content:
                        data = json.loads(result.content[0].text)
                        items = data.get('collection', {}).get('items', [])
                        print(f"✅ Found {len(items)} Mars rover images!")
                        
                        for i, item in enumerate(items[:2]):
                            if item.get('data') and len(item['data']) > 0:
                                title = item['data'][0].get('title', 'No title')
                                print(f"   {i+1}. {title}")
                    else:
                        print("❌ No content returned")
                        
                except Exception as e:
                    print(f"❌ Error in image search: {e}")
                
                # Test 2: Get NASA APOD for a specific date
                print("\n🌟 Test 2: Getting NASA APOD for January 1, 2024...")
                try:
                    result = await session.call_tool("get_nasa_apod", {
                        "date": "2024-01-01"
                    })
                    
                    if result.content:
                        data = json.loads(result.content[0].text)
                        if 'error' not in data:
                            print(f"✅ APOD Success!")
                            print(f"   Title: {data.get('title', 'No title')}")
                            print(f"   Date: {data.get('date', 'No date')}")
                            print(f"   Media Type: {data.get('media_type', 'Unknown')}")
                        else:
                            print(f"❌ APOD Error: {data['error']}")
                    else:
                        print("❌ No content returned")
                        
                except Exception as e:
                    print(f"❌ Error in APOD request: {e}")
                
                # Test 3: Get today's APOD (no date parameter)
                print("\n🌟 Test 3: Getting today's NASA APOD...")
                try:
                    result = await session.call_tool("get_nasa_apod", {})
                    
                    if result.content:
                        data = json.loads(result.content[0].text)
                        if 'error' not in data:
                            print(f"✅ Today's APOD Success!")
                            print(f"   Title: {data.get('title', 'No title')}")
                            print(f"   Date: {data.get('date', 'No date')}")
                        else:
                            print(f"❌ Today's APOD Error: {data['error']}")
                    else:
                        print("❌ No content returned")
                        
                except Exception as e:
                    print(f"❌ Error in today's APOD: {e}")
                
                print("\n✅ MCP Client testing complete!")
                
    except Exception as e:
        print(f"❌ Failed to connect to MCP server: {e}")
        print("💡 Make sure the server dependencies are installed and the server can start")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())