from models import Grade
from database import db_session

class GradeRepository:
    def __init__(self):
        self.session = db_session

    def get_grades(self):
        """Retrieve all grades."""
        return self.session.query(Grade).all()

    def get_grade(self, grade_id):
        """Retrieve grade by ID."""
        return self.session.query(Grade).filter_by(id=grade_id).first()

    def create_grade(self, student_id, assignment_id, grade):
        """Create new grade."""
        grade = Grade(student_id=student_id, assignment_id=assignment_id, grade=grade)
        self.session.add(grade)
        self.session.commit()
        return grade

    def update_grade(self, grade_id, grade):
        """Update existing grade."""
        grade_obj = self.get_grade(grade_id)
        if grade_obj:
            grade_obj.grade = grade
            self.session.commit()
            return grade_obj
        return None

    def delete_grade(self, grade_id):
        """Delete grade by ID."""
        grade = self.get_grade(grade_id)
        if grade:
            self.session.delete(grade)
            self.session.commit()
            return True
        return False