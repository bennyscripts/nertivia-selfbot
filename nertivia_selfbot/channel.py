import requests

from .message import Message
from .extra import Extra
from .embed import Embed
from .user import User

class Channel:
    def __init__(self, id, name="", serverId=""):
        if name == "" or serverId == "":
            response = requests.get(
                f"https://nertivia.net/api/channels/{id}",
                headers={"authorization": Extra.getauthtoken()}
            )

            self.id = response.json()["channelID"]
            self.name = response.json()["name"]
            self.serverId = response.json()["server_id"]
        
        else:
            self.id = id
            self.name = name
            self.serverId = serverId

    def send(self, content, embed: Embed = None):
        body={"message": content}
        if embed != None:
            body["htmlEmbed"] = embed.json

        response = requests.post(
            f"https://nertivia.net/api/messages/channels/{self.id}",
            headers={"authorization": Extra.getauthtoken()},
            json=body
        )

        return Message(response.json()["messageCreated"]["messageID"], self.id)

    def edit(self, name):
        response = requests.patch(
            f"https://nertivia.net/api/servers/{self.serverId}/channels/{self.id}",
            headers={"authorization": Extra.getauthtoken()},
            json={
                "name": name
            }
        )

        self.name = name

        return response.json()

    def getMessages(self, amount: int = 1):
        messages = []
        index = 0
        response = requests.get(
            f"https://nertivia.net/api/messages/channels/{self.id}",
            headers={"authorization": Extra.getauthtoken()}
        )

        for item in response.json()["messages"]:
            index += 1
            try:
                author = User(item["creator"]["id"], item["creator"]["username"], item["creator"]["tag"], item["creator"]["avatar"])
                message = Message(item["messageID"], self.id, author, item["message"], item["created"])
                messages.append(message)
            except:
                pass

            if index == amount:
                break
        
        return messages