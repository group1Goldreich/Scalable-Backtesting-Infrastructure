from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database_connection import Base


class Scene(Base):
    __tablename__ = 'scenes'
    scene_id = Column(Integer, primary_key=True, index=True)
    scene_name = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)



    users = relationship("User", secondary="scene_user", back_populates="scenes")
    backtests = relationship("BacktestResult", back_populates="scene")


scene_user = Table(
    'scene_user', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('scene_id', Integer, ForeignKey('scenes.scene_id'), primary_key=True)
)