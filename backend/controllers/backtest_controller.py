from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.backtest_result_model import BacktestResult
from ..models.scene_model import Scene
from ..backtest.sma_strategy import SmaStrategy
from ..backtest.ema_strategy import EmaStrategy
from ..backtest.rsi_strategy import RsiStrategy
from ..backtest import run_backtest
from ..models.indicator_model import Indicator
from ..view_models.scenes_vm import ScenesBaseVM
from ..backtest.logger import setup_logger


logger = setup_logger('MainLogger')

def backtest(db: Session, data: ScenesBaseVM):
    try:
        strategy_map = {
            'sma': SmaStrategy,
            'ema': EmaStrategy,
            'rsi': RsiStrategy
        }

        if data.strategy_name in strategy_map:
            strategy_class = strategy_map[data.strategy_name]
            results = run_backtest(strategy_class, data.params, './backtest/data/BTC-USD.csv', data.start_date, data.end_date, data.start_cash, data.commission)

            # Create Indicator record
            db_indicator = Indicator(
                indicator_name=data.strategy_name,
                indicator_params=data.params
            )

            # Add Indicator to session
            db.add(db_indicator)
            db.flush()  # Ensure the indicator gets an ID before it's used in Scene

            # Create Scene record
            db_scene = Scene(
                start_cash=data.start_cash,
                commission=data.commission,
                start_date=data.start_date,
                end_date=data.end_date,
                indicator=db_indicator  # Assign the indicator object to scene
            )

            # Add Scene to session
            db.add(db_scene)
            db.flush()  # Ensure the scene gets an ID before it's used in BacktestResult

            # Create BacktestResult record
            db_backtest_result = BacktestResult(
                scene=db_scene,  # Assign the scene object to backtest_result
                final_portfolio_value=results['final_portfolio_value'],
                total_trades=results['total_trades'],
                winning_trades=results['winning_trades'],
                losing_trades=results['losing_trades'],
                max_drawdown=results['max_drawdown'],
                max_moneydown=results['max_moneydown'],
                sharpe_ratio=results['sharpe_ratio']
            )

            # Add BacktestResult to session
            db.add(db_backtest_result)
            db.commit()  # Commit all changes to the database

            return db_backtest_result

        else:
            logger.error(f"Strategy {data.strategy_name} is not recognized.")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Strategy {data.strategy_name} is not recognized.")

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred.")
