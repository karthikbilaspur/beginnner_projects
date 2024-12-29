class TeamGameMode:
    def __init__(self, team1_name, team2_name):
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.team1_score = 0
        self.team2_score = 0
        self.team1_turn = True

    def display_scores(self):
        print(f"{self.team1_name}: {self.team1_score} | {self.team2_name}: {self.team2_score}")

    def update_score(self, team, points):
        if team == self.team1_name:
            self.team1_score += points
        else:
            self.team2_score += points

    def switch_turns(self):
        self.team1_turn = not self.team1_turn

    def check_win(self, target_score):
        return self.team1_score >= target_score or self.team2_score >= target_score

    def play(self, word_list, rounds):
        for round in range(rounds):
            print(f"\nRound {round+1}:")
            if self.team1_turn:
                print(f"{self.team1_name}'s turn:")
                guess = input(f"{self.team1_name}, guess a letter: ")
                # Process guess for team1
                self.switch_turns()
            else:
                print(f"{self.team2_name}'s turn:")
                guess = input(f"{self.team2_name}, guess a letter: ")
                # Process guess for team2
                self.switch_turns()
            self.display_scores()
            if self.check_win(10):  # Target score
                break
        print(f"\nFinal Scores - {self.team1_name}: {self.team1_score} | {self.team2_name}: {self.team2_score}")
        if self.team1_score > self.team2_score:
            print(f"{self.team1_name} wins!")
        elif self.team2_score > self.team1_score:
            print(f"{self.team2_name} wins!")
        else:
            print("It's a tie!")

# Example usage
team_game_mode = TeamGameMode("Team A", "Team B")
team_game_mode.play(["apple", "banana", "cherry"], 5)