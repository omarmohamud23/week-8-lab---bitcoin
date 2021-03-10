import unittest
from unittest import TestCase
from unittest.mock import patch, call
import bitcon

class TestBitCoins(TestCase):

    ## coversation is correct 
    @patch('bitcon.requests_rate')
    def test_convert(self, mock_rate ):
        mock_rate_float = 1234.56
        example_api_response={'bpi': 'USD', 'rate_float': mock_rate_float}
        mock_rate.side_effect = [example_api_response]
        conversion = bitcon.math_conversion(100, mock_rate_float)
        self.assertEqual(123456, conversion)

    ##Numbers only 
    @patch('builtins.input', side_effect=['2', '', 'cat', 'sdfa', 'dfs5'])
    def test_get_coins_input(self, mock_input):
        bicoins = bitcon.get_bitcoins()
        self.assertEqual(2, bicoins)
  



if __name__ == "__main__":
    unittest.main()