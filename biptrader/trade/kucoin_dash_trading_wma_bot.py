import time
from datetime import datetime
import pandas as pd
import numpy as np
import ccxt
import talib
# from config import wazirx_config

# TRADING API KEY & SECRET
# kucoin

API_PASSPHRASE = "ldaram2648"
API_KEY = '618ce81a3f018700015de3ac'
API_SECRET = '02d62fe2-2bce-4411-aa4a-d5126c573fb8'

# Initialize Variables
CANDLE_DURATION_IN_MIN = 1

CCXT_TICKER_NAME = 'DASH/USDT'
TRADING_TICKER_NAME = 'dashusdt'

INVESTMENT_AMOUNT_DOLLARS = 1
HOLDING_QUANTITY = 0.0

TICKER_OK_FLOAT_NO=3

class MyKucoin(ccxt.kucoin):
    def describe(self):
        d = super().describe()
        d['urls']['api']['public']='https://api.kucoin.com'
        d['urls']['api']['private']='https://api.kucoin.com'
        return d

exchange = MyKucoin({
    'adjustForTimeDifference': True,
    "apiKey": API_KEY,
    "secret": API_SECRET,
    'password': API_PASSPHRASE,
})

# STEP 1: FETCH THE DATA
def fetch_data(ticker):
    global exchange
    bars,ticker_df = None, None

    try:
        bars = exchange.fetch_ohlcv(ticker, timeframe=f'{CANDLE_DURATION_IN_MIN}m', limit=100)
    except:
        print(f"Error in fetching data from the exchange:{ticker}")

    if bars is not None:
        ticker_df = pd.DataFrame(bars[:-1], columns=['at', 'open', 'high', 'low', 'close', 'vol'])
        ticker_df['Date'] = pd.to_datetime(ticker_df['at'], unit='ms')
        ticker_df['symbol'] = ticker

    return ticker_df

# STEP 2: COMPUTE THE TECHNICAL INDICATORS & APPLY THE TRADING STRATEGY
def get_trade_recommendation(ticker_df):
    wma_result = 'WAIT'
    wma = talib.WMA(ticker_df['close'], timeperiod=10)
    wma_last = wma.iloc[-1]
    wma_prev = wma.iloc[-2]
    last_high = ticker_df['high'].iloc[-1]
    last_low = ticker_df['low'].iloc[-1]
    prev_high = ticker_df['high'].iloc[-2]
    prev_low = ticker_df['low'].iloc[-2]
    if not np.isnan(wma_last) \
            and not np.isnan(wma_prev) \
            and not np.isnan(last_high) \
            and not np.isnan(last_low) \
            and not np.isnan(prev_high) \
            and not np.isnan(prev_low):
        if wma_last<last_low and wma_prev>=prev_low:
            wma_result = 'BUY'
        elif wma_last>last_high and wma_prev<=prev_high:
            wma_result = 'SELL'
    # if wma_result in ["BUY","SELL"]:
    #     print('signal:',wma_result,'last_high(%s)<=wma_last(%s)>=(%s)last_low'%(last_high,wma_last,last_low)
    #           ,'prev_high(%s)<wma_prev(%s)>=(%s)prev_low'%(prev_high,wma_prev,prev_low))
    return wma_result


# STEP 3: EXECUTE THE TRADE
def execute_trade(trade_rec_type, trading_ticker):
    global HOLDING_QUANTITY,INVESTMENT_AMOUNT_DOLLARS
    order_placed = False
    try:
        ticker_price_response = exchange.fetch_ticker(trading_ticker)
        print("TICKER PRICE:",ticker_price_response)
        if (ticker_price_response['symbol'] ==CCXT_TICKER_NAME):
            current_price = float(ticker_price_response['last'])
            order_amount = round(INVESTMENT_AMOUNT_DOLLARS/current_price,TICKER_OK_FLOAT_NO) if trade_rec_type=="BUY" else HOLDING_QUANTITY

            print(f"PLACING ORDER {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: "
                  f"{trading_ticker}, {trade_rec_type}, {current_price}, {order_amount}, {HOLDING_QUANTITY}, {INVESTMENT_AMOUNT_DOLLARS}, {int(time.time() * 1000)} ")

            if trade_rec_type == "BUY":
                order = exchange.create_market_buy_order(trading_ticker, order_amount)
                if order['id']:
                    HOLDING_QUANTITY = order['amount']
                    INVESTMENT_AMOUNT_DOLLARS=0
            elif trade_rec_type == "SELL":
                order = exchange.create_market_sell_order(trading_ticker, order_amount)
                if order['id']:
                    HOLDING_QUANTITY = 0
                    INVESTMENT_AMOUNT_DOLLARS=order['amount']*current_price

            if order['id']:
                print(f"ORDER PLACED {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: "
                      f"{trading_ticker}, {trade_rec_type}, {current_price}, {order['amount']}, {HOLDING_QUANTITY}, {INVESTMENT_AMOUNT_DOLLARS}, {int(time.time() * 1000)}, {order['id']}, {order['clientOrderId']} ")
                order_placed = True
            else :
                print(f"NOT ORDER PLACED: {trading_ticker}, {trade_rec_type}, {current_price}, {order_amount}")

    except Exception as ex:
        print(f"\nALERT!!! UNABLE TO COMPLETE ORDER",ex)

    return order_placed


def run_bot_for_ticker(ccxt_ticker, trading_ticker):
    print(__file__,'run_bot_for_ticker(ccxt_ticker=%s, trading_ticker=%s)'%(ccxt_ticker, trading_ticker))

    currently_holding = False
    while 1:
        # STEP 1: FETCH THE DATA
        ticker_data = fetch_data(ccxt_ticker)
        if ticker_data is not None:
            # print('ticker_data=%s'%ticker_data)

            # STEP 2: COMPUTE THE TECHNICAL INDICATORS & APPLY THE TRADING STRATEGY
            trade_rec_type = get_trade_recommendation(ticker_data)
            print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}  TRADING RECOMMENDATION: {trade_rec_type}')

            # STEP 3: EXECUTE THE TRADE
            if (trade_rec_type == 'BUY' and not currently_holding) or \
                (trade_rec_type == 'SELL' and currently_holding):
                print(f'Placing {trade_rec_type} order')
                trade_successful = execute_trade(trade_rec_type,ccxt_ticker)
                currently_holding = not currently_holding if trade_successful else currently_holding


            time.sleep(CANDLE_DURATION_IN_MIN*60)
        else:
            print(f'Unable to fetch ticker data - {ccxt_ticker}. Retrying!!')
            time.sleep(5)

run_bot_for_ticker(CCXT_TICKER_NAME,TRADING_TICKER_NAME)

