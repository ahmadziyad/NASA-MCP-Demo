#!/usr/bin/env python3
"""
Interactive testing script for NASA MCP server
"""

import json
from nasa_mcp_server import get_apod_data, search_images_data

def print_separator():
    print("\n" + "=" * 60)

def test_image_search():
    """Interactive test for image search"""
    print_separator()
    print("🔍 NASA IMAGE SEARCH TEST")
    print_separator()
    
    while True:
        query = input("\nEnter search query (or 'quit' to exit): ").strip()
        if query.lower() in ['quit', 'exit', 'q']:
            break
            
        if not query:
            print("Please enter a search query.")
            continue
            
        try:
            size = input("Number of results (default 3): ").strip()
            size = int(size) if size else 3
            
            print(f"\n🔍 Searching for '{query}' (showing {size} results)...")
            result = search_images_data(query, size)
            
            if result:
                data = json.loads(result)
                if 'collection' in data and 'items' in data['collection']:
                    items = data['collection']['items']
                    print(f"\n✅ Found {len(items)} results:")
                    
                    for i, item in enumerate(items, 1):
                        if item.get('data') and len(item['data']) > 0:
                            item_data = item['data'][0]
                            title = item_data.get('title', 'No title')
                            description = item_data.get('description', 'No description')
                            date = item_data.get('date_created', 'No date')
                            
                            print(f"\n{i}. {title}")
                            print(f"   Date: {date}")
                            print(f"   Description: {description[:100]}{'...' if len(description) > 100 else ''}")
                            
                            # Show image links if available
                            if 'links' in item:
                                for link in item['links']:
                                    if link.get('rel') == 'preview':
                                        print(f"   Preview: {link.get('href', 'N/A')}")
                else:
                    print("❌ No results found")
            else:
                print("❌ Search failed")
                
        except ValueError:
            print("❌ Please enter a valid number for results")
        except Exception as e:
            print(f"❌ Error: {e}")

def test_apod():
    """Interactive test for APOD"""
    print_separator()
    print("🌟 NASA APOD (Astronomy Picture of the Day) TEST")
    print_separator()
    
    while True:
        date = input("\nEnter date (YYYY-MM-DD) or press Enter for today (or 'quit' to exit): ").strip()
        if date.lower() in ['quit', 'exit', 'q']:
            break
            
        try:
            print(f"\n🌟 Getting APOD for {date if date else 'today'}...")
            result = get_apod_data(date if date else None)
            
            if result:
                data = json.loads(result)
                if 'error' not in data:
                    print(f"\n✅ APOD Success!")
                    print(f"Title: {data.get('title', 'No title')}")
                    print(f"Date: {data.get('date', 'No date')}")
                    print(f"Media Type: {data.get('media_type', 'Unknown')}")
                    print(f"URL: {data.get('url', 'No URL')}")
                    
                    explanation = data.get('explanation', 'No explanation')
                    print(f"\nExplanation: {explanation[:200]}{'...' if len(explanation) > 200 else ''}")
                    
                    if data.get('copyright'):
                        print(f"Copyright: {data['copyright']}")
                else:
                    print(f"❌ APOD Error: {data['error']}")
            else:
                print("❌ APOD request failed")
                
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main interactive testing menu"""
    print("🚀 NASA MCP Server - Interactive Testing")
    print("=" * 50)
    print("This script lets you test the NASA MCP tools interactively")
    
    while True:
        print_separator()
        print("TESTING MENU")
        print("1. Test Image Search")
        print("2. Test APOD (Astronomy Picture of the Day)")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            test_image_search()
        elif choice == '2':
            test_apod()
        elif choice == '3':
            print("\n👋 Thanks for testing the NASA MCP server!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()