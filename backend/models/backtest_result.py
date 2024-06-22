
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database_connection import Base



class BacktestResult(Base):
    __tablename__ = 'backtest_results'
    backtest_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    indicator_id = Column(Integer, ForeignKey('indicators.indicator_id'))
    scene_id = Column(Integer, ForeignKey('scenes.scene_id'))
    return_ = Column(String)
    number_of_trades = Column(Integer)
    winning_trades = Column(Integer)
    losing_trades = Column(Integer)
    max_drawdown = Column(Integer)
    sharpe_ratio = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User")
    indicator = relationship("Indicator")
    scene = relationship("Scene", back_populates="backtests")