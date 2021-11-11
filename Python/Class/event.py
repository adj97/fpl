from datetime import datetime

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
