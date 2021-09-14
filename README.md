## py-mcws

### 使い方
```sh
pip install git+https://github.com/HRTK92/py-mcws
```

### 例
```python
import asyncio

import py_mcws

class MyWsClient(py_mcws.WsClient):
    def event_ready(self):
        print(f"Ready {self.host}:{self.port}")
    
    async def event_connect(self):
        print("Connected!")
        await self.command("say Hello")
    
    async def event_disconnect(self):
        print("disconnect!")

    async def event_message(self, event):
        print(event)

MyWsClient().start(host="0.0.0.0", port=19132)
```