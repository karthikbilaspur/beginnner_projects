import random
from word_list import word_list
from utils.display_hangman import display_hangman
from difficulty import DifficultySettings
from game_mode import GameModeSettings
from hangman.features.hint_system import HintSystem
from hangman.features.power_ups import PowerUps
from hangman.features.leaderboards import Leaderboards

class Hangman:
    def __init__(self):
        self.difficulty_settings = DifficultySettings()
        self.game_mode_settings = GameModeSettings()
        self.hint_system = HintSystem("")
        self.power_ups = PowerUps()
        self.leaderboards = Leaderboards()
        self.word = ""
        self.guessed_word = []
        self.guessed_letters = []
        self.tries = 0
        self.score = 0
        self.difficulty = None
        self.game_mode = None

    def start_game(self):
        print("Advanced Hangman Game Started.")
        self.select_difficulty()
        self.select_game_mode()
        self.initialize_game()
        self.gameplay()

    def select_difficulty(self):
        print("Select difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty_choice = int(input("Enter choice (1/2/3): "))
        self.difficulty = self.difficulty_settings.set_difficulty(Difficulty(difficulty_choice))

    def select_game_mode(self):
        print("Select game mode:")
        print("1. Single Player")
        print("2. Multiplayer")
        game_mode_choice = int(input("Enter choice (1/2): "))
        self.game_mode = self.game_mode_settings.set_game_mode(GameMode(game_mode_choice))

    def initialize_game(self):
        self.word_length = self.difficulty_settings.get_difficulty_settings(self.difficulty)["word_length"]
        self.tries = self.difficulty_settings.get_difficulty_settings(self.difficulty)["tries"]
        self.word_list = self.game_mode_settings.get_game_mode_settings(self.game_mode)["word_list"]
        self.score_limit = self.game_mode_settings.get_game_mode_settings(self.game_mode)["score_limit"]
        self.word = random.choice(word_list[self.word_list])
        self.guessed_word = ["_"] * len(self.word)

    def gameplay(self):
        while self.tries > 0 and "_" in self.guessed_word:
            print(f"\nDifficulty: {self.difficulty.name}")
            print(f"Game Mode: {self.game_mode.name}")
            print(display_hangman(self.tries))
            print(" ".join(self.guessed_word))
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1:
                print("Please guess one letter at a time.")
            elif guess in self.guessed_letters:
                print("You already guessed this letter. Try another one.")
            elif guess not in self.word:
                self.tries -= 1
                self.guessed_letters.append(guess)
                print(f"Incorrect! You have {self.tries} tries left.")
            else:
                self.guessed_letters.append(guess)
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.guessed_word[i] = guess
                self.score += 1

            # Hint System
            if self.hint_system.is_hint_available():
                print("Hint available. Use 'hint' to reveal a letter.")

            # Power-Ups
            if self.power_ups.is_power_up_available():
                print("Power-up available. Use 'power-up' to skip a turn.")

            if self.score == self.score_limit:
                print("Congratulations! You reached the score limit.")
                break

        if "_" not in self.guessed_word:
            print(f"\nCongratulations! You guessed {self.word}. Score: {self.score}.")
        else:
            print(display_hangman(self.tries))
            print(f"\nGame Over! The word was {self.word}. Score: {self.score}.")

        self.leaderboards.update_score(self.score)
        self.leaderboards.display_leaderboard()

    def play_again(self):
        play = input("Play again? (yes/no): ")
        if play.lower() == "yes":
            self.start_game()
        else:
            print("Thank you for playing.")

if __name__ == "__main__":
    hangman = Hangman()
    hangman.start_game()
    hangman.play_again()