import tkinter as tk
import time

class HangmanAnimations:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def draw_base(self):
        self.canvas.create_line(50, 350, 350, 350)  # base
        self.canvas.create_line(200, 350, 200, 50)  # vertical line
        self.canvas.create_line(200, 50, 300, 50)  # horizontal line

    def animate_hangman(self, tries):
        self.draw_base()
        self.root.update()
        time.sleep(1)
        if tries == 5:
            self.canvas.create_oval(280, 50, 320, 90)  # head
        elif tries == 4:
            self.canvas.create_line(300, 90, 300, 190)  # body
        elif tries == 3:
            self.canvas.create_line(300, 120, 250, 150)  # left arm
        elif tries == 2:
            self.canvas.create_line(300, 120, 350, 150)  # right arm
        elif tries == 1:
            self.canvas.create_line(300, 190, 250, 220)  # left leg
        elif tries == 0:
            self.canvas.create_line(300, 190, 350, 220)  # right leg
        self.root.update()
        time.sleep(1)

    def display(self):
        self.root.mainloop()

# Example usage
animations = HangmanAnimations()
for i in range(5, -1, -1):
    animations.animate_hangman(i)
animations.display()