from datetime import datetime
import json

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

        # # Phases
        # print(response['phases'][0])

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
        repr += "Done"
        return str(repr)
        
class event:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.deadline_time = datetime.strptime(json['deadline_time'], '%Y-%m-%dT%H:%M:%SZ')
        self.average_entry_score = json['average_entry_score']
        self.finished = json['finished']
        self.data_checked = json['data_checked']
        self.highest_scoring_entry = json['highest_scoring_entry']
        self.deadline_time_epoch = json['deadline_time_epoch']
        self.deadline_time_game_offset = json['deadline_time_game_offset']
        self.highest_score = json['highest_score']
        self.is_previous = json['is_previous']
        self.is_current = json['is_current']
        self.is_next = json['is_next']
        self.most_selected = json['most_selected']
        self.most_transferred_in = json['most_transferred_in']
        self.top_element = json['top_element']
        self.transfers_made = json['transfers_made']
        self.most_captained = json['most_captained']
        self.most_vice_captained = json['most_vice_captained']

        self.chip_plays = {"bboost": 0, "freehit": 0, "wildcard": 0, "3xc": 0}
        for chip in json['chip_plays']:
            self.chip_plays[chip['chip_name']] = chip['num_played']

        try:
            self.top_element_info = {
                "id": json['top_element_info']["id"], 
                "points": json['top_element_info']["points"]
            }
        except:
            # no top element info yet
            pass

class gamesettings:

    length = 0 
    settings = {}

    def __init__(self, json):
        for obj in json:
            self.settings[obj] = json[obj]
            self.length += 1
