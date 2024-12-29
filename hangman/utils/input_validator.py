class InputValidator:
    def __init__(self):
        pass

    def validate_letter_input(self, input_str):
        if len(input_str) != 1:
            return "Please enter a single letter."
        elif not input_str.isalpha():
            return "Please enter a letter."
        else:
            return True

    def validate_difficulty_input(self, input_str):
        if input_str not in ["1", "2", "3"]:
            return "Invalid difficulty choice. Please choose 1, 2 or 3."
        else:
            return True

    def validate_game_mode_input(self, input_str):
        if input_str not in ["1", "2"]:
            return "Invalid game mode choice. Please choose 1 or 2."
        else:
            return True

# Example usage in Hangman game
input_validator = InputValidator()
guess = input("Guess a letter: ")
result = input_validator.validate_letter_input(guess)
if result is True:
    # Process guess
else:
    print(result)