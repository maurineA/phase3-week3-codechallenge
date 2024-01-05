from sqlalchemy import Column, Integer, String
from base import Base
from sqlalchemy.orm import relationship




class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship("Review", back_populates="customer")
    # customers = relationship("Customer", secondary="reviews", back_populates="restaurants")

    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).limit(1).first()

    def reviews(self):
        return [review.full_review() for review in self.reviews]

    def customers(self):
        return [customer.full_name() for customer in self.customers]

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]
