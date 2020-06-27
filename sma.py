import backtrader as bt

# Create a subclass of Strategy to define the indicators and logic

class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,     # period for the fast moving average data0
        pslow=30,     # period for the slow moving average data0
        pfast_d1=10,  # period for the fast moving average data1
        pslow_d1=30   # period for the slow moving average data1
    )

    def __init__(self):
        # Indicators for data0 the 
        sma1 = bt.ind.SMA(period=int(self.p.pfast))  # fast moving average
        sma2 = bt.ind.SMA(period=int(self.p.pslow))  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

        # Indicators for data1
        sma1_d1 = bt.ind.SMA(self.data1,period=int(self.p.pfast_d1))  # fast moving average
        sma2_d1 = bt.ind.SMA(self.data1,period=int(self.p.pslow_d1))  # slow moving average
        self.crossover_d1 = bt.ind.CrossOver(sma1_d1, sma2_d1)  # crossover signal


    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0 and self.crossover_d1 > 0:  # if fast crosses slow to the upside in both datas
                self.buy()  # enter long

        elif self.crossover < 0 and self.crossover_d1 < 0:  # in the market & both cross to the downside
            self.close()  # close long position
