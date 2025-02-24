from datetime import datetime
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

VOICE_MESSAGES_DIR = os.path.join("data", "voice_messages")

os.makedirs(VOICE_MESSAGES_DIR, exist_ok=True)


def generate_voice_message(text):
    """
    Converts a love message into speech using ElevenLabs API
    and saves it to the data/voice_messages directory.
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
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"love_note_{timestamp}.mp3"
        file_path = os.path.join(VOICE_MESSAGES_DIR, filename)

        with open(file_path, "wb") as f:
            f.write(response.content)

        print("🕐 File is being saved... Please wait.")

        while not os.path.exists(file_path):
            time.sleep(1)

        print(f"✅ Love note saved at: {file_path}")
        return file_path
    else:
        print(f"❌ Error: {response.json()}")
        return None
