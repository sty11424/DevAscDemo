# import the requests library for APIs
import requests
import json

# base URL and endpoint is what we are looking for
base_url = "https://swapi.dev/api/"
endpoint = "people/"

# store the GET API response in variable 'response'
response = requests.get(base_url + endpoint)
# stores the GET response in data and uses the requests method json() to parse the text into Python dictionary
data = response.json()
# prints the data as a dictionary out to the terminal
print(data['results'][0])

