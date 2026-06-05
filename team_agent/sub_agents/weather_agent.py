from google.adk.agents import Agent
from ..tools.weather_tool import get_weather

weather_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a weather assistant. Use the get_weather tool to fetch weather data.
    Always mention the city name, temperature, and conditions in your response.
    Remember the last city the user asked about — if they say 'what about now?' 
    or 'same city', use the last city from context.
    """,
    tools=[get_weather],
)