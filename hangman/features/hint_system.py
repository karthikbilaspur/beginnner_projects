import random

class HintSystem:
    def __init__(self, word):
        self.word = word

    def provide_hint(self):
        hint_types = ["letter", "word_length", "category"]
        hint_type = random.choice(hint_types)

        if hint_type == "letter":
            hint_letter = random.choice(self.word)
            print(f"HINT: The word contains '{hint_letter}'.")
        elif hint_type == "word_length":
            print(f"HINT: Word length is {len(self.word)}.")
        else:
            # Assuming category is known
            print(f"HINT: Category is {self.get_category()}.")

    def get_category(self):
        # Mock category retrieval
        return "Animal"