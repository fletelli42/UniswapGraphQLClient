class Transaction:
    
    def __init__(self, id, timestamp, amount0In, amount0Out, amount1In, amount1Out, pair, transaction_id):
        self.id = id
        self.timestamp = timestamp
        self.amount0In = amount0In
        self.amount0Out = amount0Out
        self.amount1In = amount1In
        self.amount1Out = amount1Out
        self.pair = pair  # This could be an object of Pair class
        self.transaction_id = transaction_id
    
    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data['id'],
            json_data['timestamp'],
            json_data['amount0In'],
            json_data['amount0Out'],
            json_data['amount1In'],
            json_data['amount1Out'],
            json_data['pair'],
            json_data['transaction']['id']
        )
