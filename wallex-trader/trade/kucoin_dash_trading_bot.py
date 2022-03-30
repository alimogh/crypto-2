import time
from datetime import datetime
import pandas as pd
import numpy as np
import ccxt
import talib
# from config import wazirx_config

# TRADING API KEY & SECRET
# kucoin
from trade.mykucoin import MyKucoin

API_PASSPHRASE = "ldaram2648"
API_KEY = '618ce81a3f018700015de3ac'
API_SECRET = '02d62fe2-2bce-4411-aa4a-d5126c573fb8'

# Initialize Variables
CANDLE_DURATION_IN_MIN = 1

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

# CCXT_TICKER_NAME = 'BTC/USDT'
CCXT_TICKER_NAME = 'DASH/USDT'
TRADING_TICKER_NAME = 'dashusdt'

# INVESTMENT_AMOUNT_DOLLARS = 10
INVESTMENT_AMOUNT_DOLLARS = 1
# HOLDING_QUANTITY = 0
HOLDING_QUANTITY = 1

# exchange = ccxt.kucoin()
# exchange = ccxt.kucoin({
#     'adjustForTimeDifference': True,
#     "apiKey": API_KEY,
#     "secret": API_SECRET,
#     'password': '550525',
# })

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

# wx_client = Client(api_key=API_KEY, secret_key=API_SECRET)

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

    macd_result = 'WAIT'
    final_result = 'WAIT'

    # BUY or SELL based on MACD crossover points and the RSI value at that point
    macd, signal, hist = talib.MACD(ticker_df['close'], fastperiod = 12, slowperiod = 26, signalperiod = 9)
    last_hist = hist.iloc[-1]
    prev_hist = hist.iloc[-2]
    if not np.isnan(prev_hist) and not np.isnan(last_hist):
        # If hist value has changed from negative to positive or vice versa, it indicates a crossover
        macd_crossover = (abs(last_hist + prev_hist)) != (abs(last_hist) + abs(prev_hist))
        if macd_crossover:
            macd_result = 'BUY' if last_hist > 0 else 'SELL'

    if macd_result != 'WAIT':
        rsi = talib.RSI(ticker_df['close'], timeperiod = 14)
        # Consider last 3 RSI values
        last_rsi_values = rsi.iloc[-3:]

        if (last_rsi_values.min() <= RSI_OVERSOLD):
            final_result = 'BUY'
        elif (last_rsi_values.max() >= RSI_OVERBOUGHT):
            final_result = 'SELL'

    return final_result


# STEP 3: EXECUTE THE TRADE
in_position = False
def execute_trade(trade_rec_type, trading_ticker):
    # global wx_client, HOLDING_QUANTITY
    global HOLDING_QUANTITY,in_position
    order_placed = False
    side_value = 'buy' if (trade_rec_type == "BUY") else 'sell'
    try:
        # ticker_price_response = wx_client.send("ticker", { "symbol": trading_ticker})
        # ticker_price_response = exchange.createOrder('ADA/USDT:USDT', 'limit', 'buy', 1, 1, {'leverage': 10})
        ticker_price_response = exchange.fetch_ticker(trading_ticker)
        print(ticker_price_response)
        if (ticker_price_response[0] in [200, 201]):
            current_price = float(ticker_price_response[1]['lastPrice'])

            scrip_quantity = round(INVESTMENT_AMOUNT_DOLLARS/current_price,5) if trade_rec_type == "BUY" else HOLDING_QUANTITY
            print(f"PLACING ORDER {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: "
                  f"{trading_ticker}, {side_value}, {current_price}, {scrip_quantity}, {int(time.time() * 1000)} ")

            # order_response = wx_client.send("create_order",
            #                             {"symbol": trading_ticker, "side": side_value, "type": "limit",
            #                              "price": current_price, "quantity": scrip_quantity,
            #                              "recvWindow": 10000, "timestamp": int(time.time() * 1000)})
            if trade_rec_type == "BUY":
                order = exchange.create_market_buy_order(trading_ticker, scrip_quantity)
                print(order)
            elif trade_rec_type == "SELL":
                order = exchange.create_market_sell_order(trading_ticker, scrip_quantity)
                print(order)

            print(f"ORDER PLACED")
            HOLDING_QUANTITY = scrip_quantity if trade_rec_type == "BUY" else HOLDING_QUANTITY
            order_placed = True
    except:
        print(f"\nALERT!!! UNABLE TO COMPLETE ORDER")

    return order_placed


def run_bot_for_ticker(ccxt_ticker, trading_ticker):
    print('run_bot_for_ticker(ccxt_ticker=%s, trading_ticker=%s)'%(ccxt_ticker, trading_ticker))

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

