from googletrans import LANGUAGES

from src.core.translators.google_translator import GoogleTranslator


def main():
    translator = GoogleTranslator(max_workers=10)

    user_text = input("Enter text to translate: ")

    if user_text.strip():
        print("\nTranslating... Please wait.")

        results = translator.translate_all(user_text)

        print("\nTranslated Texts:")
        for i, (lang_code, translation) in enumerate(results.items(), start=1):
            print(f"{i}. {LANGUAGES[lang_code].capitalize()} ({lang_code}): {translation}")
    else:
        print("No input provided.")
