# import requests

# url = "https://api.foursquare.com/v3/places/search"

# params = {
#   	"query": "tourist",
#   	"near": "Mumbai",
#   	"open_now": "true",
#   	"sort":"DISTANCE"
# }

# headers = {
#     "Accept": "application/json",
#     "Authorization": "fsq3tiwckB5KfwtTck0np5WTH0XRLKcfUD3ilr7tzXVIt7k="
# }

# response = requests.request("GET", url, params=params, headers=headers)
# list_place = [i['name'] for i in response.json()["results"]]

# for i in list_place:
#     print(i)

import requests
import json

def fetch_tourist_attractions(city: str) -> str:
    # API endpoint and key for Foursquare
    api_endpoint = "https://api.foursquare.com/v3/places/search"
    api_key = "fsq3tiwckB5KfwtTck0np5WTH0XRLKcfUD3ilr7tzXVIt7k="
    
    # Request parameters
    parameters = {
        "query": "tourist",
        "near": city,
        "open_now": "true",
        "sort": "DISTANCE"
    }

    # Headers for the API request
    headers = {
        "Accept": "application/json",
        "Authorization": api_key
    }

    try:
        # Make the API call
        response = requests.get(api_endpoint, params=parameters, headers=headers)

        # Check the response status
        if response.status_code == 200:
            response_data = response.json()

            # Extract the tourist attraction names
            attractions = [place['name'] for place in response_data.get("results", [])]

            # Return the attractions in JSON format
            return json.dumps({"city": city, "tourist_attractions": attractions})
        else:
            # Handle errors by returning a JSON error message
            return json.dumps({"error": "Failed to retrieve tourist attractions", "status_code": response.status_code})

    except Exception as error:
        # Handle exceptions and return an error message
        return json.dumps({"error": f"Exception occurred: {str(error)}"})

if __name__ == "__main__":
    # Example usage
    city_name = "London"  # Replace with any city name
    print(fetch_tourist_attractions(city_name))

