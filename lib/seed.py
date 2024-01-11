from faker import Faker
from modules.customer import Customer  
from modules.restaurant import Restaurant
from modules.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random
from modules.base import Base 

fake = Faker()

# Create a fresh session with a bound engine
engine = create_engine('sqlite:///restaurant_review.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ensure tables exist (create if not)
Base.metadata.create_all(engine)

# Clear existing data (if any)
# session.query(Customer).delete()
# session.query(Review).delete()
# session.query(Restaurant).delete()
session.commit()

# Generate data and persist to database
customers = [
    Customer(first_name=fake.first_name(), last_name=fake.last_name())
    for _ in range(10)
]
session.add_all(customers)
session.commit()

restaurants = [
    Restaurant(name=fake.name(), price=fake.random_int(min=1, max=5))
    for _ in range(5)
]
session.add_all(restaurants)
session.commit()

reviews = [
    Review(
        star_rating=fake.random_int(min=1, max=5),
        customer=random.choice(customers),
        restaurant=random.choice(restaurants)
    )
    for _ in range(20)
]
session.add_all(reviews)
session.commit()

# Close the session
session.close()
