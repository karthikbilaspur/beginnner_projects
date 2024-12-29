import random
import json
import tkinter as tk
from tkinter import messagebox

class WordJumbleGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Word Jumble Game")
        self.categories = self.load_categories('word_list.json')
        self.score = 0
        self.current_category = 0
        self.current_word = 0
        self.display_category()

    def load_categories(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)['categories']

    def jumble_word(self, word):
        return ''.join(random.sample(word, len(word)))

    def display_category(self):
        category = self.categories[self.current_category]
        self.category_label = tk.Label(self.root, text=category['name'], font=('Arial', 24))
        self.category_label.pack()
        self.display_word(category)

    def display_word(self, category):
        word = category['words'][self.current_word]
        self.word_label = tk.Label(self.root, text=self.jumble_word(word['word']), font=('Arial', 24))
        self.word_label.pack()
        self.definition_label = tk.Label(self.root, text=f"Definition: {word['definition']}", font=('Arial', 18))
        self.definition_label.pack()
        self.answer_entry = tk.Entry(self.root, font=('Arial', 24))
        self.answer_entry.pack()
        self.submit_button = tk.Button(self.root, text="Submit", command=lambda: self.check_answer(category))
        self.submit_button.pack()
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}/{len(self.categories[self.current_category]['words'])}", font=('Arial', 18))
        self.score_label.pack()

    def check_answer(self, category):
        word = category['words'][self.current_word]
        user_answer = self.answer_entry.get()
        if user_answer.lower() == word['word'].lower():
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Incorrect", f"Correct answer: {word['word']}")
        self.current_word += 1
        if self.current_word < len(category['words']):
            self.word_label['text'] = self.jumble_word(category['words'][self.current_word]['word'])
            self.definition_label['text'] = f"Definition: {category['words'][self.current_word]['definition']}"
            self.answer_entry.delete(0, tk.END)
            self.score_label['text'] = f"Score: {self.score}/{len(category['words'])}"
        else:
            self.current_category += 1
            if self.current_category < len(self.categories):
                self.display_category()
            else:
                self.game_over()

    def game_over(self):
        self.category_label['text'] = "Game Over!"
        self.word_label['text'] = ""
        self.definition_label['text'] = ""
        self.answer_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        self.score_label['text'] = f"Final Score: {self.score}"

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = WordJumbleGame()
    game.run()