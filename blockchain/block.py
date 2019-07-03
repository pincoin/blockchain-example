from hashlib import sha256

from django.utils.timezone import datetime


class Block:
    def __init__(self, index, previous_block_hash, data, difficulty=2, nonce=0, timestamp=None):
        """Constructor for block

        Parameters
        ----------
        index : block index counter
        previous_block_hash : previous block hash to mingle with current block hash
        data : block data such as transactions
        difficulty :
        nonce :
        timestamp : timestamp when block is created
        """
        self.index = index
        self.previous_block_hash = previous_block_hash
        self.data = data

        self.difficulty = difficulty
        self.nonce = nonce

        self.timestamp = timestamp if timestamp else datetime.now().timestamp()
        self.hash = self.create_hash()

    def create_hash(self):
        block_contents = str(self.index) + str(self.previous_block_hash) + str(self.timestamp) + str(self.data)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()
