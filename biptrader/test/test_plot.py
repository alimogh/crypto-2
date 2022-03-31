""" test_plot :
    3/30/2022 12:29 PM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase

import pandas as pd


class TestPlot(TestCase):

    def test_plotly(self):
        import plotly.graph_objects as go
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        print(df)
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                             open=df['AAPL.Open'],
                                             high=df['AAPL.High'],
                                             low=df['AAPL.Low'],
                                             close=df['AAPL.Close']
                                             )])
        fig.show()

    def test_plotly_buy_signals(self):
        import plotly.graph_objects as go
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        df = df[df.Date>"2016-12-01"]

        candle = go.Candlestick(x=df['Date'],
                                open=df['AAPL.Open'],
                                high=df['AAPL.High'],
                                low=df['AAPL.Low'],
                                close=df['AAPL.Close']
                                )

        buy_signals = [["2017-02-01",127.010002]
            ,["2017-01-03",114.760002]
            ,["2016-12-01",109.029999]]
        buys = go.Scatter(
            x=[item[0] for item in buy_signals],
            y = [item[1] for item in buy_signals],
            name = "Buy Signals",
            mode = "markers",
            marker_symbol="triangle-up",
            marker_color="yellow",
            marker_size=15,
        )

        sell_signals = [["2017-02-15",135.520004]
            ,["2017-01-13",119.110001]
            ,["2016-12-15",115.379997]]
        sells = go.Scatter(
            x=[item[0] for item in sell_signals],
            y = [item[1] for item in sell_signals],
            name = "Sell Signals",
            mode = "markers",
            marker_symbol="triangle-down",
            marker_color="blue",
            marker_size=15,
        )

        macdh=go.Scatter(
            x=df['Date'],
            y=df['mavg'],
            name="Macdh",
            line = dict(color=('rgba(102, 207, 255, 50)')))


        fig = go.Figure(data=[candle,sells,buys,macdh])
        fig.show()


    def test_mplfinance(self):
        import mplfinance as mpf
        # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv',index_col=0,parse_dates=True)
        df = pd.read_csv('../data/dash-daily-20170101-20220330-yahoo.csv',index_col=0,parse_dates=True)
        mpf.plot(df, type='candle', style='yahoo', volume=True)
