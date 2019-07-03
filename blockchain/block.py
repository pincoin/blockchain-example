import json
from hashlib import sha256

from django.utils.timezone import datetime


class Block:
    def __init__(self, index, previous_block_hash, data, difficulty=2, nonce=0, timestamp=None):
        """ Constructor for a block

        :param index: block index counter
        :param previous_block_hash: previous block hash to mingle with current block data, timestamp and index
        :param data: block data in JSON format (ie. transactions)
        :param difficulty:
        :param nonce:
        :param timestamp: timestamp when block is created
        """

        self.index = index
        self.previous_block_hash = previous_block_hash
        self.data = json.dumps(data)

        self.difficulty = difficulty
        self.nonce = nonce

        self.timestamp = timestamp if timestamp else datetime.now().timestamp()
        self.hash = self.create_hash()

    def create_hash(self):
        block_contents = str(self.index) + str(self.previous_block_hash) + str(self.timestamp) + self.data
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()
