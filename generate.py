import openai
import os

def generate_recap(notes):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"Turn these event notes into a polished professional event recap:\n\n{notes}\n\nRecap:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
