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

    # returns the full name of the customer, with the first name and the last name  concatenated
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    #returns the restaurant instance that has the highest star rating from this customer
    def favorite_restaurant(self, session: Session):
        sorted_reviews = sorted(self.reviews, key=lambda x: x.star_rating, reverse=True)
        if sorted_reviews:
            return sorted_reviews[0].restaurant
        return None