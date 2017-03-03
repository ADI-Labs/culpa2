from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class departmemt(Base):
    __tablename__ = 'departments'
    name = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self.name)