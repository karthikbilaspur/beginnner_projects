import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.directory = ""
        self.mapping = {}
        self.exclude = []

        # Create GUI widgets
        tk.Label(root, text="Directory:").grid(row=0, column=0)
        self.dir_entry = tk.Entry(root, width=50)
        self.dir_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.browse_directory).grid(row=0, column=2)

        tk.Label(root, text="Custom Mapping:").grid(row=1, column=0)
        self.map_entry = tk.Text(root, width=50, height=10)
        self.map_entry.grid(row=1, column=1)

        tk.Label(root, text="Exclude File Types:").grid(row=2, column=0)
        self.exclude_entry = tk.Entry(root, width=50)
        self.exclude_entry.grid(row=2, column=1)

        tk.Button(root, text="Organize", command=self.organize_files).grid(row=3, column=1)

    def browse_directory(self):
        self.directory = filedialog.askdirectory()
        self.dir_entry.delete(0, tk.END)
        self.dir_entry.insert(0, self.directory)

    def organize_files(self):
        # Parse custom mapping
        self.mapping = {}
        for line in self.map_entry.get("1.0", tk.END).splitlines():
            folder, extensions = line.split(":")
            self.mapping[folder.strip()] = [ext.strip() for ext in extensions.split(",")]

        # Parse exclude file types
        self.exclude = [ext.strip() for ext in self.exclude_entry.get().split(",")]

        # Organize files
        for root, dirs, files in os.walk(self.directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_extension = os.path.splitext(filename)[1].lower()
                if file_extension not in self.exclude:
                    for folder, extensions in self.mapping.items():
                        if file_extension in extensions:
                            destination_path = os.path.join(self.directory, folder, filename)
                            shutil.move(file_path, destination_path)
                            print(f"Moved {filename} to {folder}")
                            break

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizer(root)
    root.mainloop()