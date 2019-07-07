from rest_framework import (
    status, views
)
from rest_framework.response import Response

from .blockchain import Blockchain
from .p2p import P2P
from .serializers import (
    BlockSerializer, PeerSerializer
)


class BlockchainListView(views.APIView):
    def get(self, request):
        blockchain = Blockchain()

        results = BlockSerializer(blockchain.chain, many=True).data
        return Response(results)

    def post(self, request):
        blockchain = Blockchain()

        serializer = BlockSerializer(data=request.data)

        if serializer.is_valid():
            blockchain.new_block(serializer.validated_data['data'],
                                 serializer.validated_data['difficulty'],
                                 serializer.validated_data['nonce'])

            return Response(BlockSerializer(blockchain.chain, many=True).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeerView(views.APIView):
    def post(self, request):
        serializer = PeerSerializer(data=request.data)

        if serializer.is_valid():
            P2P().connect_to_peer(serializer.validated_data['peer'])

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
