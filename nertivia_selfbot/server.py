import requests

from .channel import Channel
from .user import User
from .extra import Extra

class Server:
    def __init__(self, id, name="", avatar="", defaultChannelId="", created="", banner=""):
        if name == "" or avatar == "" or defaultChannelId == "" or created == "" or banner == "":
            response = requests.get(
                f"https://nertivia.net/api/servers/{id}",
                headers={"authorization": Extra.getauthtoken()}
            )

            self.id = response.json()["server_id"]
            self.name = response.json()["name"]
            self.avatar = response.json()["avatar"]
            self.defaultChannel = Channel(response.json()["default_channel_id"])
            self.created = response.json()["created"]
            # self.banner = response.json()["banner"]

        else:
            self.id = id
            self.name = name
            self.avatar = avatar
            self.defaultChannel = Channel(defaultChannelId)
            self.created = created
            # self.banner = banner

    def edit(self, name):
        response = requests.patch(
            f"https://nertivia.net/api/servers/{self.id}",
            headers={"authorization": Extra.getauthtoken()},
            json={
                "name": name
            }
        )

        self.name = response.json()["name"]
        return response.json()

    def delete(self):
        response = requests.delete(
            f"https://nertivia.net/api/servers/{self.id}",
            headers={"authorization": Extra.getauthtoken()}
        )

        return response.json()

    def getBans(self):
        response = requests.get(
            f"https://nertivia.net/api/servers/{self.id}/bans",
            headers={"authorization": Extra.getauthtoken()}
        )

        if "missing permission" not in response.text.lower():
            bans = []

            for user in response.json():
                user = user["user"]
                user2 = User(user["id"])
                bans.append(user2)

            return bans
        
        else:
            return "Incorrect permissions."

    def banMember(self, user: User):
        userId = user.id
        response = requests.put(
            f"https://nertivia.net/api/servers/{self.id}/bans/{userId}",
            headers={"authorization": Extra.getauthtoken()}
        )

        return response.json()

    def kickMember(self, user: User):
        userId = user.id
        response = requests.delete(
            f"https://nertivia.net/api/servers/{self.id}/members/{userId}",
            headers={"authorization": Extra.getauthtoken()}
        )

        return response.json()

    def unbanMember(self, user: User):
        userId = user.id
        response = requests.delete(
            f"https://nertivia.net/api/servers/{self.id}/bans/{userId}",
            headers={"authorization": Extra.getauthtoken()}
        )

        return response.json()