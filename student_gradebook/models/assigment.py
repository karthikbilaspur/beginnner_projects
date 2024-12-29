from database import engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    due_date = Column(Date)

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'due_date': self.due_date}