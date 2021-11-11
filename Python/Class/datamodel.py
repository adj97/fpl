from Class.event import event
from Class.gamesettings import gamesettings
from Class.phase import phase

class datamodel:

    events = []
    #game_settings = {}
    phases = []
    teams = []
    total_players = 0
    elements = []
    element_stats = []
    element_types = []

    def __init__(self, response):
        # Events
        for eventjson in response['events']:
            self.events.append(event(eventjson))

        # Game settings
        self.game_settings = gamesettings(response['game_settings'])

        # Phases
        for phasejson in response['phases']:
            self.phases.append(phase(phasejson))

        # # Teams
        # print(response['teams'][0])

        # # Total players
        # print(response['total_players'])

        # # Elements
        # print(response['elements'][0])

        # # Element stats
        # print(response['element_stats'])

        # # Element types
        # print(response['element_types'])

    def __repr__(self):
        repr = "Printing current model:\n"
        repr += "> " + str(len(self.events)) + " events\n"
        repr += "> " + str(self.game_settings.length) + " game settings\n"
        repr += "> " + str(len(self.phases)) + " phases\n"
        repr += "Done"
        return str(repr)
