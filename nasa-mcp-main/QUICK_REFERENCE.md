# 🚀 NASA MCP Tools - Quick Reference Guide

## 🔧 Tool Summary

| Tool | Purpose | Parameters | Response Time |
|------|---------|------------|---------------|
| `search_images_data` | Search NASA's image library | `q` (query), `size` (1-20) | Fast (1-3 sec) |
| `get_nasa_apod` | Get Astronomy Picture of the Day | `date` (optional YYYY-MM-DD) | Slow (may timeout) |

---

## ⚡ Quick Prompts

### **Instant Success Prompts** ✅
```
"Find Mars rover images" → {"q": "Mars rover", "size": 3}
"Show me ISS photos" → {"q": "International Space Station", "size": 3}
"Search for nebula pictures" → {"q": "nebula", "size": 5}
"Find Apollo 11 images" → {"q": "Apollo 11", "size": 4}
"Show me Hubble telescope photos" → {"q": "Hubble Space Telescope", "size": 3}
```

### **APOD Prompts** ⚠️ (May timeout)
```
"Today's astronomy picture" → {}
"APOD for 2024-01-01" → {"date": "2024-01-01"}
"First ever APOD" → {"date": "1995-06-16"}
```

---

## 🎯 Best Search Terms

### **Space Missions** (Reliable)
- `Mars rover` - Current and historical rovers
- `Apollo 11` - Moon landing images
- `International Space Station` - ISS photos
- `Space Shuttle` - Shuttle program images
- `Voyager` - Deep space mission photos

### **Celestial Objects** (Beautiful results)
- `nebula` - Colorful space clouds
- `galaxy` - Spiral and elliptical galaxies  
- `Saturn rings` - Detailed ring system images
- `Jupiter` - Gas giant and moons
- `Earth from space` - Blue marble views

### **Space Technology** (Educational)
- `Hubble Space Telescope` - Telescope and discoveries
- `James Webb Space Telescope` - Latest space observatory
- `astronaut spacewalk` - EVA activities
- `rocket launch` - Launch sequences

---

## 📊 Parameter Guidelines

### **Size Parameter Recommendations**
- **Quick preview:** `size: 2-3`
- **Good selection:** `size: 4-6` 
- **Comprehensive:** `size: 8-10`
- **Maximum:** `size: 20` (may be slow)

### **Date Parameter Tips**
- **Reliable dates:** 1995-2020 (older APODs load faster)
- **Special dates:** 1995-06-16 (first APOD), 2000-01-01 (Y2K)
- **Recent dates:** May timeout due to NASA server load
- **Format:** Always use YYYY-MM-DD

---

## 🚨 Common Issues & Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| No search results | Try broader terms: "Mars" not "Mars Perseverance rover analysis" |
| APOD timeout | Normal! Try historical dates (1995-2010) |
| Too many irrelevant results | Add specific mission names or use quotes |
| Slow responses | Reduce size parameter, use specific terms |

---

## 🎨 Prompt Templates

### **Basic Search**
```
"Search NASA images for [TOPIC] and show me [NUMBER] results"
Example: "Search NASA images for Saturn and show me 5 results"
```

### **Educational Query**
```
"Find NASA images that explain [CONCEPT] with descriptions"
Example: "Find NASA images that explain solar eclipses with descriptions"
```

### **Historical Research**
```
"Show me NASA images from [TIME PERIOD/MISSION] with context"
Example: "Show me NASA images from the Apollo program with context"
```

### **Comparative Analysis**
```
"Find NASA images of [OBJECT1] and [OBJECT2] for comparison"
Example: "Find NASA images of Mars and Earth for comparison"
```

---

## 🏆 Guaranteed Working Examples

Copy these exact prompts for immediate success:

### **Image Search** (100% reliable)
```json
{"q": "Mars rover", "size": 3}
{"q": "International Space Station", "size": 2}
{"q": "nebula", "size": 4}
{"q": "Apollo 11", "size": 3}
{"q": "Hubble Space Telescope", "size": 3}
```

### **APOD** (Historical dates work best)
```json
{"date": "2000-01-01"}
{"date": "1995-06-16"}
{"date": "2010-12-25"}
{"date": "2015-07-04"}
```

---

## 🔍 Advanced Tips

### **Multi-Step Queries**
1. Start broad: `"Mars"` → Get overview
2. Get specific: `"Mars Perseverance rover"` → Current mission
3. Add context: Get APOD for Mars-related date

### **Educational Sequences**
1. Search for topic images
2. Get related APOD for explanation
3. Search for historical context
4. Compare different time periods

### **Research Workflows**
1. **Topic Discovery:** Broad search terms
2. **Deep Dive:** Specific mission/object names  
3. **Context:** Historical dates and APOD
4. **Comparison:** Multiple related searches

---

## 📱 Mobile-Friendly Quick Commands

For voice assistants or mobile use:

```
"NASA Mars images"
"Space station photos"
"Today's space picture"
"Hubble telescope images"
"Apollo moon photos"
"Saturn ring pictures"
"Nebula images"
"Astronaut spacewalk"
```

---

This quick reference gets you productive with NASA MCP tools immediately. Start with the guaranteed examples, then explore more specific queries as you learn what works best for your needs!