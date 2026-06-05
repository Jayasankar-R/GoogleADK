from google.adk.agents import Agent
from .sub_agents.weather_agent import weather_agent
from .sub_agents.greeting_agent import greeting_agent
from .sub_agents.safety_agent import safety_agent

root_agent = Agent(
    name="weather_bot_orchestrator",
    model="gemini-2.0-flash",
    instruction="""
    You are the orchestrator of a Weather Bot system. Your job is to route 
    user messages to the right sub-agent:

    1. First, ALWAYS pass the message to safety_agent. If it returns anything 
       other than 'SAFE', relay that response to the user and stop.
    2. If the message is a greeting or farewell → route to greeting_agent.
    3. If the message is about weather → route to weather_agent.
    4. If unsure, ask the user to clarify.

    Remember context across the conversation — especially the last city checked.
    """,
    sub_agents=[safety_agent, greeting_agent, weather_agent],
)