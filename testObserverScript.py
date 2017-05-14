from socketIO_client import SocketIO, LoggingNamespace, BaseNamespace
import logging
import requests
import json
import datetime

OBSERVER_ID = "1"
OBSERVER_LOCATION = "Location 1"

class BlueHatObserver(BaseNamespace):
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

    def handleMessage(self):
        print('observer_json_msg', args)


if __name__ == "__main__":
    socketIO = SocketIO('http://127.0.0.1', 8000)
    bluehatObserver_socket = socketIO.define(BlueHatObserver, '/BlueHatObserver')
    bluehatObserver_socket.emit('observer_json_msg', {'xxx': 'yyy'})
    logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
    logging.basicConfig()
