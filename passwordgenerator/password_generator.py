import random
import string

def generate_password_diceware(length=12):
    """
    Generates password using Diceware method.

    Args:
    length (int): The length of the password. Defaults to 12.

    Returns:
    str: The generated password.
    """
    words = ["apple", "banana", "cherry"]  # Example word list
    password = ' '.join(random.choice(words) for _ in range(length))
    return password


def generate_password_xkcd(length=12):
    """
    Generates password using XKCD method.

    Args:
    length (int): The length of the password. Defaults to 12.

    Returns:
    str: The generated password.
    """
    words = ["correct", "horse", "battery", "staple"]  # Example word list
    password = ' '.join(random.choice(words) for _ in range(length))
    return password