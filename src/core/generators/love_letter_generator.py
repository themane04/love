import random
from src.statics.love_letter_templates import LOVE_LETTER_TEMPLATES


class LoveLetterGenerator:
    def __init__(self):
        """ Initializes the love letter generator with predefined templates. """
        self.templates = LOVE_LETTER_TEMPLATES

    def generate_love_letter(self, name, mood="sweet"):
        """
        Generates a love letter with the given name and mood.

        :param name: The recipient's name.
        :param mood: The style of the letter (sweet, passionate, poetic).
        :return: A formatted love letter.
        """
        if mood not in self.templates:
            return "Invalid mood. Please choose 'sweet', 'passionate', or 'poetic'."

        template = random.choice(self.templates[mood])
        return template.format(name=name)

    def save_to_file(self, letter, filename="love_letter.txt"):
        """
        Saves the generated love letter to a file.

        :param letter: The letter content.
        :param filename: The name of the file to save.
        """
        with open(filename, "w", encoding="utf-8") as file:
            file.write(letter)
        print(f"💌 Love letter saved to {filename}!")
