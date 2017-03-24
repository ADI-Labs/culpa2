from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column, Integer, String


Base = declarative_base()


class course(Base):
    __tablename__ = 'courses'
    department_ids = Column(String)
    name = Column(String)
    course_key = Column(Integer, primary_key=True)
    number = Column(String)
    id = Column(Integer)

    def __repr__(self):
        return str(self.name)
