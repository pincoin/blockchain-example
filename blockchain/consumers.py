import logging

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class PeerConsumer(AsyncJsonWebsocketConsumer):
    logger = logging.getLogger(__name__)

    async def connect(self):
        await self.accept()
        self.logger.info('connected')
        self.logger.info(dir(self))

    async def disconnect(self, close_code):
        self.logger.info('disconnected')

    async def receive_json(self, content):
        self.logger.debug(content['peer'])


class EchoConsumer(AsyncConsumer):
    logger = logging.getLogger(__name__)

    async def websocket_connect(self, event):
        self.logger.info('connected from client')
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        self.logger.info('received message')
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    async def websocket_disconnect(self, event):
        self.logger.info('disconnected')
