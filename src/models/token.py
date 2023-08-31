class Token:
    def __init__(self, id, symbol, name, decimals):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.decimals = decimals

    def __repr__(self):
        return f"Token(id={self.id}, symbol={self.symbol}, name={self.name}, decimals={self.decimals})"

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data.get('id', ''),
            symbol=json_data.get('symbol', ''),
            name=json_data.get('name', ''),
            decimals=json_data.get('decimals', 0)
        )
