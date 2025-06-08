import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recap(notes):
    prompt = f"Turn these event notes into a polished professional event recap:\n\n{notes}\n\nRecap:"
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
