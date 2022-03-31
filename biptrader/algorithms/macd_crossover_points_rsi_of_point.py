""" MACD_crossover_points_RSI_of_point :
    3/31/2022 9:05 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import numpy as np
import talib

class MACD_crossover_points_RSI_of_point:

    def recommendation(self,ticker_df):
        RSI_PERIOD = 14
        RSI_OVERBOUGHT = 70
        RSI_OVERSOLD = 30

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
