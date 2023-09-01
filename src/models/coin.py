class Coin:
    def __init__(self, id, symbol, name):
        self.id = id
        self.symbol = symbol
        self.name = name

    @classmethod
    def from_json(cls, json_obj):
        return cls(json_obj['id'], json_obj['symbol'], json_obj['name'])
