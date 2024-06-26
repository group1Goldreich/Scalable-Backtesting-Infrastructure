from sma_strategy import SmaStrategy
from ema_strategy import EmaStrategy
from rsi_strategy import RsiStrategy
from macd_strategy import MacdStrategy
from adx_strategy import AdxStrategy
from cci_strategy import CciStrategy
from backtest import run_backtest
import sys
import os
import json

# sys.path.append(os.path.abspath(os.path.join("../Scalable-Backtesting-Infrastructure/kafka_scripts")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kafka_scripts.kafka_consumer import consume_backtest_request
from kafka_scripts.kafka_producer import send_backtest_results

# sys.path.append(os.path.abspath(os.path.join("../Scalable-Backtesting-Infrastructure/mlflow")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../mlflow')))

from mlflow_track import track

with open('./config.json', 'r') as f:
    data_config = json.load(f)


def main(name, strategy_name, start_date, end_date, params, start_cash, comm):
    strategy_map = {
        'sma': SmaStrategy,
        'ema': EmaStrategy,
        'rsi': RsiStrategy,
        'macd': MacdStrategy,
        'adx': AdxStrategy,
        'cci': CciStrategy
    }
    data_path = f'data/{data_config[name]}.csv'

    if strategy_name in strategy_map:
        strategy = strategy_map[strategy_name]
        results = run_backtest( strategy, params, data_path, start_date, end_date, start_cash, comm)
        
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
        print("----metrics",metrics)
        # send_backtest_results(metrics)
        track(name, strategy, start_date, end_date, start_cash, comm, params, metrics)

        # Return extracted metrics
        return metrics
    else:
        print(f"Strategy {strategy_name} is not recognized.")
        return None

if __name__ == '__main__':
    for inputs in consume_backtest_request():
        print(inputs)
        results = main(*inputs)
        send_backtest_results(results)
        
        print(results)
