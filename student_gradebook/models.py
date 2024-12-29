class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

class Assignment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

class Grade:
    def __init__(self, id, student_id, assignment_id, grade):
        self.id = id
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.grade = grade

    def to_dict(self):
        return {'id': self.id, 'student_id': self.student_id, 'assignment_id': self.assignment_id, 'grade': self.grade}