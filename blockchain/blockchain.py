from hashlib import sha256

from django.utils.timezone import datetime


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.hash()

    def print_block(self):
        print('timestamp: {}'.format(self.timestamp))
        print('transactions: {}'.format(self.transactions))
        print('current hash: {}'.format(self.hash()))

    def hash(self):
        block_header = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()


class BlockChain:
    """블록체인

    블록체인은 분산 공개 장부(a distributed, decentralized, public ledger)
    permanent book of records that keeps a log of all transactions that have taken place in chronological order

    블록은 유효한 거래 정보의 묶음

    블록 헤더
    version: 소프트웨어, 프로토콜 버전
    previous_block_hash: 블록체인에서 바로 이전 블록의 블록 헤더 해시값
    merkle_hash: 개별 거래 정보의 거래 해시를 2진 트리 형태로 구성할 때, 트리 루트에 위치하는 해시값
    time: 블록 생성 시각
    bits: 난이도 조절용 수치
    nonce: 최초 0에서 시작하여 조건을 만족하는 해쉬값을 찾아낼때까지의 1씩 증가하는 계산 횟수
    """

    def __init__(self, transactions, previous_block_hash, nonce=0):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # 체인에 새 블록을 만들어 추가

        """
        In order for a new block to be added,
        51% of all of the participants in the blockchain network must verify that the new block is not fraudulent.
        Once a block has been verified as a valid transaction, it is added to each participant’s copy of the blockchain.
        """
        pass

    def new_transaction(self):
        # 거래 리스트에 새 거래를 추가
        pass

    @staticmethod
    def hash(block):
        # 블록 헤더 해시
        pass

    @property
    def last_block(self):
        # 체인에서 마지막 블록 반환
        pass
