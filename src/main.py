from api.client import UniswapClient
from api.client_v3 import UniswapV3Client
from api.client_coingecko import CoinGeckoClient
import csv


def find_closest_swap(swaps, target_timestamp):
    return min(swaps, key=lambda x: abs(int(x['timestamp']) - target_timestamp))

def calculate_price(closest_swap, token_decimals, amount_key, amount_usd_key):
    amount_usd = float(closest_swap[amount_usd_key])
    amount = float(closest_swap[amount_key])
    
    if amount == 0:
        return 0  # Prevent division by zero

    calculated_price = amount_usd / amount
    if amount > 10 ** 10:
        calculated_price *=  10 ** token_decimals
    return calculated_price


def calculate_token_price(token, target_timestamp, client, version):
    token_id = token.id.lower()
    decimals = token.decimals

    token_price = 0
    diff = 0

    response = client.fetch_swaps_for_token_at_timestamp(token_id, target_timestamp)
    if not response:
        return token_price, diff

    swaps1, swaps2 = response
    closest_swaps = [
        find_closest_swap(swaps1, target_timestamp),
        find_closest_swap(swaps2, target_timestamp)
    ]

    if not closest_swaps:
        return token_price, diff

    absolute_closest_swap = find_closest_swap(closest_swaps, target_timestamp)

    print(absolute_closest_swap)
    if version == 'v2':
        amount_usd_key, amount_in_key, amount_out_key = "amountUSD", "amount0In", "amount0Out"
    else:  # version == 'v3'
        amount_usd_key, amount_in_key, amount_out_key = "amountInUSD", "amountIn", "amountOut"

    amount_key = amount_in_key if float(absolute_closest_swap.get(amount_in_key, 0)) != 0 else amount_out_key
    amount_usd_key = amount_usd_key if float(absolute_closest_swap.get(amount_usd_key, 0)) != 0 else "amountOutUSD"
    token_price = calculate_price(absolute_closest_swap, decimals, amount_key, amount_usd_key)

    diff = int(absolute_closest_swap['timestamp']) - target_timestamp
    print(f"Token: {token.symbol}")
    print(f"Timestamp diff: {diff}")
    print(f"Token price: {token_price}")

    return token_price, diff

def main():
    client = UniswapClient()
    client_v3 = UniswapV3Client()
    coingecko_client = CoinGeckoClient()
    target_timestamp = 1693487300
    tokens = client_v3.fetch_token_list()

    with open('token_prices.csv', 'w', newline='') as csvfile:
        fieldnames = ['Token Symbol', 'Token Price V2', 'Diff Token Price V2', 'Token Price V3', 'Diff Token Price V3', 'CoinGecko Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        for token in tokens:
            print(f"V2: {token.symbol}")
            price_v2, diff_v2 = calculate_token_price(token, target_timestamp, client, 'v2')

            print(f"V3: {token.symbol}")
            price_v3, diff_v3 = calculate_token_price(token, target_timestamp, client_v3, 'v3')

            coingecko_price = coingecko_client.fetch_historical_price(token.symbol, target_timestamp)
            
            writer.writerow({
                    'Token Symbol': token.symbol,
                    'Token Price V2': price_v2,
                    'Diff Token Price V2': diff_v2,
                    'Token Price V3': price_v3,
                    'Diff Token Price V3': diff_v3,
                    'CoinGecko Price': coingecko_price
                })

if __name__ == "__main__":
    main()
