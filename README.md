# nertivia-selfbot
(WIP) A python library for creating selfbots/automating your Nertivia account.

### how to use
Download the nertivia_selfbot folder from the repo and paste it into your project's folder.  
Now make a python script in your projects folder outside the nertivia_selfbot folder.  
Enter your newly made python script and import nertivia_selfbot.  
If you're using an IDE with autocomplete it will make making a selfbot easier.  

### example
```python
import nertivia_selfbot

channel_id = 123
token = "TOKEN_HERE"

selfbot = nertivia_selfbot.Nertivia(token)
channel = selfbot.getChannel(channel_id)

channel.send("Hello World!")
```

### gateway example
```python
import nertivia_selfbot

token = "TOKEN_HERE"
prefix = "."

selfbot = nertivia_selfbot.gateway.Client()

@selfbot.event
def on_connect(event):
    print("Connected!")

@selfbot.event
def on_message(event):
    message = nertivia_selfbot.Message(event["message"]["messageID"], event["message"]["channelID"])
    print(message.content)

    if message.creator.id == selfbot.user.id:
        if message.content.startswith(prefix):
            command = message.content.split(" ")[0][1:]

            if command == "ping":
                message.reply("pong!")

selfbot.run(token)
```

### to do
- upload to pypi
- add command system
