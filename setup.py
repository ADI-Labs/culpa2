from sqlalchemy import create_engine
import requests
from Models.Reviews import Review
from sqlalchemy.orm import sessionmaker
URI = "postgres://xeeqkeipvcflil:fead0f891152e8f657d7ee59ba256aa36c24fed629a0ee765b6a6aac6da2610f@ec2-54-225-236-102.compute-1.amazonaws.com:5432/d7mipabothqsm0"
engine = create_engine(URI)
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


def setup():
    connect()
    print("I got here")
    test()


def connect():
    review = Review(professor="Test", engagement=0)
    session.add(review)
    session.commit()


def test():
    reviewed = session.query(Review).filter_by(professor="Test").first()
    print(reviewed)


setup()