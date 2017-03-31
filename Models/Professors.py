from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class professor(Base):
    __tablename__ = 'professors'
    nugget = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    professor_key = Column(Integer, primary_key=True, autoincrement=True)

    def to_dict(self):
        return {
            'nugget': self.nugget,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'profesorr_key': self.professor_key
        }

    def __repr__(self):
        return str(self.first_name) + str(self.middle_name) + str(self.last_name)
