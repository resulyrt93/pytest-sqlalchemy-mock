from typing import List

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)
from sqlalchemy.orm import Mapped, declarative_base, relationship
from sqlalchemy.testing.schema import Table

Base = declarative_base()


user_department_association_table = Table(
    "user_department",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column(
        "department_id", Integer, ForeignKey("department.id"), primary_key=True
    ),
)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    is_admin = Column(Boolean, default=False)
    city = Column(String)
    join_date = Column(DateTime(timezone=True), server_default=func.now())
    departments: Mapped[List["Department"]] = relationship(
        secondary=user_department_association_table, back_populates="users"
    )


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users: Mapped[List[User]] = relationship(
        secondary=user_department_association_table,
        back_populates="departments",
    )
