import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import views
from rest_framework.response import Response

from .blockchain import Blockchain
from .serializers import BlockSerializer


def index(request):
    return render(request, 'blockchain/index.html', {})


def room(request, room_name):
    return render(request, 'blockchain/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class BlockchainListView(views.APIView):
    def get(self, request):
        chain = Blockchain().chain
        results = BlockSerializer(chain, many=True).data
        return Response(results)
