from api.client import UniswapClient
from services.metrics import calculate_liquidity, calculate_trading_volume, calculate_price, calculate_price_from_swaps
from services.pagination import Paginator
from services.real_time import real_time_data_updater

from operator import itemgetter
def calculate_token_price_at_timestamp(token_id, target_timestamp, client):
    # Step 1: Fetch pairs for the token
    token_id = token_id.lower()
    pairs = client.fetch_pairs_for_token(token_id)
    if not pairs:
        return None  # Return None if no pairs are found
    
    closest_swaps = []
    
 
    # Step 2: For each pair, fetch swap transactions around the target timestamp
    for pair in pairs:
        swaps = client.fetch_swaps_for_pair_at_timestamp(pair.id, target_timestamp)
        
        if not swaps:
            continue  # Skip to next pair if no swaps are found for the current pair
        
        # Step 3: Find the closest swap to the target timestamp for each pair
        closest_swap = min(swaps, key=lambda x: abs(int(x['timestamp']) - target_timestamp))
        
        closest_swaps.append(closest_swap)
        
    if not closest_swaps:
        return None  # Return None if no swaps are found for any pairs
    print(closest_swaps)
    # Among the closest_swaps, find the absolute closest swap
    absolute_closest_swap = min(closest_swaps, key=lambda x: abs(int(x['timestamp']) - target_timestamp))
    
    print(absolute_closest_swap)
    # Step 4: Calculate the price based on the 'amountUSD' field of the absolute closest swap
    amountUSD = float(absolute_closest_swap['amountUSD'])

    if float(absolute_closest_swap['amount1In']):
        amountIn = float(absolute_closest_swap['amount1In'])
    elif float(absolute_closest_swap['amount0In']):
        amountIn = float(absolute_closest_swap['amount0In'])
    if float(absolute_closest_swap['amount0Out']):
        amountOut = float(absolute_closest_swap['amount0Out'])
    if float(absolute_closest_swap['amount1Out']):
        amountOut = float(absolute_closest_swap['amount1Out'])
    
    print("Amount USD:" , amountUSD)
    token0_price = amountUSD / amountIn
    token1_price = amountUSD / amountOut

    #print(token0_price, token1_price)
    return token0_price, token1_price



def main():
    # Initialize API client
    client = UniswapClient()

    # token0_id = "0x50327c6c5a14DCaDE707ABad2E27eB517df87AB5"
    # token1_id = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"

    token0_id = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"
    token1_id = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    target_timestamp = 1693487300

    price = calculate_token_price_at_timestamp(token0_id, target_timestamp, client)
    
    if price is not None:
        print(price)
if __name__ == "__main__":
    main()
