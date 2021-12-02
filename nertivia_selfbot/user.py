import requests

from .embed import Embed
from .extra import Extra
from .dmchannel import DMChannel

class User:
    def __init__(self, id, username="", tag="", avatar="", banner="", created="", blocked=""):
        if username == "" or tag == "" or avatar == "":
            response = requests.get(f"https://nertivia.net/api/user/{id}", headers={"Authorization": Extra.getauthtoken()})
            self.id = response.json()["user"]["id"]
            self.avatar = response.json()["user"]["avatar"]
            try:
                self.banner = response.json()["user"]["banner"]
            except:
                pass
            self.username = response.json()["user"]["username"]
            self.tag = response.json()["user"]["tag"]
            try:
                self.created = response.json()["user"]["created"]
            except:
                pass
            try:
                self.blocked = response.json()["isBlocked"]
            except:
                pass
        else:
            self.id = id
            self.avatar = avatar
            self.banner = banner
            self.username = username
            self.tag = tag
            self.created = created
            self.blocked = blocked
        self.avatar_url = f"https://media.nertivia.net/{self.avatar}"

    def __str__(self):
        return f"{self.username}:{self.tag}"
    
    def __repr__(self):
        return f"{self.username}:{self.tag}"
    
    def sendFriendRequest(self):
        response = requests.post(
            "https://nertivia.net/api/user/relationship",
            headers={
                "Authorization": Extra.getauthtoken(),
                "Content-Type": "application/json"
            },
            json={
                "username": self.username,
                "tag": self.tag
            }
        )

        return response.json()

    def acceptFriendRequest(self):
        response = requests.put(
            "https://nertivia.net/api/user/relationship",
            headers={
                "Authorization": Extra.getauthtoken(),
                "Content-Type": "application/json"
            },
            json={
                "id": self.id
            }
        )
        
        return response.json()

    def declineFriendRequest(self):
        response = requests.delete(
            "https://nertivia.net/api/user/relationship",
            headers={
                "Authorization": Extra.getauthtoken(),
                "Content-Type": "application/json"
            },
            json={
                "id": self.id
            }
        )

        return response.json()

    def block(self):
        response = requests.post(
            "https://nertivia.net/api/user/block",
            headers={
                "Authorization": Extra.getauthtoken(),
                "Content-Type": "application/json"
            },
            json={
                "id": self.id
            }
        )

        return response.json()

    def unblock(self):
        response = requests.delete(
            "https://nertivia.net/api/user/block",
            headers={
                "Authorization": Extra.getauthtoken(),
                "Content-Type": "application/json"
            },
            json={
                "id": self.id
            }
        )

        return response.json()

    def dm(self, message, embed: Embed = None):
        response = requests.post(
            f"https://nertivia.net/api/channels/{self.id}",
            headers={
                "Authorization": Extra.getauthtoken(),
                "Content-Type": "application/json"
            }
        )

        dmchannel = DMChannel(response.json()["channel"]["channelID"])
        
        return dmchannel.send(message, embed=embed)