import requests


class api:

    def constructrurl(self):
        prefix = "https:/"
        base = "fantasy.premierleague.com"
        api = "api"
        api_function = ["bootstrap-static"]
        api_subfunction = [""]

        full_url = '/'.join([prefix, base, api, api_function[0], api_subfunction[0]])

        self.url = full_url
        return

    def call(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return