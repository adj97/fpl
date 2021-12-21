class team:
    def __init__(self, json):
        self.code = json['code']
        self.draw = json['draw']
        self.form = json['form']
        self.id = json['id']
        self.loss = json['loss']
        self.name = json['name']
        self.played = json['played']
        self.points = json['points']
        self.position = json['position']
        self.short_name = json['short_name']
        self.strength = json['strength']
        self.team_division = json['team_division']
        self.unavailable = json['unavailable']
        self.win = json['win']
        self.strength_overall_home = json['strength_overall_home']
        self.strength_overall_away = json['strength_overall_away']
        self.strength_attack_home = json['strength_attack_home']
        self.strength_attack_away = json['strength_attack_away']
        self.strength_defence_home = json['strength_defence_home']
        self.strength_defence_away = json['strength_defence_away']
        self.pulse_id = json['pulse_id']

    def __repr__(self):
        return str(self.__dict__)