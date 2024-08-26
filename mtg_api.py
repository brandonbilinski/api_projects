import requests
import json

req = "https://api.scryfall.com/cards/random"
response = requests.get(req)
response = response.json()

print(response['name'])
print(response['image_uris']['large'])
    

