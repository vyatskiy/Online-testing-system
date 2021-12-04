from flask import Flask, request, render_template, redirect, flash
from questions import QAquestions, AnalitixQuestions, DevelopersQuestions
from answers import AnalitixAnswer, QAAnswers, DeveloperAnswer, TYPE_TEST, Answers
import pandas as pd
import pandas.io.sql as sqlio
import pdfkit as pdf
import psycopg2
import os, sys, subprocess, platform
import re

app = Flask(__name__)
app.secret_key = "secret key"

questions = [0] * 5
answersA = [0] * 5
answersB = [0] * 5
answersC = [0] * 5
SecondTaskA = [0] * 3
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/developer/', methods=['POST','GET'])
def developer():
    TYPE_TEST.type_test = 'Developer'
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
    TYPE_TEST.type_test = 'Tester'
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
    TYPE_TEST.type_test = 'Analitix'    
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

    elif re.search(r'\d', first_name) != None or re.search(r'[/\.,;:@\'\"#$%^&-+{}<>!*`~|\[\]\s\t\n\r]', first_name) \
        != None or len(first_name) > 20 or first_name[0].isupper() != True:
        data = False
        flash('Поле Имя заполненно некорректно', category='error')

    elif re.search(r'\d', second_name) != None or re.search(r'[/\.,;:@\'\"#$%^&-+{}<>!*`~|\[\]\s\t\n\r]', second_name) \
        != None or len(second_name) > 20 or second_name[0].isupper() != True:
        data = False
        flash('Поле Фамилия заполненно некорректно', category='error')

    elif re.search(r'\d', city) != None or re.search(r'[/\.,;:@\'\"#$%^&-+{}<>!*`~|\[\]\s\t\n\r]', city) \
        != None or len(city) > 20 or city[0].isupper() != True:
        data = False
        flash('Поле Город заполненно некорректно', category='error')

    elif re.search(r'\D', year) != None or len(year) > 3:
        data = False
        flash('Поле Возраст заполненно некорректно', category='error')

    elif data:
        flash('Данные сохранены', category='success')  

        try:
            with open('logs.txt', 'r') as f:
                for line in f:
                    dbname, user, password, host = line.split()
            
            conn = psycopg2.connect(dbname=dbname, user=user, 
                                password=password,
                                host=host)
        except:
            print("I am unable to connect to the database") 

        curs = conn.cursor()
        curs.execute("INSERT INTO users (first_name, second_name, city, age) \
            VALUES (%s, %s, %s, %s)", (first_name, second_name, city, year))
        conn.commit()
        TYPE_TEST.OPEN_FORM = 0

        # curs.execute("select * from users")
        # records = curs.fetchall()
        # for row in records:
        #     print(row)
        
        curs.close()
        conn.close()
        f.close()
 
    return render_template('index.html', data = data)

@app.route('/end_and_save', methods=['POST','GET'])
def end_and_save():
    type_test = TYPE_TEST.type_test 
    print(type_test)
    type = 0
    data = True
    if type_test == 'DeveloperSECOND':
        type = 1
    if type_test == 'TesterSECOND':
        type = 2
    if type_test == 'AnalitixSECOND':
        type = 3                                
    sixth_answer = request.form['FIRST']
    seventh_answer = request.form['SECOND']  
    eighth_answer = request.form['THIRD']  
    insert_answers_bd(type, data, Answers.FIRST, Answers.SECOND, Answers.THIRD,
                Answers.FOURTH, Answers.FIVE, sixth_answer, seventh_answer, eighth_answer)     
    flash('Ответы сохранены, благодарим Вас', category='success')               
    return render_template('index.html')

@app.route('/end', methods=['POST','GET'])
def end():   
    flash('Вы не смогли пройти тестирование! Попробуйте снова!', category='error') 
    return render_template('index.html')


@app.route('/save_answers', methods=['POST','GET'])
def save_answers():
    data = True
    type_test = TYPE_TEST.type_test
    type = 0
    CORRECTS = 0
    if TYPE_TEST.OPEN_FORM == 0:
        TYPE_TEST.OPEN_FORM = 1
        if type_test == 'Developer' or type_test == 'Tester' or type_test == 'Analitix':
            FIRST = request.form.getlist('FIRST')
            SECOND = request.form.getlist('SECOND')
            THIRD = request.form.getlist('THIRD')
            FOURTH = request.form.getlist('FOURTH')
            FIFTH = request.form.getlist('FIFTH') 
            if type_test == 'Developer':
                type = 1
                if FIRST == DeveloperAnswer.CORRECT_ANSWER_D1:
                    CORRECTS += 1 
                    Answers.FIRST = FIRST
                if SECOND == DeveloperAnswer.CORRECT_ANSWER_D2:
                    CORRECTS += 1
                    Answers.SECOND = SECOND
                if THIRD == DeveloperAnswer.CORRECT_ANSWER_D3:
                    CORRECTS += 1
                    Answers.THIRD = THIRD
                if FOURTH == DeveloperAnswer.CORRECT_ANSWER_D4:
                    CORRECTS += 1
                    Answers.FOURTH = FOURTH
                if FIFTH == DeveloperAnswer.CORRECT_ANSWER_D5:
                    CORRECTS += 1     
                    Answers.FIVE = FIFTH
            if type_test == 'Tester':
                type = 2
                if FIRST == QAAnswers.CORRECT_ANSWER_QA1:
                    CORRECTS += 1    
                if SECOND == QAAnswers.CORRECT_ANSWER_QA2:
                    CORRECTS += 1
                if THIRD == QAAnswers.CORRECT_ANSWER_QA3:
                    CORRECTS += 1
                if FOURTH == QAAnswers.CORRECT_ANSWER_QA4:
                    CORRECTS += 1
                if FIFTH == QAAnswers.CORRECT_ANSWER_QA4:
                    CORRECTS += 1 
            if type_test == 'Analitix':
                type = 3
                if FIRST == AnalitixAnswer.CORRECT_ANSWER_A1:
                    CORRECTS += 1    
                if SECOND == AnalitixAnswer.CORRECT_ANSWER_A2:
                    CORRECTS += 1
                if THIRD == AnalitixAnswer.CORRECT_ANSWER_A3:
                    CORRECTS += 1
                if FOURTH == AnalitixAnswer.CORRECT_ANSWER_A4:
                    CORRECTS += 1
                if FIFTH == AnalitixAnswer.CORRECT_ANSWER_A4:
                    CORRECTS += 1   

            if CORRECTS >= 4 :
                type_test = type_test + 'SECOND'
                TYPE_TEST.type_test = type_test
                if type_test == 'DeveloperSECOND':
                    SecondTaskA[0] = DevelopersQuestions.DS1  
                    SecondTaskA[1] = DevelopersQuestions.DS2    
                    SecondTaskA[2] = DevelopersQuestions.DS3  
                if type_test == 'TesterSECOND':
                    SecondTaskA[0] = QAquestions.QS1  
                    SecondTaskA[1] = QAquestions.QS2   
                    SecondTaskA[2] = QAquestions.QS3
                if type_test == 'AnalitixSECOND':
                    SecondTaskA[0] = AnalitixQuestions.AS1 
                    SecondTaskA[1] = AnalitixQuestions.AS2    
                    SecondTaskA[2] = AnalitixQuestions.AS3          
                return render_template('correct_answers.html', correct = CORRECTS, SecondTaskA = SecondTaskA)
            else:
                sixth_answer = ''
                seventh_answer = ''
                eighth_answer = ''
                insert_answers_bd(type, data, FIRST, SECOND, THIRD,
                FOURTH, FIFTH, sixth_answer, seventh_answer, eighth_answer)

                return render_template('correct_answers.html', correct = CORRECTS)
    else:
        flash("Ошибка: попытка повторного прохождения теста!", category='error')    
        return render_template('index.html')            

def insert_answers_bd(type, data, FIRST, SECOND, THIRD, FOURTH, FIFTH, sixth_answer, seventh_answer, eighth_answer):
    if data:
        try:
            with open('logs.txt', 'r') as f:
                for line in f:
                    dbname, user, password, host = line.split()
            
            conn = psycopg2.connect(dbname=dbname, user=user, 
                                password=password,
                                host=host)
        except:
            print("I am unable to connect to the database") 

        curs = conn.cursor()
        curs.execute("INSERT INTO answers (type_test, first_quest, second_quest, \
                    third_quest, fourth_quest, fifth_quest, sixth_quest, seventh_quest, \
                    eighth_quest) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                    (type, FIRST, SECOND, THIRD, FOURTH, \
                    FIFTH, sixth_answer, seventh_answer, eighth_answer))
        conn.commit()

        curs.execute("select * from answers")
        records = curs.fetchall()
        for row in records:
            print(row)
        
        curs.close()
        conn.close()
        f.close()
    


@app.route('/get-pdf/', methods=['POST','GET'])
def get_pdf():

    if platform.system() == "Windows":
            pdfkit_config = pdf.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
            os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
            WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
                stdout=subprocess.PIPE).communicate()[0].strip()
            print(WKHTMLTOPDF_CMD)
            pdfkit_config = pdf.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
    
    CORRECTS = 5 
    try:
        with open('logs.txt', 'r') as f:
            for line in f:
                dbname, user, password, host = line.split()
        
        conn = psycopg2.connect(dbname=dbname, user=user, 
                            password=password,
                            host=host)
    except:
        print("I am unable to connect to the database")

    sql_request = "select * from users;"
    df = sqlio.read_sql_query(sql_request, conn)
    df.to_html('temp.html')
    report = 'report.pdf'
    pdf.from_file('temp.html', report, configuration=pdfkit_config)
    
    conn.close()
    f.close()

    return render_template('correct_answers.html', correct = CORRECTS)

if __name__ == "__main__":
    app.run(debug=True)