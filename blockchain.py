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

    def __str__(self):
        return f"""
index: {self.index}
timestamp: {self.timestamp}
transactions: {self.transactions}
hash: {self.hash}
previous_hash: {self.previous_hash}
nonce: {self.nonce}
"""

    def calculate_hash(self):
        string_to_hash = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        block_hash = hashlib.sha3_256(bytes(string_to_hash, 'utf-8'))
        return block_hash.hexdigest()
