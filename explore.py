import json
import requests
from config import API_KEY

def buildAPIString():
    #use API_KEY from config file
    strAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + "2001-01-01" + "&end_date=" + "2001-01-01" + "&api_key=" + API_KEY    
    return strAPI

def get_raw_data():
    response = requests.get(buildAPIString())
    json_data = json.loads(response.text)
    return json_data


def describe(value, label="value"):
    """Print what a piece of data is and what is inside it."""
    kind = type(value).__name__
    if isinstance(value, dict):
        print(f"{label}: dict with {len(value)} keys: {list(value.keys())}")
    elif isinstance(value, list):
        print(f"{label}: list with {len(value)} items")
    else:
        print(f"{label}: {kind} = {value}")
 
def pretty(value, limit=1500):
    """Print any data as indented JSON, cut off after limit characters."""
    text = json.dumps(value, indent=2)
    print(text[:limit])
    if len(text) > limit:
        print(f"... ({len(text) - limit} more characters)")
 
def peek(items, count=2):
    """Print the first few items of a list, nicely indented."""
    for item in items[:count]:
        pretty(item, 600)
        print("-----")
 
def outline(value, indent=0, max_depth=4):
    """Print the shape of nested data as an indented tree.
    Lists show only their first item, since the rest share its shape."""
    pad = "    " * indent
    if indent > max_depth:
        print(pad + "...")
    elif isinstance(value, dict):
        for key, item in value.items():
            print(f"{pad}{key}: {type(item).__name__}")
            if isinstance(item, (dict, list)):
                outline(item, indent + 1, max_depth)
    elif isinstance(value, list):
        if len(value) == 0:
            print(pad + "(empty list)")
        else:
            print(f"{pad}[0] of {len(value)}: {type(value[0]).__name__}")
            if isinstance(value[0], (dict, list)):
                outline(value[0], indent + 1, max_depth)







def main():
    raw_data = get_raw_data()
    #print("The raw data: ", raw_data)
    outline(raw_data)


if __name__ == "__main__":
    main()