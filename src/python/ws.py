# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:59:25 2019

@author: User1
"""

from websocket import WebSocketApp
from websocket import WebSocket
from json import dumps, loads
from pprint import pprint

URL = 'wss://ws-feed.pro.coinbase.com'

def on_message(_, message):
    """Callback executed when a message comes.

    Positional argument:
    message -- The message itself (string)
    """
    pprint(loads(message))
    print
    
def on_open(socket):
    """Callback executed at socket opening.

    Keyword argument:
    socket -- The websocket itself
    """

    params = {
        "type": "subscribe",
        "channels": [{"name": "full", "product_ids": ["BTC-EUR"]}]
    }
    socket.send(dumps(params))

def main():
    """Main function."""
    ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
    ws.run_forever()


if __name__ == '__main__':
    main()
