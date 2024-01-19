from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .review import Review
from .base import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        # Assuming that the highest rating means the favorite restaurant
        highest_rating_review = max(self.reviews, key=lambda review: review.star_rating, default=None)
        return highest_rating_review.restaurant if highest_rating_review else None
    
    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        self.reviews.append(new_review)

    def get_reviews(self):
        return [review.full_review() for review in self.reviews]

    def delete_reviews(self, restaurant):
        # Remove all reviews for the specified restaurant
        self.reviews = [review for review in self.reviews if review.restaurant != restaurant]


    def restaurants(self):
        return [review.restaurant.name for review in self.reviews]

    
   
  