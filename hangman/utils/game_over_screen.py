class GameOverScreen:
    def __init__(self):
        pass

    def display_game_over_screen(self, word, score):
        print("\n" + "="*20)
        print("Game Over")
        print("="*20)
        print(f"Word: {word}")
        print(f"Score: {score}")
        print("="*20 + "\n")

# Example usage in Hangman game
game_over_screen = GameOverScreen()
game_over_screen.display_game_over_screen("hangman", 10)