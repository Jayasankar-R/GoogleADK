import requests

def get_weather(city: str) -> dict:
    """Fetches current weather for a given city."""
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        current = data["current_condition"][0]
        return {
            "city": city,
            "temp_c": current["temp_C"],
            "feels_like_c": current["FeelsLikeC"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
        }
    except Exception as e:
        return {"error": str(e)}