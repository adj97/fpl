class gamesettings:

    length = 0 
    settings = {}

    def __init__(self, json):
        for obj in json:
            self.settings[obj] = json[obj]
            self.length += 1
