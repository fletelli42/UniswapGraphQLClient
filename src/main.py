from api.client import UniswapClient
from services.metrics import calculate_liquidity, calculate_trading_volume, calculate_price, calculate_price_from_swaps
from services.pagination import Paginator
from services.real_time import real_time_data_updater

from operator import itemgetter

def calculate_token_price_at_timestamp(token0_id, token1_id, target_timestamp):
    client = UniswapClient()

    token0_id = token0_id.lower()
    token1_id = token1_id.lower()

    pair = client.fetch_specific_pair(token0_id, token1_id)
    if pair is None:
        return None  # Pair doesn't exist

    target_pair = next((item for item in pair if item is not None), None)
    
    if target_pair is not None:
        print(f"Found pair: {target_pair.id}")
    else:
        print("No valid pair found.")
        return None  # No valid pair exists

    swaps = client.fetch_swaps_for_pair_at_timestamp(target_pair.id, target_timestamp)
  
    
    if len(swaps) == 0:
        return None  # No swaps occurred around the given timestamp

    # Find the swap closest to the target timestamp
    closest_swap = min(swaps, key=lambda x: abs(int(x['timestamp']) - target_timestamp))
    print(closest_swap)
    if float(closest_swap['amount1In']):
        amountIn = float(closest_swap['amount1In'])
    elif float(closest_swap['amount0In']):
        amountIn = float(closest_swap['amount0In'])
    if float(closest_swap['amount0Out']):
        amountOut = float(closest_swap['amount0Out'])
    if float(closest_swap['amount1Out']):
        amountOut = float(closest_swap['amount1Out'])
    token0_price = amountOut / amountIn
    token1_price = amountIn / amountOut

    print(token0_price, token1_price)
    return token0_price, token1_price



def main():
    # Initialize API client
    client = UniswapClient()

    # token0_id = "0x50327c6c5a14DCaDE707ABad2E27eB517df87AB5"
    # token1_id = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"

    token0_id = "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"
    token1_id = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    target_timestamp = 1693487300

    price = calculate_token_price_at_timestamp(token0_id, token1_id, target_timestamp)
    
    if price is not None:
        print(price)
if __name__ == "__main__":
    main()
