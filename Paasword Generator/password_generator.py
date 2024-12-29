import secrets
import string
import json
import os

class PasswordGenerator:
    def __init__(self):
        self.char_sets = {
            "letters": string.ascii_letters,
            "digits": string.digits,
            "punctuation": string.punctuation
        }

    def generate_password(self, length, use_uppercase, use_digits, use_punctuation):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += self.char_sets["letters"]
        if use_digits:
            characters += self.char_sets["digits"]
        if use_punctuation:
            characters += self.char_sets["punctuation"]

        password = []
        if use_uppercase:
            password.append(secrets.choice(self.char_sets["letters"]))
        if use_digits:
            password.append(secrets.choice(self.char_sets["digits"]))
        if use_punctuation:
            password.append(secrets.choice(self.char_sets["punctuation"]))

        for _ in range(length - len(password)):
            password.append(secrets.choice(characters))
        random.shuffle(password)
        return ''.join(password)

    def get_user_input(self):
        length = int(input("Enter password length (8-32): "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_punctuation = input("Include punctuation? (y/n): ").lower() == "y"
        return length, use_uppercase, use_digits, use_punctuation

    def save_password(self, password):
        with open("passwords.json", "a") as f:
            json.dump({"password": password}, f)
            f.write("\n")

def main():
    generator = PasswordGenerator()
    length, use_uppercase, use_digits, use_punctuation = generator.get_user_input()

    if 8 <= length <= 32:
        password = generator.generate_password(length, use_uppercase, use_digits, use_punctuation)
        print(f"Generated Password: {password}")
        save = input("Save password? (y/n): ").lower() == "y"
        if save:
            generator.save_password(password)
            print("Password saved to passwords.json")
    else:
        print("Invalid length")

if __name__ == "__main__":
    main()