from database import engine
from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', backref='grades')
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    assignment = relationship('Assignment', backref='grades')
    grade = Column(Float)

    def __init__(self, student_id, assignment_id, grade):
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.grade = grade

    def to_dict(self):
        return {'id': self.id, 'student_id': self.student_id, 'assignment_id': self.assignment_id, 'grade': self.grade}