from .token_v3 import TokenV3

class PairV3:
    def __init__(self, id, token0, token1, fee_tier, liquidity):
        self.id = id
        self.token0 = token0
        self.token1 = token1
        self.fee_tier = fee_tier
        self.liquidity = liquidity

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data.get("id", ""),
            token0=TokenV3.from_json(json_data.get("token0", {})),
            token1=TokenV3.from_json(json_data.get("token1", {})),
            fee_tier=json_data.get("feeTier", ""),
            liquidity=json_data.get("liquidity", "")
        )
    
    def __str__(self):
        return (
            f"PairV3(ID: {self.id}, "
            f"Token0: {self.token0}, "
            f"Token1: {self.token1}, "
            f"Fee Tier: {self.fee_tier}, "
            f"Liquidity: {self.liquidity})"
        )

    def __repr__(self):
        return self.__str__()
