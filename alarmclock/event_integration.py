from google_calendar import GoogleCalendarEvents
from apple_calendar import AppleCalendarEvents
from microsoft_outlook import MicrosoftOutlookEvents

class EventIntegration:
    def __init__(self):
        self.google_calendar = GoogleCalendarEvents()
        self.apple_calendar = AppleCalendarEvents()
        self.microsoft_outlook = MicrosoftOutlookEvents()

    def integrate_events(self, calendar_type):
        if calendar_type == "Google Calendar":
            return self.google_calendar.get_events()
        elif calendar_type == "Apple Calendar":
            return self.apple_calendar.get_events()
        elif calendar_type == "Microsoft Outlook":
            return self.microsoft_outlook.get_events()
        else:
            raise ValueError("Unsupported calendar type")