import requests
from config import API_KEY

APOD_URL = "https://api.nasa.gov/planetary/apod"

def get_response(url, params):
    """Send a GET request and return the response."""
    return requests.get(url, params=params)

def show_response(response):
    """Print the status, the rate-limit headers and the raw body."""
    print("Status:", response.status_code)
    print("Limit:", response.headers.get("X-RateLimit-Limit"))
    print("Remaining:", response.headers.get("X-RateLimit-Remaining"))
    print(response.text)

def main():
    response = get_response(APOD_URL, {"api_key": API_KEY})
    show_response(response)

main()
