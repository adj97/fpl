import requests
from Api.request import api
from Class.datamodel import datamodel

if __name__ == '__main__':

    fplapi = api()
    fplapi.constructrurl()
    fplapi.call()

    if(fplapi.status_code==200):
        model = datamodel(fplapi.json)
        print(model)