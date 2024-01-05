from faker import Faker
from customer import Customer
from restaurant import Restaurant 
from review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

fake = Faker()

# Create a session for interacting with the database
engine = create_engine('sqlite:///restaurant_review.db')
Session = sessionmaker(bind=engine)  # Replace `engine` with your SQLAlchemy engine
session = Session()

# Generate customers
customers = [
    Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    for _ in range(10)  # Generate 10 customers
]
session.add_all(customers)
session.commit()

# Generate restaurants
restaurants = [
    Restaurant(
        name=fake.name(),
        price=fake.random_int(min=1, max=5)  # Random price between 1 and 5
    )
    for _ in range(5)  # Generate 5 restaurants
]
session.add_all(restaurants)
session.commit()

# Generate reviews, associating them with customers and restaurants
reviews = [
    Review(
        star_rating=fake.random_int(min=1, max=5),
        customer=random.choice(customers),
        restaurant=random.choice(restaurants)
    )
    for _ in range(20)  # Generate 20 reviews
]
session.add_all(reviews)
session.commit()

session.close()