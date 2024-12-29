class Leaderboards:
    def __init__(self):
        self.scores = []

    def update_score(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)

    def display_leaderboard(self):
        print("Leaderboard:")
        for i, score in enumerate(self.scores):
            print(f"{i+1}. {score}")