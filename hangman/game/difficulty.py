from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class DifficultySettings:
    def __init__(self):
        self.difficulty_levels = {
            Difficulty.EASY: {"word_length": 5, "tries": 6},
            Difficulty.MEDIUM: {"word_length": 7, "tries": 5},
            Difficulty.HARD: {"word_length": 9, "tries": 4}
        }

    def get_difficulty_settings(self, difficulty):
        return self.difficulty_levels[difficulty]

    def set_difficulty(self, difficulty):
        if difficulty in self.difficulty_levels:
            return difficulty
        else:
            raise ValueError("Invalid difficulty level")

# Example usage
difficulty_settings = DifficultySettings()
print(difficulty_settings.get_difficulty_settings(Difficulty.EASY))