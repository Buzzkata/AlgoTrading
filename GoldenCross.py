import os, math
import sys
import backtrader
import pandas

class GoldenCross(backtrader.Strategy):
    params = (('fast', 50),
              ('slow', 200),
              ('order_pct', 0.95),
              ('ticker', 'SPY'))

    def __init__(self):
        self.fastma = backtrader.indicators.SimpleMovingAverage(
            self.data.close, 
            period=self.p.fast, 
            plotname='50 day'
        )

        self.slowma = backtrader.indicators.SimpleMovingAverage(
            self.data.close, 
            period=self.p.slow, 
            plotname='200 day'
        )

        self.crossover = backtrader.indicators.CrossOver(
            self.fastma, 
            self.slowma
        )

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:  # We buy when the crossover is bigger than 0, meaning a golden cross has occured.
                amount = (self.p.order_pct * self.broker.cash)
                self.size = math.floor(amount / self.data.close)

                print("Buy {} shares of {} at {}".format(self.size, self.p.ticker, self.data.close[0]))
                self.buy(size=self.size)
            
        if self.position.size > 0:
            if (self.crossover < 0): # We sell when the crossover is less than 0, meaning a death cross has occured (which indicates bearish price movement).
                print("Sell {} shares of {} at {}".format(self.size, self.p.ticker, self.data.close[0]))
                self.close()