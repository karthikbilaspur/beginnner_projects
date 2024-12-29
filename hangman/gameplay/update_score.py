class UpdateScore:
    def __init__(self):
        self.score = 0

    def increment_score(self):
        self.score += 1
        return self.score

    def reset_score(self):
        self.score = 0
        return self.score

    def get_score(self):
        return self.score

# Example usage
update_score = UpdateScore()
print(update_score.increment_score())  # 1
print(update_score.increment_score())  # 2
print(update_score.reset_score())  # 0