# Import the GoogleCalendarAPI Class.
from google_calendar_v3 import GoogleCalendarAPI

# Define a token handler for use on token refresh.
def new_token_handler(token):
    # Do something with your token. Like stick it in a db.
    print ("A new token arrived: ")
    print (token)

# Enter in your various credentials here.
access_token = "<YOUR_ACCESS_TOKEN>"
refresh_token = "<YOUR_REFRESH_TOKEN>"
client_id = "<YOUR_CLIENT_ID>"
client_secret = "<YOUR_CLIENT_SECRET>"

# Create an instance of the Google Calendar API.
gapi = GoogleCalendarAPI(client_id=client_id, client_secret=client_secret,
             acc_token=access_token, ref_token=refresh_token, expires_in=-30,
             token_updater=new_token_handler)

# Do something with it.
r  = gapi.settings_list("dateFieldOrder")
print (t.text)