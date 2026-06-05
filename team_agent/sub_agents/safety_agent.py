from google.adk.agents import Agent

safety_agent = Agent(
    name="safety_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a safety filter. Review the user's message.
    If it contains harmful, offensive, or completely unrelated requests 
    (not weather or greetings), politely decline and explain you only 
    handle weather-related queries.
    Otherwise, approve the message by saying 'SAFE'.
    """,
)