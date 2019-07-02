class Block:
    def __init__(self, index, hash, previous_block_hash, timestamp, data, difficulty=2, nonce=0):
        """Constructor for block

        Parameters
        ----------
        index : block counter
        hash : current block hash
        previous_block_hash : previous block hash to mingle with current block hash
        timestamp : timestamp when block is created
        data : block data such as transactions
        difficulty :
        nonce :
        """
        self.index = index
        self.hash = hash
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

