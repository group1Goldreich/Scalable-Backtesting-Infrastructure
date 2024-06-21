from sma_strategy import SmaStrategy
from ema_strategy import EmaStrategy
from rsi_strategy import RsiStrategy
from backtest import run_backtest
from logger import setup_logger

logger = setup_logger('MainLogger')

def main(strategy_name, start_date, end_date, params, start_cash, comm):

    strategy_map = {
        'sma': SmaStrategy,
        'ema': EmaStrategy,
        'rsi': RsiStrategy
    }

    if strategy_name in strategy_map:
        strategy = strategy_map[strategy_name]
        results = run_backtest(strategy, params, 'data/BTC-USD.csv', start_date, end_date, start_cash, comm)

        logger.info(f"Final Portfolio Value: {results['final_value']}")
        logger.info(f"Trade Analyzer: {results['trade_analyzer']}")
        logger.info(f"Drawdown: {results['drawdown']}")
        logger.info(f"Sharpe Ratio: {results['sharperatio']}")

    else:
        logger.error(f"Strategy {strategy_name} is not recognized.")

if __name__ == '__main__':
    main('rsi', '2023-06-18', '2024-06-18', {'rsi_period':15, 'oversold':30, 'overbought':70}, 1000000, 0.001)
    