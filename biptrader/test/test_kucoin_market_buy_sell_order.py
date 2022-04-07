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
        order = self.exchange.create_market_buy_order(self.CCXT_TICKER_NAME, 0.001)
        print(order)
# {'id': '624e754b09b9040001c41913', 'clientOrderId': '1499576d-db1a-4006-aaf0-396af9033c1a'
    # , 'info': {'orderId': '624e754b09b9040001c41913'}, 'timestamp': 1649309004796, 'datetime': '2022-04-07T05:23:24.796Z'
    # , 'lastTradeTimestamp': None, 'symbol': 'DASH/USDT', 'type': 'market', 'side': 'buy', 'price': None
    # , 'amount': 0.01, 'cost': None, 'average': None, 'filled': None, 'remaining': None, 'status': None
    # , 'fee': None, 'trades': None}


    def test_kucoin_market_sell_order(self):
        order = self.exchange.create_market_sell_order(self.CCXT_TICKER_NAME, 0.001)
        print(order)
    # {'id': '624e759827218b0001e137d0', 'clientOrderId': '63c0189f-82c7-4112-a964-22f0a1037fdc'
    # , 'info': {'orderId': '624e759827218b0001e137d0'}, 'timestamp': 1649309081699, 'datetime': '2022-04-07T05:24:41.699Z'
    # , 'lastTradeTimestamp': None, 'symbol': 'DASH/USDT', 'type': 'market', 'side': 'sell', 'price': None
    # , 'amount': 0.01, 'cost': None, 'average': None, 'filled': None, 'remaining': None, 'status': None
    # , 'fee': None, 'trades': None}
