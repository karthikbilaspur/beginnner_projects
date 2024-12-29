import threading
import time
from datetime import datetime

class Reminder:
    def __init__(self):
        self.reminder_time = None
        self.reminder_label = None

    def set_reminder(self, label, hour, minute):
        self.reminder_label = label
        self.reminder_time = datetime.now()
        self.reminder_time = self.reminder_time.replace(hour=hour, minute=minute, second=0)
        threading.Thread(target=self.remind_user).start()

    def remind_user(self):
        while True:
            current_time = datetime.now()
            if current_time >= self.reminder_time:
                print(f"Reminder: {self.reminder_label}")
                # Add notification implementation (e.g., beep, popup)
                break
            time.sleep(1)