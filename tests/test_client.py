# tests/test_client.py

import unittest
from client import UniswapClient

class TestUniswapClient(unittest.TestCase):

    def setUp(self):
        self.client = UniswapClient()

    def test_fetch_token(self):

        response = self.client.fetch_token('some_token_id')
        self.assertIsInstance(response, dict)
    
    def test_fetch_pairs_for_token(self):
    
        response = self.client.fetch_pairs_for_token('some_token_id')
        self.assertIsInstance(response, list)

if __name__ == '__main__':
    unittest.main()
