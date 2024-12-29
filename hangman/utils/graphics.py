import tkinter as tk

class HangmanGraphics:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def draw_base(self):
        self.canvas.create_line(50, 350, 350, 350)  # base
        self.canvas.create_line(200, 350, 200, 50)  # vertical line
        self.canvas.create_line(200, 50, 300, 50)  # horizontal line
        self.canvas.create_oval(280, 50, 320, 90)  # head

    def draw_head(self):
        self.canvas.create_oval(280, 50, 320, 90)  # head

    def draw_body(self):
        self.canvas.create_line(300, 90, 300, 190)  # body

    def draw_arm1(self):
        self.canvas.create_line(300, 120, 250, 150)  # left arm

    def draw_arm2(self):
        self.canvas.create_line(300, 120, 350, 150)  # right arm

    def draw_leg1(self):
        self.canvas.create_line(300, 190, 250, 220)  # left leg

    def draw_leg2(self):
        self.canvas.create_line(300, 190, 350, 220)  # right leg

    def draw_hangman(self, tries):
        self.draw_base()
        if tries == 5:
            self.draw_head()
        elif tries == 4:
            self.draw_head()
            self.draw_body()
        elif tries == 3:
            self.draw_head()
            self.draw_body()
            self.draw_arm1()
        elif tries == 2:
            self.draw_head()
            self.draw_body()
            self.draw_arm1()
            self.draw_arm2()
        elif tries == 1:
            self.draw_head()
            self.draw_body()
            self.draw_arm1()
            self.draw_arm2()
            self.draw_leg1()
        elif tries == 0:
            self.draw_head()
            self.draw_body()
            self.draw_arm1()
            self.draw_arm2()
            self.draw_leg1()
            self.draw_leg2()

    def display(self):
        self.root.mainloop()

# Example usage
graphics = HangmanGraphics()
graphics.draw_hangman(5)
graphics.display()