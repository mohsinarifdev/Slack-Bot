# Slack-Bot
Slack bot reads incoming messages from a channel. It is made to maintain all chat records of a group in google spread sheet with username, message text, date and time.

Here is how you can get this code in working 
1. Google Cloud Platform:
    a) Make a service account in google cloud Platform
    b) Add libraries google spread sheet and google drive
    c) Once added go to th credentials and make credentials and download .json file in to your project directory so python script can access the spread sheet
    d) Make a new spread sheet or use an existing one on google drive 

2. Slack API
    a) Visit slack API make an app from scratch 
    b) Add permissions of reading channel and user names
    c) Get the bot and app token from basic information window of app
    d) Replace these tokens with already used in bot.python or just simply

3. install the packages:
    a) Open the terminal create a vistual env or use existing one 
    b) Run pip install -r requirements.txt

4. Run Script:
    a) Open bot.py
    b) Replace APP_Token and Bot_Token with your own tokens from slack API
    c) Replace json with your file from google cloud platforms
    d) Run Bot.py


