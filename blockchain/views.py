import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import generic

from .blockchain import Blockchain


def index(request):
    return render(request, 'blockchain/index.html', {})


def room(request, room_name):
    return render(request, 'blockchain/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class BlockchainListView(generic.ListView):
    context_object_name = 'blocks'
    template_name = 'blockchain/blockchain_list.html'

    def get_queryset(self):
        return Blockchain().chain
