# py-mcws

![PyPI - Version](https://img.shields.io/pypi/v/py-mcws)
[![Downloads](https://static.pepy.tech/badge/py-mcws)](https://pepy.tech/project/py-mcws)
![PyPI - License](https://img.shields.io/pypi/l/py-mcws)
[![Upload Python Package](https://github.com/HRTK92/py-mcws/actions/workflows/python-publish.yml/badge.svg)](https://github.com/HRTK92/py-mcws/actions/workflows/python-publish.yml)

> MinecraftとPythonを繋げるためのシンプルなライブラリ

---

## インストール

```sh
pip install py-mcws
```

## 使い方

```python
import py_mcws

server = py_mcws.WebsocketServer()


@server.event
async def on_ready(host, port):
    print("サーバーを起動しました。")
    print(f"'/connect {host}:{port}' で接続できます")


@server.event
async def on_connect():
    print("接続しました")
    await server.command("say Hello World!") # メッセージを送信


@server.event
async def on_PlayerMessage(event):
    print(event)

server.start(host="0.0.0.0", port=19132)
```

## 接続の仕方

> [!WARNING]
> ワールドの設定でチートを有効にする必要があります。

Minecraft内のチャットで以下のコマンドを実行してください。

```cmd
/connect host:port
```

## イベントを受け取る

> [!NOTE]
> Minecraftで受け取れるイベントは以下から確認してください。  
> [MCPE & W10 Event Names](https://gist.github.com/jocopa3/5f718f4198f1ea91a37e3a9da468675c#file-mcpe-w10-event-names) by jocopa3

`PlayerMessage`イベントを受け取る例

```python
@server.event
async def on_PlayerMessage(event):
    print(event)
```

## コマンドを実行する

Minecraft と接続している状態でコマンドを実行してください。

```python
cmd = await server.command("say Hello World!")
print(cmd)
```

## 記事

以下の記事は、[inunosinsi](https://github.com/inunosinsi)さんによる記事です。  
thanks!

- [クロームブックのマインクラフト統合版でプログラミングをしてみる](https://saitodev.co/microbit/chromebook/article/57)
- [py-mcwsの仕組みを見てみよう](https://saitodev.co/microbit/chromebook/article/58)
- [py-mcwsでプレイヤーの頭上でニワトリを召喚してみる](https://saitodev.co/microbit/chromebook/article/61)
- [py-mcwsでプレイヤーの前に任意のブロックを置いてみる](https://saitodev.co/microbit/chromebook/article/62)
