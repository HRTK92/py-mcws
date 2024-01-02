import asyncio
import sys
import json
import uuid

import websockets

from .Events import Events


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
        await self.listen_event()
        await self.event("connect")  # self.event_connect()
        try:
            while True:
                data = await self.ws.recv()
                msg = json.loads(data)
                await self.parse_command(msg)
        except (
                websockets.exceptions.ConnectionClosedOK,
                websockets.exceptions.ConnectionClosedError,
                websockets.exceptions.ConnectionClosed):
            await self.event("disconnect")  # self.event_disconnect()
            sys.exit()

    async def listen_event(self):
        for event in self.events:
            await self.ws.send(json.dumps({
                "body": {
                    "eventName": event
                },
                "header": {
                    "requestId": "00000000-0000-0000-0000-000000000000",
                    "messagePurpose": "subscribe",
                    "version": 1,
                    "messageType": "commandRequest"
                }
            }))

    async def parse_command(self, message):
        if message["header"]["messagePurpose"] == "event":
            event_name = message["header"]["eventName"]
            await self.event(event_name, message)
            if (
                message["header"]["eventName"] == "PlayerMessage" and
                message["body"]["type"] == 'chat'
            ):
                pass
        elif message["header"]["messagePurpose"] == "error":
            await self.event("error", message)

    async def command(self, cmd):
        uuid4 = str(uuid.uuid4())
        cmd_json = json.dumps({
            "body": {
                "origin": {
                    "type": "player"
                },
                "commandLine": cmd,
                "version": 1
            },
            "header": {
                "requestId": uuid4,
                "messagePurpose": "commandRequest",
                "version": 1,
                "messageType": "commandRequest"
            }
        })
        await self.ws.send(cmd_json)
        data = await self.ws.recv()
        msg = json.loads(data)
        if (msg["header"]["messagePurpose"] == "commandResponse" and
                msg["header"]["requestId"] == uuid4):
            return msg
        else:
            return None

    async def event(self, name, *args):
        func = f"self.event_{name}"
        if args == ():
            try:
                await eval(f"{func}()")
            except NameError:
                print(f"event_{name}")
        else:
            try:
                await eval(f"{func}({args})")
            except NameError:
                print(f"event_{name}")


class WebsocketServer():
    def __init__(self):
        self.ws = None
        self.events = []
        self.auto_listen_event = None

    def _warning(self, msg: str):
        print(f"\033[33m[警告] {msg}\033[0m")

    async def _run_server(self, host: str, port: int):
        self.ws = await websockets.serve(self._receive, host, port)
        await self._run_event("ready", host, port)
        await self.ws.wait_closed()

    async def _run_event(self, event_name: str, *args):
        for event in self.events:
            if event[0] == event_name:
                await event[1](*args)

    def start(self, host="0.0.0.0", port=19132, auto_listen_event=True):
        """websocket サーバーを起動する"""
        if self.ws:
            raise Exception("すでにWebsocketサーバーが起動しています。")
        self.auto_listen_event = auto_listen_event
        asyncio.run(self._run_server(host, port))

    def event(self, func):
        """イベントを登録するデコレーター"""
        if func.__name__.startswith("on_"):
            event_name = func.__name__.replace("on_", "")
        else:
            self._warning(f"イベント名が不正です: {func.__name__}")
        if event_name not in Events:
            self._warning(f"イベント名が不正です: {event_name}")
        self.events.append([event_name, func])
        return func

    async def _receive(self, websocket):
        """データを受信する"""
        self.ws = websocket
        await self._run_event("connect")
        # イベントを自動で登録する
        if self.auto_listen_event:
            for event in self.events:
                if event[0] in ["ready", "connect", "disconnect", "error"]:
                    continue
                if event[0] not in Events:
                    continue
                await self.listen_event(event[0])
                print(f"\033[32m{event[0]}を登録しました\033[0m")
        try:
            while True:
                data = await self.ws.recv()
                msg = json.loads(data)
                await self._parse_command(msg)
        except (
                websockets.exceptions.ConnectionClosedOK,
                websockets.exceptions.ConnectionClosedError,
                websockets.exceptions.ConnectionClosed):
            await self._run_event("disconnect")
            sys.exit()

    async def listen_event(self, event_name: str):
        """受信するイベントを登録する"""
        if self.ws:
            await self.ws.send(json.dumps({
                "body": {
                    "eventName": event_name
                },
                "header": {
                    "requestId": "00000000-0000-0000-0000-000000000000",
                    "messagePurpose": "subscribe",
                    "version": 1,
                    "messageType": "commandRequest"
                }
            }))
        else:
            self._warning("WebSocket接続が確立されていません。")

    async def _parse_command(self, message):
        if message["header"]["messagePurpose"] == "event":
            event_name = message["header"]["eventName"]
            await self._run_event(event_name, message)
        elif message["header"]["messagePurpose"] == "error":
            await self._run_event("error", message)

    async def command(self, cmd: str):
        """コマンドを送信し、レスポンスを受信する"""
        if self.ws is False:
            return None
        uuid4 = str(uuid.uuid4())
        cmd_json = json.dumps({
            "body": {
                "origin": {
                    "type": "player"
                },
                "commandLine": cmd,
                "version": 1
            },
            "header": {
                "requestId": uuid4,
                "messagePurpose": "commandRequest",
                "version": 1,
                "messageType": "commandRequest"
            }
        })
        await self.ws.send(cmd_json)
        data = await self.ws.recv()
        msg = json.loads(data)
        if (msg["header"]["messagePurpose"] == "commandResponse" and
                msg["header"]["requestId"] == uuid4):
            return msg
        else:
            return None
