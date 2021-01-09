class Game:
    def __init__(self, team1, team2, team1_score, team2_score, timeLeft):
        self.team1 = team1.strip()
        self.team2 = team2.strip()
        self.team1_score = team1_score.strip()
        self.team2_score = team2_score.strip()
        self.timeLeft = timeLeft.strip()
    def __str__(self):
        return self.team1 + " " + self.team1_score + " - " + self.team2_score + " " + self.team2 + " @ " + self.timeLeft
    def __repr__(self):
        return self.team1 + " " + self.team1_score + " - " + self.team2_score + " " + self.team2 + " @ " + self.timeLeft
    