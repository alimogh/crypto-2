""" test_check_alg_online :
    3/31/2022 10:34 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase
# from biptrader.check.check_alg_online import CheckTradeAlgorithmOnline
# from biptrader.algorithms import MACD_crossover_points_RSI_of_point
from biptrader import CheckTradeAlgorithmOnline, Plot
from biptrader import MACD_crossover_points_RSI_of_point
from biptrader.algorithms.wma_cross import WMA_cross_point
from biptrader.check.pattern_recognition import CandlestickPattern


class TestCheckTradeAlgorithmOnline(TestCase):


    def test_check_all(self):
        # self.fail()
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_all(alg.recommendation,period="5y")
        # checker.check_all(getattr(alg,"recommendation"))
        print(checker.df_conclusion.to_string())

    def test_plot_ETHUSD(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastyears(alg.recommendation, "ETH-USD")
        p = Plot(checker.df)
        p.set_title(checker.get_summary())
        p.add_signals()
        p.show()

    def test_plot_DASHUSD(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastyears(alg.recommendation, "DASH-USD",years=1)
        p = Plot(checker.df)
        p.set_title(checker.get_summary())
        p.add_signals()
        p.show()

    def test_plot_DASHUSD_lastmonth_1h(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastmonths(alg.recommendation, "DASH-USD",months=1,interval="1h")
        p = Plot(checker.df)
        p.set_title(checker.get_summary())
        p.add_signals()
        p.show()

    def test_plot_DASHUSD_lastday_1m(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastdays(alg.recommendation, "DASH-USD",days=1,interval="1m")
        p = Plot(checker.df)
        p.set_title(checker.get_summary())
        p.add_signals()
        p.show()

    def test_plot_DASHUSD_lastmonth_1h_MACD_SMA_RSI_STOCH_WMA(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastmonths(alg.recommendation, "DASH-USD",months=1,interval="1h")
        analysis = checker.get_technical_indicators()
        p = Plot(checker.df)
        p.set_title(checker.get_summary())
        p.add_signals()
        p.add_MACD(analysis)
        p.add_SMA(analysis)
        p.add_RSI(analysis)
        p.add_STOCH(analysis)
        p.add_WMA(analysis)
        p.show()

    def test_plot_DASHUSD_lastmonth_1h_PatternRecognition(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastmonths(alg.recommendation, "DASH-USD",months=1,interval="1h")
        patterns = checker.get_patterns()
        # p = Plot(checker.df,rows=2,row_heights=[0.8,0.2])
        p = Plot(patterns,rows=2,row_heights=[0.8,0.2])
        p.set_title(checker.get_summary())
        p.add_signals()
        p.add_pattern(patterns)
        p.show()


    def test_plot_DASHUSD_lastmonth_1h_WMA(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastmonths(alg.recommendation, "DASH-USD",months=1,interval="1h")
        analysis = checker.get_technical_indicators()
        p = Plot(checker.df,rows=2,cols=1,row_heights=[0.8,0.2])
        p.set_title(checker.get_summary())
        p.add_WMA(analysis)
        p.show()

    def test_plot_DASHUSD_lastmonth_5m_WMA(self):
        checker = CheckTradeAlgorithmOnline()
        alg = WMA_cross_point()
        checker.recommander_title="WMA_cross_point"
        checker.check_lastmonths(alg.recommendation, "DASH-USD",months=1,interval="5m")
        analysis = checker.get_technical_indicators()
        p = Plot(checker.df,rows=2,cols=1,row_heights=[0.8,0.2])
        p.set_title(checker.get_summary())
        p.add_signals()
        p.add_WMA(analysis)
        p.show()

    def test_plot_DASHUSD_mar_8_9_5m_WMA(self):
        checker = CheckTradeAlgorithmOnline()
        alg = WMA_cross_point()
        checker.recommander_title="WMA_cross_point"
        checker.check_recommender(alg.recommendation, "DASH-USD",start="2022-03-08",end="2022-03-10",interval="5m")
        analysis = checker.get_technical_indicators()
        p = Plot(checker.df,rows=2,cols=1,row_heights=[0.8,0.2])
        p.set_title(checker.get_summary())
        p.add_signals()
        p.add_WMA(analysis)
        p.show()

    def test_plot_DASHUSD_2month_5m_WMA(self):
        checker = CheckTradeAlgorithmOnline()
        alg = WMA_cross_point()
        checker.recommander_title="WMA_cross_point"
        checker.check_lastdays(alg.recommendation, "DASH-USD",days=60,interval="5m")
        analysis = checker.get_technical_indicators()
        p = Plot(checker.df,rows=2,cols=1,row_heights=[0.8,0.2])
        p.set_title(checker.get_summary())
        p.add_signals()
        p.add_WMA(analysis)
        p.show()

    def test_plot_DASHUSD_lastmonth_1m_WMA(self):
        checker = CheckTradeAlgorithmOnline()
        alg = WMA_cross_point()
        checker.recommander_title="WMA_cross_point"
        # checker.check_lastdays(alg.recommendation, "DASH-USD",days=15,interval="5m")
        checker.check_recommender(alg.recommendation, "DASH-USD",start="2022-03-22",end="2022-03-24",interval="5m") #30=>+8, 10=>
        # checker.check_recommender(alg.recommendation, "DASH-USD",start="2022-04-06",end="2022-04-07",interval="5m") # -1.3
        # checker.check_recommender(alg.recommendation, "DASH-USD",start="2022-04-05",end="2022-04-06",interval="5m") # 30=>-3.4 ,10=>0.8
        analysis = checker.get_technical_indicators()
        p = Plot(checker.df,rows=2,cols=1,row_heights=[0.8,0.2])
        p.set_title(checker.get_summary())
        p.add_signals()
        p.add_WMA(analysis)
        p.show()

    def test_check_all_WMA_cross_point(self):
        # self.fail()
        checker = CheckTradeAlgorithmOnline()
        alg = WMA_cross_point()
        checker.recommander_title="WMA_cross_point"
        # checker.check_all(alg.recommendation,period="3d",interval="1m")
        # checker.check_lastdays(alg.recommendation,tickers="DASH-USD",days=7,interval="5m")
        checker.check_recommender(alg.recommendation,tickers="DASH-USD",period="60d",interval="5m")
        # checker.check_recommender(alg.recommendation,tickers="DASH-USD",period="7d",interval="1m")
        print(checker.df_conclusion.to_string())

