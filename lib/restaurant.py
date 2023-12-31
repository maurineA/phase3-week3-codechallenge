from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

    #relations
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")

    # returns _one_ restaurant instance for the restaurant that has the highest price
    @classmethod
    def fanciest(cls, session: Session):
        return (
            session.query(cls)
            .order_by(cls.price.desc())
            .limit(1)
            .first()
        )
    
    
    #should return an list of strings with all the reviews for this restaurant
    def reviews(self, session: Session):
        return [review.full_review() for review in self.reviews]

    def customers(self, session: Session):
        return [customer.full_name() for customer in self.customers]

    def all_reviews(self, session: Session):
        return [review.full_review() for review in self.reviews]
    


