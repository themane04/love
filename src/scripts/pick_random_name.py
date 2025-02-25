from src.core.generators.a_name_generator import LoveNameGenerator


def main():
    love_name_generator = LoveNameGenerator()
    print("Here’s a lovely name for your wife: ❤️", love_name_generator.get_random_name())
