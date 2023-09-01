import json
import requests
from .gql_queries import FETCH_TOKEN_QUERY, FETCH_PAIRS_FOR_TOKEN_QUERY, FETCH_SWAP_TRANSACTIONS_QUERY, FETCH_SWAP_TRANSACTIONS_FOR_TIMESTAMP_QUERY, FETCH_SPECIFIC_PAIR
from models.pair import Pair
from models.token import Token
from models.transaction import Transaction


class UniswapClient:

    def __init__(self, endpoint='https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v2-dev'):
        self.endpoint = endpoint

    def send_query(self, query, variables={}):
        payload = {'query': query, 'variables': variables}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.endpoint, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Query failed with status code {response.status_code}")

        return json.loads(response.content.decode())

    def fetch_token(self, token_id):
        response = self.send_query(FETCH_TOKEN_QUERY, {'id': token_id})
        token_data = response.get('data', {}).get('token', {})
        
        if token_data:
            return Token.from_json(token_data)
        return None
    

    def fetch_pairs_for_token(self, token_id):
        response = self.send_query(FETCH_PAIRS_FOR_TOKEN_QUERY, {'id': token_id})
        pairs_data = response.get('data', {}).get('pairs', [])
        
        pairs = []
        for pair_data in pairs_data:
            pairs.append(Pair.from_json(pair_data))
        
        return pairs
    
    def fetch_swap_transactions(self, pair_id, first=10, order_by="timestamp", order_direction="desc"):
        variables = {
            'pairId': pair_id,
            'first': first,
            'orderBy': order_by,
            'orderDirection': order_direction
        }
        response = self.send_query(FETCH_SWAP_TRANSACTIONS_QUERY, variables)
        swaps_data = response.get('data', {}).get('swaps', [])
        
        transactions = []
        for swap_data in swaps_data:
            transactions.append(Transaction.from_json(swap_data))
        
        return transactions

    def fetch_swaps_for_pair_at_timestamp(self, pair_id, target_timestamp, time_range=600000):
        # Time range in seconds (default is +/- 10 minutes)
        start_time = target_timestamp - time_range
        end_time = target_timestamp + time_range

        variables = {
            'pair_id': pair_id,
            'start_time': start_time,
            'end_time': end_time
        }

        # Your existing GraphQL query assumed to include the time range filter
        query = FETCH_SWAP_TRANSACTIONS_FOR_TIMESTAMP_QUERY

        #print(query, variables)
        response = self.send_query(query, variables)
        return response.get('data', {}).get('swaps', [])


    def fetch_pairs_for_token(self, token_id):
        response = self.send_query(FETCH_PAIRS_FOR_TOKEN_QUERY, {'id': token_id})
        pairs_data = response.get('data', {}).get('pairs', [])
        
        pairs = []
        for pair_data in pairs_data:
            pair = Pair.from_json(pair_data)
            try:
                pair.reserve0 = float(pair_data.get('reserve0', 0))
                pair.reserve1 = float(pair_data.get('reserve1', 0))
            except ValueError:
                pair.reserve0 = 0
                pair.reserve1 = 0
            pairs.append(pair)
        
        return pairs
    
    def fetch_specific_pair(self, token0_id, token1_id):
        token0_id = token0_id.lower()
        token1_id = token1_id.lower()
        variables = {'token0_id': token0_id, 'token1_id': token1_id}
        
        response = self.send_query(FETCH_SPECIFIC_PAIR, variables)
        pairs_data = response.get('data', {})

        pair0_data = pairs_data.get('pair0', [])
        pair1_data = pairs_data.get('pair1', [])
        
        pair0 = Pair.from_json(pair0_data[0]) if pair0_data else None
        pair1 = Pair.from_json(pair1_data[0]) if pair1_data else None
        
        return pair0, pair1
