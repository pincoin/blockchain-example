from .block import Block

GENESIS_BLOCK = Block(
    0,
    '9BBCB57B172A75ACD6AFA7DFA7BD852818788B44BFC5B1C6E8E4E6919C799370',
    None,
    1562084809,
    'This is a genesis block.',
)

block_chain = [GENESIS_BLOCK, ]
