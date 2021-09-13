import asyncio

import py_mcws
WsClient = py_mcws.WsClient()


@WsClient.event
def event_ready(event):
    print(event)

@WsClient.event
def event_connect(event):
    print(event)

@WsClient.event
def event_message(event):
    print(event)


WsClient.start()
