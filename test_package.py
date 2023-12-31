import py_mcws


def test_mcws():
    print(py_mcws.__version__)


def test_server():
    server = py_mcws.WebsocketServer()

    @server.event
    async def on_ready(host, port):
        server.close()

    server.start()
