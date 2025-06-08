# Event Recap Generator

Generate polished event summaries from bullet points using OpenAI GPT-4.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your OpenAI API key to a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

3. Run the app:
```
flask run
```

## Deploy to Render

- Set the start command: `gunicorn app:app`
- Add environment variable `OPENAI_API_KEY` in the dashboard
