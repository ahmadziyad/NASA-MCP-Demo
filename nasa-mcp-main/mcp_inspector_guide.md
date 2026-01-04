# 🔍 MCP Inspector v0.18.0 - Complete Testing Guide

## What is MCP Inspector?

MCP Inspector is the official testing tool for MCP (Model Context Protocol) servers. It provides a web-based interface to:
- Connect to your MCP server
- View available tools and their schemas
- Test tool calls with custom parameters
- See raw MCP protocol messages
- Debug server responses

## Step-by-Step Testing Process

### 1. Start MCP Inspector
Open a terminal in the `nasa-mcp-main` directory and run:

```bash
npx @modelcontextprotocol/inspector uv run python nasa_mcp_server.py
```

**What happens:**
- Downloads MCP Inspector v0.18.0 (if not cached)
- Starts your NASA MCP server as a subprocess
- Launches a web interface (usually at http://localhost:5173)
- Automatically opens your browser

### 2. Inspector Interface Overview

When the web interface opens, you'll see:

**Left Panel - Server Info:**
- Connection status
- Server capabilities
- Available tools list

**Main Panel - Testing Area:**
- Tool selection dropdown
- Parameter input (JSON format)
- Execute button
- Response display

**Bottom Panel - Protocol Messages:**
- Raw MCP messages
- Request/response logs
- Debug information

### 3. Test Cases to Try

#### Test Case 1: NASA Image Search
**Tool:** `search_images_data`
**Parameters:**
```json
{
  "q": "Mars rover",
  "size": 3
}
```

**Expected Result:**
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
        ],
        "links": [
          {
            "href": "https://images-assets.nasa.gov/image/...",
            "rel": "preview"
          }
        ]
      }
    ]
  }
}
```

#### Test Case 2: International Space Station
**Tool:** `search_images_data`
**Parameters:**
```json
{
  "q": "International Space Station",
  "size": 2
}
```

#### Test Case 3: NASA APOD (may timeout)
**Tool:** `get_nasa_apod`
**Parameters:**
```json
{
  "date": "2024-01-01"
}
```

#### Test Case 4: Today's APOD
**Tool:** `get_nasa_apod`
**Parameters:**
```json
{}
```

### 4. What to Look For

#### ✅ Success Indicators:
- **Connection Status**: Green "Connected" indicator
- **Tool Discovery**: Both tools listed (`get_nasa_apod`, `search_images_data`)
- **Response Format**: Valid JSON responses
- **Image Results**: Array of NASA images with titles, descriptions, URLs
- **Protocol Messages**: Clean request/response cycle in debug panel

#### ⚠️ Expected Issues:
- **APOD Timeouts**: NASA's APOD API can be slow (this is normal)
- **Slow Responses**: NASA servers can be sluggish
- **Empty Results**: Some search terms might not return images

#### ❌ Actual Problems:
- **Connection Failed**: Server won't start
- **Tools Not Listed**: MCP registration issues
- **JSON Parse Errors**: Malformed responses
- **Consistent Failures**: All requests fail

### 5. Advanced Testing

#### Custom Search Queries:
Try these search terms to test different scenarios:
- `"Apollo 11"` - Historic mission
- `"nebula"` - Space phenomena
- `"Hubble telescope"` - Space telescope images
- `"Earth from space"` - Earth photography
- `"astronaut"` - Human spaceflight

#### Parameter Variations:
- Different `size` values (1, 5, 10, 20)
- Various date formats for APOD
- Edge cases (empty strings, very large sizes)

### 6. Interpreting Results

#### Successful Image Search Response:
```json
{
  "collection": {
    "version": "1.1",
    "href": "http://images-api.nasa.gov/search?q=...",
    "items": [
      {
        "data": [
          {
            "nasa_id": "PIA12345",
            "title": "Image Title",
            "description": "Detailed description...",
            "date_created": "2020-01-01T00:00:00Z",
            "media_type": "image",
            "center": "JPL"
          }
        ],
        "links": [
          {
            "href": "https://images-assets.nasa.gov/image/...",
            "rel": "preview",
            "render": "image"
          }
        ]
      }
    ]
  }
}
```

#### Successful APOD Response:
```json
{
  "title": "A Galaxy Far Far Away",
  "date": "2024-01-01",
  "explanation": "Long description of the astronomical phenomenon...",
  "url": "https://apod.nasa.gov/apod/image/2401/galaxy.jpg",
  "media_type": "image",
  "service_version": "v1"
}
```

### 7. Troubleshooting

#### If Inspector Won't Start:
```bash
# Check if npx is working
npx --version

# Try installing explicitly
npm install -g @modelcontextprotocol/inspector

# Run with explicit path
npx @modelcontextprotocol/inspector@0.18.0 uv run python nasa_mcp_server.py
```

#### If Server Won't Connect:
```bash
# Test server independently
uv run python nasa_mcp_server.py

# Check dependencies
uv sync
```

#### If No Tools Appear:
- Check the MCP server logs in the Inspector
- Verify tool registration in `nasa_mcp_server.py`
- Look for Python errors in the debug panel

### 8. Expected Test Results

**✅ What Should Work:**
- Inspector connects to server
- Both tools appear in the tool list
- Image search returns 1-3 results for most queries
- JSON responses are properly formatted
- Protocol messages show clean communication

**⚠️ What Might Have Issues:**
- APOD requests may timeout (NASA server issue)
- Some search queries might return no results
- Responses might be slow during peak usage

**🎯 Success Criteria:**
If you can successfully search for "Mars rover" and get back NASA images with titles and descriptions, your MCP server is working perfectly!

## Next Steps After Testing

Once MCP Inspector confirms everything works:
1. **Integrate with Claude Desktop** - Add server to MCP config
2. **Build Custom Clients** - Use the MCP protocol patterns you see
3. **Extend the Server** - Add more NASA APIs or other data sources
4. **Deploy for Production** - Your server is ready for real use

The MCP Inspector is your gateway to understanding how MCP clients will interact with your server!