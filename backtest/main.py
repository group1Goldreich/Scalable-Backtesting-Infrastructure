from sma_strategy import SmaStrategy
from ema_strategy import EmaStrategy
from rsi_strategy import RsiStrategy
from backtest import run_backtest
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../Scalable-Backtesting-Infrastructure/mlflow")))
from mlflow_track import track

def main(strategy_name, start_date, end_date, params, start_cash, comm):

    strategy_map = {
        'sma': SmaStrategy,
        'ema': EmaStrategy,
        'rsi': RsiStrategy
    }

    if strategy_name in strategy_map:
        strategy = strategy_map[strategy_name]
        results = run_backtest(strategy, params, 'data/BTC-USD.csv', start_date, end_date, start_cash, comm)
        return results

    else:
         print(f"Strategy {strategy_name} is not recognized.")

if __name__ == '__main__':
    strategy = 'rsi'
    start_date = '2023-06-18'
    end_date = '2024-06-18'
    params = {'rsi_period':15, 'oversold':30, 'overbought':70}
    start_cash = 1000000
    commission = 0.001
    results = main('rsi', '2023-06-18', '2024-06-18', {'rsi_period':15, 'oversold':30, 'overbought':70}, 1000000, 0.001)
    
    trade_analyzer = results['trade_analyzer']
    drawdown = results['drawdown']

    track(strategy, start_date, end_date, start_cash, commission, params, drawdown)
    print(results)