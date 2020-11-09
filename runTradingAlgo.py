import os, sys, argparse
import pandas
import backtrader
from backtrader import Cerebro
from strategies.BuyAndHold import BuyAndHold
from strategies.GoldenCross import GoldenCross

cerebro = backtrader.Cerebro()

pricesData = pandas.read_csv('SPY.csv', index_col='Date', parse_dates=True)

# initializing Cerebro 
cerebro = Cerebro()
cerebro.broker.setcash(100000)

feed = backtrader.feeds.PandasData(dataname=pricesData)  # add data feed
cerebro.adddata(feed)

strategies = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyAndHold
}


parser = argparse.ArgumentParser()   # parse command line arguments
parser.add_argument("strategy", help="Which strategy to run", type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("Invalid strategy, must select one of {}".format(strategies.keys()))
    sys.exit()

cerebro.addstrategy(strategy=strategies[args.strategy])
cerebro.run()
cerebro.plot()  # plot the chart