# 🚀 NASA MCP Server - Build Your First MCP Server

> **Learn Model Context Protocol (MCP) by wrapping familiar NASA APIs**

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-1.9.4%2B-purple.svg)](https://modelcontextprotocol.io/)

A hands-on tutorial for building your first **Model Context Protocol (MCP)** server using NASA's public APIs. This project demonstrates how to convert REST APIs into MCP tools that AI assistants like Claude can use to access real-world data.

## 📋 Table of Contents

- [Overview](#overview)
- [What You'll Learn](#what-youll-learn)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Available MCP Tools](#available-mcp-tools)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Integration with Claude Desktop](#integration-with-claude-desktop)
- [Project Structure](#project-structure)
- [Adapting for Your Own APIs](#adapting-for-your-own-apis)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)
- [License](#license)

## 🌟 Overview

This repository serves as a **practical tutorial** for building MCP servers. We use NASA's public APIs as examples because they're:
- ✅ Well-documented and reliable
- ✅ Free to use (with API key)
- ✅ Interesting and educational
- ✅ Perfect for demonstrating real-world API integration

The techniques shown here can be applied to wrap **any REST API** as an MCP server, making it accessible to AI assistants.

## 🎓 What You'll Learn

- **MCP Server Architecture**: How to structure an MCP server project
- **API Integration**: Converting REST API calls into MCP tools
- **Authentication**: Handling API keys and environment variables
- **Error Management**: Proper error handling and response formatting
- **Testing Strategies**: Using MCP Inspector, Claude Desktop, and custom test scripts
- **Best Practices**: Documentation, prompt engineering, and tool design

## ✨ Features

- 🛠️ **Two Powerful MCP Tools**:
  - `get_nasa_apod` - Fetch NASA's Astronomy Picture of the Day
  - `search_images_data` - Search NASA's vast image and video library
  
- 🧪 **Comprehensive Testing Suite**:
  - Direct API tests
  - MCP tool tests
  - Interactive testing scripts
  - MCP Inspector integration
  
- 📚 **Extensive Documentation**:
  - Setup guides
  - Prompt examples
  - Tool usage documentation
  - Integration guides

## 📦 Prerequisites

Before you begin, ensure you have:

- **Python 3.12+** installed
- **uv** package manager ([installation guide](https://github.com/astral-sh/uv))
- **NASA API Key** (free - get yours at [api.nasa.gov](https://api.nasa.gov/))
- **Claude Desktop** (optional - for AI assistant integration)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nasa-mcp-demo.git
cd nasa-mcp-main
```

### 2. Install Dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```bash
NASA_API_KEY=your_api_key_here
```

> 💡 **Get your free NASA API key**: Visit [api.nasa.gov](https://api.nasa.gov/) and sign up instantly.

## ⚡ Quick Start

### Start the MCP Server

```bash
uv run python nasa_mcp_server.py
```

The server will start and listen for MCP client connections via stdio.

### Test the APIs Directly

```bash
# Test NASA APIs
uv run python test_nasa.py

# Test MCP tools
uv run python test_mcp.py

# Interactive testing
uv run python test_interactive.py
```

## 🛠️ Available MCP Tools

### 1. `get_nasa_apod`

Get NASA's Astronomy Picture of the Day with detailed explanations.

**Parameters:**
- `date` (optional): Date in YYYY-MM-DD format (1995-06-16 to today)

**Example:**
```python
{
  "date": "2024-01-01"  # Optional - defaults to today
}
```

**Returns:**
- Title of the astronomical image/video
- Detailed explanation
- High-resolution image URL
- Date and copyright information
- Media type (image/video)

### 2. `search_images_data`

Search NASA's extensive image and video library.

**Parameters:**
- `q` (required): Search query string
- `size` (optional): Number of results (default: 3, max recommended: 20)

**Example:**
```python
{
  "q": "Mars rover",
  "size": 5
}
```

**Returns:**
- Array of matching images/videos
- Titles and descriptions
- Image URLs and thumbnails
- Creation dates
- Keywords and metadata

## 💡 Usage Examples

### Example 1: Get Today's Astronomy Picture

```python
# Natural language prompt for AI assistant:
"What's today's astronomy picture from NASA?"

# MCP tool call:
get_nasa_apod()
```

### Example 2: Search for Mars Images

```python
# Natural language prompt:
"Find me 5 images of Mars rovers"

# MCP tool call:
search_images_data(q="Mars rover", size=5)
```

### Example 3: Historical APOD

```python
# Natural language prompt:
"Show me NASA's astronomy picture from Christmas 2023"

# MCP tool call:
get_nasa_apod(date="2023-12-25")
```

For more examples, see [PROMPT_EXAMPLES.json](PROMPT_EXAMPLES.json) and [TOOL_PROMPTS.md](TOOL_PROMPTS.md).

## 🧪 Testing

### Using MCP Inspector

The MCP Inspector is a powerful tool for testing MCP servers:

```bash
npx @modelcontextprotocol/inspector uv run python nasa_mcp_server.py
```

See [MCP_INSPECTOR_PROMPT_TESTING.md](MCP_INSPECTOR_PROMPT_TESTING.md) for detailed testing workflows.

### Running Test Scripts

```bash
# Test NASA APIs directly
uv run python test_nasa.py

# Test MCP tool functionality
uv run python test_mcp.py

# Interactive testing session
uv run python test_interactive.py

# Simulate inspector tests
uv run python simulate_inspector_tests.py
```

## 🤖 Integration with Claude Desktop

### Configuration

Add this to your Claude Desktop MCP settings file:

**macOS/Linux**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "nasa-mcp": {
      "command": "uv",
      "args": ["run", "python", "nasa_mcp_server.py"],
      "cwd": "/absolute/path/to/nasa-mcp-main"
    }
  }
}
```

### Using with Claude

Once configured, you can ask Claude:

- "Show me today's astronomy picture from NASA"
- "Find images of the International Space Station"
- "Get NASA's featured image from New Year's Day 2024"
- "Search for pictures of Jupiter's moons"

See [CLAUDE_INTEGRATION.md](CLAUDE_INTEGRATION.md) for detailed integration instructions.

## 📁 Project Structure

```
nasa-mcp-main/
├── api/
│   └── nasa.py                          # NASA API client functions
├── nasa_mcp_server.py                   # Main MCP server implementation
├── pyproject.toml                       # Project dependencies
├── .env                                 # Environment variables (API keys)
├── test_nasa.py                         # Direct API tests
├── test_mcp.py                          # MCP tool tests
├── test_interactive.py                  # Interactive testing
├── simulate_inspector_tests.py          # Inspector simulation
├── PROMPT_EXAMPLES.json                 # Example prompts and queries
├── TOOL_PROMPTS.md                      # Prompt engineering guide
├── SETUP_COMPLETE.md                    # Setup verification guide
├── TESTING_GUIDE.md                     # Testing documentation
├── MCP_INSPECTOR_PROMPT_TESTING.md      # Inspector testing guide
├── CLAUDE_INTEGRATION.md                # Claude Desktop integration
├── QUICK_REFERENCE.md                   # Quick reference guide
└── README.md                            # This file
```

## 🔧 Adapting for Your Own APIs

This project is designed as a **template** for building MCP servers with any API. Here's how to adapt it:

### Step 1: Replace the API Client

Update `api/nasa.py` → `api/your_api.py`:

```python
import requests

def your_api_function(param1, param2):
    """Your API function documentation"""
    response = requests.get(
        "https://your-api.com/endpoint",
        params={"key": param1, "value": param2}
    )
    return response.json()
```

### Step 2: Update MCP Tools

Modify `nasa_mcp_server.py`:

```python
from mcp.server.fastmcp import FastMCP
from api.your_api import your_api_function

mcp = FastMCP()

@mcp.tool("your_tool_name")
def your_mcp_tool(param1: str, param2: int = 10):
    """Tool description for AI assistant"""
    result = your_api_function(param1, param2)
    return json.dumps(result, indent=4)
```

### Step 3: Update Environment Variables

Change `.env` to include your API credentials:

```bash
YOUR_API_KEY=your_key_here
YOUR_API_SECRET=your_secret_here
```

### Step 4: Update Documentation

- Update tool descriptions in the code
- Create prompt examples for your API
- Document parameters and return values
- Add usage examples

## 📚 Documentation

- **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** - Verify your setup is working
- **[TOOL_PROMPTS.md](TOOL_PROMPTS.md)** - Effective prompts for querying tools
- **[PROMPT_EXAMPLES.json](PROMPT_EXAMPLES.json)** - JSON examples of all prompt types
- **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - Comprehensive testing strategies
- **[MCP_INSPECTOR_PROMPT_TESTING.md](MCP_INSPECTOR_PROMPT_TESTING.md)** - Inspector usage
- **[CLAUDE_INTEGRATION.md](CLAUDE_INTEGRATION.md)** - Claude Desktop setup
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick command reference

## 🐛 Troubleshooting

### Server Won't Start

**Issue**: `ModuleNotFoundError` or import errors

**Solution**:
```bash
# Reinstall dependencies
uv sync --force

# Or with pip
pip install -r requirements.txt --force-reinstall
```

### API Key Errors

**Issue**: `401 Unauthorized` or API key errors

**Solution**:
- Verify `.env` file exists and contains `NASA_API_KEY=your_key`
- Check your API key at [api.nasa.gov](https://api.nasa.gov/)
- Ensure no extra spaces or quotes around the key

### No Results from Search

**Issue**: Search returns empty results

**Solution**:
- Use broader search terms (e.g., "Mars" instead of "Mars Perseverance rover soil analysis")
- Check spelling of astronomical terms
- Try mission names (Apollo, Voyager, Cassini)
- Use different synonyms (spacecraft vs satellite)

### Claude Desktop Not Detecting Server

**Issue**: MCP server not appearing in Claude

**Solution**:
- Verify the absolute path in `claude_desktop_config.json`
- Restart Claude Desktop completely
- Check server logs for errors
- Ensure `uv` is in your system PATH

For more troubleshooting tips, see the [TESTING_GUIDE.md](TESTING_GUIDE.md).

## 📖 Resources

### MCP Resources
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/modelcontextprotocol/fastmcp)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

### NASA API Resources
- [NASA Open APIs](https://api.nasa.gov/)
- [APOD API Documentation](https://github.com/nasa/apod-api)
- [NASA Image and Video Library](https://images.nasa.gov/)

## 🎯 Next Steps

After completing this tutorial, you can:

1. **Extend this server** - Add more NASA APIs (Mars Rover Photos, Earth Observatory, etc.)
2. **Build your own MCP server** - Use this as a template for your favorite APIs
3. **Integrate with AI apps** - Connect to Claude Desktop, custom chatbots, or AI agents
4. **Contribute** - Share your improvements or create tutorials for other APIs

## 📄 License

MIT License - Feel free to use this as a template for your own MCP servers!

**Remember**: The goal isn't to build the perfect NASA server—it's to learn the patterns that work for any API. Start here, then build something amazing with your favorite APIs! 🚀

---

**Made with ❤️ for the MCP community**

*Questions or feedback? Open an issue or contribute to make this tutorial better!*
