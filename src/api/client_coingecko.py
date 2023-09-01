import requests
import json
from models.coin import Coin
from utils.coin_utils import find_coin_id_by_symbol
import datetime

class CoinGeckoClient:

    BASE_URL = "https://api.coingecko.com/api/v3"

    @classmethod
    def fetch_historical_price(client, symbol, target_timestamp):
        coin_id = find_coin_id_by_symbol(symbol)

        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history"
        
        # Convert the timestamp to a datetime object and then to the required date format
        date = datetime.datetime.fromtimestamp(target_timestamp).strftime('%d-%m-%Y')
        
        params = {'date': date, 'localization': 'false'}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if 'market_data' is present in response
            if 'market_data' in data:
                usd_price = data['market_data']['current_price']['usd']
                return usd_price
            else:
                return None  # Could not fetch the price
        else:
            return None  # HTTP request failed

    @classmethod
    def fetch_coins_list(cls):
        url = f"{cls.BASE_URL}/coins/list"
        response = cls._send_request(url)
        return [Coin.from_json(coin) for coin in response]

    @staticmethod
    def _send_request(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
