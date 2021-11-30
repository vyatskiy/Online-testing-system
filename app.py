from flask import Flask, request, render_template, redirect, flash
from questions import QAquestions, AnalitixQuestions, DevelopersQuestions
from answers import AnalitixAnswer, QAAnswers, DeveloperAnswer
import psycopg2

app = Flask(__name__)
app.secret_key = "secret key"

questions = [0] * 5
answersA = [0] * 5
answersB = [0] * 5
answersC = [0] * 5
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/developer/', methods=['POST','GET'])
def developer():
    questions[0] = DevelopersQuestions.D1
    questions[1] = DevelopersQuestions.D2
    questions[2] = DevelopersQuestions.D3
    questions[3] = DevelopersQuestions.D4
    questions[4] = DevelopersQuestions.D5        
    answersA[0] = DeveloperAnswer.A1  
    answersA[1] = DeveloperAnswer.A2    
    answersA[2] = DeveloperAnswer.A3 
    answersA[3] = DeveloperAnswer.A4 
    answersA[4] = DeveloperAnswer.A5  
    answersB[0] = DeveloperAnswer.B1  
    answersB[1] = DeveloperAnswer.B2    
    answersB[2] = DeveloperAnswer.B3 
    answersB[3] = DeveloperAnswer.B4 
    answersB[4] = DeveloperAnswer.B5 
    answersC[0] = DeveloperAnswer.C1  
    answersC[1] = DeveloperAnswer.C2    
    answersC[2] = DeveloperAnswer.C3 
    answersC[3] = DeveloperAnswer.C4 
    answersC[4] = DeveloperAnswer.C5                
    return render_template('developer.html', questions = questions, answersA = answersA, answersB = answersB, answersC = answersC)

@app.route('/tester/', methods=['POST','GET'])
def tester():
    questions[0] = QAquestions.Q1
    questions[1] = QAquestions.Q2
    questions[2] = QAquestions.Q3
    questions[3] = QAquestions.Q4
    questions[4] = QAquestions.Q5        
    answersA[0] = QAAnswers.A1  
    answersA[1] = QAAnswers.A2    
    answersA[2] = QAAnswers.A3 
    answersA[3] = QAAnswers.A4 
    answersA[4] = QAAnswers.A5  
    answersB[0] = QAAnswers.B1  
    answersB[1] = QAAnswers.B2    
    answersB[2] = QAAnswers.B3 
    answersB[3] = QAAnswers.B4 
    answersB[4] = QAAnswers.B5 
    answersC[0] = QAAnswers.C1  
    answersC[1] = QAAnswers.C2    
    answersC[2] = QAAnswers.C3 
    answersC[3] = QAAnswers.C4 
    answersC[4] = QAAnswers.C5  
    return render_template('tester.html', questions = questions, answersA = answersA, answersB = answersB, answersC = answersC)

@app.route('/analitix/', methods=['POST','GET'])
def analite():
    questions[0] = AnalitixQuestions.A1
    questions[1] = AnalitixQuestions.A2
    questions[2] = AnalitixQuestions.A3
    questions[3] = AnalitixQuestions.A4
    questions[4] = AnalitixQuestions.A5        
    answersA[0] = AnalitixAnswer.A1  
    answersA[1] = AnalitixAnswer.A2    
    answersA[2] = AnalitixAnswer.A3 
    answersA[3] = AnalitixAnswer.A4 
    answersA[4] = AnalitixAnswer.A5  
    answersB[0] = AnalitixAnswer.B1  
    answersB[1] = AnalitixAnswer.B2    
    answersB[2] = AnalitixAnswer.B3 
    answersB[3] = AnalitixAnswer.B4 
    answersB[4] = AnalitixAnswer.B5 
    answersC[0] = AnalitixAnswer.C1  
    answersC[1] = AnalitixAnswer.C2    
    answersC[2] = AnalitixAnswer.C3 
    answersC[3] = AnalitixAnswer.C4 
    answersC[4] = AnalitixAnswer.C5  
    return render_template('analitix.html', questions = questions, answersA = answersA, answersB = answersB, answersC = answersC)

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
            conn = psycopg2.connect(dbname='d6hhit4rffokqg', user='jwibgjcvlajkpb', 
                                    password='e2f65328ae6f46ee34770897eb4ebf481f6c34d1d77848e8bb4edc902ce1e832',
                                    host='ec2-23-23-219-25.compute-1.amazonaws.com')
        except:
            print("I am unable to connect to the database") 

        curs = conn.cursor()
        curs.execute("INSERT INTO users (first_name, second_name, city, age) \
            VALUES (" + first_name + ", " + second_name + ", " + city + ", " + year + ")")

        curs.execute("select * from users")
        records = curs.fetchall()
        for row in records:
            print(row)
        
        conn.commit()
        curs.close()
        conn.close()
 
    return render_template('index.html', data = data)


if __name__ == "__main__":
    app.run(debug=True)