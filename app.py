from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from lib.modules.customer import Customer
from lib.modules.restaurant import Restaurant
from lib.modules.base import session



# Create instances
restaurant = Restaurant(name=" Cheka", price=400)
customer = Customer(first_name="John", last_name="Doe")

# Add a review
customer.add_review(restaurant, 5, session)

# Print customer output
print(customer.full_name())
print([review.full_review() for review in customer.reviews])

# Print restaurant information
print([review.full_review() for review in restaurant.reviews(session)])
print([customer.full_name() for customer in restaurant.customers(session)])

session.close()

