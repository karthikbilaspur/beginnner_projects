class DisplayMessages:
    def __init__(self):
        pass

    def display_welcome_message(self):
        print("Welcome to Hangman!")

    def display_game_over_message(self, word, score):
        print(f"\nGame Over! The word was {word}. Score: {score}.")

    def display_congratulations_message(self, word, score):
        print(f"\nCongratulations! You guessed {word}. Score: {score}.")

    def display_hint_message(self, hint):
        print(f"HINT: {hint}")

    def display_power_up_message(self, power_up):
        print(f"Power-up: {power_up}")

# Example usage in Hangman game
display_messages = DisplayMessages()
display_messages.display_welcome_message()