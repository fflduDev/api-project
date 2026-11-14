import requests
from config import API_KEY

OPTIONS = [
"Number of characters",
"List of character names",
"Tallest character",
"Characters taller than a height you choose",
"Search for a character by name",
]
def show_menu():
    print()
    print("===== Star Wars Explorer =====")
    for number, option in enumerate(OPTIONS, start=1):
        print(f"{number}. {option}")
        print("0. Quit")

def get_choice():
    """Ask until the user enters a valid option number; return it as an int."""
    while True:
        text = input("Choose an option: ").strip()
        if text.isdigit() and int(text) <= len(OPTIONS):
            return int(text)
        print(f"Please enter a number from 0 to {len(OPTIONS)}.")

def pause():
    input("\nPress Enter to return to the menu...")

def confirm_quit():
    answer = input("Are you sure you want to quit? (y/n) ").strip().lower()
    return answer == "y"



def show_count(response):
    print("[stub] Will show how many characters are in the database.")

def show_names(response):
    print("[stub] Will list the characters' names.")
    # ...one stub function for each remaining option

def main():

    while True:
        show_menu()
        choice = get_choice()


if __name__ == "__main__":
    main()