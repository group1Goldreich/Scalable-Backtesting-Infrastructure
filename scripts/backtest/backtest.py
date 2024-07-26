import backtrader as bt
import datetime


def run_backtest(strategy, strategy_params, data_path, start_date, end_date, start_cash, comm, stake=10):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy, **strategy_params)

    data = bt.feeds.YahooFinanceCSVData(
        dataname=data_path,
        fromdate=datetime.datetime.strptime(start_date, '%Y-%m-%d'),
        todate=datetime.datetime.strptime(end_date, '%Y-%m-%d'),
        reverse=False
    )

    cerebro.adddata(data)
    cerebro.broker.setcash(start_cash)
    cerebro.addsizer(bt.sizers.FixedSize, stake=stake)
    cerebro.broker.setcommission(commission=comm)

    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='tradeanalyzer')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharperatio')

    results = cerebro.run()

    res = results[0]

    trade_analyzer = res.analyzers.tradeanalyzer.get_analysis()
    drawdown = res.analyzers.drawdown.get_analysis()
    sharperatio = res.analyzers.sharperatio.get_analysis()

    return {
        'trade_analyzer': trade_analyzer,
        'drawdown': drawdown,
        'sharperatio': sharperatio,
        'final_value': cerebro.broker.getvalue()
    }
