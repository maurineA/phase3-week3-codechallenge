from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session
from lib.review import Review

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
    
    # takes a `restaurant` (an instance of the `Restaurant` class) and a rating - creates a new review for the restaurant with the given `restaurant_id`
    def add_review(self, restaurant, rating, session: Session):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(review)
        session.commit()
        return review
    
    # takes a `restaurant` (an instance of the `Restaurant` class) and - removes **all** their reviews for this restaurant - you will have to delete rows from the `reviews` table to get this to work!
    def delete_reviews(self, restaurant, session: Session):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()