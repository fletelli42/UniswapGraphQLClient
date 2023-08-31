import json
import requests
from api.gql_queries import FETCH_TOKEN_QUERY, FETCH_PAIRS_FOR_TOKEN_QUERY, FETCH_SWAP_TRANSACTIONS_QUERY
from models.pair import Pair
from models.token import Token
from models.transaction import Transaction


class UniswapClient:

    def __init__(self, endpoint='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'):
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
