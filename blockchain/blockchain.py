class Block:
    def __init__(self, index, hash, previous_block_hash, timestamp, data):
        self.index = index
        self.hash = hash
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.data = data
