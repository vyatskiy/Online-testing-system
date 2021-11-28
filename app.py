from flask import Flask, render_template, redirect
from questions import QAquestions, AnalitixQuestions, DevelopersQuestions

app = Flask(__name__)

questions = [0]*10
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/developer/', methods=['POST','GET'])
def developer():
    questions[0] = DevelopersQuestions.D1
    questions[1] = DevelopersQuestions.D2
    return render_template('developer.html', questions = questions)

@app.route('/tester/', methods=['POST','GET'])
def tester():
    questions[0] = QAquestions.QA1
    questions[1] = QAquestions.QA2
    return render_template('tester.html', questions = questions)

@app.route('/analitix/', methods=['POST','GET'])
def analite():
    questions[0] = AnalitixQuestions.A1
    questions[1] = AnalitixQuestions.A2
    return render_template('analitix.html', questions = questions)

@app.route('/save/', methods=['POST','GET'])
def save():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)