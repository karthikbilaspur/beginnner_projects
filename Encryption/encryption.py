import getpass
import hashlib
import json
import os

class Encryptor:
    def __init__(self):
        self.key = None
        self.password = None

    def generate_key(self, password):
        """Generates encryption key from password"""
        self.key = int(hashlib.sha256(password.encode()).hexdigest(), 16) % 26
        return self.key

    def encrypt(self, plain_text):
        """Encrypts plain text using Caesar Cipher"""
        cipher_text = ""
        for char in plain_text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                cipher_text += chr((ord(char) - ascii_offset + self.key) % 26 + ascii_offset)
            else:
                cipher_text += char
        return cipher_text

    def decrypt(self, cipher_text):
        """Decrypts cipher text using Caesar Cipher"""
        plain_text = ""
        for char in cipher_text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                plain_text += chr((ord(char) - ascii_offset - self.key) % 26 + ascii_offset)
            else:
                plain_text += char
        return plain_text

    def save_key(self):
        """Saves key to file"""
        with open("key.json", "w") as f:
            json.dump({"key": self.key, "password": self.password}, f)

    def load_key(self):
        """Loads key from file"""
        if os.path.exists("key.json"):
            with open("key.json", "r") as f:
                data = json.load(f)
                self.key = data["key"]
                self.password = data["password"]
                return True
        return False

def main():
    encryptor = Encryptor()
    
    if encryptor.load_key():
        print("Loaded existing key")
    else:
        password = getpass.getpass("Enter password: ")
        encryptor.password = password
        encryptor.generate_key(password)
        encryptor.save_key()
        print("Key generated and saved")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            plain_text = input("Enter text to encrypt: ")
            cipher_text = encryptor.encrypt(plain_text)
            print(f"Encrypted: {cipher_text}")
        elif choice == "2":
            cipher_text = input("Enter text to decrypt: ")
            plain_text = encryptor.decrypt(cipher_text)
            print(f"Decrypted: {plain_text}")
        elif choice == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()