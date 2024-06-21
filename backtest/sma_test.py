from __future__ import (absolute_import, division, print_function, unicode_literals)
import datetime
import os.path
import backtrader as bt
from logger import setup_logger

logger = setup_logger('SmaStrategyLogger')

class SmaStrategy(bt.Strategy):

    params = (
        ('short_period', 15),
        ('long_period', 200),
        ('comm', 0.0),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None

        self.smashort = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.short_period)
        self.smalong = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.long_period)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
                logger.info(f'BUY EXECUTED, Price: {self.buyprice}, Cost: {order.executed.value}, Comm: {self.buycomm}')
            else:
                self.bar_executed = len(self)
                logger.info(f'SELL EXECUTED, Price: {order.executed.price}, Cost: {order.executed.value}, Comm: {order.executed.comm}')

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            logger.warning('Order Canceled/Margin/Rejected')
            self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        logger.info(f'TRADE PROFIT, GROSS {trade.pnl}, NET {trade.pnlcomm}')

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.smashort[0] > self.smalong[0]:
                self.order = self.buy()
                logger.info(f'BUY CREATE, {self.dataclose[0]}')
        else:
            if self.smashort[0] < self.smalong[0]:
                self.order = self.sell()
                logger.info(f'SELL CREATE, {self.dataclose[0]}')

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(SmaStrategy, short_period=15, long_period=200, comm=0.001)
    datapath = 'data/BTC-USD.csv'
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2023, 6, 18),
        todate=datetime.datetime(2024, 6, 18),
        reverse=False
    )
    cerebro.adddata(data)
    cerebro.broker.setcash(100000)
    logger.info(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")
    cerebro.run()
    logger.info(f"Ending Portfolio Value: {cerebro.broker.getvalue()}")
