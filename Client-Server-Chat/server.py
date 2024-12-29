import socket
import threading
import datetime
import json

class ChatServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicknames = []
        self.banned_nicknames = []

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connected to {client_address}")

            nickname = client_socket.recv(1024).decode()
            if nickname in self.banned_nicknames:
                client_socket.sendall("Banned".encode())
                client_socket.close()
                continue

            self.nicknames.append(nickname)
            self.clients.append(client_socket)
            print(f"Client {nickname} connected")

            self.broadcast(f"{nickname} joined the chat!".encode())

            client_handler = threading.Thread(
                target=self.handle_client,
                args=(client_socket, nickname)
            )
            client_handler.start()

    def handle_client(self, client_socket, nickname):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message == "/exit":
                    break
                elif message.startswith("/private"):
                    self.private_message(client_socket, nickname, message)
                elif message.startswith("/ban"):
                    self.ban_nickname(client_socket, nickname, message)
                else:
                    self.broadcast(f"{nickname}: {message}".encode())
                    self.log_message(nickname, message)
            except Exception as e:
                print(f"Error: {e}")
                break
        self.clients.remove(client_socket)
        self.nicknames.remove(nickname)
        client_socket.close()
        self.broadcast(f"{nickname} left the chat!".encode())

    def broadcast(self, message):
        for client in self.clients:
            client.sendall(message)

    def private_message(self, sender_socket, sender_nickname, message):
        recipient_nickname = message.split(" ")[1]
        recipient_socket = self.clients[self.nicknames.index(recipient_nickname)]
        recipient_socket.sendall(f"{sender_nickname} (private): {message.split(' ', 2)[2]}".encode())

    def ban_nickname(self, sender_socket, sender_nickname, message):
        banned_nickname = message.split(" ")[1]
        self.banned_nicknames.append(banned_nickname)
        self.broadcast(f"{banned_nickname} has been banned!".encode())
        if banned_nickname in self.nicknames:
            index = self.nicknames.index(banned_nickname)
            self.clients[index].close()
            self.clients.pop(index)
            self.nicknames.pop(index)

    def log_message(self, nickname, message):
        with open("chat_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} {nickname}: {message}\n")

if __name__ == "__main__":
    server = ChatServer()
    server.start_server()