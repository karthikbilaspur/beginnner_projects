import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser

class TextEditor:
    def __init__(self, root):
        self.text_area = tk.Text(root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.file_name = None
        self.create_menu(root)
        self.create_shortcuts(root)
        self.create_status_bar(root)

    def create_menu(self, root):
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        filemenu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        filemenu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        filemenu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")

        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        editmenu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        editmenu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        editmenu.add_command(label="Find", command=self.find_text, accelerator="Ctrl+F")
        editmenu.add_command(label="Replace", command=self.replace_text, accelerator="Ctrl+R")

        formatmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Format", menu=formatmenu)
        formatmenu.add_command(label="Font", command=self.change_font)
        formatmenu.add_command(label="Background Color", command=self.change_background_color)
        formatmenu.add_command(label="Text Color", command=self.change_text_color)

    def create_shortcuts(self, root):
        root.bind_all("<Control-n>", lambda event: self.new_file())
        root.bind_all("<Control-o>", lambda event: self.open_file())
        root.bind_all("<Control-s>", lambda event: self.save_file())
        root.bind_all("<Control-S>", lambda event: self.save_as_file())
        root.bind_all("<Control-q>", lambda event: root.quit())
        root.bind_all("<Control-x>", lambda event: self.cut_text())
        root.bind_all("<Control-c>", lambda event: self.copy_text())
        root.bind_all("<Control-v>", lambda event: self.paste_text())
        root.bind_all("<Control-f>", lambda event: self.find_text())
        root.bind_all("<Control-r>", lambda event: self.replace_text())

    def create_status_bar(self, root):
        self.status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_name = None
        self.status_bar.config(text="New file created")

    def open_file(self):
        self.file_name = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        if self.file_name:
            self.text_area.delete(1.0, tk.END)
            with open(self.file_name, "r") as file:
                self.text_area.insert(1.0, file.read())
            self.status_bar.config(text=f"Opened {self.file_name}")

    def save_file(self):
        if self.file_name is None:
            self.save_as_file()
        else:
            with open(self.file_name, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(text=f"Saved {self.file_name}")

    def save_as_file(self):
        self.file_name = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        if self.file_name:
            with open(self.file_name, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(text=f"Saved as {self.file_name}")

    def cut_text(self):
        root.clipboard_clear()
        root.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first", "sel.last")
        self.status_bar.config(text="Text cut")

    def copy_text(self):
        root.clipboard_clear()
        root.clipboard_append(self.text_area.selection_get())
        self.status_bar.config(text="Text copied")

    def paste_text(self):
        try:
            self.text_area.insert(tk.INSERT, root.clipboard_get())
            self.status_bar.config(text="Text pasted")
        except tk.TclError:
            pass

    def find_text(self):
        find_str = simpledialog.askstring("Find", "Enter text to find")
        if find_str:
            self.text_area.tag_remove('match', 1.0, tk.END)
            self.text_area.tag_add('match', 1.0, tk.END)
            self.text_area.tag_config('match', background="yellow")
            start_pos = 1.0
            while True:
                start_pos = self.text_area.search(find_str, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                lastidx = '%s+%dc' % (start_pos, len(find_str))
                self.text_area.tag_add('match', start_pos, lastidx)
                start_pos = lastidx
            self.status_bar.config(text=f"Found '{find_str}'")

    def replace_text(self):
        find_str = simpledialog.askstring("Replace", "Enter text to replace")
        replace_str = simpledialog.askstring("Replace", "Enter replacement text")
        if find_str and replace_str:
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_str, replace_str)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, new_content)
            self.status_bar.config(text=f"Replaced '{find_str}' with '{replace_str}'")

    def change_font(self):
        font_name = simpledialog.askstring("Font", "Enter font name")
        font_size = simpledialog.askinteger("Font", "Enter font size")
        if font_name and font_size:
            self.text_area.config(font=(font_name, font_size))
            self.status_bar.config(text=f"Font changed to {font_name} {font_size}")

    def change_background_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(bg=color)
            self.status_bar.config(text=f"Background color changed to {color}")

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)
            self.status_bar.config(text=f"Text color changed to {color}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Advanced Text Editor")
    text_editor = TextEditor(root)
    root.geometry("800x600")
    root.mainloop()