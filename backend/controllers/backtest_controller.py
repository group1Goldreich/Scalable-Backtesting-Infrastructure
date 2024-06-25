import os
import sys
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from backend.models.indicator_parameter import IndicatorParameter
from backend.view_models.backtest_result import BackTestResult
from ..models.backtest_result_model import BacktestResult
from ..models.scene_model import Scene
from ..models.indicator_model import Indicator
from ..view_models.scenes_vm import ScenesBaseVM
# sys.path.append(os.path.abspath(os.path.join("../Scalable-Backtesting-Infrastructure/kafka_scripts")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from kafka_scripts.kafka_consumer import consume_backtest_results 
from kafka_scripts.kafka_producer import send_backend_request
import asyncio
# async def backtest(db: Session, data: ScenesBaseVM):
#     try:
#             db_indicator = Indicator(
#                indicator_name=data.strategy_name
#             )
            
            
            

#             # # Add Indicator to session
#             # db.add(db_indicator)
#             # db.flush()  # Ensure the in
            
#             # indicator = db.execute(select(Indicator).filter(Indicator.indicator_name ==  data.strategy_name)).scalars().first()
            
#             indicator = db.query(Indicator).filter(Indicator.indicator_name ==  data.strategy_name).first()
#             if(indicator):
#                 for param_data in data.params:
#                     db_param = IndicatorParameter(
#                         indicator_id=indicator.indicator_id,
#                         parameter_name =param_data.name, 
#                         parameter_value=param_data.value)
#                     db.add(db_param)
            
#                 db.flush()  # Ensure the indicator gets an ID before it's used in Scene
#             else:
#                 return HTTPException(status_code=400, detail="Strategy not found")
#             # # Create Scene record
#             db_scene = Scene(
#                 coin_name = data.coin_name,
#                 start_cash=data.start_cash,
#                 commission=data.commission,
#                 start_date=data.start_date,
#                 end_date=data.end_date,
#             )

#             # # Add Scene to session
#             db.add(db_scene)
#             db.flush()  # Ensure the scene gets an ID before it's used in BacktestResult

#             # # Create BacktestResult record
#             # # db_backtest_result = BacktestResult(
#             # #     scene=db_scene,  # Assign the scene object to backtest_result
#             # #     final_portfolio_value=data['final_portfolio_value'],
#             # #     total_trades=results['total_trades'],
#             # #     winning_trades=results['winning_trades'],
#             # #     losing_trades=results['losing_trades'],
#             # #     max_drawdown=results['max_drawdown'],
#             # #     max_moneydown=results['max_moneydown'],
#             # #     sharpe_ratio=results['sharpe_ratio']
#             # # )
            
#             # # db_backtest_result = BacktestResult(
#             # #     scene=db_scene,  # Assign the scene object to backtest_result
#             # #     final_portfolio_value=data.final_portfolio_value,
#             # #     total_trades= data.total_trades,
#             # #     winning_trades=data.winning_trades,
#             # #     losing_trades=data.losing_trades,
#             # #     max_drawdown=data.max_drawdown,
#             # #     max_moneydown=data.max_moneydown,
#             # #     sharpe_ratio=data.sharpe_ratio
#             # # )

#             # # Add BacktestResult to session
#             # # db.add(db_backtest_result)
#             db.commit()  # Commit all changes to the database

#             return db_scene

       

#     except SQLAlchemyError as e:
#         db.rollback()
      
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred.")

async def backtest(db: Session, data: ScenesBaseVM):
    
   

    name = 'Bitcoin'    
    strategy = 'macd'
    start_date = '2023-06-24'
    end_date ='2024-06-24'

    params = {'fast_period':12, 'slow_period':26, 'signal_period':9, 'comm':0.0}
    start_cash = 1000000
    commission=0.001

    send_backend_request(name, start_date, end_date, strategy, params, start_cash, commission)

    loop = asyncio.get_event_loop()
    metrics = await loop.run_in_executor(None, consume_backtest_results)
    
    print("METRICS", metrics)
    print("METRICS", metrics['Number of trades'])
    print("METRICS", metrics['Max drawdown'])
    print("METRICS", metrics['Sharpe ratio'])
    
    res = BackTestResult(
        final_portfolio_value = 0.0,
        total_trades  =  metrics['Number of trades'],
        winning_trades = 0.0,
        losing_trades = 0.0,
        max_drawdown =  metrics['Max drawdown'],
        max_moneydown = 0.0,
        sharpe_ratio = metrics['Sharpe ratio']
        
    )
    return res
    



