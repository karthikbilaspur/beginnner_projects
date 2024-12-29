import string 
def get_user_input(prompt, default='y'):
    """
    Gets user input with a default value.

    Args:
    prompt (str): The prompt to display.
    default (str): The default value. Defaults to 'y'.

    Returns:
    bool: True if the user input is 'y', False otherwise.
    """
    user_input = input(prompt).lower()
    return user_input == 'y' or user_input == default


def validate_password_length(length):
    """
    Validates the password length.

    Args:
    length (int): The password length.

    Returns:
    bool: True if the length is valid, False otherwise.
    """
    return isinstance(length, int) and length >= 8


def estimate_password_strength(password):
    """
    Estimates password strength.

    Args:
    password (str): The password.

    Returns:
    str: Estimated password strength.
    """
    strength = 0
    if len(password) >= 12:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 0:
        return "Very Weak"
    elif strength <= 2:
        return "Weak"
    elif strength <= 3:
        return "Medium"
    else:
        return "Strong"