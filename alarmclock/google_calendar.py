import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GoogleCalendarEvents:
    def __init__(self):
        self.creds = Credentials.from_authorized_user_file('credentials.json')
        self.service = build('calendar', 'v3', credentials=self.creds)

    def get_events(self):
        # Retrieve Google Calendar events
        events_result = self.service.events().list(calendarId='primary').execute()
        events = events_result.get('items', [])
        event_details = []
        for event in events:
            event_summary = event['summary']
            event_start = event['start'].get('dateTime', event['start'].get('date'))
            event_end = event['end'].get('dateTime', event['end'].get('date'))
            event_details.append({
                'summary': event_summary,
                'start': event_start,
                'end': event_end
            })
        return event_details