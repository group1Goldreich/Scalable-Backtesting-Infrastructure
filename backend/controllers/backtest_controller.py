from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from backend.models.indicator_parameter import IndicatorParameter
from ..models.backtest_result_model import BacktestResult
from ..models.scene_model import Scene
from ..models.indicator_model import Indicator
from ..view_models.scenes_vm import ScenesBaseVM




async def backtest(db: Session, data: ScenesBaseVM):
    try:
            db_indicator = Indicator(
                indicator_name=data.strategy_name
            )

            # # Add Indicator to session
            # db.add(db_indicator)
            # db.flush()  # Ensure the in
            
            # indicator = db.execute(select(Indicator).filter(Indicator.indicator_name ==  data.strategy_name)).scalars().first()
            
            indicator = db.query(Indicator).filter(Indicator.indicator_name ==  data.strategy_name).first()
            if(indicator):
                for param_data in data.params:
                    db_param = IndicatorParameter(
                        indicator_id=indicator.indicator_id,
                        parameter_name =param_data.name, 
                        parameter_value=param_data.value)
                    db.add(db_param)
            
                db.flush()  # Ensure the indicator gets an ID before it's used in Scene
            else:
                return HTTPException(status_code=400, detail="Strategy not found")
            # # Create Scene record
            db_scene = Scene(
                coin_name = data.coin_name,
                start_cash=data.start_cash,
                commission=data.commission,
                start_date=data.start_date,
                end_date=data.end_date,
            )

            # # Add Scene to session
            db.add(db_scene)
            db.flush()  # Ensure the scene gets an ID before it's used in BacktestResult

            # # Create BacktestResult record
            # # db_backtest_result = BacktestResult(
            # #     scene=db_scene,  # Assign the scene object to backtest_result
            # #     final_portfolio_value=data['final_portfolio_value'],
            # #     total_trades=results['total_trades'],
            # #     winning_trades=results['winning_trades'],
            # #     losing_trades=results['losing_trades'],
            # #     max_drawdown=results['max_drawdown'],
            # #     max_moneydown=results['max_moneydown'],
            # #     sharpe_ratio=results['sharpe_ratio']
            # # )
            
            # # db_backtest_result = BacktestResult(
            # #     scene=db_scene,  # Assign the scene object to backtest_result
            # #     final_portfolio_value=data.final_portfolio_value,
            # #     total_trades= data.total_trades,
            # #     winning_trades=data.winning_trades,
            # #     losing_trades=data.losing_trades,
            # #     max_drawdown=data.max_drawdown,
            # #     max_moneydown=data.max_moneydown,
            # #     sharpe_ratio=data.sharpe_ratio
            # # )

            # # Add BacktestResult to session
            # # db.add(db_backtest_result)
            db.commit()  # Commit all changes to the database

            return db_scene

       

    except SQLAlchemyError as e:
        db.rollback()
      
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred.")
