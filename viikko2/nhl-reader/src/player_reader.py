import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()

        players = []
        for player_dict in response:
            players.append(Player(player_dict))

        return players