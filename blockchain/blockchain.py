from django.utils.timezone import now

from .block import Block

GENESIS_BLOCK = Block(
    0,
    '9BBCB57B172A75ACD6AFA7DFA7BD852818788B44BFC5B1C6E8E4E6919C799370',
    None,
    1562084809,
    'This is a genesis block.',
)

block_chain = [GENESIS_BLOCK, ]


def get_last_block():
    return block_chain[-1]


def get_timestamp():
    return now().timestamp()


def create_new_block():
    previous_block = get_last_block()
    new_block_index = previous_block.index + 1
    new_timestamp = get_timestamp()
