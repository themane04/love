import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def generate_voice_message(text, filename="love_note.mp3"):
    """
    Converts a love message into speech using ElevenLabs API.
    """

    url = f"{os.getenv('ELEVENLABS_URL')}{os.getenv('ELEVENLABS_VOICE_ID')}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY")
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    print("🔊 Generating audio message... Please wait.")
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

        print("🕐 File is being saved... Please wait.")

        while not os.path.exists(filename):
            time.sleep(1)

        print(f"✅ Love note saved as {filename}!")
    else:
        print(f"❌ Error: {response.json()}")
