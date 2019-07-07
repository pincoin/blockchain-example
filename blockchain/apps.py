from django.apps import AppConfig


class BlockchainConfig(AppConfig):
    name = 'blockchain'

    def ready(self):
        from .models import WebSocket
        WebSocket.objects.all().delete()
