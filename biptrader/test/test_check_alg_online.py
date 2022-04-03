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
from biptrader.check.pattern_recognition import CandlestickPattern


class TestCheckTradeAlgorithmOnline(TestCase):


    def test_check_all(self):
        # self.fail()
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_all(alg.recommendation,years=5)
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

    def test_plot_DASHUSD_lastmonth_1h_MACD_SMA_RSI_STOCH(self):
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

