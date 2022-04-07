""" MACD_crossover_points_RSI_of_point :
    3/31/2022 9:05 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import numpy as np
import talib

class WMA_cross_point:

    def recommendation(self,ticker_df):
        wma_result = 'WAIT'
        final_result = 'WAIT'

        # BUY or SELL based on MACD crossover points and the RSI value at that point
        # wma = talib.WMA(ticker_df['Close'], timeperiod=50)
        # wma = talib.WMA(ticker_df['Close'], timeperiod=30)
        # wma = talib.WMA(ticker_df['Close'], timeperiod=20)
        wma = talib.WMA(ticker_df['Close'], timeperiod=10)

        wma_last = wma.iloc[-1]
        wma_prev = wma.iloc[-2]
        # wma_prev = wma.iloc[-6] if len(wma)>=6 else np.nan
        last_high = ticker_df['High'].iloc[-1]
        last_low = ticker_df['Low'].iloc[-1]
        prev_high = ticker_df['High'].iloc[-2]
        prev_low = ticker_df['Low'].iloc[-2]
        if not np.isnan(wma_last) \
                and not np.isnan(wma_prev) \
                and not np.isnan(last_high) \
                and not np.isnan(last_low) \
                and not np.isnan(prev_high) \
                and not np.isnan(prev_low):
            # if(wma_last>=last_low and wma_last<=last_high \
            #     and (wma_prev<prev_low-0.2 or wma_prev>prev_high+0.2)):
            #     wma_result = 'BUY' if wma_last<=last_low else 'SELL'
            if(wma_last<last_low or wma_last>last_high) \
                and (wma_prev>=prev_low and wma_prev<=prev_high):
                wma_result = 'BUY' if wma_last<=last_low else 'SELL'
            # if wma_last<last_low and wma_prev>=prev_low:
            #     wma_result = 'BUY'
            # elif wma_last>last_high and wma_prev<=prev_high:
            #     wma_result = 'SELL'

        if wma_result in ["BUY","SELL"]:
            print('signal:',wma_result,'last_high(%s)<=wma_last(%s)>=(%s)last_low'%(last_high,wma_last,last_low)
                  ,'prev_high(%s)<wma_prev(%s)>=(%s)prev_low'%(prev_high,wma_prev,prev_low))
        final_result = wma_result
        return final_result
