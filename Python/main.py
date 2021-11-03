import requests
from datamodel import datamodel

if __name__ == '__main__':
    response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    response_json = response.json()

    if(response.status_code==200):
        model = datamodel(response_json)
        print(model)