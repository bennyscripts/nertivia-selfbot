import requests
import socketio
import asyncio
import traceback
import base64

from ..extra import Extra
from ..user import User

class Client:
    def __init__(self, debug=False):
        self.token = ""
        self.socket = socketio.Client(engineio_logger=False, logger=debug)
        self.socketIp = "https://nertivia.net/"
        self.headers = {"Authorization": self.token, "content-type": "application/json"}
        self.user = ""
        Extra.setauthtoken(self.token)    

    def run(self, token):
        response = requests.get("https://nertivia.net/api/user", headers={"Authorization": token})
        self.token = token
        self.user = User(response.json()["user"]["id"], response.json()["user"]["username"], response.json()["user"]["tag"], response.json()["user"]["avatar"], response.json()["user"]["banner"], response.json()["user"]["created"])
        Extra.setauthtoken(token)
        self.socket.connect(self.socketIp, namespaces=["/"], transports=["websocket"])
        self.socket.emit("authentication", {"token": token})

    def event(self, *args):
        event = args[0].__name__

        events = {
            "on_connect": "success", 
            "on_message": "receiveMessage", 
            "on_quit": "disconnect",
            "on_status_change": "member:custom_status_change", 
            "on_message_delete": "delete_message",
            "on_message_edit": "update_message",
            "on_typing": "typingStatus"
        }

        for key, value in events.items():
            if event == key:
                return self.socket.on(value, args[0])