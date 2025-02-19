import sys
from src.scripts.translate_love_language import main as translate_love_language
from src.scripts.names_list import main as random_love_name
from src.scripts.generate_love_letter import main as generate_love_letter
from src.statics.menu import clear_console, display_menu


def main():
    """Main function that handles user input and runs selected scripts."""
    while True:
        clear_console()
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            translate_love_language()
        elif choice == "2":
            random_love_name()
        elif choice == "3":
            generate_love_letter()
        elif choice == "4":
            print("Goodbye! 💕")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter a valid option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
