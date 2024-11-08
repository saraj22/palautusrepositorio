class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        print(f"Players from {nationality}\n")
        filtered_players = [player for player in self.reader if player.nationality == nationality]
        return sorted(filtered_players, key=lambda player: player.score, reverse=True)