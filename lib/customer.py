from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, configure_mappers
from review import Review
from base import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Review", back_populates="customer")
    # restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")

    def __repr__(self):
        return (
            f"Customer {self.id}: "
            + f"First name {self.first_name}, "
            + f"Last name {self.last_name}"
        )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        sorted_reviews = sorted(self.reviews, key=lambda x: x.star_rating, reverse=True)
        if sorted_reviews:
            return sorted_reviews[0].restaurant
        return None

    def add_review(self, restaurant, rating, session):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(review)
        session.commit()
        return review

    def delete_reviews(self, restaurant, session):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()
