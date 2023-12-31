from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

DATABASE_URL = "sqlite:///restaurant_review.db"
engine = create_engine(DATABASE_URL)
session = Session(engine)

# Assuming you have a session object
session = Session()

# Create instances of Restaurant and Customer
restaurant = Restaurant(name='Sample Restaurant', price=3)
customer = Customer(first_name='John', last_name='Doe')

# Create a review and associate it with the restaurant and customer
review = Review(star_rating=4, restaurant=restaurant, customer=customer)

# Add the instances to the session and commit
session.add_all([restaurant, customer, review])
session.commit()