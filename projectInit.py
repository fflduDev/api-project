import requests

#tools:

#
#https://www.epochconvert.com/en/
#https://latitudelongitudefinder.com/tools/address-to-coordinates


 
#This works but you need a key
#https://api.nasa.gov
def nasaTest():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(url)
    print(response.text)
 
#(lat lon in decimal)
#https://api.weather.gov/
def weatherTest():
    print ("----- WEATHER \n")
    url = "https://api.weather.gov/points/41.16,-73.26"
    response = requests.get(url)
    print(response.text)

## earthquakes
# https://www.usgs.gov/programs/earthquake-hazards
def earthquakeTest():
    print ("----- EARTHQUAKES\n")
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    response = requests.get(url)
    print(response.text)

#https://wheretheiss.at/
def satelliteTest():
    print ("-----SATELLITES\n")
    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps=1436029892,1436029902&units=miles"
    response = requests.get(url)
    print(response.text)

#alpha vantage
#https://www.alphavantage.co/
def financeTest():
    print ("-----FINANCE\n")
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo"
    response = requests.get(url)
    print(response.text)
