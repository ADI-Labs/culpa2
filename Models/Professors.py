from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class professor(Base):
    __tablename__ = 'professors'
    nugget = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self.first_name) + str(self.middle_name) + str(self.last_name)
