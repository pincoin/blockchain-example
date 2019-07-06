from rest_framework import serializers


class BlockSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    data = serializers.CharField()
    difficulty = serializers.IntegerField()
    nonce = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    previous_block_hash = serializers.CharField()
    hash = serializers.CharField()
