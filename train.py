from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

client_id = "729675636971-etnd7b3qip2jv0ksof9eedpfel4dqkg3.apps.googleusercontent.com"
client_s = "KD6HkoZoyRVF3Dr_szAKGH3e"

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
     creds = None
     # The file token.pickle stores the user's access and refresh tokens, and is
     # created automatically when the authorization flow completes for the first
     # time.
     if os.path.exists('token.pickle'):
          with open('token.pickle', 'rb') as token:
               creds = pickle.load(token)
     # If there are no (valid) credentials available, let the user log in.
     if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
          else:
               flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
               creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open('token.pickle', 'wb') as token:
               pickle.dump(creds, token)

     service = build('drive', 'v3', credentials=creds)

     # file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
     # request = service.files().get_media(fileId=file_id)
     # fh = io.BytesIO()
     # downloader = MediaIoBaseDownload(fh, request)
     # done = False
     # while done is False:
     #      status, done = downloader.next_chunk()
     #      print ("Download %d%%." % int(status.progress() * 100))
     


if __name__ == '__main__':
    main()