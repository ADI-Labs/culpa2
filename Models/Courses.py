from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column, Integer, String


Base = declarative_base()


class course(Base):
    __tablename__ = 'courses'
    department_ids = Column(String)
    name = Column(String)
    id = Column(Integer)
    number = Column(Integer)

    def __repr__(self):
        return str(self.name)
