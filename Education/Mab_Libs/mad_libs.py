import random

class MadLibsGame:
    def __init__(self):
        self.words = {}

    def get_user_input(self):
        self.words = {
            "name": input("Enter a name: "),
            "adjective1": input("Enter an adjective: "),
            "adjective2": input("Enter another adjective: "),
            "adjective3": input("Enter one more adjective: "),
            "noun1": input("Enter a noun: "),
            "noun2": input("Enter another noun: "),
            "animal": input("Enter an animal: "),
            "food": input("Enter a food: "),
            "verb": input("Enter a verb: "),
            "city": input("Enter a city: "),
            "sport": input("Enter a sport: ")
        }

    def generate_story(self, template):
        return template.format(**self.words)

    def display_story(self, story):
        print("Here's your Mad Libs story:")
        print(story)

    def play_game(self):
        print("Welcome to Mad Libs Game!")
        self.get_user_input()

        templates = [
            """Once upon a time, {name} was a very {adjective1} person.
They had a {adjective2} {noun1} and a {adjective3} {noun2}.
One day, {name} saw a {animal} eating {food} in {city}.
It was very {adjective1}!""",
            """{name} loved playing {sport} with their {adjective2} friends.
They had a {adjective3} {noun1} and a {adjective1} {noun2}.
One day, {name} {verb} a {animal} eating {food}.""",
            """In {city}, {name} met a {adjective1} {animal} who loved {food}.
They {verb} together and played {sport} with a {noun1}."""
        ]
        template = random.choice(templates)
        story = self.generate_story(template)
        self.display_story(story)

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.play_game()
        else:
            print("Goodbye!")

if __name__ == "__main__":
    game = MadLibsGame()
    game.play_game()