import tkinter as tk
from gui import AlarmClockGUI
from google_calendar import GoogleCalendarEvents
from apple_calendar import AppleCalendarEvents
from microsoft_outlook import MicrosoftOutlookEvents
from sleep_quality import SleepQualityTracker
from reminder import Reminder
from event_integration import EventIntegration

class SmartAlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.gui = AlarmClockGUI(self.root)
        self.google_calendar = GoogleCalendarEvents()
        self.apple_calendar = AppleCalendarEvents()
        self.microsoft_outlook = MicrosoftOutlookEvents()
        self.sleep_quality_tracker = SleepQualityTracker()
        self.reminder = Reminder()
        self.event_integration = EventIntegration()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SmartAlarmClock()
    app.run()