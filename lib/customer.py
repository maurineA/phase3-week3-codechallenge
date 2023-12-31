from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    pass