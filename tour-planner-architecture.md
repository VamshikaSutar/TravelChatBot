# Tour Planning Application - Implementation Guide

## 1. System Architecture Overview

### A. Backend Components
1. **Database Layer**
   - Neo4j for graph database (user preferences and relationships)
   - Vector database for semantic search and memory
   - PostgreSQL/MongoDB for user management and chat history

2. **API Layer (FastAPI)**
   - User authentication endpoints
   - Chat interaction endpoints
   - Itinerary management endpoints
   - Weather and news integration endpoints

3. **LLM Integration Layer**
   - Model endpoints using Transformers/Ollama/vLLM
   - Function calling implementation using Outlines/Ollama

### B. Agent System
1. **User Interaction Agent**
   ```python
   class UserInteractionAgent:
       - gather_preferences()
       - validate_inputs()
       - handle_chat_context()
   ```

2. **Itinerary Generation Agent**
   ```python
   class ItineraryAgent:
       - create_initial_plan()
       - optimize_sequence()
       - calculate_timings()
   ```

3. **Optimization Agent**
   ```python
   class OptimizationAgent:
       - optimize_route()
       - calculate_costs()
       - adjust_for_constraints()
   ```

4. **Weather & News Agent**
   ```python
   class EnvironmentalAgent:
       - fetch_weather()
       - check_local_events()
       - get_attraction_status()
   ```

5. **Memory Agent**
   ```python
   class MemoryAgent:
       - store_preferences()
       - update_user_profile()
       - retrieve_context()
   ```

## 2. Implementation Steps

### Phase 1: Setup & Infrastructure
1. Set up development environment
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate

   # Install core dependencies
   pip install fastapi streamlit neo4j transformers nltk pandas
   ```

2. Initialize database schemas
   ```python
   # Neo4j schema for user preferences
   CREATE (:User {id: STRING, name: STRING})
   CREATE (:Preference {type: STRING, value: STRING})
   CREATE (:Location {name: STRING, type: STRING})
   ```

### Phase 2: Core Components Implementation

1. **User Authentication System**
   ```python
   from fastapi import FastAPI, Depends
   from fastapi_security import OAuth2PasswordBearer

   app = FastAPI()

   @app.post("/login")
   async def login(username: str, password: str):
       # Implement user authentication
       pass
   ```

2. **Chat Interface (Streamlit)**
   ```python
   import streamlit as st

   def create_chat_interface():
       st.title("Tour Planning Assistant")
       with st.chat_message("assistant"):
           st.write("Welcome! Let's plan your trip.")
   ```

3. **Memory System Implementation**
   ```python
   from neo4j import GraphDatabase

   class MemorySystem:
       def __init__(self):
           self.driver = GraphDatabase.driver(uri, auth=(user, password))

       def store_preference(self, user_id, preference_type, value):
           with self.driver.session() as session:
               session.run("""
                   MERGE (u:User {id: $user_id})
                   MERGE (p:Preference {type: $type, value: $value})
                   MERGE (u)-[:PREFERS]->(p)
               """, user_id=user_id, type=preference_type, value=value)
   ```

### Phase 3: Agent Implementation

1. **LLM Integration**
   ```python
   from transformers import AutoTokenizer, AutoModelForCausalLM

   class LLMHandler:
       def __init__(self):
           self.model = AutoModelForCausalLM.from_pretrained("appropriate-model")
           self.tokenizer = AutoTokenizer.from_pretrained("appropriate-model")

       def generate_response(self, prompt):
           inputs = self.tokenizer(prompt, return_tensors="pt")
           outputs = self.model.generate(**inputs)
           return self.tokenizer.decode(outputs[0])
   ```

2. **Function Calling Setup**
   ```python
   from outlines import functions

   @functions.register
   def get_weather(location: str, date: str):
       # Implement weather API integration
       pass

   @functions.register
   def optimize_route(locations: list, constraints: dict):
       # Implement route optimization
       pass
   ```

### Phase 4: Integration & Testing

1. **System Integration**
   ```python
   class TourPlanningSystem:
       def __init__(self):
           self.memory_agent = MemoryAgent()
           self.llm_handler = LLMHandler()
           self.weather_agent = WeatherAgent()
           
       async def process_user_input(self, user_id: str, message: str):
           context = self.memory_agent.get_context(user_id)
           response = await self.llm_handler.generate_response(
               context + message
           )
           return response
   ```

2. **Testing Framework**
   ```python
   import pytest

   @pytest.mark.asyncio
   async def test_tour_planning():
       system = TourPlanningSystem()
       response = await system.process_user_input(
           "test_user",
           "I want to visit Rome tomorrow"
       )
       assert "budget" in response.lower()
   ```

## 3. Deployment Steps

1. **Docker Configuration**
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Environment Configuration**
   ```yaml
   # docker-compose.yml
   version: '3'
   services:
     web:
       build: .
       ports:
         - "8000:8000"
     neo4j:
       image: neo4j:latest
     streamlit:
       build: ./frontend
       ports:
         - "8501:8501"
   ```

## 4. Monitoring & Maintenance

1. **Logging System**
   ```python
   import logging

   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )
   ```

2. **Performance Monitoring**
   ```python
   from prometheus_client import Counter, Histogram

   requests_total = Counter('requests_total', 'Total requests')
   response_time = Histogram('response_time_seconds', 'Response time')
   ```
