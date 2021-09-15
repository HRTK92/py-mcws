## py-mcws(作成中)

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

        #受け取るイベント
        self.events = ["PlayerMessage", "PlayerDied","MobKilled", "BlockPlaced", "BlockBroken"]
    
    async def event_connect(self):
        print("Connected!")

        #コマンドを実行
        await self.command("say Hello")
    
    async def event_disconnect(self):
        print("disconnect!")

    async def event_PlayerMessage(self, event):
        print(event)

MyWsClient().start(host="0.0.0.0", port=19132)
```

### イベント
[イベント一覧](https://gist.github.com/jocopa3/5f718f4198f1ea91a37e3a9da468675c#file-mcpe-w10-event-names)

```python
self.events["PlayerMessage"]

async def event_PlayerMessage(self, event):
    print(event)
```

### コマンド
```python
await self.command("say hello")
```
