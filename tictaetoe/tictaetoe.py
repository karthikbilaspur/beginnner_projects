import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import socket
import threading
import numpy as np
from tensorflow import keras

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()
        self.difficulty = tk.StringVar()
        self.difficulty.set("Easy")
        self.board_size = tk.StringVar()
        self.board_size.set("3x3")
        self.visual_theme = tk.StringVar()
        self.visual_theme.set("Classic")
        self.sound_effects = tk.BooleanVar()
        self.sound_effects.set(True)
        self.levels = 1000
        self.current_level = 1
        self.leaderboard = []

        # AI algorithms
        self.ai_minimax = MinimaxAI()
        self.ai_alpha_beta = AlphaBetaAI()

        # Machine learning model
        self.ml_model = keras.models.load_model('tic_tac_toe_model.h5')

        # Online leaderboard
        self.leaderboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.leaderboard_socket.connect(('localhost', 8080))

    def start_game(self):
        self.game_over = False
        self.board = [[' ' for _ in range(int(self.board_size.get().split('x')[1]))] for _ in range(int(self.board_size.get().split('x')[0]))]
        self.buttons = []
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[0])):
                button = tk.Button(self.window, command=lambda i=i, j=j: self.click(i, j), height=3, width=6)
                button.grid(row=i + 6, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, i, j):
        if self.game_over:
            return
        if self.board[i][j] == ' ':
            self.board[i][j] = "X"
            self.buttons[i][j].config(text="X")
            result = self.check_win()
            if result:
                self.game_over = True
                self.update_leaderboard()
                messagebox.showinfo("Game Over", f"Player {result} wins!")
            else:
                self.ai_move()

    def ai_move(self):
        if self.difficulty.get() == "Easy":
            move = self.ai_minimax.get_move(self.board)
        elif self.difficulty.get() == "Medium":
            move = self.ai_alpha_beta.get_move(self.board)
        elif self.difficulty.get() == "Hard":
            move = self.ml_model.predict(np.array(self.board))
        self.board[move[0]][move[1]] = "O"
        self.buttons[move[0]][move[1]].config(text="O")

    def check_win(self):
        # Check rows, columns and diagonals for wins
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        if ' ' not in [cell for row in self.board for cell in row]:
            return 'Tie'
        return False

    def update_leaderboard(self):
        self.leaderboard_socket.sendall(f"{self.player1_name.get()} {self.current_level}".encode())
        self.leaderboard = self.leaderboard_socket.recv(1024).decode().split(',')

    def run(self):
        self.window.mainloop()

class MinimaxAI:
    def get_move(self, board):
        best_score = float('-inf')
        best_move = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = self.minimax(board, 0, False)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_win(board):
            return -10 + depth if is_maximizing else 10 - depth
        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

class AlphaBetaAI:
    def get_move(self, board):
        best_score = float('-inf')
        best_move = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = self.alpha_beta(board, 0, float('-inf'), float('inf'), False)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def alpha_beta(self, board, depth, alpha, beta, is_maximizing):
        if self.check_win(board):
            return -10 + depth if is_maximizing else 10 - depth
        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.alpha_beta(board, depth + 1, alpha, beta, False)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.alpha_beta(board, depth + 1, alpha, beta, True)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score

if __name__ == "__main__":
    game = TicTacToe()
    game.run()