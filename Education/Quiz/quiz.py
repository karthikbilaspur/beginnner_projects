import random

# Dictionary with questions, options, and answers
quiz_data = {
    "What is the capital of India?": {
        "A": "Mumbai",
        "B": "New Delhi",
        "C": "Kolkata",
        "D": "Chennai",
        "Answer": "B",
        "Explanation": "New Delhi is the capital of India since 1911."
    },
    "Who is the founder of Microsoft?": {
        "A": "Bill Gates",
        "B": "Steve Jobs",
        "C": "Mark Zuckerberg",
        "D": "Larry Page",
        "Answer": "A",
        "Explanation": "Bill Gates co-founded Microsoft in 1975."
    },
    "What is the largest planet in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "Answer": "C",
        "Explanation": "Jupiter is the largest planet, with a diameter of approximately 142,984 km."
    }
}

def display_quiz():
    print("Quiz Menu:")
    print("1. Start Quiz")
    print("2. View Questions")
    print("3. Add Question")
    print("4. Exit")

def start_quiz():
    score = 0
    questions = list(quiz_data.keys())
    random.shuffle(questions)
    for question in questions:
        options = quiz_data[question]
        print(f"\nQuestion: {question}")
        for option, value in options.items():
            if option != "Answer" and option != "Explanation":
                print(f"{option}: {value}")
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == options["Answer"]:
            print("Correct answer!")
            score += 1
        else:
            print(f"Incorrect answer. The correct answer is {options['Answer']}.")
            print(f"Explanation: {options['Explanation']}")
    print(f"\nQuiz completed! Your final score is {score}/{len(quiz_data)}")

def view_questions():
    print("\nQuiz Questions:")
    for i, question in enumerate(quiz_data.keys(), start=1):
        print(f"{i}. {question}")
def add_question():
    question = input("Enter your question: ")
    options = {}
    for option in ["A", "B", "C", "D"]:
        options[option] = input(f"Enter option {option}: ")
    answer = input("Enter the correct answer (A/B/C/D): ").upper()
    explanation = input("Enter the explanation: ")
    quiz_data[question] = {**options, "Answer": answer, "Explanation": explanation}
    print("Question added successfully!")
def main():
    while True:
        display_quiz()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            start_quiz()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            add_question()
        elif choice == "4":
            print("Exiting quiz. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()