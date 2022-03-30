""" test_kucoin_market_buy_sell_order :
    3/28/2022 9:52 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase
import ccxt

# class MyKucoin(ccxt.kucoin):
#     def describe(self):
#         d = super().describe()
#         d['urls']['api']['public']='https://api.kucoin.com'
#         d['urls']['api']['private']='https://api.kucoin.com'
#         return d
#
#
class MyKucoin(ccxt.kucoin):
    def describe(self):
        d = super().describe()
        d['urls']['api']['public']='https://api.kucoin.com'
        d['urls']['api']['private']='https://api.kucoin.com'
        return d

class Test(TestCase):

    CCXT_TICKER_NAME = 'DASH/USDT'
    TRADING_TICKER_NAME = 'dashusdt'

    API_PASSPHRASE = "ldaram2648"
    API_KEY = '618ce81a3f018700015de3ac'
    API_SECRET = '02d62fe2-2bce-4411-aa4a-d5126c573fb8'
    exchange = MyKucoin({
        'adjustForTimeDifference': True,
        "apiKey": API_KEY,
        "secret": API_SECRET,
        'password': API_PASSPHRASE,
    })

    def setUp(self) -> None:
        super().setUp()

    def test_fetch_ticker(self):
        ticker_price_response = self.exchange.fetch_ticker(self.CCXT_TICKER_NAME)
        print(ticker_price_response)

    def test_fetch_balance(self):
        balance = self.exchange.fetch_balance()
        print(balance)


    def test_kucoin_market_buy_order(self):
        order = self.exchange.create_market_buy_order(self.CCXT_TICKER_NAME, 0.002)
        print(order)

    def test_kucoin_market_sell_order(self):
        order = self.exchange.create_market_sell_order(self.CCXT_TICKER_NAME, 0.002)
        print(order)