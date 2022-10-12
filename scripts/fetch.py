import requests


def fetchSodaApi():
    import json
    import os

    # Fetch data from Soda API
    url = "https://data.cityofnewyork.us/resource/ymhw-9cz9.json"
    response = requests.get(url)
    data = json.loads(response.text)

    # Create a new directory if it doesn't exist
    if not os.path.exists('../data'):
        os.makedirs('../data')

    # Write the data to a file
    with open('../data/hospitals.json', 'w') as outfile:
        json.dump(data, outfile)

    # Print the number of records fetched
    print("Number of records fetched: " + str(len(data)))




print(f"Fetching data from Soda API...")
fetchSodaApi()

