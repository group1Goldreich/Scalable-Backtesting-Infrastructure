from sma_strategy import SmaStrategy
from ema_strategy import EmaStrategy
from rsi_strategy import RsiStrategy
from backtest import run_backtest

def main(strategy_name, start_date, end_date, params, start_cash, comm):

    strategy_map = {
        'sma': SmaStrategy,
        'ema': EmaStrategy,
        'rsi': RsiStrategy
    }

    if strategy_name in strategy_map:
        strategy = strategy_map[strategy_name]
        results = run_backtest(strategy, params, 'data/BTC-USD.csv', start_date, end_date, start_cash, comm)

    else:
         print(f"Strategy {strategy_name} is not recognized.")

if __name__ == '__main__':
    main('rsi', '2023-06-18', '2024-06-18', {'rsi_period':15, 'oversold':30, 'overbought':70}, 1000000, 0.001)
    