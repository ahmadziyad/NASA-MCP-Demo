# 🧪 NASA MCP Server - Testing Guide

## Testing Options

### 1. 🎮 Interactive Testing (Recommended for Beginners)
**Best for**: Manual testing and exploring the APIs

```bash
uv run python test_interactive.py
```

This provides a user-friendly menu to:
- Search NASA images with custom queries
- Get APOD for specific dates or today
- See formatted results with descriptions

### 2. 🔍 MCP Inspector (Recommended for MCP Development)
**Best for**: Testing the actual MCP protocol and debugging

**Prerequisites**: Node.js and npm installed

```bash
npx @modelcontextprotocol/inspector uv run python nasa_mcp_server.py
```

This will:
- Open a web interface in your browser
- Connect to your MCP server
- Let you test tools with JSON parameters
- Show raw MCP protocol messages

### 3. 🤖 MCP Client Testing (Advanced)
**Best for**: Testing as if you were an MCP client application

```bash
uv run python test_mcp_client.py
```

This simulates how Claude Desktop or other MCP clients would interact with your server.

### 4. 🔧 Direct API Testing
**Best for**: Testing the underlying NASA APIs

```bash
uv run python test_nasa.py
```

Tests the NASA APIs directly without MCP protocol.

## 📋 Test Cases to Try

### Image Search Tests
- `"Mars rover"` - Should find Mars exploration images
- `"International Space Station"` - ISS photos
- `"nebula"` - Space nebula images
- `"Apollo 11"` - Historic moon landing
- `"Hubble telescope"` - Hubble space telescope images

### APOD Tests
- No date (today's APOD)
- `"2024-01-01"` - New Year's Day 2024
- `"1995-06-16"` - First ever APOD
- `"2023-12-25"` - Christmas 2023

## 🚨 Troubleshooting

### Common Issues

**"Request timeout"**: 
- NASA APIs can be slow sometimes
- Try again or use a different date

**"No results found"**:
- Try different search terms
- Some queries might not have images

**"MCP connection failed"**:
- Make sure no other instance is running
- Check that all dependencies are installed

### Checking Server Status
```bash
# See if server process is running
uv run python -c "print('Server can start')"

# Test NASA API directly
uv run python -c "from api.nasa import search_nasa_images; print('API works' if search_nasa_images('test', 1) else 'API failed')"
```

## 🎯 Expected Results

### Successful Image Search
```json
{
  "collection": {
    "items": [
      {
        "data": [
          {
            "title": "Mars Rover Studies Soil on Mars",
            "description": "...",
            "date_created": "2004-01-15T00:00:00Z"
          }
        ]
      }
    ]
  }
}
```

### Successful APOD
```json
{
  "title": "A Galaxy Far Far Away",
  "date": "2024-01-01",
  "explanation": "...",
  "url": "https://apod.nasa.gov/apod/image/...",
  "media_type": "image"
}
```

## 🔗 Integration Testing

### With Claude Desktop
1. Add server config to Claude Desktop MCP settings
2. Restart Claude Desktop
3. Ask Claude: "Search for Mars rover images using NASA"
4. Ask Claude: "Get today's astronomy picture from NASA"

### With Other MCP Clients
Use the MCP Inspector to understand the exact protocol messages, then implement in your client.

---

**Ready to test?** Start with the interactive testing for the best experience!