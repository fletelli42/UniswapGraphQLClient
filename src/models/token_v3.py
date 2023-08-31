# models/token_v3.py
class TokenV3:
    def __init__(self, id, symbol, name, decimals):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.decimals = decimals  # New field for V3

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data.get("id", ""),
            symbol=json_data.get("symbol", ""),
            name=json_data.get("name", ""),
            decimals=json_data.get("decimals", 18)
        )
