import hashlib
import getpass

def store_password(password):
    """
    Stores the password securely.

    Args:
    password (str): The password.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("stored_passwords.txt", "a") as file:
        file.write(hashed_password + "\n")


def verify_stored_password(password):
    """
    Verifies a stored password.

    Args:
    password (str): The password.

    Returns:
    bool: True if verified, False otherwise.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("stored_passwords.txt", "r") as file:
        stored_passwords = file.readlines()
    return hashed_password + "\n" in stored_passwords