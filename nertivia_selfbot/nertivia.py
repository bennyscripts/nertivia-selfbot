import requests

from .channel import Channel
from .server import Server
from .user import User
from .bot import Bot
from .extra import Extra

class Nertivia:
    def __init__(self, token):
        global __token
        response = requests.get("https://nertivia.net/api/user", headers={"Authorization": token})
        self.token = token
        self.id = response.json()["user"]["id"]
        self.avatar = response.json()["user"]["avatar"]
        self.banner = response.json()["user"]["banner"]
        self.username = response.json()["user"]["username"]
        self.tag = response.json()["user"]["tag"]
        self.created = response.json()["user"]["created"]

        Extra.setauthtoken(self.token)

    def getServer(self, id):
        return Server(id)

    def getChannel(self, id):
        return Channel(id)

    def getUser(self, id):
        return User(id)

    def setStatus(self, status):
        response = requests.post(
            "https://nertivia.net/api/settings/status",
            headers={"Authorization": self.token, "content-type": "application/json"},
            json={"status": status}
        )

        return response.json()

    def setCustomStatus(self, text):
        response = requests.post(
            "https://nertivia.net/api/settings/custom-status",
            headers={"Authorization": self.token, "content-type": "application/json"},
            json={"custom_status": text}
        )

        return response.json()

    def getBots(self):
        response = requests.get(
            "https://nertivia.net/api/bots",
            headers={"Authorization": self.token}
        )

        bots = []

        for bot in response.json():
            bot2 = Bot(bot["id"])
            bots.append(bot2)

        return bots

    def createBot(self):
        response = requests.post(
            "https://nertivia.net/api/bots",
            headers={"Authorization": self.token, "content-type": "application/json"}
        )

        return Bot(response.json()["id"])

    def getBot(self, id):
        response = requests.get(
            "https://nertivia.net/api/bots/" + str(id),
            headers={"Authorization": self.token}
        )

        bot = Bot(response.json()["id"], response.json()["username"], response.json()["tag"], response.json()["avatar"], response.json()["botCommands"])
        return bot

    def deleteBot(self, id):
        response = requests.delete(
            "https://nertivia.net/api/bots/" + str(id),
            headers={"Authorization": self.token}
        )

        return response.json()

    