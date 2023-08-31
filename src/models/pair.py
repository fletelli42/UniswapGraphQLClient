class Pair:
    def __init__(self, id, token0, token1, volume):
        self.id = id
        self.reserve0 = 0
        self.reserve1 = 0
        self.token0 = token0
        self.token1 = token1
        self.volume = volume

    def __repr__(self):
        return f"Pair(id={self.id}, token0={self.token0}, token1={self.token1}, volume={self.volume})"

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data.get('id', ''),
            token0=json_data.get('token0', {}),
            token1=json_data.get('token1', {}),
            volume=json_data.get('volume', 0)
        )
