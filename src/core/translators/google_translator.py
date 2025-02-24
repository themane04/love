import concurrent.futures
from googletrans import Translator, LANGUAGES


class GoogleTranslator:
    """
    A class that uses the Google Translate API to translate text into multiple languages.
    """

    def __init__(self, max_workers=10):
        """
        Initialize the translator with a configurable number of threads.

        :param max_workers: The maximum number of threads to use for translation.
        :return: A new instance of the GoogleTranslator class.
        """
        self.translator = Translator()
        self.max_workers = max_workers

    def translate_single(self, text, lang_code):
        """
        Translates text into a single language.

        :param text: The text to translate.
        :param lang_code: The language code to translate the text into.
        :return: The translated text.
        """
        try:
            translated = self.translator.translate(text, dest=lang_code)
            return lang_code, translated.text
        except Exception as e:
            return lang_code, f"Error: {e}"

    def translate_all(self, text):
        """
        Translates text into all available languages using multithreading.

        :param text: The text to translate.
        :return: A dictionary of translations for each language.
        """
        translations = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_lang = {executor.submit(self.translate_single, text, lang): lang for lang in LANGUAGES.keys()}

            for future in concurrent.futures.as_completed(future_to_lang):
                lang_code, translation = future.result()
                translations[lang_code] = translation

        return translations
