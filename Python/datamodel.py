from datetime import datetime

class datamodel:

    events = []
    game_settings = {}
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

        # # Game settings
        # print(response['game_settings'])

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
        repr = []
        for event in self.events:
            repr.append(event.id)
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
        #self.chip_plays': [{'chip_name': 'bboost', 'num_played': 145658}, {'chip_name': '3xc', 'num_played': 225749}]
        self.most_selected = json['most_selected']
        self.most_transferred_in = json['most_transferred_in']
        self.top_element = json['top_element']
        #self.top_element_info': {'id': 277, 'points': 20}
        self.transfers_made = json['transfers_made']
        self.most_captained = json['most_captained']
        self.most_vice_captained = json['most_vice_captained']