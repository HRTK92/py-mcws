import py_mcws

server = py_mcws.WebsocketServer()


@server.event
async def on_ready(host, port):
    print(f"サーバーを起動しました。\n'/connect {host}:{port}'で接続できます")


@server.event
async def on_connect():
    print("接続しました")
    await server.command("say Hello World!")

@server.event
async def on_disconnect():
    print("切断しました")

@server.event
async def on_PlayerMessage(event):
    print(f"{event['body']['sender']}: {event['body']['message']}")
    if event["body"]["message"] == "こんにちは":
        await server.command("say こんにちは！")

server.start(host="0.0.0.0", port=19132)
