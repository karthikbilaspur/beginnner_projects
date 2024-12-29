import requests
import msal

class MicrosoftOutlookEvents:
    def __init__(self):
        client_id = 'your_client_id'
        client_secret = 'your_client_secret'
        tenant_id = 'your_tenant_id'
        authority = f'https://login.microsoftonline.com/{tenant_id}'
        scope = ['https://graph.microsoft.com/.default']

        # Get access token
        app = msal.ConfidentialClientApplication(
            client_id=client_id,
            client_credential=client_secret,
            authority=authority
        )
        result = app.acquire_token_silent(scopes=scope, account=None)
        if not result:
            result = app.acquire_token_for_client(scopes=scope)

        self.headers = {'Authorization': f'Bearer {result["access_token"]}'}

    def get_events(self):
        # Retrieve Microsoft Outlook events using Microsoft Graph API
        response = requests.get('https://graph.microsoft.com/v1.0/me/events', headers=self.headers)
        event_details = []
        for event in response.json()['value']:
            event_summary = event['subject']
            event_start = event['start']['dateTime']
            event_end = event['end']['dateTime']
            event_details.append({
                'summary': event_summary,
                'start': event_start,
                'end': event_end
            })
        return event_details