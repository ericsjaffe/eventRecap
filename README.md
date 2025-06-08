# Event Recap Generator with Media

Generate event recaps based on bullet points and an optional uploaded photo or video.

## Features

- Upload image or video with event notes
- Generate recap using OpenAI GPT-3.5
- Display uploaded media on result page

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
- Add environment variable `OPENAI_API_KEY`
