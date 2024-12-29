from flask import Flask, render_template, request
from questions import questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        answer = request.form[f'question_{i}']
        if int(answer) == question['answer']:
            score += 1
    return render_template('results.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)