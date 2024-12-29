import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
import subprocess

def list_files_and_directories(path, recursive=False, hidden=False, sort_by='name', filter_extension=''):
    # Existing listing function

def gui():
    root = tk.Tk()
    root.title("File Explorer")

    # Directory path entry
    path_label = tk.Label(root, text="Directory Path:")
    path_label.pack()
    path_entry = tk.Entry(root, width=50)
    path_entry.pack()

    # Clipboard import button
    def import_from_clipboard():
        path_entry.delete(0, tk.END)
        path_entry.insert(0, pyperclip.paste())

    clipboard_button = tk.Button(root, text="Import from Clipboard", command=import_from_clipboard)
    clipboard_button.pack()

    # Browse directory button
    def browse_directory():
        path = filedialog.askdirectory()
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)

    browse_button = tk.Button(root, text="Browse Directory", command=browse_directory)
    browse_button.pack()

    # Multiple directory paths entry
    multiple_paths_label = tk.Label(root, text="Additional Directory Paths (comma-separated):")
    multiple_paths_label.pack()
    multiple_paths_entry = tk.Entry(root, width=50)
    multiple_paths_entry.pack()

    # Recursive, hidden, sort and filter options
    recursive_var = tk.BooleanVar()
    hidden_var = tk.BooleanVar()
    sort_by_var = tk.StringVar()
    filter_extension_var = tk.StringVar()

    recursive_checkbox = tk.Checkbutton(root, text="Recursive", variable=recursive_var)
    recursive_checkbox.pack()
    hidden_checkbox = tk.Checkbutton(root, text="Hidden Files", variable=hidden_var)
    hidden_checkbox.pack()

    sort_by_option = tk.OptionMenu(root, sort_by_var, 'name', 'size', 'modified')
    sort_by_option.pack()
    filter_extension_entry = tk.Entry(root, width=20)
    filter_extension_entry.pack()

    # List button
    def list_files():
        path = path_entry.get()
        multiple_paths = multiple_paths_entry.get().split(',')
        recursive = recursive_var.get()
        hidden = hidden_var.get()
        sort_by = sort_by_var.get()
        filter_extension = filter_extension_entry.get()

        for p in [path] + multiple_paths:
            list_files_and_directories(p, recursive, hidden, sort_by, filter_extension)

    list_button = tk.Button(root, text="List Files", command=list_files)
    list_button.pack()

    # Integration buttons
    def open_in_file_explorer():
        path = path_entry.get()
        subprocess.run(f'explorer "{path}"', shell=True)

    open_button = tk.Button(root, text="Open in File Explorer", command=open_in_file_explorer)
    open_button.pack()

    def copy_to_clipboard():
        pyperclip.copy(path_entry.get())

    copy_button = tk.Button(root, text="Copy Path to Clipboard", command=copy_to_clipboard)
    copy_button.pack()

    root.mainloop()


if __name__ == "__main__":
    gui()