import hashlib
import hmac
import bcrypt
import argon2
import pyotp
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

class AdvancedEncryptionTool:
    def __init__(self):
        """
        Initialize the encryption tool.
        """
        pass

    # Hashing Algorithms
    def sha256_hash(self, message):
        return hashlib.sha256(message.encode()).hexdigest()

    def md5_hash(self, message):
        return hashlib.md5(message.encode()).hexdigest()

    # Digital Signatures
    def generate_rsa_keypair(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def rsa_sign(self, private_key, message):
        signature = private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()

    def rsa_verify(self, public_key, signature, message):
        try:
            public_key.verify(
                base64.b64decode(signature.encode()),
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Verification error: {e}")
            return False

    # Key Exchange Protocols
    def diffie_hellman_key_exchange(self, private_key, public_key):
        shared_key = private_key.exchange(public_key)
        return hashlib.sha256(shared_key).hexdigest()

    # Block Cipher Modes
    def aes_encrypt(self, message, key, mode):
        if mode == 'CBC':
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key.encode()), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
            return base64.b64encode(iv + encrypted_message).decode()
        elif mode == 'ECB':
            cipher = Cipher(algorithms.AES(key.encode()), modes.ECB(), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
            return base64.b64encode(encrypted_message).decode()
        elif mode == 'CFB':
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
            return base64.b64encode(iv + encrypted_message).decode()

    def aes_decrypt(self, encrypted_message, key, mode):
        encrypted_message = base64.b64decode(encrypted_message.encode())
        if mode == 'CBC':
            iv = encrypted_message[:16]
            encrypted_message = encrypted_message[16:]
            cipher = Cipher(algorithms.AES(key.encode()), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
            return decrypted_message.decode()
        elif mode == 'ECB':
            cipher = Cipher(algorithms.AES(key.encode()), modes.ECB(), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
            return decrypted_message.decode()
        elif mode == 'CFB':
            iv = encrypted_message[:16]
            encrypted_message = encrypted_message[16:]
            cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
            return decrypted_message.decode()

    # Randomized Encryption
    def randomized_encrypt(self, message):
        key = os.urandom(32)
        encrypted_message = self.aes_encrypt(message, key.hex(), 'CBC')
        return key.hex(), encrypted_message

    # Steganography
    def hide_message(self, image_path, message):
        # Hide message within image
        pass

    def reveal_message(self, image_path):
        # Reveal hidden message from image
        pass

    # Secure Password Storage
    def bcrypt_hash(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()

    def argon2_hash(self, password):
        hashed_password = argon2.hash(password.encode())
        return hashed_password.decode()

    # Two-Factor Authentication
    def generate_totp_secret(self):
        totp_secret = pyotp.random_base32()
        return totp_secret

    def verify_totp_token(self, totp_secret, token):
        totp = pyotp.TOTP(totp_secret)
        return totp.verify(token)


tool = AdvancedEncryptionTool()

# Hashing
message = "Hello, World!"
sha256_hash = tool.sha256_hash(message)
md5_hash = tool.md5_hash(message)
print(f"SHA-256 Hash: {sha256_hash}")
print(f"MD5 Hash: {md5_hash}")

# Digital Signatures
private_key, public_key = tool.generate_rsa_keypair()
signature = tool.rsa_sign(private_key, message)
print(f"RSA Signature: {signature}")
is_valid = tool.rsa_verify(public_key, signature, message)
print(f"Signature Validity: {is_valid}")

# Key Exchange
shared_key = tool.diffie_hellman_key_exchange(private_key, public_key)
print(f"Shared Key: {shared_key}")

# Block Cipher Modes
encrypted_message = tool.aes_encrypt(message, "secretkey", "CBC")
print(f"Encrypted Message (CBC): {encrypted_message}")
decrypted_message = tool.aes_decrypt(encrypted_message, "secretkey", "CBC")
print(f"Decrypted Message (CBC): {decrypted_message}")

# Randomized Encryption
key, encrypted_message = tool.randomized_encrypt(message)
print(f"Randomized Encryption Key: {key}")
print(f"Randomized Encrypted Message: {encrypted_message}")

# Secure Password Storage
bcrypt_hashed_password = tool.bcrypt_hash("password123")
argon2_hashed_password = tool.argon2_hash("password123")
print(f"Bcrypt Hashed Password: {bcrypt_hashed_password}")
print(f"Argon2 Hashed Password: {argon2_hashed_password}")

# Two-Factor Authentication
totp_secret = tool.generate_totp_secret()
token = "123456"  # Replace with actual TOTP token
is_valid = tool.verify_totp_token(totp_secret, token)
print(f"TOTP Token Validity: {is_valid}")
