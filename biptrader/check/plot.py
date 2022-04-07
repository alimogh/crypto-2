""" plot :
    3/31/2022 8:04 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import pandas as pd

class Plot:
    fig : None

    # def __init__(self,df,rows=7,cols=1,row_heights=[0.46, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09],template="plotly_white"
    def __init__(self,df,rows=6,cols=1,row_heights=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1],template="plotly_white"
                 ,hover_pattern_name=None):
        self.df = df
        pio.templates.default = template
        self.fig = make_subplots(vertical_spacing = 0.1, rows=rows, cols=cols, row_heights=row_heights)
        self.fig.add_trace(self._get_candlestick(df,hover_pattern_name))

    def set_title(self,title):
        self.fig.update_layout(title=title)

    def add_trades(self):
        df = self.df
        buys = self._get_buys(df[df.profit==0][["Date","Close"]].to_numpy())
        sells = self._get_sells(df[(df.profit.notnull()) & (df.profit!=0)][["Date","Close"]].to_numpy())
        self.fig.add_trace([buys,sells], row=1, col=1)

    def add_signals(self):
        df = self.df
        buys = self._get_buys(df[df.signal=="BUY"][["Date","Close"]].to_numpy())
        sells = self._get_sells(df[df.signal=="SELL"][["Date","Close"]].to_numpy())
        self.fig.add_trace(buys, row=1, col=1)
        self.fig.add_trace(sells, row=1, col=1)

# fig.add_trace(go.Scatter(x=df['Date'], y = df['mavg']), row=2, col=1)
# fig.add_trace(go.Scatter(x=df['Date'], y = df['mavg']*1.1), row=2, col=1)
# fig.add_trace(go.Bar(x=df['Date'], y = df['AAPL.Volume']), row=3, col=1)
#
# fig.update_layout(xaxis_rangeslider_visible=False,
#                   xaxis=dict(zerolinecolor='black', showticklabels=False),
#                   xaxis2=dict(showticklabels=False))
#

    def show(self):
        self.fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=False)
        self.fig.show()

    def _get_candlestick(self,df,hover_pattern_name=None):
        return go.Candlestick(x=df['Date'],
                              open=df['Open'],
                              high=df['High'],
                              low=df['Low'],
                              close=df['Close'],
                              hovertext=self.df[hover_pattern_name] if hover_pattern_name else None,
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

    def add_scatter(self,df,y,x="Date",title=None,row=2,col=1):
        scatter = go.Scatter(
            x=df[x],
            y=df[y],
            name=title,
        )
        self.fig.add_trace(scatter, row=row, col=col)

    def add_MACD(self,df,macd="macd",macdSignal="macdSignal",macdHist="macdHist",macd_test="macd_test",row=3,col=1):
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[macd]      ,name=macd, ), row=row, col=col)
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[macdSignal],name=macdSignal, ), row=row, col=col)
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[macdHist]  ,name=macdHist, ), row=row, col=col)

        # macd_test_df = df[df[macd_test]==1]
        # self.fig.add_trace(
        #     go.Scatter(x=macd_test_df['Date'],y=macd_test_df[macd_test]+5 ,name=macd_test
        #         ,mode = "markers",marker_symbol="circle",marker_size=5,)
        #     , row=row, col=col)
        # # diamond, tar-triangle-down, triangle-down, diamond-tall, line-ns, y-down, y-up, x-thin

    def add_SMA(self,df,sma_f="sma_f",sma_s="sma_s",sma_r="sma_r",row=4,col=1):
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[sma_f] ,name=sma_f, ), row=row, col=col)
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[sma_s] ,name=sma_s, ), row=row, col=col)
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[sma_r] ,name=sma_r, ), row=row, col=col)

    def add_RSI(self,df,rsi="rsi",row=5,col=1):
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[rsi] ,name=rsi, ), row=row, col=col)

    def add_STOCH(self,df,stoch_k="stoch_k",stoch_d="stoch_d",row=6,col=1):
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[stoch_k] ,name=stoch_k, ), row=row, col=col)
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[stoch_d] ,name=stoch_d, ), row=row, col=col)

    def add_WMA(self,df,wma_m="wma_m",wma_f="wma_f",wma_s="wma_s",row=1,col=1):
        self.fig.add_trace( go.Scatter(x=df['Date'],y=df[wma_m] ,name=wma_f, ), row=row, col=col)
        # self.fig.add_trace( go.Scatter(x=df['Date'],y=df[wma_f] ,name=wma_f, ), row=row, col=col)
        # self.fig.add_trace( go.Scatter(x=df['Date'],y=df[wma_s] ,name=wma_s, ), row=row, col=col)

    def add_pattern(self,df,pattern='candlestick_pattern',row=1,col=1):
        # self.fig.update_layout(annotations=[
        #     go.layout.Annotation(x=row['Date'],
        #                          y=row['High'],
        #                          text=row['candlestick_pattern'],
        #                          align='center',
        #                          showarrow=False,
        #                          yanchor='bottom',
        #                          textangle=90) for row in df.iterrows()])
        df_filter = df[df[pattern]!='']
        self.fig.add_trace( go.Scatter(x=df_filter['Date'], y=df_filter['High']
                ,mode="markers"
                ,hovertext=df_filter[pattern]
                ,marker_symbol="star"
                ,marker_color="purple"
                ,name="pattern_recognition"
                ,marker_size=5
        ) , row=row, col=col)
