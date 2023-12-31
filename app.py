from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

DATABASE_URL = "sqlite:///restaurant_review.db"
engine = create_engine(DATABASE_URL)
session = Session(engine)

# Create instances
restaurant1 = Restaurant(name="Hotpoint", price=300)
restaurant2 = Restaurant(name="Yummies", price=500)

customer1 = Customer(first_name="Elisha", last_name="Mwangi")
customer2 = Customer(first_name="Sophia", last_name="Njeri")

# Add reviews
customer1.add_review(restaurant1, 5, session)
customer2.add_review(restaurant2, 4, session)
customer1.add_review(restaurant1, 3, session)

# customer details
print(customer1.full_name())
print([review.full_review() for review in customer1.reviews])
print([restaurant.name for restaurant in customer1.restaurants])
favorite_restaurant = customer1.favorite_restaurant(session)
print(favorite_restaurant.name if favorite_restaurant else "No favorite restaurant")

# restaurant information
print([review.full_review() for review in restaurant1.reviews(session)])
print([customer.full_name() for customer in restaurant1.customers(session)])
print(restaurant1.all_reviews(session))
fanciest_restaurant = Restaurant.fanciest(session)
print(fanciest_restaurant.name if fanciest_restaurant else "No fanciest restaurant")

# review details
print([review.full_review() for review in Review.all(session)])

session.close()
