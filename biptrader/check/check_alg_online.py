""" check_alg_online :
    3/31/2022 9:26 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import datetime

import pandas as pd

# from check_alg import CheckTradeAlgorithm
import yfinance as yf

from biptrader import CheckTradeAlgorithm


class CheckTradeAlgorithmOnline(CheckTradeAlgorithm):

    # df_conclusion:pd.DataFrame(data=[[]],columns=["recommender","ticker","start","end","interval","init_invest","revenue","profit"])
    recommander_title=None
    df_conclusion=pd.DataFrame(columns=["recommender","ticker","start","end","interval","init_invest","buy_count","sell_count","revenue","profit","remain"])
    popular_tickers=["AAPL","TSLA","BTC-USD","ETH-USD","DASH-USD"]

    def __init__(self):
        super(CheckTradeAlgorithmOnline, self).__init__()

    def check_recommender(self,fn_recommendation,tickers,period="max",start=None,end=None,interval="1d"):
        self.__init__()
        self.df = yf.download(tickers,start=start,end=end,
                              progress=False,interval=interval,period=period)
        if not "Date" in self.df.columns:
            self.df.reset_index(inplace=True)
            if "Datetime" in self.df.columns:
                self.df = self.df.rename(columns = {'Datetime':'Date'})
            else:
                self.df = self.df.rename(columns = {'index':'Date'})
        self.signal(fn_recommendation)
        self.calculate_profit()
        new_row = {"recommender": (self.recommander_title if self.recommander_title else fn_recommendation.__name__)
            ,"ticker":tickers
            ,"start":start
            ,"end":end
            ,"interval":interval
            ,"init_invest":self.INVESTMENT_AMOUNT_DOLLARS
            ,"buy_count":self.get_buy_signal_count()
            ,"sell_count":self.get_sell_signal_count()
            ,"revenue":self.get_revenue()
            ,"profit":self.get_profit()
            ,"remain":self.INVESTMENT_AMOUNT_DOLLARS
        }
        # self.df_conclusion = self.df_conclusion.append(new_row,ignore_index=True) #FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
        self.df_conclusion = pd.concat([self.df_conclusion,pd.Series(new_row)],ignore_index=True)

    def check_lastyears(self,fn_recommendation,tickers,years=1,interval="1d"):
        year = datetime.date.today().year
        start = "%i-01-01"%(year-years)
        end = "%i-12-31"%(year-1)
        self.check_recommender(fn_recommendation,tickers,start=start,end=end,interval=interval)

    def check_lastmonths(self,fn_recommendation,tickers,months=1,interval="1h"):
        self.check_recommender(fn_recommendation,tickers,period="%imo"%(months),start=None,end=None,interval=interval)

    def check_lastdays(self,fn_recommendation,tickers,days=1,interval="1m"):
        self.check_recommender(fn_recommendation,tickers,period="%id"%(days),start=None,end=None,interval=interval)

    def check_all(self,fn_recommendation,years=1,interval="1d"):
        for ticker in self.popular_tickers:
            self.check_lastyears(fn_recommendation,ticker,years,interval)

    def check_AAPL_5_year(self,fn_recommendation):
        self.check_lastyears(fn_recommendation,"AAPL",years=5)

    def check_TSLA_5_year(self,fn_recommendation):
        self.check_lastyears(fn_recommendation,"TSLA",years=5)

    def check_BTC_5_year(self,fn_recommendation):
        self.check_lastyears(fn_recommendation,"BTC-USD",years=5)

    def check_ETH_5_year(self,fn_recommendation):
        self.check_lastyears(fn_recommendation,"ETH-USD",years=5)

    def check_DASH_5_year(self,fn_recommendation):
        self.check_lastyears(fn_recommendation,"DASH-USD",years=5)

