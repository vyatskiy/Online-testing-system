from flask import Flask, request, render_template, redirect, flash
from questions import QAquestions, AnalitixQuestions, DevelopersQuestions
import psycopg2

app = Flask(__name__)
app.secret_key = "secret key"

questions = [0] * 10
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

        try:
            with open('logs.txt', 'r') as f:
                for line in f:
                    dbname, user, password, host = line.split()
            print(dbname, user, password, host) 
            
            conn = psycopg2.connect(dbname=dbname, user=user, 
                                password=password,
                                host=host)
        except:
            print("I am unable to connect to the database") 

        curs = conn.cursor()
        curs.execute("INSERT INTO users (first_name, second_name, city, age) \
            VALUES (%s, %s, %s, %s)", (first_name, second_name, city, year))
        conn.commit()

        curs.execute("select * from users")
        records = curs.fetchall()
        for row in records:
            print(row)
        
        curs.close()
        conn.close()
        f.close()
 
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)