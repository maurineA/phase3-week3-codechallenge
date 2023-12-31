from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

DATABASE_URL = "sqlite:///restaurant_review.db"
engine = create_engine(DATABASE_URL)
session = Session(engine)