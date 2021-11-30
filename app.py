from flask import Flask, request, render_template, redirect, flash
from questions import QAquestions, AnalitixQuestions, DevelopersQuestions

app = Flask(__name__)
app.secret_key = "secret key"

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

@app.route('/save', methods=['POST','GET'])
def save():
    data = True
    first_name = request.form['firstname']
    second_name = request.form['secondname']  
    city = request.form['city']  
    year = request.form['year']
    if (first_name  == '') or (second_name == '') or (city == '') or (year ==''):
        data = False
        flash('Не заполнены обязательные поля', category='error')
    else:
        flash('Данные сохранены', category='success')    
 
    return render_template('index.html',data = data)

#@app.route('/check_answer', method = ['POST', 'GET'])
#def check():
        

if __name__ == "__main__":
    app.run(debug=True)