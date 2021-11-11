import requests


class api:
    def __init__(self, url):
        self.response = requests.get(url)
        self.response_json = self.response.json()
        self.status_code = self.response.status_code