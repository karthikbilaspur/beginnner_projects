class GuessLetter:
    def __init__(self):
        self.guessed_letters = []

    def guess(self, letter):
        if len(letter) != 1:
            return "Please guess one letter at a time."
        elif letter in self.guessed_letters:
            return "You already guessed this letter. Try another one."
        else:
            self.guessed_letters.append(letter)
            return f"Guessed letter: {letter}"

    def get_guessed_letters(self):
        return self.guessed_letters

# Example usage
guess_letter = GuessLetter()
print(guess_letter.guess("a"))  # Guessed letter: a
print(guess_letter.guess("a"))  # You already guessed this letter. Try another one.