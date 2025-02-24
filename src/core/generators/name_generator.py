import random

from src.statics.names import LOVELY_NAMES


class LoveNameGenerator:
    """
    A generator class that provides random lovely names.
    """

    def __init__(self):
        self.lovely_names = LOVELY_NAMES

    def get_random_name(self):
        return random.choice(self.lovely_names)
