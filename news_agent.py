import requests
import json

def get_news(query: str, from_date: str, to_date: str, language: str = "en") -> str:
    # Define the API endpoint and the key
    api_key = 'pub_587490b53d269d365ad2aba1ec4bf392f6277'
    url = f'https://newsdata.io/api/1/archive?apikey={api_key}&q={query}&language={language}&from_date={from_date}&to_date={to_date}'
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            articles = [
                {
                    "title": article.get("title", "No Title"),
                    "description": article.get("description", "No Description"),
                    "pubDate": article.get("pubDate", "No Date")
                }
                for article in data.get("results", [])
            ]
            
            # Return the news data as JSON
            return json.dumps({"query": query, "articles": articles}, indent=2)
        
        else:
            return json.dumps({"error": "Unable to fetch news data", "status_code": response.status_code})
    
    except Exception as e:
        return json.dumps({"error": f"Error: {str(e)}"})

if __name__ == "__main__":
    print(get_news(query, from_date, to_date))
