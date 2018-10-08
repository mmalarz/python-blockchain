import hashlib
import datetime as dt


class Block:

    def __init__(self, index, timestamp, transactions, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def __repr__(self):
        return (
            f'Block(index={self.index}, '
            f'timestamp={self.timestamp}, '
            f'transactions={self.transactions}, '
            f'previous_hash={self.previous_hash}, '
            f'hash={self.hash}, '
            f'nonce={self.nonce})'
        )

    def __str__(self):
        return (
            f'index: {self.index}'
            f'timestamp: {self.timestamp}'
            f'transactions: {self.transactions}'
            f'hash: {self.hash}'
            f'previous_hash: {self.previous_hash}'
            f'nonce: {self.nonce}'
        )

    def calculate_hash(self):
        string_to_hash = (
            str(self.index) +
            str(self.timestamp) +
            str(self.transactions) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        block_hash = hashlib.sha3_256(bytes(string_to_hash, 'utf-8'))
        return block_hash.hexdigest()


class Blockchain:

    def __init__(self):
        self.chain = list()
        self.chain.append(Blockchain.create_genesis_block())

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def get_latest_block(self):
        return self.chain[-1]

    def is_chain_valid(self):

        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    @staticmethod
    def create_genesis_block():
        return Block(0, dt.datetime.now(), '', '')


if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.add_block(Block(1, 2, 3, '23fev'))
    blockchain.add_block(Block(2, 3, 4, 'er34qd'))

    for block in blockchain.chain:
        print(block)
