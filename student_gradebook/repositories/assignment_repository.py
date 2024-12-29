from models import Assignment
from database import db_session

class AssignmentRepository:
    def __init__(self):
        self.session = db_session

    def get_assignments(self):
        """Retrieve all assignments."""
        return self.session.query(Assignment).all()

    def get_assignment(self, assignment_id):
        """Retrieve assignment by ID."""
        return self.session.query(Assignment).filter_by(id=assignment_id).first()

    def create_assignment(self, name, due_date):
        """Create new assignment."""
        assignment = Assignment(name=name, due_date=due_date)
        self.session.add(assignment)
        self.session.commit()
        return assignment

    def update_assignment(self, assignment_id, name, due_date):
        """Update existing assignment."""
        assignment = self.get_assignment(assignment_id)
        if assignment:
            assignment.name = name
            assignment.due_date = due_date
            self.session.commit()
            return assignment
        return None

    def delete_assignment(self, assignment_id):
        """Delete assignment by ID."""
        assignment = self.get_assignment(assignment_id)
        if assignment:
            self.session.delete(assignment)
            self.session.commit()
            return True
        return False