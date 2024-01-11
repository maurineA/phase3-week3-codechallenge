from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base





class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship("Restaurant", back_populates="reviews")

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="reviews")

    def __repr__(self):
        return (
            f"Review {self.id}: "
            + f"Restaurant Id {self.restaurant_id}, "
            + f"Customer Id {self.customer_id}, "
            + f"Star Rating {self.star_rating}"
        )

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
