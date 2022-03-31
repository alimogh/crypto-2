""" check-macd-dash-kucoin :
    3/30/2022 8:59 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import numpy
import numpy as np
import pandas as pd
import talib
import plotly.graph_objects as go
# https://plotly.com/python/marker-style/
import yfinance as yf

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
INVESTMENT_AMOUNT_DOLLARS=100


def get_trade_recommendation(ticker_df):

    macd_result = 'WAIT'
    final_result = 'WAIT'

    # BUY or SELL based on MACD crossover points and the RSI value at that point
    macd, signal, hist = talib.MACD(ticker_df['Close'], fastperiod = 12, slowperiod = 26, signalperiod = 9)
    last_hist = hist.iloc[-1]
    prev_hist = hist.iloc[-2]
    if not np.isnan(prev_hist) and not np.isnan(last_hist):
        # If hist value has changed from negative to positive or vice versa, it indicates a crossover
        macd_crossover = (abs(last_hist + prev_hist)) != (abs(last_hist) + abs(prev_hist))
        if macd_crossover:
            macd_result = 'BUY' if last_hist > 0 else 'SELL'

    if macd_result != 'WAIT':
        rsi = talib.RSI(ticker_df['Close'], timeperiod = 14)
        # Consider last 3 RSI values
        last_rsi_values = rsi.iloc[-3:]

        if (last_rsi_values.min() <= RSI_OVERSOLD):
            final_result = 'BUY'
        elif (last_rsi_values.max() >= RSI_OVERBOUGHT):
            final_result = 'SELL'

    return final_result

def plot_show(df,title):
    candle = go.Candlestick(x=df['Date'],
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close']
                            )

    buy_signals = df[df.profit==0][["Date","Close"]].to_numpy()
    print(buy_signals)

    buys = go.Scatter(
        x=[item[0] for item in buy_signals],
        y = [item[1] for item in buy_signals],
        name = "Buy Signals",
        mode = "markers",
        marker_symbol="triangle-up",
        marker_color="yellow",
        marker_size=15,
    )

    sell_signals = df[(df.profit.notnull()) & (df.profit!=0)][["Date","Close"]].to_numpy()
    print(sell_signals)

    sells = go.Scatter(
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


    fig = go.Figure(data=[candle,sells,buys])
    # fig = go.Figure(data=[candle])

    fig.update_layout(title=title)

    fig.show()


# df = pd.read_csv("dash-daily-20220101-20220330-yahoo.csv",header=0)
df = pd.read_csv("../data/dash-daily-20170101-20220330-yahoo.csv", header=0)
# df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by=["Date"],ascending=True,inplace=True)
df = df.reindex()
print(df)

# print(df[df.Date<"2022-01-05"])

counter =0
HOLDING_QUANTITY=None
for i,row in df.iterrows():
    if counter>0:
        ticker_df_before_date = df[df.Date<=row["Date"]]
        # print(ticker_df_before_date)
        signal = get_trade_recommendation(ticker_df_before_date)
        # row["signal"]=signal
        df._set_value(i,"signal",signal)

        current_price = float(row['Close'])
        if signal=="BUY" and not HOLDING_QUANTITY:
            HOLDING_QUANTITY = round(INVESTMENT_AMOUNT_DOLLARS/current_price,5)
            # df._set_value(i,"first_buy_first_sell",0)
            df._set_value(i,"revenue",-INVESTMENT_AMOUNT_DOLLARS)
            df._set_value(i,"profit",0)
        elif signal=="SELL" and HOLDING_QUANTITY:
            # revenue = (round(INVESTMENT_AMOUNT_DOLLARS/current_price,5) - HOLDING_QUANTITY)*current_price
            revenue = HOLDING_QUANTITY*current_price
            profit=revenue-INVESTMENT_AMOUNT_DOLLARS
            # df._set_value(i,"first_buy_first_sell",profit)
            df._set_value(i,"revenue",revenue)
            df._set_value(i,"profit",profit)
            INVESTMENT_AMOUNT_DOLLARS=revenue
            HOLDING_QUANTITY=None

        # print(row)
    counter+=1

    # if counter>2:break

print(df[df.signal!="WAIT"])
title = "total revenue=%f, profit=%f, remain=%f"%(df["revenue"].sum(),df["profit"].sum(),INVESTMENT_AMOUNT_DOLLARS)
print(title)

plot_show(df,title)
# plot_show(df[(df.Date>="2018-03-25") & (df.Date<="2018-03-30")])

