from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    professor = Column(String)
    course = Column(String)
    engagement = Column(Integer)
    helpful = Column(Integer)
    workload = Column(Integer)
    quiz = Column(Integer)
    experience = Column(Integer)
    recommend = Column(Boolean)
    comment = Column(String)
    professorid = Column(Integer)
    courseid = Column(Integer)

    def __repr__(self):
        return self.professor + self.course + self.engagement