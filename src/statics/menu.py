import os


def clear_console():
    """Clears the console screen for better readability."""
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():
    """Displays the main menu with available script options."""
    print("\n💖 Welcome to PyLove 💖")
    print("1️⃣ Translate a Love Message")
    print("2️⃣ Get a Random Lovely Name")
    print("3️⃣ Generate a Love Letter")
    print("4️⃣ Exit")
