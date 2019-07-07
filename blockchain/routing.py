from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/blockchain/<str:room_name>/', consumers.ChatConsumer),
]
