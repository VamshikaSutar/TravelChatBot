import requests
import json

def fetch_weather_info(city_name: str) -> str:
    # API key and endpoint configuration
    api_key = '677f8bbdf8e34cd0b1e95337240911'
    api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}'

    try:
        # Make the API request
        response = requests.get(api_url)

        # Check the response status code
        if response.ok:
            weather_data = response.json()

            # Extract temperature and weather condition details
            city = weather_data['location']['name']
            temp_celsius = weather_data['current']['temp_c']
            condition = weather_data['current']['condition']['text']

            # Format and return the weather information as JSON
            return json.dumps({
                "city": city,
                "temperature": temp_celsius,
                "condition": condition
            })

        else:
            # Return an error message if the request fails
            return json.dumps({
                "error": "Failed to retrieve weather information",
                "status_code": response.status_code
            })

    except Exception as error:
        # Handle exceptions and return an error message
        return json.dumps({
            "error": f"An exception occurred: {str(error)}"
        })

if __name__ == "__main__":
    city_name = "London"  # Example city; you can replace it with any city name
    print(fetch_weather_info(city_name))
