import random

class AiOpponent:
    def __init__(self, word_list, difficulty):
        self.word_list = word_list
        self.difficulty = difficulty
        self.word_length = self.get_word_length()
        self.word = self.generate_word()

    def get_word_length(self):
        if self.difficulty == "easy":
            return random.randint(4, 6)
        elif self.difficulty == "medium":
            return random.randint(7, 9)
        else:
            return random.randint(10, 12)

    def generate_word(self):
        words = [word for word in self.word_list if len(word) == self.word_length]
        return random.choice(words)

    def make_guess(self):
        return random.choice("abcdefghijklmnopqrstuvwxyz")

    def update_word(self, guess, word):
        updated_word = ""
        for i in range(len(word)):
            if word[i] == guess:
                updated_word += guess
            else:
                updated_word += word[i]
        return updated_word

    def check_win(self, word):
        return "_" not in word

# Example usage in hangman.py
ai_opponent = AiOpponent(word_list, "medium")
word = ai_opponent.word
guess = ai_opponent.make_guess()