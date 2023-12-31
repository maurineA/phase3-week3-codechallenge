from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

    reviews = relationship("Review", back_populates="customer")
    customers = relationship("Customer", secondary="reviews", back_populates="restaurants")

    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).limit(1).first()

    def reviews(self, session):
        return [review.full_review() for review in self.reviews]

    def customers(self, session):
        return [customer.full_name() for customer in self.customers]

    def all_reviews(self, session):
        return [review.full_review() for review in self.reviews]
