import asyncio
import logging

import websockets

from .models import WebSocket


class P2P:
    logger = logging.getLogger(__name__)

    def __init__(self):
        pass

    @property
    def sockets(self):
        return WebSocket.objects.all()

    def connect_to_peer(self, uri):
        """
        socket = WebSocket()
        socket.uri = uri
        socket.save()
        """
        self.init_socket(uri)

    def disconnect_from_peer(self, uri):
        WebSocket.objects.filter(uri=uri).delete()

    def init_socket(self, socket):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(connect(socket))
        loop.close()

        self.logger.info(socket)

        self.logger.info('push socket')

        self.logger.info('register message handlers')

        self.logger.info('register error handlers')

        self.logger.info('send latest block')

        self.logger.info('send all mempool to all')


async def connect(uri):
    async with websockets.connect(uri) as websocket:
        pass
