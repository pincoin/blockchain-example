import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import (
    status, views
)
from rest_framework.response import Response

from .blockchain import Blockchain
from .serializers import (
    BlockSerializer, PeerSerializer
)


def index(request):
    return render(request, 'blockchain/index.html', {})


def room(request, room_name):
    return render(request, 'blockchain/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class BlockchainListView(views.APIView):
    def get(self, request):
        blockchain = Blockchain()

        results = BlockSerializer(blockchain.chain, many=True).data
        return Response(results)


class PeerView(views.APIView):
    def post(self, request):
        serializer = PeerSerializer(data=request.data)

        if serializer.is_valid():
            print(request.data['peer'])
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
