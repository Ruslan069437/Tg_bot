import sqlalchemy
from sqlalchemy import Column, Integer, DECIMAL, String
from sqlalchemy.orm import declarative_base



Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    balance = Column(DECIMAL, nullable=False)