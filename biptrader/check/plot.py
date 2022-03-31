""" plot :
    3/31/2022 8:04 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import plotly.graph_objects as go

class Plot:

    def show_with_trades(self,df,title):
        candle = self._get_candlestick(df)
        buys = self._get_buys(df[df.profit==0][["Date","Close"]].to_numpy())
        sells = self._get_sells(df[(df.profit.notnull()) & (df.profit!=0)][["Date","Close"]].to_numpy())
        fig = go.Figure(data=[candle,sells,buys])
        fig.update_layout(title=title)
        fig.show()

    def show_with_signals(self,df,title):
        candle = self._get_candlestick(df)
        buys = self._get_buys(df[df.signal=="BUY"][["Date","Close"]].to_numpy())
        sells = self._get_sells(df[df.signal=="SELL"][["Date","Close"]].to_numpy())
        fig = go.Figure(data=[candle,sells,buys])
        fig.update_layout(title=title)
        fig.show()

    def _get_candlestick(self,df):
        return go.Candlestick(x=df['Date'],
                              open=df['Open'],
                              high=df['High'],
                              low=df['Low'],
                              close=df['Close']
                              )

    def _get_buys(self,buy_signals):
        return go.Scatter(
            x=[item[0] for item in buy_signals],
            y = [item[1] for item in buy_signals],
            name = "Buy Signals",
            mode = "markers",
            marker_symbol="triangle-up",
            marker_color="yellow",
            marker_size=15,
        )

    def _get_sells(self,sell_signals):
        return go.Scatter(
            x=[item[0] for item in sell_signals],
            y = [item[1] for item in sell_signals],
            name = "Sell Signals",
            mode = "markers",
            marker_symbol="triangle-down",
            marker_color="blue",
            marker_size=15,
        )


        # macdh=go.Scatter(
        #     x=df['Date'],
        #     y=df['mavg'],
        #     name="Macdh",
        #     line = dict(color=('rgba(102, 207, 255, 50)')))
