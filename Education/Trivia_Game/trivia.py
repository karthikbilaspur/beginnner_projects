import random
import json

class TriviaGame:
    def __init__(self, filename='trivia_questions.json'):
        self.filename = filename
        self.questions = self.load_questions()
        self.score = 0
        self.question_index = 0

    def load_questions(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_questions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.questions, file, indent=4)

    def display_question(self):
        question = self.questions[self.question_index]
        print(f"\nCategory: {question['category']}\nQuestion {self.question_index + 1}: {question['question']}")
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self):
        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): ")) - 1
                if 0 <= user_answer <= 3:
                    return user_answer
                else:
                    print("Invalid answer. Please enter 1-4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, user_answer):
        question = self.questions[self.question_index]
        if user_answer == question["answer"]:
            print("Correct answer!")
            self.score += 1
        else:
            print(f"Incorrect answer. Correct answer: {question['options'][question['answer']]}")

    def play_game(self):
        random.shuffle(self.questions)
        while self.question_index < len(self.questions):
            self.display_question()
            user_answer = self.get_user_answer()
            self.check_answer(user_answer)
            self.question_index += 1
        self.display_results()

    def display_results(self):
        print(f"\nGame over! Your final score is {self.score}/{len(self.questions)}")
        if self.score >= len(self.questions) * 0.7:
            print("Excellent!")
        elif self.score >= len(self.questions) * 0.4:
            print("Good job!")
        else:
            print("Better luck next time!")

    def add_question(self):
        category = input("Enter category: ")
        question = input("Enter question: ")
        options = []
        for i in range(4):
            options.append(input(f"Enter option {i+1}: "))
        answer = int(input("Enter correct answer (1-4): ")) - 1
        self.questions.append({"category": category, "question": question, "options": options, "answer": answer})
        self.save_questions()
        print("Question added successfully!")


def main():
    game = TriviaGame()
    while True:
        print("\n1. Play Game")
        print("2. Add Question")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            game.play_game()
        elif choice == "2":
            game.add_question()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()