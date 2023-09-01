from api.client_v3 import UniswapV3Client

def calculate_token_price_at_timestamp_v3(token_id, target_timestamp, client):
    # Step 1: Fetch pairs for the token
    token_id = token_id.lower()
    token_info = client.fetch_token(token_id)
    
    decimals = token_info.decimals
    print(decimals)
    swaps1, swaps2 = client.fetch_swaps_for_token_at_timestamp(token_id, target_timestamp)
    if not swaps1 or not swaps2:
        return None  # Return None if no pairs are found

    closest_swaps = []

    # Step 3: Find the closest swap to the target timestamp for each pair
    closest_swap1 = min(swaps1, key=lambda x: abs(int(x['timestamp']) - target_timestamp))
    
    closest_swaps.append(closest_swap1)

    closest_swap2 = min(swaps2, key=lambda x: abs(int(x['timestamp']) - target_timestamp))

    closest_swaps.append(closest_swap2)

    if not closest_swaps:
        return None  # Return None if no swaps are found for any pairs
   
    # Among the closest_swaps, find the absolute closest swap
    absolute_closest_swap = min(closest_swaps, key=lambda x: abs(int(x['timestamp']) - target_timestamp))
    

    if "amountIn" in absolute_closest_swap:
        amountUSD = float(absolute_closest_swap['amountInUSD'])
        amountIn = float(absolute_closest_swap["amountIn"])
        token_price = (amountUSD / amountIn)  * (10 ** int(decimals))
    elif "amountOut" in absolute_closest_swap:
        amountUSD = float(absolute_closest_swap['amountOutUSD'])
        amountOut = float(absolute_closest_swap["amountOut"])
        token_price = (amountUSD / amountOut) * (10 ** int(decimals))

    print("Token: ", token_info.symbol)
    print("Timestamp diff: ", int(absolute_closest_swap['timestamp']) - target_timestamp)
    print("Token price: ", token_price)
    return token_price



def main():
    client = UniswapV3Client()
    # Fetch a specific pair by token IDs
    example_token0_id = "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
    example_token1_id = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    target_timestamp = 1693487300
    calculate_token_price_at_timestamp_v3(example_token0_id, target_timestamp, client)

    tokens = client.fetch_token_list()
    for token in tokens:
        print("Token: ", token.symbol)
        calculate_token_price_at_timestamp_v3(token.id, target_timestamp, client)


if __name__ == "__main__":
    main()
