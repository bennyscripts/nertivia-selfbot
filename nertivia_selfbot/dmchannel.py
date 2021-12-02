from types import NoneType
import requests

from .embed import Embed
from .extra import Extra

class DMChannel:
    def __init__(self, id):
        self.id = id

    def send(self, message, embed: Embed = None):
        body = {"message": message}
        if embed is not None:
            body["htmlEmbed"] = embed.json

        response = requests.post(
            f"https://nertivia.net/api/messages/channels/{self.id}",
            headers={"authorization": Extra.getauthtoken()},
            json=body
        )

        return response.json()