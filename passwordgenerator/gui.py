import tkinter as tk
from password_generator import generate_password
from password_storage import store_password
from password_strength_estimator import display_password_strength, estimate_password_strength
class PasswordGeneratorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")

        # Input fields
        tk.Label(self.window, text="Password Length").grid(row=0)
        tk.Label(self.window, text="Include Uppercase").grid(row=1)
        tk.Label(self.window, text="Include Numbers").grid(row=2)
        tk.Label(self.window, text="Include Special Chars").grid(row=3)

        self.length_entry = tk.Entry(self.window)
        self.uppercase_var = tk.BooleanVar()
        self.numbers_var = tk.BooleanVar()
        self.special_chars_var = tk.BooleanVar()

        self.length_entry.grid(row=0, column=1)
        tk.Checkbutton(self.window, variable=self.uppercase_var).grid(row=1, column=1)
        tk.Checkbutton(self.window, variable=self.numbers_var).grid(row=2, column=1)
        tk.Checkbutton(self.window, variable=self.special_chars_var).grid(row=3, column=1)

        # Generate password button
        tk.Button(self.window, text="Generate Password", command=self.generate_password).grid(row=4)

        # Password display
        self.password_label = tk.Label(self.window, text="")
        self.password_label.grid(row=5)

        # Store password button
        tk.Button(self.window, text="Store Password", command=self.store_password).grid(row=6)

        # Password strength display
        self.strength_label = tk.Label(self.window, text="")
        self.strength_label.grid(row=7)

    def generate_password(self):
        length = int(self.length_entry.get())
        has_uppercase = self.uppercase_var.get()
        has_numbers = self.numbers_var.get()
        has_special_chars = self.special_chars_var.get()

        password = generate_password(length, has_uppercase, has_numbers, has_special_chars)
        self.password_label['text'] = f"Generated Password: {password}"
        display_password_strength(password)
        self.strength_label['text'] = f"Password Strength: {estimate_password_strength(password)}"

    def store_password(self):
        password = self.password_label['text'].split(": ")[1]
        store_password(password)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = PasswordGeneratorGUI()
    gui.run()