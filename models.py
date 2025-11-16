from sqlalchemy import Integer, Column, String
from database import Base

class Favorit(Base):
    __tablename__ = "favorite_stocks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(20), unique=True, nullable=False)
    company_name = Column(String(100), nullable=False)