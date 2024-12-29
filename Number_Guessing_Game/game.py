import random

def number_guessing_game():
    print("Welcome to the Enhanced Number Guessing Game!")
    
    # Ask for difficulty level
    difficulty_levels = {
        "easy": (1, 10, 3),
        "medium": (1, 50, 6),
        "hard": (1, 100, 8)
    }
    
    print("Choose your difficulty level:")
    for i, (level, _) in enumerate(difficulty_levels.items()):
        print(f"{i+1}. {level.capitalize()}")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        
        try:
            choice = int(choice)
            if 1 <= choice <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter 1, 2 or 3.")
    
    difficulty = list(difficulty_levels.keys())[choice - 1]
    min_num, max_num, max_attempts = difficulty_levels[difficulty]
    
    # Computer thinks of a number within chosen range
    number_to_guess = random.randint(min_num, max_num)
    
    # Initialize number of attempts
    attempts = 0
    
    print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess the number.\n")
    
    while attempts < max_attempts:
        # Get user's guess
        while True:
            user_guess = input(f"Attempt {attempts + 1}: ")
            
            try:
                user_guess = int(user_guess)
                if min_num <= user_guess <= max_num:
                    break
                else:
                    print(f"Please enter a number between {min_num} and {max_num}.")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        
        # Check if user's guess is correct
        attempts += 1
        if user_guess == number_to_guess:
            print(f"\nCongratulations! You've guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    else:
        print(f"\nGame over! The number was {number_to_guess}.")

def main():
    play_again = 'y'
    score = 0
    total_attempts = 0
    while play_again.lower() == 'y':
        number_guessing_game()
        play_again = input("\nPlay again? (y/n): ")
        play_again_choice = input("Do you want to update score? (y/n): ")
        if play_again_choice.lower() == 'y':
            outcome = input("Did you win? (y/n): ")
            if outcome.lower() == 'y':
                score += 1
            total_attempts += 1
            print(f"\nCurrent Score: {score}/{total_attempts}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()