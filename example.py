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
async def on_PlayerMessage(event):
    print()

server.start()
