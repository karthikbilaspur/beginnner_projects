import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dropbox import Dropbox

def upload_to_google_drive(password, file_name):
    """
    Uploads password to Google Drive.

    Args:
    password (str): The password.
    file_name (str): File name.
    """
    service = build('drive', 'v3')
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_name, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()


def upload_to_dropbox(password, file_name):
    """
    Uploads password to Dropbox.

    Args:
    password (str): The password.
    file_name (str): File name.
    """
    dbx = Dropbox('YOUR_ACCESS_TOKEN')
    dbx.files_upload(password.encode(), file_name)