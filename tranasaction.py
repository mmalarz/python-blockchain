import hashlib


class Transaction:

    def __init__(self, from_address, to_address, amount, timestamp):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f'Transaction('
            f'from_address={self.from_address}, '
            f'timestamp={self.to_address}, '
            f'transactions={self.amount}, '
            f'previous_hash={self.timestamp})'
        )
