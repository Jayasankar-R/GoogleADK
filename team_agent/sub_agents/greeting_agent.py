from google.adk.agents import Agent

greeting_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    instruction="""
    You handle greetings and farewells only.
    If the user says hi, hello, bye, thanks — respond warmly and naturally.
    Do NOT answer weather questions. Transfer back to the orchestrator for those.
    """,
)