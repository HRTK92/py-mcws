import asyncio
import json

import websockets
from websockets import serve

class WsClient:
    def start(self, host="0.0.0.0", port=19132):
        self.ws = websockets.serve(self.receive, host, port)
        self.host = host
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.ws)
        self.event_ready()
        self.loop.run_forever()

    async def receive(self, websocket, path):
        self.ws = websocket
        await self.event_connect()
        while True:
            data = await self.ws.recv()
            msg = json.loads(data)
            await self.parse_command(msg)

    async def parse_command(self, message):
        if msg["header"]["messagePurpose"] == "event":
            if msg["body"]["eventName"] == "PlayerMessage" and msg["body"]["properties"]['MessageType'] == 'chat':
                await self.event_message(message)

    def event(self, func):
        def wrapper(*args, **kwargs):
            print(func.__name__)
            res = func(*args, **kwargs)
        return wrapper
