import asyncio

import py_mcws
WsClient = py_mcws.WsClient

class MyWsClient(WsClient):
    def event_ready(self):
        print(f"{self.host}:{self.port}")
    
    async def event_connect(self):
        print(event)

    def event_message(self, event):
        print(event)

MyWsClient().start(host="0.0.0.0", port=19132)