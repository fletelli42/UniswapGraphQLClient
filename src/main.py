from api.client import UniswapClient
from services.metrics import calculate_liquidity, calculate_trading_volume
from services.pagination import Paginator
from services.real_time import real_time_data_updater


def main():
    # Initialize API client
    client = UniswapClient()

    # Fetch and print information about a specific token
    token_data = client.fetch_token('0x6b175474e89094c44da98b954eedeac495271d0f')  # Replace with actual contract address
    print(f"Token Data: {token_data}")

    # Fetch pairs for a specific token
    pairs = client.fetch_pairs_for_token('0x6b175474e89094c44da98b954eedeac495271d0f')  # Replace with actual contract address
    print(f"Pairs: {pairs}")

    # Fetch swap transactions for a specific pair
    swap_transactions = client.fetch_swap_transactions(pairs[0].id)  # Replace with actual pair id
    print(f"Swap Transactions: {swap_transactions}")

        # Display transaction details
    for i, transaction in enumerate(swap_transactions):
        print(f"Transaction {i + 1}:")
        print(f"  ID: {transaction.id}")
        print(f"  Timestamp: {transaction.timestamp}")
        print(f"  Amount0In: {transaction.amount0In}")
        print(f"  Amount0Out: {transaction.amount0Out}")
        print(f"  Amount1In: {transaction.amount1In}")
        print(f"  Amount1Out: {transaction.amount1Out}")
        print(f"  Pair: {transaction.pair}")
        print(f"  Transaction ID: {transaction.transaction_id}")
        print("-------------------")

if __name__ == "__main__":
    main()
