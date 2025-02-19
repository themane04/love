import concurrent.futures
from googletrans import Translator, LANGUAGES


class GoogleTranslator:
    def __init__(self, max_workers=10):
        """ Initialize the translator with a configurable number of threads. """
        self.translator = Translator()
        self.max_workers = max_workers

    def translate_single(self, text, lang_code):
        """ Translates text into a single language. """
        try:
            translated = self.translator.translate(text, dest=lang_code)
            return lang_code, translated.text
        except Exception as e:
            return lang_code, f"Error: {e}"

    def translate_all(self, text):
        """ Translates text into all available languages using multithreading. """
        translations = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_lang = {executor.submit(self.translate_single, text, lang): lang for lang in LANGUAGES.keys()}

            for future in concurrent.futures.as_completed(future_to_lang):
                lang_code, translation = future.result()
                translations[lang_code] = translation

        return translations
