from .models import WebSocket


class P2P:
    def __init__(self):
        pass

    @property
    def sockets(self):
        return WebSocket.objects.all()

    def connect_to_peer(self, url):
        socket = WebSocket()
        socket.url = url
        socket.save()

    def disconnect_from_peer(self, url):
        WebSocket.objects.filter(url=url).delete()
