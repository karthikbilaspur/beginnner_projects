import socket
import threading

class ChatClient:
    def __init__(self, host='localhost', port=5500):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        self.client_socket.connect((self.host, self.port))
        nickname = input("Enter nickname: ")
        self.client_socket.sendall(nickname.encode())
        print(f"Connected to {self.host}:{self.port}")

        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.start()

        while True:
            message = input()
            if message == "/exit":
                self.client_socket.sendall(message.encode())
                break
            elif message.startswith("/private"):
                self.client_socket.sendall(message.encode())
            elif message.startswith("/ban"):
                self.client_socket.sendall(message.encode())
            else:
                self.client_socket.sendall(message.encode())

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message == "Banned":
                    print("You are banned!")
                    break
                print(message)
            except Exception as e:
                print(f"Error: {e}")
                break
        self.client_socket.close()

if __name__ == "__main__":
    client = ChatClient()
    client.start_client()