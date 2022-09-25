from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    is_admin = Column(Boolean, default=False)
    city = Column(String)
    join_date = Column(DateTime(timezone=True), server_default=func.now())
