#!/usr/bin/env python3
"""
Instructions for testing with MCP Inspector
"""

import subprocess
import sys
import os

def check_npx():
    """Check if npx is available"""
    try:
        result = subprocess.run(['npx', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def main():
    print("🔍 NASA MCP Server - MCP Inspector Testing Guide")
    print("=" * 50)
    
    print("\n📋 Prerequisites:")
    print("1. Node.js and npm/npx installed")
    print("2. NASA MCP server configured (✅ Done)")
    
    # Check if npx is available
    if check_npx():
        print("✅ npx is available")
    else:
        print("❌ npx not found - you'll need to install Node.js first")
        print("   Download from: https://nodejs.org/")
        return
    
    print("\n🚀 How to test with MCP Inspector:")
    print("\n1. Open a new terminal/command prompt")
    print("2. Navigate to the nasa-mcp-main directory:")
    print("   cd nasa-mcp-main")
    
    print("\n3. Run MCP Inspector with this command:")
    print("   npx @modelcontextprotocol/inspector uv run python nasa_mcp_server.py")
    
    print("\n4. This will:")
    print("   - Start the MCP Inspector web interface")
    print("   - Connect to your NASA MCP server")
    print("   - Open a browser window with the testing interface")
    
    print("\n🧪 In the MCP Inspector, you can:")
    print("   - See available tools (get_nasa_apod, search_images_data)")
    print("   - Test tool calls with different parameters")
    print("   - View JSON responses")
    print("   - Debug any issues")
    
    print("\n💡 Example test cases to try:")
    print("   Tool: search_images_data")
    print("   Parameters: {\"q\": \"Mars rover\", \"size\": 3}")
    print()
    print("   Tool: get_nasa_apod") 
    print("   Parameters: {\"date\": \"2024-01-01\"}")
    print()
    print("   Tool: get_nasa_apod")
    print("   Parameters: {} (for today's APOD)")
    
    print("\n" + "=" * 50)
    print("Ready to test! Run the npx command above in a new terminal.")

if __name__ == "__main__":
    main()