import requests
from Api.request import api
from Class.datamodel import datamodel

if __name__ == '__main__':

    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = api(url)

    if(response.status_code==200):
        model = datamodel(response.response_json)
        print(model)