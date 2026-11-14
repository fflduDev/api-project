import json
import requests
from config import API_KEY

def buildAPIString():
    #use API_KEY from config file
    strAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + "2000-01-01" + "&end_date=" + "2000-01-01" + "&api_key=" + API_KEY    
    return strAPI

def get_raw_data():
    response = requests.get(buildAPIString())
    json_data = json.loads(response.text)
    return json_data

def main():
    raw_data = get_raw_data()
    print("The raw data: ", raw_data)


if __name__ == "__main__":
    main()