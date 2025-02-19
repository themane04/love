import random

from src.statics.lovely_names import LOVELY_NAMES


class LoveNameGenerator:
    def __init__(self):
        self.lovely_names = LOVELY_NAMES

    def get_random_name(self):
        return random.choice(self.lovely_names)
