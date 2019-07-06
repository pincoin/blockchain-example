from django.urls import path

from . import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),

    path('blocks', views.BlockchainListView.as_view(), name='blockchain-list'),
    path('peers', views.PeerView.as_view(), name='blockchain-peer-list'),
]
