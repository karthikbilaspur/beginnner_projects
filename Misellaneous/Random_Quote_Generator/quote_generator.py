import json
import random
import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
import os

class QuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Quote Generator")
        self.categories = ["inspiration", "motivation", "humor"]
        self.quotes = {category: self.load_quotes(category) for category in self.categories}

        # GUI Components
        self.category_label = tk.Label(root, text="Category:")
        self.category_label.pack()
        self.category_option = tk.StringVar(root)
        self.category_option.set(self.categories[0])
        self.category_menu = tk.OptionMenu(root, self.category_option, *self.categories)
        self.category_menu.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search_quotes)
        self.search_button.pack()
        self.random_button = tk.Button(root, text="Random Quote", command=self.random_quote)
        self.random_button.pack()
        self.quote_label = tk.Label(root, text="", wraplength=400)
        self.quote_label.pack()
        self.share_button = tk.Button(root, text="Share on Twitter", command=self.share_quote)
        self.share_button.pack()
        self.save_button = tk.Button(root, text="Save Quote", command=self.save_quote)
        self.save_button.pack()
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

    def load_quotes(self, category):
        filename = f"{category}.json"
        with open(filename, 'r') as file:
            return json.load(file)

    def search_quotes(self):
        keyword = self.search_entry.get()
        category = self.category_option.get()
        quotes = self.quotes[category]
        matching_quotes = [quote for quote in quotes if keyword.lower() in quote['quote'].lower()]
        if matching_quotes:
            self.quote_label.config(text=f"\"{random.choice(matching_quotes)['quote']}\" - {random.choice(matching_quotes)['author']}")
        else:
            self.quote_label.config(text="No quotes found.")

    def random_quote(self):
        category = self.category_option.get()
        quotes = self.quotes[category]
        self.quote_label.config(text=f"\"{random.choice(quotes)['quote']}\" - {random.choice(quotes)['author']}")

    def share_quote(self):
        quote = self.quote_label.cget("text")
        twitter_url = f"https://twitter.com/intent/tweet?text={quote}"
        webbrowser.open(twitter_url)

    def save_quote(self):
        quote = self.quote_label.cget("text")
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, 'w') as file:
                file.write(quote)
            messagebox.showinfo("Quote Saved", "Quote saved successfully.")

def main():
    root = tk.Tk()
    quote_generator = QuoteGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()