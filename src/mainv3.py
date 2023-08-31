from api.client_v3 import UniswapV3Client

def calculate_token_price_at_timestamp_v3(token0_id, token1_id, target_timestamp):
    client = UniswapV3Client()

    token0_id = token0_id.lower()
    token1_id = token1_id.lower()

    target_pair = client.fetch_specific_pair(token0_id, token1_id)

    if target_pair is None:
        print("No valid pair found.")
        return None
  

    swaps = client.fetch_swaps_for_pair_at_timestamp(target_pair.id, target_timestamp)
    
    #print(swaps)
    if len(swaps) == 0:
        return None  # No swaps occurred around the given timestamp

    
    # Find the swap closest to the target timestamp
    closest_swap = min(swaps, key=lambda x: abs(int(x['timestamp']) - target_timestamp))
    print(closest_swap)
    # Using hypothetical fields, please replace these with actual V3 schema fields if they differ
    token0_price = abs(float(closest_swap['amount0'])) / abs(float(closest_swap['amount1']))  # Replace 'token0Price' with the actual field name if it's different
    token1_price = abs(float(closest_swap['amount1'])) / abs(float(closest_swap['amount0']))   # Replace 'token1Price' with the actual field name if it's different

    print(token0_price, token1_price)
    return token0_price, token1_price



def main():

    # Fetch a specific pair by token IDs
    example_token0_id = "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"
    example_token1_id = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    target_timestamp = 1693487300
    calculate_token_price_at_timestamp_v3(example_token0_id, example_token1_id, target_timestamp)


if __name__ == "__main__":
    main()
