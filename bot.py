from slack_bolt.app import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

SLACK_APP_TOKEN = "xapp-1-A08708SFQLC-8232954410581-1b3dbbd38814ffa5dff18a32e80f4272f5a13b94cef8942b3c26d6466d360115"
SLACK_BOT_TOKEN = "xoxb-8219170797511-8235807991762-fEYRndQ4i5dQOBH7W537cUnG"
SERVICE_ACCOUNT_FILE = "slack-chat-data-a17194b40b7d.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]


def write_in_google_spread_sheet(username,date,time,msg_text):
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(credentials)
    spreadsheet = client.open("Chat records")  
    sheet = spreadsheet.get_worksheet(0)
    sheet.append_row([username,date, time, msg_text])



app = App(token=SLACK_BOT_TOKEN)

@app.event("message")
def message(args):

    event_data = args.body.get("event", {})

    user_id = event_data.get("user")
    user_info = app.client.users_info(user=user_id)
    username = user_info.get("user", {}).get("real_name", "Unknown User")
    
    text = event_data.get("text")
    
    timestamp = event_data.get("ts")
    ts = float(timestamp)
    date = datetime.fromtimestamp(ts).strftime("%d/%B/%Y")
    time = datetime.fromtimestamp(ts).strftime("%I:%M:%S %p")
    
    print(f"Username: {username}")
    print(f"Text: {text}")
    print(f"Timestamp: {time}")
    write_in_google_spread_sheet(username,date,time,text)

handler = SocketModeHandler(app, SLACK_APP_TOKEN)
handler.start()
