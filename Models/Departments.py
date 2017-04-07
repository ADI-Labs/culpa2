from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class department(Base):
    __tablename__ = 'departments'
    name = Column(String)
    department_key = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer)

    def __repr__(self):
        return str(self.name)
