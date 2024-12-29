class GameStartScreen:
    def __init__(self):
        pass

    def display_game_start_screen(self):
        print("\n" + "="*20)
        print("Hangman Game")
        print("="*20)
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("="*20 + "\n")

    def display_game_mode_screen(self):
        print("\n" + "="*20)
        print("Select Game Mode")
        print("="*20)
        print("1. Single Player")
        print("2. Multiplayer")
        print("="*20 + "\n")

# Example usage in Hangman game
game_start_screen = GameStartScreen()
game_start_screen.display_game_start_screen()