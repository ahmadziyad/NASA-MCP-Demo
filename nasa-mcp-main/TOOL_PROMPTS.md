# 🚀 NASA MCP Tools - Query Prompts Guide

This guide defines effective prompts for querying the NASA MCP tools through AI assistants like Claude Desktop or custom MCP clients.

## 🔧 Available Tools Overview

### 1. `search_images_data` - NASA Image Search
**Purpose:** Search NASA's extensive image and video library
**Parameters:** 
- `q` (string): Search query
- `size` (integer): Number of results (default: 3, max recommended: 20)

### 2. `get_nasa_apod` - Astronomy Picture of the Day
**Purpose:** Get NASA's featured astronomy image/video with explanation
**Parameters:**
- `date` (string, optional): Date in YYYY-MM-DD format (1995-06-16 to today)

---

## 🎯 Effective Query Prompts

### NASA Image Search Prompts

#### **Space Exploration & Missions**
```
"Show me images of Mars rover missions"
"Find pictures of the Apollo 11 moon landing"
"Search for International Space Station photos"
"Get images of SpaceX Dragon capsule"
"Show me Curiosity rover discoveries on Mars"
"Find photos from the Artemis program"
"Search for images of lunar surface exploration"
"Show me pictures of astronauts on spacewalks"
```

#### **Celestial Objects & Phenomena**
```
"Find images of the Orion Nebula"
"Show me pictures of Saturn's rings"
"Search for images of black holes"
"Get photos of Jupiter's Great Red Spot"
"Find images of solar eclipses"
"Show me pictures of the Milky Way galaxy"
"Search for images of supernovas"
"Find photos of comet approaches"
```

#### **Space Telescopes & Observations**
```
"Show me Hubble Space Telescope images"
"Find James Webb Space Telescope photos"
"Search for images from the Spitzer telescope"
"Get pictures taken by the Kepler telescope"
"Show me deep space observations"
"Find images of exoplanets"
"Search for telescope views of distant galaxies"
```

#### **Earth from Space**
```
"Show me Earth from space"
"Find images of Earth's atmosphere"
"Search for photos of Earth at night"
"Get images of weather patterns from space"
"Show me pictures of Earth's continents from orbit"
"Find images of aurora from space"
"Search for photos of Earth's curvature"
```

#### **Historical Space Missions**
```
"Find images from the Mercury program"
"Show me Gemini mission photos"
"Search for Apollo program images"
"Get pictures from the Space Shuttle era"
"Find images of the first satellite launches"
"Show me photos from early space exploration"
"Search for images of space race milestones"
```

### NASA APOD (Astronomy Picture of the Day) Prompts

#### **Current & Recent**
```
"Get today's astronomy picture from NASA"
"Show me this week's astronomy pictures"
"What's NASA's current featured space image?"
"Get the latest astronomy picture of the day"
```

#### **Historical Dates**
```
"Show me NASA's astronomy picture for January 1, 2024"
"Get the APOD for my birthday: [YYYY-MM-DD]"
"What was NASA's featured image on Christmas 2023?"
"Show me the astronomy picture from New Year's Day 2020"
"Get the APOD from the first day it was published: June 16, 1995"
```

#### **Special Occasions**
```
"Show me NASA's astronomy picture for the solar eclipse date"
"Get the APOD from when James Webb took its first image"
"What was NASA's featured image during the Mars rover landing?"
"Show me the astronomy picture from the day humans first walked on the moon"
```

---

## 📝 Prompt Templates for AI Assistants

### Template 1: Basic Image Search
```
"Use the NASA MCP server to search for images of [TOPIC]. 
Show me [NUMBER] results with titles and descriptions."

Example:
"Use the NASA MCP server to search for images of Mars rovers. 
Show me 5 results with titles and descriptions."
```

### Template 2: Specific Mission Search
```
"Search NASA's image database for photos related to [MISSION/PROGRAM]. 
Include details about when the images were taken."

Example:
"Search NASA's image database for photos related to the Apollo 11 mission. 
Include details about when the images were taken."
```

### Template 3: APOD Request
```
"Get NASA's Astronomy Picture of the Day for [DATE/TODAY]. 
Explain what the image shows and provide the full description."

Example:
"Get NASA's Astronomy Picture of the Day for December 25, 2023. 
Explain what the image shows and provide the full description."
```

### Template 4: Comparative Search
```
"Search for NASA images of [TOPIC1] and [TOPIC2]. 
Compare what you find and show me the most interesting examples."

Example:
"Search for NASA images of Jupiter and Saturn. 
Compare what you find and show me the most interesting examples."
```

### Template 5: Educational Query
```
"Find NASA images that would help explain [CONCEPT/PHENOMENON]. 
Provide educational context for each image."

Example:
"Find NASA images that would help explain how solar eclipses work. 
Provide educational context for each image."
```

---

## 🎨 Advanced Query Strategies

### Multi-Step Queries
```
1. "First, search for images of the Hubble Space Telescope"
2. "Then, get today's astronomy picture of the day"
3. "Finally, search for images of what Hubble has discovered"
```

### Contextual Queries
```
"I'm writing a report about Mars exploration. Find me:
- Images of different Mars rovers
- Pictures of the Martian surface
- Photos showing the scale of Mars compared to Earth"
```

### Time-Based Queries
```
"Show me how space exploration has evolved by finding:
- Images from the 1960s Apollo program
- Photos from the 1980s Space Shuttle era  
- Recent images from current Mars missions"
```

### Thematic Collections
```
"Create a collection of images showing:
- The beauty of nebulae and star formations
- The scale of our solar system
- Human achievements in space exploration"
```

---

## 🔍 Query Optimization Tips

### **For Better Image Search Results:**
- Use specific mission names (Apollo 11, Curiosity, Perseverance)
- Include object types (rover, telescope, satellite, astronaut)
- Add descriptive terms (surface, orbit, launch, landing)
- Specify celestial objects (Mars, Jupiter, Orion Nebula, Milky Way)

### **For APOD Queries:**
- Use exact date format: YYYY-MM-DD
- Try significant dates in space history
- Request explanations of the astronomical phenomena shown
- Ask for context about why the image was featured

### **For Educational Use:**
- Request multiple related images for comparison
- Ask for historical context and significance
- Include requests for technical details and explanations
- Combine image searches with APOD requests for comprehensive coverage

---

## 🚨 Common Query Pitfalls to Avoid

### **Avoid These Search Terms:**
- Too generic: "space" (use "Mars rover" instead)
- Misspelled names: "Hubel" (use "Hubble")
- Non-NASA content: "SpaceX Starship" (NASA has limited SpaceX images)
- Very recent events: NASA's database may not have immediate coverage

### **APOD Date Limitations:**
- Dates before June 16, 1995 (APOD didn't exist)
- Future dates (obviously won't work)
- Invalid date formats (use YYYY-MM-DD only)

### **Size Limitations:**
- Don't request more than 20 images at once
- Start with 3-5 results, then request more if needed
- Large requests may timeout or be slow

---

## 🎯 Example Conversation Flows

### **Educational Research Flow:**
```
User: "I need images for a presentation about Mars exploration"
Assistant: "I'll search NASA's database for Mars exploration images..."
[Calls search_images_data with "Mars exploration", size: 5]

User: "Can you also get some historical context?"
Assistant: "Let me search for Apollo program images for comparison..."
[Calls search_images_data with "Apollo program", size: 3]

User: "What about today's space image?"
Assistant: "I'll get today's Astronomy Picture of the Day..."
[Calls get_nasa_apod with no date parameter]
```

### **Curiosity-Driven Flow:**
```
User: "What's the most amazing thing NASA has photographed recently?"
Assistant: "Let me get today's featured astronomy image..."
[Calls get_nasa_apod]

User: "That's incredible! Are there more images like this?"
Assistant: "I'll search for similar astronomical phenomena..."
[Calls search_images_data based on APOD content]
```

---

This guide provides the foundation for effective interaction with the NASA MCP tools through natural language prompts, enabling rich educational and research experiences with NASA's vast image database.