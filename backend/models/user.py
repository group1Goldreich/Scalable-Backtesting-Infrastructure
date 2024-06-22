from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .database_connection import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, unique=True, index=True)
    created_at = Column(Date)

    scenes = relationship("Scene", secondary="scene_user", back_populates="users")
