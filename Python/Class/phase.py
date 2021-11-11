class phase:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.start_event = json['start_event']
        self.stop_event = json['stop_event']