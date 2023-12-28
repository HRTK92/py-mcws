# py-mcws

![PyPI - Version](https://img.shields.io/pypi/v/py-mcws)
[![Downloads](https://static.pepy.tech/badge/py-mcws)](https://pepy.tech/project/py-mcws)
![PyPI - License](https://img.shields.io/pypi/l/py-mcws)
[![Upload Python Package](https://github.com/HRTK92/py-mcws/actions/workflows/python-publish.yml/badge.svg)](https://github.com/HRTK92/py-mcws/actions/workflows/python-publish.yml)

> MinecraftとPythonを繋げるためのライブラリ

---

## インストール

```sh
pip install py-mcws
```

## 使い方

```python
import py_mcws

class MyWsClient(py_mcws.WsClient):
    def event_ready(self):
        print(f"Ready {self.host}:{self.port}")

        #受け取るイベント
        self.events = ["PlayerMessage", "PlayerDied"]
    
    async def event_connect(self):
        print("Connected!")

        #コマンドを実行
        await self.command("say Hello")
    
    async def event_disconnect(self):
        print("disconnect!")

    async def event_PlayerMessage(self, event):
        print(event)

    async def event_PlayerDied(self, event):
        print(event)

MyWsClient().start(host="0.0.0.0", port=19132)
```

## 接続の仕方

Minecraft内のチャットで

```cmd
/connect host:port
```

## イベント

[イベント一覧](https://gist.github.com/jocopa3/5f718f4198f1ea91a37e3a9da468675c#file-mcpe-w10-event-names)

```python
self.events["PlayerMessage"]

async def event_PlayerMessage(self, event):
    print(event)
```

## コマンド

```python
cmd = await self.command("say hello")
print(cmd)
```
