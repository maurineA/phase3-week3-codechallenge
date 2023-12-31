from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

DATABASE_URL = "sqlite:///restaurant_review.db"
engine = create_engine(DATABASE_URL)
session = Session(engine)

# Create instances
restaurant1 = Restaurant(name="Hotpoint", price=3)
restaurant2 = Restaurant(name="Yummies", price=4)

customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Doe")

# Add reviews
customer1.add_review(restaurant1, 5, session)
customer1.add_review(restaurant2, 4, session)
customer2.add_review(restaurant1, 3, session)

# Print customer output
print(customer1.full_name())
print(customer1.reviews(session))
print(customer1.restaurants(session))
print(customer1.favorite_restaurant(session).name)

# Print restaurant information
print(restaurant1.reviews(session))
print(restaurant1.customers(session))
print(restaurant1.all_reviews(session))
print(Restaurant.fanciest(session).name)

# Print review information
print(Review.all_reviews(session))

session.close()