from .block import Block

GENESIS_BLOCK_DATA = 'This is a genesis block.'
GENESIS_BLOCK_TIMESTAMP = 1562132041


class Blockchain:
    def __init__(self):
        self.chain = [self.genesis_block, ]

    def new_block(self, data):
        block = Block(self.last_block.index + 1, self.last_block.hash, data)
        self.chain.append(block)

    @property
    def genesis_block(self):
        return Block(index=0, previous_block_hash=None, data=GENESIS_BLOCK_DATA, timestamp=GENESIS_BLOCK_TIMESTAMP)

    @property
    def last_block(self):
        return self.chain[-1]
