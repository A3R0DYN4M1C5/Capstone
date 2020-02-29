from __future__ import print_function
import tkinter as tk
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request




# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

HEIGHT = 700
WIDTH = 800
root = tk.Tk()

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
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

result = service.calendarList().list().execute()

calendar_id = result['items'][0]['id']

result = service.events().list(calendarId=calendar_id).execute()

now = datetime.datetime.utcnow().isoformat() + 'Z'

events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
events = events_result.get('items', [])


if not events:
    print('No upcoming events found.')

for event in events:
    datetest = event['start'].get('dateTime', event['start'].get('date'))
    justdate = datetest.split("T")
    print(justdate[0])
    start = event['start'].get('dateTime', event['start'].get('date'))
#    print(start, event['summary'])

    message = tk.Message(root, text=start + event['summary'])
    message.pack()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.grid_location(0, 0)


root.mainloop()

       # print(start, event['summary'])

if __name__ == '__main__':
    main()

