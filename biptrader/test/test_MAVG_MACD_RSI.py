""" test_MAVG_MACD_RSI :
    4/1/2022 10:44 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import numpy as np
import pandas as pd
import talib as ta


df = pd.read_csv("../data/dash-daily-20220101-20220330-yahoo.csv",header=0)
# df = pd.read_csv("../data/dash-daily-20170101-20220330-yahoo.csv", header=0)
# df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by=["Date"],ascending=True,inplace=True)
df = df.reindex()
print(df)

# Technical Analysis
SMA_FAST = 50
SMA_SLOW = 200
RSI_PERIOD = 14
RSI_AVG_PERIOD = 15
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
STOCH_K = 14
STOCH_D = 3
SIGNAL_TOL = 3
Y_AXIS_SIZE = 12

analysis = pd.DataFrame(index = df.index)
# macd, signal, hist = ta.MACD(df['close'], fastperiod = 12, slowperiod = 26, signalperiod = 9)
print(df["Close"])
analysis['sma_f'] = df["Close"].rolling(SMA_FAST).mean()  # pd.rolling_mean(df.Close, SMA_FAST)  # module 'pandas' has no attribute 'rolling_mean'
analysis['sma_s'] = df["Close"].rolling(SMA_SLOW).mean()  # pd.rolling_mean(df.Close, SMA_SLOW)
analysis['rsi'] =   ta.RSI(df.Close.to_numpy(), RSI_PERIOD)  # ta.RSI(df.Close.as_matrix(), RSI_PERIOD) # AttributeError: 'Series' object has no attribute 'as_matrix'
analysis['sma_r'] = analysis['rsi'].rolling(RSI_AVG_PERIOD).mean()  # pd.rolling_mean(analysis.rsi, RSI_AVG_PERIOD) # check shift
analysis['macd'], analysis['macdSignal'], analysis['macdHist'] = ta.MACD(df.Close.to_numpy(), fastperiod=MACD_FAST, slowperiod=MACD_SLOW, signalperiod=MACD_SIGNAL) # ta.MACD(df.Close.as_matrix(), fastperiod=MACD_FAST, slowperiod=MACD_SLOW, signalperiod=MACD_SIGNAL)
analysis['stoch_k'], analysis['stoch_d'] = ta.STOCH(df.High.to_numpy(), df.Low.to_numpy(), df.Close.to_numpy(), slowk_period=STOCH_K, slowd_period=STOCH_D) # ta.STOCH(df.High.as_matrix(), df.Low.as_matrix(), df.Close.as_matrix(), slowk_period=STOCH_K, slowd_period=STOCH_D)

analysis['sma'] = np.where(analysis.sma_f > analysis.sma_s, 1, 0)
analysis['macd_test'] = np.where((analysis.macd > analysis.macdSignal), 1, 0)
analysis['stoch_k_test'] = np.where((analysis.stoch_k < 50) & (analysis.stoch_k > analysis.stoch_k.shift(1)), 1, 0)
analysis['rsi_test'] = np.where((analysis.rsi < 50) & (analysis.rsi > analysis.rsi.shift(1)), 1, 0)

print(analysis.to_string())