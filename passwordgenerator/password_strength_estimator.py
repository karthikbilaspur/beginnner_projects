from utils import estimate_password_strength
import string

def advanced_estimate_password_strength(password):
    """
    Estimates password strength using NIST guidelines.

    Args:
    password (str): The password.

    Returns:
    str: Estimated password strength.
    """
    strength = estimate_password_strength(password)
    if len(password) >= 20 and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in string.punctuation for char in password):
        strength = "Very Strong"
    return strength