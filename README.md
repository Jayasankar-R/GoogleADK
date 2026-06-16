 # Google ADK Weather Bot

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-adk
```

## Run
```bash
cp team_agent/.env.example team_agent/.env
# Add your GOOGLE_API_KEY to .env
adk web
```

## Agents
- **weather_bot_orchestrator** — routes messages
- **greeting_agent** — handles hi/bye
- **weather_agent** — fetches weather
- **safety_agent** — blocks unsafe queries
- **streaming_agent** — STT and TTS