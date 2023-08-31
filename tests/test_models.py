# tests/test_models.py

import unittest
from models.pair import Pair
from models.token import Token
from models.transaction import Transaction

class TestModels(unittest.TestCase):

    def test_pair_model(self):
        pair = Pair('token0_id', 'token1_id')
        self.assertEqual(pair.token0_id, 'token0_id')
        self.assertEqual(pair.token1_id, 'token1_id')

    def test_token_model(self):
        token = Token('some_id', 'some_symbol')
        self.assertEqual(token.token_id, 'some_id')
        self.assertEqual(token.symbol, 'some_symbol')
        
    def test_transaction_model(self):
        transaction = Transaction('some_hash')
        self.assertEqual(transaction.tx_hash, 'some_hash')

# More tests can go here...

if __name__ == '__main__':
    unittest.main()
