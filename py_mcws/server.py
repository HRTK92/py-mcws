import asyncio
import json

import websockets
from websockets import serve

from __main__ import *


class WsClient():
    def __init__(self, host="0.0.0.0", port="19132"):
        self.host = host
        self.port = port

    def start(self):
        self.ws = websockets.serve(self.receive, self.host, self.port)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.ws)
        event_ready(self.ws)
        self.loop.run_forever()

    async def receive(self, websocket, path):
        self.ws = websocket
        event_connect(websocket)
        while True:
            data = await self.ws.recv()
            msg = json.loads(data)
            await self.parse_command(msg)

    async def parse_command(self, message):
        if msg["header"]["messagePurpose"] == "event":
            if msg["body"]["eventName"] == "PlayerMessage" and msg["body"]["properties"]['MessageType'] == 'chat':
                event_message(message)

    def event(self, func):
        def wrapper(*args, **kwargs):
            print(func.__name__)
        return wrapper
