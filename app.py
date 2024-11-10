import json
import ollama
import asyncio
from weather_agent import get_weather
from Itinerary_agent import get_tourist_places
from news_agent import get_news

# Function to get antonyms
def get_antonyms(word: str) -> str:
    antonyms = {
        "hot": "cold",
        "small": "big",
        "weak": "strong",
        "light": "dark",
        "lighten": "darken",
        "dark": "bright",
    }
    return json.dumps(antonyms.get(word, "Antonym not available in the database"))

# Function to simulate fetching flight times (in a real application, this could be an API call)
def get_flight_times(departure: str, arrival: str) -> str:
    flights = {
        "NYC-LAX": {"departure": "08:00 AM", "arrival": "11:30 AM", "duration": "5h 30m"},
        "LAX-NYC": {"departure": "02:00 PM", "arrival": "10:30 PM", "duration": "5h 30m"},
        "LHR-JFK": {"departure": "10:00 AM", "arrival": "01:00 PM", "duration": "8h 00m"},
        
    }
    key = f"{departure}-{arrival}".upper()
    return json.dumps(flights.get(key, {"error": "Flight not found"}))

async def run_interaction(model: str, user_input: str):
    client = ollama.AsyncClient()

    # User's initial query
    messages = [{"role": "user", "content": user_input}]

    # Initial API call to process the user's query
    response = await client.chat(
        model=model,
        messages=messages,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_flight_times",
                    "description": "Get the flight times between two cities",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "departure": {"type": "string", "description": "Departure city"},
                            "arrival": {"type": "string", "description": "Arrival city"},
                        },
                        "required": ["departure", "arrival"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "City name"},
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_news",
                    "description": "Retrieve the latest news for a city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "City name"},
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_itinerary",
                    "description": "Fetch popular tourist itineraries for a city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "City name"},
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_antonyms",
                    "description": "Get antonyms for a given word",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "word": {"type": "string", "description": "The word to find antonyms for"},
                        },
                        "required": ["word"],
                    },
                },
            },
        ],
    )

    # Handle the model's response
    messages.append(response["message"])

    if not response["message"].get("tool_calls"):
        print("Model Response:", response["message"]["content"])
        return

    # Check if the model used any functions and execute them
    available_functions = {
        "get_flight_times": get_flight_times,
        "get_antonyms": get_antonyms,
        "get_weather": get_weather,
        "get_itinerary": get_tourist_places,
        "get_news": get_news,
    }

    for tool in response["message"]["tool_calls"]:
        func = available_functions.get(tool["function"]["name"])
        if func:
            args = tool["function"]["arguments"]
            function_response = func(**args)
            print(f"{tool['function']['name']} Response:", function_response)

# Main loop to interact with the user
if __name__ == "__main__":
    while True:
        user_input = input("Ask something (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        asyncio.run(run_interaction("llama3.2:1b", user_input))
