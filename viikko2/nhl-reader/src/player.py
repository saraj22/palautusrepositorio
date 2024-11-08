class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
        self.score = self.assists + self.goals
    
    def __str__(self):
        return (f"{self.name:<20} {self.team:<4} {self.goals:2} + {self.assists:2} = {self.score:3}")