import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recap(notes, media_url=""):
    media_desc = f"A media file was uploaded: {media_url}" if media_url else "No media uploaded."
    prompt = f"Based on the following event notes and media description, write a professional event recap:\n\nNotes: {notes}\n\nMedia: {media_desc}\n\nRecap:"
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
