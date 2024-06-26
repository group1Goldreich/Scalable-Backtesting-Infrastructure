from sqlalchemy import Column, ForeignKey, Integer, String
from ..utils.database_connection import Base
from sqlalchemy.orm import relationship

    
class Indicator(Base):
    __tablename__ = "indicators"
    indicator_id = Column(Integer, primary_key=True, index=True)
    indicator_name = Column(String, index=True)
   
    parameters = relationship("IndicatorParameter", back_populates="indicators")
    backtest_results = relationship("BacktestResult", back_populates="indicator")
    
    
