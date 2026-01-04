#!/usr/bin/env python3

from api.nasa import get_nasa_apod, search_nasa_images
import json

print("Testing NASA API...")

# Test APOD
print("\n1. Testing NASA APOD (Astronomy Picture of the Day):")
apod_result = get_nasa_apod()
if apod_result:
    print(f"✅ APOD Success! Title: {apod_result.get('title', 'No title')}")
    print(f"   Date: {apod_result.get('date', 'No date')}")
    print(f"   URL: {apod_result.get('url', 'No URL')}")
else:
    print("❌ APOD Failed")

# Test Image Search
print("\n2. Testing NASA Image Search:")
search_result = search_nasa_images("Mars rover", size=2)
if search_result and 'collection' in search_result:
    items = search_result['collection'].get('items', [])
    print(f"✅ Search Success! Found {len(items)} results")
    for i, item in enumerate(items[:2]):
        if item.get('data') and len(item['data']) > 0:
            title = item['data'][0].get('title', 'No title')
            print(f"   {i+1}. {title}")
else:
    print("❌ Search Failed")

print("\n✅ NASA API testing complete!")