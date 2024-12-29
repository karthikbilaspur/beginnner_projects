import random
import time
import json
import os

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.options = ["rock", "paper", "scissors"]
        self.game_modes = {
            "1": "Infinity War",
            "2": "Best of 3",
            "3": "Best of 5",
            "4": "Timed Games",
            "5": "Tournament Mode"
        }
        self.user_profiles = self.load_user_profiles()

    def load_user_profiles(self):
        if os.path.exists("user_profiles.json"):
            with open("user_profiles.json", "r") as file:
                return json.load(file)
        else:
            return {}

    def save_user_profiles(self):
        with open("user_profiles.json", "w") as file:
            json.dump(self.user_profiles, file)

    def display_welcome(self):
        print("*"*50)
        self.name = input("Enter your Name: ")
        if self.name not in self.user_profiles:
            self.user_profiles[self.name] = {"wins": 0, "losses": 0, "ties": 0}
        print(f"Welcome, {self.name}!")

    def display_game_modes(self):
        print("\n"*2 + "*"*50)
        print("\tRock, Paper, Scissors")
        print("*"*50 + "\n")
        print("Game Modes")
        for key, value in self.game_modes.items():
            print(f"{key}. {value}")

    def get_user_choice(self):
        while True:
            user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            if user_input == "q":
                return "quit"
            elif user_input in self.options:
                return user_input
            print("Invalid input. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.options)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        if (user_choice == "rock" and computer_choice == "scissors") or \
           (user_choice == "paper" and computer_choice == "rock") or \
           (user_choice == "scissors" and computer_choice == "paper"):
            return "user"
        return "computer"

    def play_game(self, mode):
        if mode == "Infinity War":
            while True:
                user_choice = self.get_user_choice()
                if user_choice == "quit":
                    break
                computer_choice = self.get_computer_choice()
                print(f"Computer picked {computer_choice}.")
                winner = self.determine_winner(user_choice, computer_choice)
                if winner == "user":
                    self.user_score += 1
                    self.user_profiles[self.name]["wins"] += 1
                    print("You won!")
                elif winner == "computer":
                    self.computer_score += 1
                    self.user_profiles[self.name]["losses"] += 1
                    print("You lost!")
                else:
                    self.user_profiles[self.name]["ties"] += 1
                    print("Both chose same - No Points")
        elif mode == "Best of 3":
            for i in range(3):
                user_choice = self.get_user_choice()
                if user_choice == "quit":
                    break
                computer_choice = self.get_computer_choice()
                print(f"Computer picked {computer_choice}.")
                winner = self.determine_winner(user_choice, computer_choice)
                if winner == "user":
                    self.user_score += 1
                    self.user_profiles[self.name]["wins"] += 1
                    print("You won!")
                elif winner == "computer":
                    self.computer_score += 1
                    self.user_profiles[self.name]["losses"] += 1
                    print("You lost!")
                else:
                    self.user_profiles[self.name]["ties"] += 1
                    print("Both chose same - No Points")
                if self.user_score == 2 or self.computer_score == 2:
                    break
        elif mode == "Best of 5":
            for i in range(5):
                user_choice = self.get_user_choice()
                if user_choice == "quit":
                    break
                computer_choice = self.get_computer_choice()
                print(f"Computer picked {computer_choice}.")
                winner = self.determine_winner(user_choice, computer_choice)
                if winner == "user":
                    self.user_score += 1
                    self.user_profiles[self.name]["wins"] += 1
                    print("You won!")
                elif winner == "computer":
                    self.computer_score += 1
                    self.user_profiles[self.name]["losses"] += 1
                    print("You lost!")
                else:
                    self.user_profiles[self.name]["ties"] += 1
                    print("Both chose same - No Points")
                if self.user_score == 3 or self.computer_score == 3:
                    break
        elif mode == "Timed Games":
            print("You have 30 seconds to make as many choices as possible.")
            start_time = time.time()
            while True:
                user_choice = self.get_user_choice()
                if user_choice == "quit":
                    break
                computer_choice = self.get_computer_choice()
                print(f"Computer picked {computer_choice}.")
                winner = self.determine_winner(user_choice, computer_choice)
                if winner == "user":
                    self.user_score += 1
                    self.user_profiles[self.name]["wins"] += 1
                    print("You won!")
                elif winner == "computer":
                    self.computer_score += 1
                    self.user_profiles[self.name]["losses"] += 1
                    print("You lost!")
                else:
                    self.user_profiles[self.name]["ties"] += 1
                    print("Both chose same - No Points")
                if time.time() - start_time >= 30:
                    break
        elif mode == "Tournament Mode":
            print("You will play a series of games. The winner of each game will advance to the next round.")
            while True:
                user_choice = self.get_user_choice()
                if user_choice == "quit":
                    break
                computer_choice = self.get_computer_choice()
                print(f"Computer picked {computer_choice}.")
                winner = self.determine_winner(user_choice, computer_choice)
                if winner == "user":
                    self.user_score += 1
                    self.user_profiles[self.name]["wins"] += 1
                    print("You won! You advance to the next round.")
                elif winner == "computer":
                    self.computer_score += 1
                    self.user_profiles[self.name]["losses"] += 1
                    print("You lost! You are eliminated from the tournament.")
                    break
                else:
                    self.user_profiles[self.name]["ties"] += 1
                    print("Both chose same - No Points. You will play another game.")

    def display_scoreboard(self):
        print(f"\nFinal Score - {self.name}: {self.user_score}, Computer: {self.computer_score}")
        if self.user_score > self.computer_score:
            print(f"{self.name} wins!")
        elif self.user_score < self.computer_score:
            print("Computer wins!")
        else:
            print("It's a tie!")
        print("Goodbye!")

    def display_user_profiles(self):
        print("\nUser Profiles:")
        for name, profile in self.user_profiles.items():
            print(f"{name}: {profile['wins']} wins, {profile['losses']} losses, {profile['ties']} ties")

def main():
    game = RockPaperScissors()
    game.display_welcome()
    game.display_game_modes()
    mode_choice = input("Choose game mode: ")
    game.play_game(game.game_modes[mode_choice])
    game.save_user_profiles()
    game.display_scoreboard()
    game.display_user_profiles()

if __name__ == "__main__":
    main()