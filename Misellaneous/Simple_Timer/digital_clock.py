# digital_clock.py
import time
import tkinter as tk
from tkinter import messagebox

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.time_label = tk.Label(self.root, font=("Arial", 60), bg="black", fg="green")
        self.time_label.pack()
        self.alarm_label = tk.Label(self.root, text="", font=("Arial", 20))
        self.alarm_label.pack()
        self.alarm_set = False
        self.alarm_time = None
        self.create_menu()
        self.update_time()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        alarm_menu = tk.Menu(menubar, tearoff=0)
        alarm_menu.add_command(label="Set Alarm", command=self.set_alarm)
        menubar.add_cascade(label="Alarm", menu=alarm_menu)

    def set_alarm(self):
        alarm_window = tk.Toplevel(self.root)
        tk.Label(alarm_window, text="Enter alarm time (HH:MM:SS)").pack()
        self.alarm_entry = tk.Entry(alarm_window)
        self.alarm_entry.pack()
        tk.Button(alarm_window, text="Set", command=self.save_alarm).pack()

    def save_alarm(self):
        self.alarm_time = self.alarm_entry.get()
        try:
            hours, minutes, seconds = map(int, self.alarm_time.split(':'))
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                self.alarm_set = True
                self.alarm_label.config(text=f"Alarm set for {self.alarm_time}")
            else:
                messagebox.showerror("Invalid Time", "Enter valid time")
        except ValueError:
            messagebox.showerror("Invalid Format", "Use HH:MM:SS format")

    def update_time(self):
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        if self.alarm_set and self.alarm_time == f"{hours:02}:{minutes:02}:{seconds:02}":
            messagebox.showinfo("Alarm", "Wake up!")
            self.alarm_set = False
            self.alarm_label.config(text="")
        self.root.after(1000, self.update_time)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()