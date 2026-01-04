#!/usr/bin/env python3

import asyncio
import json
from nasa_mcp_server import mcp

async def test_mcp_tools():
    """Test the MCP tools directly"""
    print("Testing MCP Server Tools...")
    
    # Test search_images_data tool
    print("\n1. Testing search_images_data tool:")
    try:
        result = mcp.get_tool("search_images_data")
        if result:
            # Call the tool function directly
            from nasa_mcp_server import search_images_data
            search_result = search_images_data("Mars rover", 2)
            print(f"✅ Search tool works! Result type: {type(search_result)}")
            if isinstance(search_result, str):
                data = json.loads(search_result)
                if 'collection' in data and 'items' in data['collection']:
                    print(f"   Found {len(data['collection']['items'])} items")
        else:
            print("❌ Tool not found")
    except Exception as e:
        print(f"❌ Error testing search tool: {e}")
    
    # Test get_apod_data tool  
    print("\n2. Testing get_apod_data tool:")
    try:
        result = mcp.get_tool("get_nasa_apod")
        if result:
            from nasa_mcp_server import get_apod_data
            apod_result = get_apod_data("2024-01-01")  # Use a specific date
            print(f"✅ APOD tool works! Result type: {type(apod_result)}")
        else:
            print("❌ Tool not found")
    except Exception as e:
        print(f"❌ Error testing APOD tool: {e}")
    
    print("\n✅ MCP tool testing complete!")

if __name__ == "__main__":
    asyncio.run(test_mcp_tools())