# models/transaction_v3.py
class TransactionV3:
    def __init__(self, id, timestamp, amount0, amount1, sqrtPriceX96, tick):
        self.id = id
        self.timestamp = timestamp
        self.amount0 = amount0
        self.amount1 = amount1
        self.sqrtPriceX96 = sqrtPriceX96  # New field for V3
        self.tick = tick  # New field for V3

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data.get("id", ""),
            timestamp=json_data.get("timestamp", ""),
            amount0=json_data.get("amount0", ""),
            amount1=json_data.get("amount1", ""),
            sqrtPriceX96=json_data.get("sqrtPriceX96", ""),
            tick=json_data.get("tick", "")
        )