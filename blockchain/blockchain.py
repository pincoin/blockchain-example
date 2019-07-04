import json
import logging

from .block import Block

GENESIS_BLOCK_DATA = 'This is a genesis block.'
GENESIS_BLOCK_TIMESTAMP = 1562132041


class Blockchain:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.chain = [self.genesis_block, ]

    def new_block(self, data):
        block = Block(self.last_block.index + 1, self.last_block.hash, data)

        if block.validate(self.last_block):
            self.chain.append(block)
            return block

        return False

    @property
    def genesis_block(self):
        return Block(index=0, previous_block_hash=None, data=GENESIS_BLOCK_DATA, timestamp=GENESIS_BLOCK_TIMESTAMP)

    @property
    def last_block(self):
        return self.chain[-1]

    def validate(self, chain):
        if json.dumps(self.genesis_block) != json.dumps(chain[0]):
            self.logger.error('genesis block is invalid.')
            return False

        for i in range(1, len(self.chain)):
            if not chain[i].validate(chain[i - 1]):
                self.logger.error('chain is broken.')
                return False

        return True

    def replace(self, chain):
        """ Update chain with the newer and longer chain

        :param chain:
        :return:
        """
        if chain.validate() and len(chain) > len(self.chain):
            self.chain = chain
            return True

        return False
