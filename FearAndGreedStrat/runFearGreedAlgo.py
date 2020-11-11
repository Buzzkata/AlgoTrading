import backtrader
from FearAndGreedStrategy import FearAndGreedStrategy


cerebro = backtrader.Cerebro()  # Initialize cerebro
cerebro.broker.setcash(100000)



class FearAndGreedData(backtrader.feeds.GenericCSVData):

    parameters = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('fear_greed', 4),
        ('volume', -1),
        ('openinterest', -1)
    )


fearGreedCsv = "data/fear-greed.csv"   # Load the data 
fearGreedFeed = FearGreedData(dataname=fearGreedCsv)

cerebro.adddata(fearGreedFeed)   # Feed the data into cerebro

cerebro.addstrategy(FearGreedStrategy)


cerebro.run()  # Run and plot
cerebro.plot(volume=False)