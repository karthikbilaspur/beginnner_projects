from models import Student
from database import db_session

class StudentRepository:
    def __init__(self):
        self.session = db_session

    def get_students(self):
        """Retrieve all students."""
        return self.session.query(Student).all()

    def get_student(self, student_id):
        """Retrieve student by ID."""
        return self.session.query(Student).filter_by(id=student_id).first()

    def create_student(self, name):
        """Create new student."""
        student = Student(name=name)
        self.session.add(student)
        self.session.commit()
        return student

    def update_student(self, student_id, name):
        """Update existing student."""
        student = self.get_student(student_id)
        if student:
            student.name = name
            self.session.commit()
            return student
        return None

    def delete_student(self, student_id):
        """Delete student by ID."""
        student = self.get_student(student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
            return True
        return False