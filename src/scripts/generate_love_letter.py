from src.core.generators.letter_generator import LoveLetterGenerator


def main():
    print("💌 Welcome to the Love Letter Generator! 💕")

    recipient_name = input("Enter the recipient's name: ").strip()
    sender_name = input("Enter your name: ").strip()
    if not recipient_name or not sender_name:
        print("❌ Name cannot be empty!")
        return

    print("\nChoose the mood of your love letter:")
    print("1️⃣ Sweet")
    print("2️⃣ Passionate")
    print("3️⃣ Poetic")

    mood_choice = input("\nEnter your choice (1-3): ").strip()
    mood_map = {"1": "sweet", "2": "passionate", "3": "poetic"}
    mood = mood_map.get(mood_choice, "sweet")

    generator = LoveLetterGenerator()
    love_letter = generator.generate_love_letter(recipient_name, sender_name, mood)

    print("\n💌 Your Love Letter:\n")
    print(love_letter)

    save = input("\nDo you want to save this letter? (y/n): ").strip().lower()
    if save == "y":
        filename = f"love_letter_for_{recipient_name.replace(' ', '_').lower()}.txt"
        generator.save_to_file(love_letter, filename)
