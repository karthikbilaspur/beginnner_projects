from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import Student, Assignment, Grade
from repositories import StudentRepository, AssignmentRepository, GradeRepository

app = Flask(__name__)

# Initialize repositories
student_repository = StudentRepository()
assignment_repository = AssignmentRepository()
grade_repository = GradeRepository()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    students = student_repository.get_students()
    return render_template('students.html', students=students)

@app.route('/assignments')
def assignments():
    assignments = assignment_repository.get_assignments()
    return render_template('assignments.html', assignments=assignments)

@app.route('/grades')
def grades():
    grades = grade_repository.get_grades()
    return render_template('grades.html', grades=grades)

@app.route('/api/students')
def api_students():
    students = student_repository.get_students()
    return jsonify([student.to_dict() for student in students])

@app.route('/create_student')
def create_student():
    return render_template('create_student.html')

@app.route('/create_assignment')
def create_assignment():
    return render_template('create_assignment.html')

@app.route('/create_grade')
def create_grade():
    students = student_repository.get_students()
    assignments = assignment_repository.get_assignments()
    return render_template('create_grade.html', students=students, assignments=assignments)

@app.route('/edit_student/<int:student_id>')
def edit_student(student_id):
    student = student_repository.get_student(student_id)
    return render_template('edit_student.html', student=student)

@app.route('/edit_assignment/<int:assignment_id>')
def edit_assignment(assignment_id):
    assignment = assignment_repository.get_assignment(assignment_id)
    return render_template('edit_assignment.html', assignment=assignment)

@app.route('/edit_grade/<int:grade_id>')
def edit_grade(grade_id):
    grade = grade_repository.get_grade(grade_id)
    students = student_repository.get_students()
    assignments = assignment_repository.get_assignments()
    return render_template('edit_grade.html', grade=grade, students=students, assignments=assignments)

@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    student_repository.delete_student(student_id)
    return redirect(url_for('students'))

@app.route('/delete_assignment/<int:assignment_id>')
def delete_assignment(assignment_id):
    assignment_repository.delete_assignment(assignment_id)
    return redirect(url_for('assignments'))

@app.route('/delete_grade/<int:grade_id>')
def delete_grade(grade_id):
    grade_repository.delete_grade(grade_id)
    return redirect(url_for('grades'))

if __name__ == '__main__':
    app.run(debug=True)