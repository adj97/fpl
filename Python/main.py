import requests
import json

class model:
    def __init__(self):
        self.events = []
        
class event:
    def __init(self):
        self.id = 1
    
response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
print(response.status_code)
print("\n Events element 0")
print(response.json()['events'][0])
print("\n Game settings")
print(response.json()['game_settings'])
print("\n Phase element 0")
print(response.json()['phases'][0])
print("\n Team element 0")
print(response.json()['teams'][0])
print("\n Total players")
print(response.json()['total_players'])
print("\n Elements element 0")
print(response.json()['elements'][0])
print("\n Element stats e.g.")
print(response.json()['element_stats'])
print("\n Element types e.g.")
print(response.json()['element_types'])