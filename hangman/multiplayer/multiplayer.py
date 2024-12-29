import socket

class Multiplayer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self, host, port):
        self.socket.connect((host, port))

    def send_challenge(self, opponent_username):
        self.socket.send(f"challenge {opponent_username}".encode())

    def receive_challenge_response(self):
        return self.socket.recv(1024).decode()

    def play_multiplayer_game(self, opponent_username):
        # Implement multiplayer game logic
        pass

# Example usage
multiplayer = Multiplayer()
multiplayer.connect_to_server("localhost", 12345)
multiplayer.send_challenge("john")
response = multiplayer.receive_challenge_response()