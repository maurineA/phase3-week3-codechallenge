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
