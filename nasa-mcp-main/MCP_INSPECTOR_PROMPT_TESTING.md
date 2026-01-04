# 🔍 Testing Prompts with MCP Inspector - Step-by-Step Guide

## 🚀 Current MCP Inspector Status

**Inspector URL:** http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=0b691a22646534905b91af0884e6b2807e6b59279f5c3d21dd3a8eec862268b2

**Status:** ✅ Running and connected to NASA MCP Server

---

## 📋 How to Test Prompts in MCP Inspector

### **Step 1: Access the Inspector Interface**

1. **Open your browser** to the Inspector URL above
2. **Verify connection** - You should see:
   - 🟢 Green "Connected" status
   - **2 tools** listed in the left sidebar:
     - `get_nasa_apod`
     - `search_images_data`

### **Step 2: Understanding the Interface**

**Left Sidebar:**
- **Tools list** with descriptions
- **Tool schemas** showing required parameters

**Main Panel:**
- **Tool selector** dropdown
- **Parameters input** (JSON format)
- **"Call Tool"** button
- **Response display** area

**Bottom Panel:**
- **Protocol messages** log
- **Request/response** details
- **Debug information**

---

## 🧪 Prompt Testing Scenarios

### **Test Scenario 1: Basic Image Search** ✅ (Guaranteed Success)

**Step-by-Step:**
1. **Select Tool:** `search_images_data` from dropdown
2. **Enter Parameters:**
   ```json
   {
     "q": "Mars rover",
     "size": 3
   }
   ```
3. **Click:** "Call Tool"
4. **Wait:** 1-3 seconds for response

**Expected Success Response:**
```json
{
  "collection": {
    "version": "1.1",
    "href": "http://images-api.nasa.gov/search?q=Mars+rover&media_type=image&page=1&page_size=3",
    "items": [
      {
        "data": [
          {
            "nasa_id": "PIA04413",
            "title": "Mars Rover Studies Soil on Mars",
            "description": "NASA's Mars Exploration Rover Spirit took this image...",
            "date_created": "2004-01-15T00:00:00Z",
            "media_type": "image",
            "center": "JPL"
          }
        ],
        "links": [
          {
            "href": "https://images-assets.nasa.gov/image/PIA04413/PIA04413~thumb.jpg",
            "rel": "preview",
            "render": "image"
          }
        ]
      }
    ]
  }
}
```

**What Success Looks Like:**
- ✅ Response appears quickly (1-3 seconds)
- ✅ JSON is properly formatted
- ✅ Contains 2-3 Mars rover images
- ✅ Each item has title, description, date, preview link
- ✅ Status shows successful completion

---

### **Test Scenario 2: International Space Station** ✅ (Reliable)

**Parameters:**
```json
{
  "q": "International Space Station",
  "size": 2
}
```

**Expected Results:**
- ISS photos from different angles
- Space station modules and configurations
- Astronaut activities on ISS

---

### **Test Scenario 3: Nebula Search** ✅ (Beautiful Results)

**Parameters:**
```json
{
  "q": "nebula",
  "size": 4
}
```

**Expected Results:**
- Colorful nebula images (Orion, Eagle, Crab nebulae)
- Deep space astronomical phenomena
- Hubble telescope observations

---

### **Test Scenario 4: Apollo 11 Historical** ✅ (Educational)

**Parameters:**
```json
{
  "q": "Apollo 11",
  "size": 3
}
```

**Expected Results:**
- Moon landing images
- Astronauts on lunar surface
- Lunar module and equipment

---

### **Test Scenario 5: NASA APOD** ⚠️ (May Timeout)

**Tool:** `get_nasa_apod`
**Parameters:**
```json
{
  "date": "2024-01-01"
}
```

**Possible Outcomes:**
- ✅ **Success:** APOD data with title, explanation, image URL
- ⚠️ **Timeout:** "Failed to retrieve APOD data" 
- ⏳ **Slow:** May take 10+ seconds

**If Successful, Response Looks Like:**
```json
{
  "title": "Quadrantids of the North",
  "date": "2024-01-01",
  "explanation": "Named for a constellation that's no longer recognized...",
  "url": "https://apod.nasa.gov/apod/image/2401/Quadrantids2024_Dandan_1080.jpg",
  "media_type": "image",
  "service_version": "v1"
}
```

---

### **Test Scenario 6: Today's APOD** ⚠️ (Current)

**Parameters:**
```json
{}
```

**Note:** Empty parameters get today's APOD

---

## 🎯 Advanced Testing Techniques

### **Parameter Variations**

**Size Testing:**
```json
{"q": "Mars rover", "size": 1}    // Minimal
{"q": "Mars rover", "size": 5}    // Good selection
{"q": "Mars rover", "size": 10}   // Comprehensive
{"q": "Mars rover", "size": 20}   // Maximum (may be slow)
```

**Query Refinement:**
```json
{"q": "Mars", "size": 3}                    // Broad
{"q": "Mars rover", "size": 3}              // Specific
{"q": "Mars Perseverance rover", "size": 3} // Very specific
{"q": "Mars rover Curiosity", "size": 3}    // Mission-specific
```

### **Edge Case Testing**

**Empty/Invalid Queries:**
```json
{"q": "", "size": 1}              // Empty query
{"q": "nonexistentterm", "size": 1} // No results expected
{"q": "Mars rover", "size": 0}     // Invalid size
```

**Date Edge Cases:**
```json
{"date": "1995-06-16"}  // First APOD ever
{"date": "1995-06-15"}  // Before APOD existed (should fail)
{"date": "2030-01-01"}  // Future date (should fail)
{"date": "invalid"}     // Invalid format (should fail)
```

---

## 📊 Interpreting Test Results

### **✅ Success Indicators**

**For Image Search:**
- Response time: 1-5 seconds
- JSON structure: Well-formed with `collection.items` array
- Content: Images with titles, descriptions, dates
- Links: Preview URLs for images
- Status: Green success indicator in Inspector

**For APOD:**
- Response time: 5-15 seconds (if successful)
- JSON structure: Contains `title`, `date`, `explanation`, `url`
- Content: Astronomical image or video with detailed explanation
- Media type: Usually "image" or "video"

### **⚠️ Expected Issues**

**APOD Timeouts:**
- Message: "Failed to retrieve APOD data"
- Cause: NASA's APOD API is often slow/overloaded
- Solution: Try historical dates (1995-2010)

**No Search Results:**
- Empty `items` array in response
- Cause: Search term has no matching images
- Solution: Try broader or different terms

**Slow Responses:**
- Taking 10+ seconds
- Cause: NASA servers under load
- Solution: Reduce `size` parameter, try different times

### **❌ Actual Problems**

**Connection Issues:**
- Inspector shows "Disconnected"
- No response to tool calls
- Python errors in debug panel

**Malformed Responses:**
- Invalid JSON structure
- Missing required fields
- Server errors in response

---

## 🔍 Using Inspector Debug Features

### **Protocol Messages Panel**

**What to Look For:**
- **initialize** request/response (connection setup)
- **tools/list** request (tool discovery)
- **tools/call** requests with your parameters
- **Response messages** with JSON content

**Example Protocol Flow:**
```
→ tools/call: search_images_data {"q": "Mars rover", "size": 3}
← Response: {"content": [{"type": "text", "text": "{\"collection\": ...}"}]}
```

### **Error Debugging**

**Common Error Messages:**
- `"Request timeout after 10 seconds"` - NASA API slow
- `"Connection error"` - Network issues
- `"JSON decode error"` - Malformed response
- `"HTTP error 429"` - Rate limiting

---

## 🎯 Systematic Testing Checklist

### **Basic Functionality Test:**
- [ ] Inspector connects successfully
- [ ] Both tools appear in sidebar
- [ ] Mars rover search returns results
- [ ] JSON responses are well-formatted
- [ ] Protocol messages show clean communication

### **Comprehensive Testing:**
- [ ] Multiple search terms work
- [ ] Different size parameters work
- [ ] Historical APOD dates work
- [ ] Edge cases handled gracefully
- [ ] Error messages are informative

### **Performance Testing:**
- [ ] Image search responds in 1-5 seconds
- [ ] Large requests (size: 20) complete
- [ ] Multiple rapid requests work
- [ ] Server handles timeouts gracefully

---

## 🚀 Next Steps After Testing

**If All Tests Pass:**
- ✅ Your MCP server is production-ready
- ✅ Ready for Claude Desktop integration
- ✅ Can be used by custom MCP clients
- ✅ Suitable for educational and research applications

**If Issues Found:**
- Check NASA API key configuration
- Verify internet connectivity
- Review server logs for errors
- Test individual API endpoints directly

---

This systematic approach ensures your NASA MCP server works correctly and handles various query patterns effectively through the MCP Inspector interface.