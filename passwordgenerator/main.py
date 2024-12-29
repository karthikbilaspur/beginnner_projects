from password_generator import generate_password
from utils import get_user_input, validate_password_length
from password_storage import store_password, verify_stored_password
from password_strength_estimator import display_password_strength

def main():
    while True:
        length = int(input("Enter password length (min 8): "))
        if validate_password_length(length):
            break
        print("Invalid length. Please enter a value greater than or equal to 8.")

    has_uppercase = get_user_input("Include uppercase letters? (y/n): ")
    has_numbers = get_user_input("Include numbers? (y/n): ")
    has_special_chars = get_user_input("Include special characters? (y/n): ")

    password = generate_password(length, has_uppercase, has_numbers, has_special_chars)
    print(f"Generated Password: {password}")

    display_password_strength(password)

    store = get_user_input("Store password? (y/n): ")
    if store:
        store_password(password)
        print("Password stored successfully.")

    verify = get_user_input("Verify stored password? (y/n): ")
    if verify:
        if verify_stored_password(password):
            print("Password verified successfully.")
        else:
            print("Password verification failed.")


if __name__ == "__main__":
    main()