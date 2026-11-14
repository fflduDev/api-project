import json
import requests

#get the api key from the config file
from config import API_KEY
 
 
def show_menu():
    print ("------------------------------")
    print("To see Raw Data press, 99: ")
    print ("To see full list of Astroids, press 1 ")
    print ("To see if there are any Dangerous Asteroids, press 2 ")
    print ("To get closest miss distance, press 4 ")
    print ("To get detail for another date, press 3 ")
    print ("To exit press 9 ")

    
def get_choice():
    """Ask until the user enters a valid option number; return it as an int."""
    
    show_menu()
    selection = int(input("Choose an option: "))
    #TODO: do some validation
    return int(selection)
       

def pause():
    input("\nPress Enter to return to the menu...")

def confirm_quit():
    answer = input("Are you sure you want to quit? (y/n) ").strip().lower()
    return answer == "y"


''' this is a good piece of work, building up the API request:
    - if you're using a KEY, get it from the config file
    - print it out to verify 
    - Then build your API String & print it ( POSTMAN is good for this too)
    - If you can hard code values to do your initial tests, do that, 
        step 1 is connectivity / request & response
        you'll likely ( i did ) run into errors with your request - missing field, bad key, misisng key.   
        that's the job - identify & correct.
    '''
def buildAPIString():
    #use API_KEY from config file
    print("Do we have an API KEY: ", API_KEY)
    strAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + "2000-01-01" + "&end_date=" + "2000-01-01" + "&api_key=" + API_KEY
    
    print("Our API Request string looks like: ", strAPI)

    return strAPI
 
def look_at_raw_data():
    """Retrieve the data and take a first look at it."""
    response = requests.get(buildAPIString())
    json_data = json.loads(response.text)
    return json_data
 

def main():

    while True:
        show_menu()
        choice = get_choice()
        print("user choice: ", choice)
        if choice == 99:
            rawData = look_at_raw_data()
            print("rawData: ", rawData)
        else:
            print("later..")
            exit()


if __name__ == "__main__":
    main()