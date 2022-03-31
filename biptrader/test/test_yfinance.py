""" test_yfinance :
    3/31/2022 8:43 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase

import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


class TestYFinance(TestCase):

    def test_TESLA(self):
        price_history = yf.Ticker('TSLA').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                          interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                          actions=False)
        print(type(price_history))
        print(price_history)

    def test_AAPL(self):
        aapl_df = yf.download('AAPL',
                              start='2019-01-01',
                              end='2021-06-12',
                              progress=False,
                              )
        aapl_df.head()

    def test_plot_AAPL(self):
        ticker = yf.Ticker('AAPL')
        aapl_df = ticker.history(period="5y")
        aapl_df['Close'].plot(title="APPLE's stock price")

    def test_BTC_USD(self):
        btc_df = yf.download('BTC-USD',
                              start='2019-01-01',
                              end='2021-06-12',
                              progress=False,
                              )
        btc_df.head()
        print(btc_df)

    def test_yahoo_financials(self):
        yahoo_financials = YahooFinancials('AAPL')
        data = yahoo_financials.get_historical_price_data(start_date='2019-01-01',
                                                          end_date='2019-12-31',
                                                          time_interval='weekly')
        aapl_df = pd.DataFrame(data['AAPL']['prices'])
        aapl_df = aapl_df.drop('date', axis=1).set_index('formatted_date')
        aapl_df.head()
        print(aapl_df)

    def test_btc_with_yahoo_finance(self):
        yahoo_financials = YahooFinancials('BTC-USD')
        data=yahoo_financials.get_historical_price_data("2019-07-10", "2021-05-30", "monthly")
        btc_df = pd.DataFrame(data['BTC-USD']['prices'])
        btc_df = btc_df.drop('date', axis=1).set_index('formatted_date')
        btc_df.head()
        print(btc_df)