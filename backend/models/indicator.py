from sqlalchemy import Column, Integer, String
from .database_connection import Base

class Indicator(Base):
    
    __tablename__ = 'indicators'
    indicator_id = Column(Integer, primary_key=True, index=True)
    indicator_name = Column(String)
    indicator_params = Column(String)