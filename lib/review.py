from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"

    pass