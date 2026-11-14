import requests
from config import API_KEY

 
def show_menu():
    print ("------------------------------")
    print ("To see full list of Astroids, press 1 ")
    print ("To see if there are any Dangerous Asteroids, press 2 ")
    print ("To get closest miss distance, press 4 ")
    print ("To get detail for another date, press 3 ")
    print ("To exit press 9 ")

    
def get_choice():
    """Ask until the user enters a valid option number; return it as an int."""
    while True:
        show_menu()
        selection = int(input("Choose an option: "))
        #TODO: do some validation
        return int(selection)
       

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
        print("user choice: ", choice)


if __name__ == "__main__":
    main()