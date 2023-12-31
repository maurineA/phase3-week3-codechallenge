from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    #relations
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")