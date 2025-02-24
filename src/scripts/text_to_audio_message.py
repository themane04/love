from src.core.generators.voice_message_generator import generate_voice_message


def main():
    text = input("💖 Enter your love message: ")
    if text.strip():
        generate_voice_message(text)
    else:
        print("❌ No text provided.")
