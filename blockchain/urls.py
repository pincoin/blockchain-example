from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

    path('blocks', views.BlockchainListView.as_view(), name='blockchain-list'),
]
