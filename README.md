# One-Day Tour Planning Assistant

## Overview
This project implements a **One-Day Tour Planning Assistant** that dynamically creates a personalized day-trip itinerary based on the user’s preferences. Using **Ollama**, the assistant interacts in real-time to collect user requirements and preferences, adjusts to new inputs, and remembers user preferences across sessions for a tailored experience. 

## Features
- **User Interaction through Chat**: A conversational interface prompts users for information on city, timings, budget, interests, starting point, and any specific preferences like restaurants or types of attractions.
   
- **Memory Persistence**: Leveraging Ollama's capabilities, the assistant remembers user preferences across interactions, allowing it to suggest itineraries based on historical user data for a more personalized experience.

- **Dynamic Itinerary Adjustment**: The assistant continuously updates the plan as users add or modify preferences, such as additional stops, specific types of attractions, or changes in budget.

- **Optimization Agent**: Routes are optimized based on time, budget, and convenience. If the user allows taxis within their budget, the assistant recommends when to take taxis for time efficiency.

- **Weather & Attraction Status Integration**: Weather conditions and attraction statuses (e.g., open, closed, under renovation) are factored into the itinerary to ensure feasibility and comfort.

- **Visual Map & Detailed Itinerary**: The assistant provides a visual map with marked points of interest and a step-by-step itinerary, including travel details, time allocations, and expected costs.

## Components

1. **LLM-Based Agents**:
   - **User Interaction Agent**: Collects user preferences and guides through the initial stages of trip planning.
   - **Itinerary Generation Agent**: Creates the itinerary based on user inputs.
   - **Optimization Agent**: Refines the itinerary, optimizing paths based on the user’s budget and time.
   - **Weather & News Agents**: Fetch current conditions to ensure the itinerary aligns with external factors like weather or local events.
   - **Memory Agent**: Stores preferences, structured as triplets, for ongoing personalization.

2. **Database**:
   - **Graph Database**: User preferences are stored in **Neo4j** with a memory structure that supports evolving user preferences and constraints. 

3. **Frontend**:
   - **Streamlit-based UI**: Users can interact with the assistant, view itineraries, and see previous conversations seamlessly. 

## Setup & Requirements

### Software Requirements
- **Python** 3.8 or higher
- **Ollama**
- **Neo4j** for graph-based memory
- **Streamlit** for frontend

### Python Libraries
- `FastAPI` for microservices
- `Transformers` for LLMs
- `Outlines` for function calling
- Additional requirements specified in `requirements.txt`

### Environment Setup
1. Clone this repository and install dependencies:  
   ```bash
   pip install -r requirements.txt
