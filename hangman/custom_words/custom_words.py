class CustomWords:
    def __init__(self):
        self.custom_words = []

    def add_custom_word(self, word):
        self.custom_words.append(word)

    def get_custom_words(self):
        return self.custom_words