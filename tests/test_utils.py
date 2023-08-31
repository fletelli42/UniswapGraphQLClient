# tests/test_utils.py

import unittest
from utils.some_util_function import some_util_function  # Replace this with your actual import

class TestUtils(unittest.TestCase):

    def test_some_util_function(self):
        result = some_util_function('some_argument')
        self.assertEqual(result, 'expected_result')


if __name__ == '__main__':
    unittest.main()
