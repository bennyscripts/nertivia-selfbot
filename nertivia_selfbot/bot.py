import requests

from .extra import Extra
from .user import User

class Bot:
    def __init__(self, id, username="", tag="", avatar="", commands=[], creator = None):
        if username == "" or tag == "" or avatar == "" or commands == [] or creator is None:
            response = requests.get(
                f"https://nertivia.net/api/bots/{id}",
                headers={"Authorization": Extra.getauthtoken()}
            )
            
            self.id = response.json()["id"]
            self.username = response.json()["username"]
            self.tag = response.json()["tag"]
            self.avatar = response.json()["avatar"]
            self.commands = response.json()["botCommands"]
            self.creator = User(response.json()["createdBy"]["id"])

        else:
            self.id = id
            self.username = username
            self.tag = tag
            self.avatar = avatar
            self.commands = commands
            self.creator = creator

    def __str__(self):
        return f"{self.username}:{self.tag}"