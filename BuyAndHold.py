import backtrader

class BuyAndHold(backtrader.Strategy):
    def start(self):
        self.startValue = self.broker.get_cash()  # get the starting cash and assign it as startValue

    def buyStart(self):
        print("buy start")  # Buys the stock using all the available cash
        print(self.broker.get_cash())
        size = int(self.broker.get_cash() / self.data)
        self.buy(size=size)

    def buyStop(self):  # return the ROI
        self.roi = (self.broker.get_value() / self.startValue) - 1.0
        print('ROI:        {:.2f}%'.format(100.0 * self.roi))