from sma_strategy import SmaStrategy
from ema_strategy import EmaStrategy
from rsi_strategy import RsiStrategy
from macd_strategy import MacdStrategy
from adx_strategy import AdxStrategy
from cci_strategy import CciStrategy
from backtest import run_backtest
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../Scalable-Backtesting-Infrastructure/kafka_scripts")))
from kafka_consumer import consume_backtest_request
from kafka_producer import send_backtest_results

sys.path.append(os.path.abspath(os.path.join("../Scalable-Backtesting-Infrastructure/mlflow")))
from mlflow_track import track

def main(strategy_name, start_date, end_date, params, start_cash, comm):
    strategy_map = {
        'sma': SmaStrategy,
        'ema': EmaStrategy,
        'rsi': RsiStrategy,
        'macd': MacdStrategy,
        'adx': AdxStrategy,
        'cci': CciStrategy
    }

    if strategy_name in strategy_map:
        strategy = strategy_map[strategy_name]
        results = run_backtest(strategy, params, 'data/BTC-USD.csv', start_date, end_date, start_cash, comm)
        
        # Extract desired metrics
        num_trades = results['trade_analyzer'].total.total
        #winning_trades = results['trade_analyzer'].won.total
        #losing_trades = results['trade_analyzer'].lost.total
        max_drawdown = results['drawdown'].max.drawdown
        sharpe_ratio = results['sharperatio']['sharperatio']

        metrics = {
            'Number of trades': num_trades,
            #'Winning trades': winning_trades,
            #'Losing trades': losing_trades,
            'Max drawdown': max_drawdown,
            'Sharpe ratio': sharpe_ratio
        }

        send_backtest_results(metrics)
        track(strategy, start_date, end_date, start_cash, comm, params, metrics)

        # Return extracted metrics
        return metrics
    else:
        print(f"Strategy {strategy_name} is not recognized.")
        return None

if __name__ == '__main__':
    for inputs in consume_backtest_request():
        print(inputs)
        results = main(*inputs)
        print(results)
