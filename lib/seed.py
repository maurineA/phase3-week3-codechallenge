from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.restaurant import Restaurant
from modules.customer import Customer
from modules.review import Review
from modules.base import Base


engine = create_engine('sqlite:///restaurant_review.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data for restaurants
restaurant1 = Restaurant(name='Restaurant A', price=50)
restaurant2 = Restaurant(name='Restaurant B', price=80)

# Sample data for customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Sample data for reviews
review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=4)
review2 = Review(restaurant=restaurant2, customer=customer1, star_rating=5)
review3 = Review(restaurant=restaurant1, customer=customer2, star_rating=3)

# Add the sample data to the session
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])

# Query and print restaurants
restaurants = session.query(Restaurant).all()
print("Restaurants:")
for restaurant in restaurants:
    print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

# Query and print customers
customers = session.query(Customer).all()
print("\nCustomers:")
for customer in customers:
    print(f"ID: {customer.id}, Name: {customer.full_name()}")

# Query and print reviews
reviews = session.query(Review).all()
print("\nReviews:")
for review in reviews:
    customer_name = review.customer.full_name() if review.customer else "Unknown Customer"
    print(f"ID: {review.id}, Rating: {review.star_rating}, Restaurant: {review.restaurant.name}, Customer: {customer_name}")


print("Fanciest Restaurant:", Restaurant.fanciest(session).name)
print("All Reviews for Restaurant A:", restaurant1.all_reviews())
print("Customers who reviewed Restaurant A:", restaurant1.customers())

print("Full Name of Customer 1:", customer1.full_name())
print("Favorite Restaurant of Customer 1:", customer1.favorite_restaurant().name)

customer1.add_review(restaurant2, 4)

for review in customer1.reviews:
    customer_name = review.customer.full_name() if review.customer else "Unknown Customer"
    print(f"ID: {review.id}, Rating: {review.star_rating}, Restaurant: {review.restaurant.name}, Customer: {customer_name}")

# Delete all reviews for Restaurant A for Customer 1
customer1.delete_reviews(restaurant1)

# Print all reviews for Customer 1 after deletion with additional checks
for review in customer1.reviews:
    customer_name = review.customer.full_name() if review.customer else "Unknown Customer"
    

# Commit the changes to the database
session.commit()

# Close the session
session.close()