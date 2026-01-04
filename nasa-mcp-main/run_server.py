#!/usr/bin/env python3

"""
Simple script to run the NASA MCP server
"""

from nasa_mcp_server import main

if __name__ == "__main__":
    print("🚀 Starting NASA MCP Server...")
    print("📡 Server will listen for MCP client connections")
    print("🔧 Available tools:")
    print("   - get_nasa_apod: Get NASA's Astronomy Picture of the Day")
    print("   - search_images_data: Search NASA's image library")
    print("\n⚡ Server starting...")
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")