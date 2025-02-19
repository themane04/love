import sys
from src.scripts.translate_love_language import main as translate_love_language
from src.scripts.names_list import main as random_love_name
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
            print("Goodbye! 💕")
            sys.exit(0)
        elif choice == "" or choice.isspace() or choice.isalpha() or int(choice) not in range(1, 4):
            print("❌ Please enter a valid option.")
        else:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
