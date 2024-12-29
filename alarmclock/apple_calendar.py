from icalendar import Calendar

class AppleCalendarEvents:
    def __init__(self):
        pass

    def get_events(self):
        # Load Apple Calendar .ics file
        with open('apple_calendar.ics', 'rb') as f:
            cal = Calendar.from_ical(f.read())

        # Extract event details
        event_details = []
        for component in cal.walk('vevent'):
            event_summary = component.get('summary').to_ical().decode('utf-8')
            event_start = component.get('dtstart').dt
            event_end = component.get('dtend').dt
            event_details.append({
                'summary': event_summary,
                'start': event_start.strftime('%Y-%m-%d %H:%M'),
                'end': event_end.strftime('%Y-%m-%d %H:%M')
            })
        return event_details