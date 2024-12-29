import random
import os

class MadLibs:
    def __init__(self):
        self.story_templates = {
            "beach": """
            Yesterday, I saw a {noun} walking along the shore.
            It was {adjective}ly {verb} to the sound of waves crashing against the sand.
            As I watched, the {noun} started {verb} with a pack of playful {plural_noun}.
            Together, they twirled and spun across the {place}.

            After working up an appetite, the {noun} and {plural_noun} took a break to enjoy slices of hot, cheesy {food}.
            It was a surreal yet wonderfully joyful scene – who knew {noun}s loved {food} parties at the {place}?
            """,
            "city": """
            I spotted a {noun} strolling through the bustling {place}.
            It was {adjective}ly {verb} past skyscrapers and busy streets.
            The {noun} danced with {plural_noun} friends, feeling carefree.
            Their laughter echoed through the {place}, filling hearts with joy.
            """,
        }
        self.word_categories = {
            "noun": ["book", "dog", "car", "phone"],
            "adjective": ["happy", "tall", "green", "vibrant"],
            "verb": ["dancing", "running", "jumping", "skipping"],
            "place": ["beach", "city", "park", "mountain"],
            "food": ["pizza", "ice cream", "burger", "sandwich"],
            "plural_noun": ["friends", "dogs", "cats", "birds"],
        }

    def get_user_input(self):
        """Collect user input"""
        inputs = {}
        for category in self.word_categories:
            while True:
                user_input = input(f"Enter a {category} ({', '.join(self.word_categories[category])}): ")
                if user_input in self.word_categories[category]:
                    inputs[category] = user_input
                    break
                else:
                    print("Invalid input. Please choose from the options.")
        return inputs

    def generate_random_word(self, category):
        """Generate random word"""
        return random.choice(self.word_categories[category])

    def generate_story(self, inputs, template_name):
        """Generate Mad Libs story"""
        template = self.story_templates[template_name]
        return template.format(**inputs)

    def save_story(self, story, filename="generated_story.txt"):
        """Save story to file"""
        with open(filename, "w") as file:
            file.write(story)
        print(f"Story saved to {os.path.abspath(filename)}")

    def play_game(self):
        """Play Mad Libs game"""
        print("Welcome to Mad Libs Game!")
        template_name = random.choice(list(self.story_templates.keys()))
        user_inputs = self.get_user_input()
        story = self.generate_story(user_inputs, template_name)
        print(f"\nGenerated {template_name.capitalize()} Story:")
        print(story)
        save_choice = input("\nSave story? (yes/no): ")
        if save_choice.lower() == "yes":
            self.save_story(story)
        self.play_again()

    def play_again(self):
        """Ask to play again"""
        choice = input("\nPlay again? (yes/no): ")
        if choice.lower() == "yes":
            self.play_game()

if __name__ == "__main__":
    game = MadLibs()
    game.play_game()