import random
import json

class JokeGenerator:
    def __init__(self, joke_file='jokes.json'):
        self.joke_file = joke_file
        self.load_jokes()
    def load_jokes(self):
        try:
            with open(self.joke_file, 'r') as file:
                self.jokes = json.load(file)
        except FileNotFoundError:
            self.jokes = []
    def save_jokes(self):
        with open(self.joke_file, 'w') as file:
            json.dump(self.jokes, file, indent=4)
    def get_random_joke(self):
        return random.choice(self.jokes)
    def display_joke(self, joke):
        print(f"Category: {joke['category']}\nSetup: {joke['setup']}\nPunchline: {joke['punchline']}\n")
    def generate_joke(self):
        joke = self.get_random_joke()
        self.display_joke(joke)
        self.ask_user()
    def ask_user(self):
        choice = input("Generate another joke? (yes/no/category/add/exit): ")
        if choice.lower() == "yes":
            self.generate_joke()
        elif choice.lower() == "category":
            self.display_categories()
            category_choice = input("Enter category: ")
            self.generate_category_joke(category_choice)
        elif choice.lower() == "add":
            self.add_joke()
        elif choice.lower() == "exit":
            self.save_jokes()
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            self.ask_user()
    def display_categories(self):
        categories = set(joke['category'] for joke in self.jokes)
        print("Available categories:")
        for category in categories:
            print(category)
    def generate_category_joke(self, category):
        category_jokes = [joke for joke in self.jokes if joke['category'] == category]
        if category_jokes:
            joke = random.choice(category_jokes)
            self.display_joke(joke)
            self.ask_user()
        else:
            print("No jokes in this category.")
    def add_joke(self):
        category = input("Enter category: ")
        setup = input("Enter joke setup: ")
        punchline = input("Enter joke punchline: ")
        self.jokes.append({"category": category, "setup": setup, "punchline": punchline})
        print("Joke added successfully!")
if __name__ == "__main__":
    joke_generator = JokeGenerator()
    joke_generator.generate_joke()