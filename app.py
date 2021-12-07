from flask import Flask, request, render_template, redirect, flash
from questions import QAquestions, AnalitixQuestions, DevelopersQuestions
from answers import AnalitixAnswer, QAAnswers, DeveloperAnswer, TYPE_TEST, Answers
import pandas.io.sql as sqlio
import psycopg2
import pdfcrowd
import sys
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
    """Метод для загрузки вопросов и ответов для Разработчика
    """
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
    """Метод для загрузки вопросов и ответов для Тестировщика
    """
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
    """Метод для загрузки вопросов и ответов для Аналитика
    """
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
    """Метод для сохранения данных пользователя, проверки с помощью регулярных выражений
    """
    data = True
    first_name = request.form['firstname']
    second_name = request.form['secondname']  
    city = request.form['city']  
    year = request.form['year'] 
    Answers.name = first_name
    Answers.surname = second_name
    Answers.city = city
    Answers.age = year 
    TYPE_TEST.OPEN_FORM = 0

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
    else:
        flash('Данные сохранены', category='success')  

    return render_template('index.html', data = data)

def insert_data(data, first_name, second_name, city, year):
    """Метод для записи данных пользователей в базу данных
    """
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
        curs.execute("INSERT INTO users (first_name, second_name, city, age) \
            VALUES (%s, %s, %s, %s)", (first_name, second_name, city, year))
        conn.commit()

        # curs.execute("select * from users")
        # records = curs.fetchall()
        # for row in records:
        #     print(row)
        
        curs.close()
        conn.close()
        f.close()


@app.route('/end_and_save', methods=['POST','GET'])
def end_and_save():
    """Метод для сохранения ответов второй части тестирования
    """
    type_test = TYPE_TEST.type_test 
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
    insert_data(data, Answers.name, Answers.surname, Answers.city, Answers.age)
    insert_answers_bd(type, data, Answers.FIRST, Answers.SECOND, Answers.THIRD,
                Answers.FOURTH, Answers.FIVE, sixth_answer, seventh_answer, eighth_answer)  
    TYPE_TEST.type_test = 'None'
       
    flash('Ответы сохранены, благодарим Вас', category='success')               
    printResults = True
    return render_template('index.html', printR = printResults)

@app.route('/end', methods=['POST','GET'])
def end():
    """Метод для выхода в главное меню, в случае недостаточного количества баллов
    """
    TYPE_TEST.OPEN_FORM = 0
    flash('Вы не смогли пройти тестирование! Попробуйте снова!', category='error')
    printResults = True
    return render_template('index.html', printR = printResults)


@app.route('/save_answers', methods=['POST','GET'])
def save_answers():
    """Метод для сохранения ответов первой части, отображения вопросов для второй
    """
    data = True
    type_test = TYPE_TEST.type_test
    type = None
    CORRECTS = 0
    if TYPE_TEST.OPEN_FORM == 0:
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
                    Answers.FIRST = FIRST
                if SECOND == QAAnswers.CORRECT_ANSWER_QA2:
                    CORRECTS += 1
                    Answers.SECOND = SECOND
                if THIRD == QAAnswers.CORRECT_ANSWER_QA3:
                    CORRECTS += 1
                    Answers.THIRD = THIRD
                if FOURTH == QAAnswers.CORRECT_ANSWER_QA4:
                    CORRECTS += 1
                    Answers.FOURTH = FOURTH
                if FIFTH == QAAnswers.CORRECT_ANSWER_QA5:
                    CORRECTS += 1 
                    Answers.FIVE = FIFTH
            if type_test == 'Analitix':
                type = 3
                if FIRST == AnalitixAnswer.CORRECT_ANSWER_A1:
                    CORRECTS += 1    
                    Answers.FIRST = FIRST
                if SECOND == AnalitixAnswer.CORRECT_ANSWER_A2:
                    CORRECTS += 1
                    Answers.SECOND = SECOND
                if THIRD == AnalitixAnswer.CORRECT_ANSWER_A3:
                    CORRECTS += 1
                    Answers.THIRD = THIRD
                if FOURTH == AnalitixAnswer.CORRECT_ANSWER_A4:
                    CORRECTS += 1
                    Answers.FOURTH = FOURTH
                if FIFTH == AnalitixAnswer.CORRECT_ANSWER_A5:
                    CORRECTS += 1   
                    Answers.FIVE = FIFTH

            if CORRECTS >= 4 :
                type_test = type_test + 'SECOND'
                TYPE_TEST.type_test = type_test
                TYPE_TEST.OPEN_FORM = 0
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
                insert_data(True, Answers.name, Answers.surname, Answers.city, Answers.age)
                insert_answers_bd(type, data, FIRST, SECOND, THIRD,
                FOURTH, FIFTH, sixth_answer, seventh_answer, eighth_answer)
                TYPE_TEST.OPEN_FORM == 1
                TYPE_TEST.type_test = 'None'
                return render_template('correct_answers.html', correct = CORRECTS)
    else:
        flash("Ошибка: попытка повторного прохождения теста!", category='error')    
        return render_template('index.html')            

def insert_answers_bd(type, data, FIRST, SECOND, THIRD, FOURTH, FIFTH, sixth_answer, seventh_answer, eighth_answer):
    """Метод для сохранения ответов в базу данных
    """
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
        curs.execute("INSERT INTO answers (ttype, q1, q2, \
                    q3, q4, q5, q6, q7, \
                    q8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
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
    """Метод для формирования и выгрузки pdf-файла
    """        
    try:
        with open('logs.txt', 'r') as f:
            for line in f:
                dbname, user, password, host = line.split()
            f.close()
        
        conn = psycopg2.connect(dbname=dbname, user=user, 
                            password=password,
                            host=host)
    except:
        print("I am unable to connect to the database")
    
    report = 'report.pdf'

    sql_request = "select * from users \
                where id_user = (select max(id_user) from users)"
    df = sqlio.read_sql_query(sql_request, conn)
    df.to_html('temp.html')

    sql_request = "select an.id_test, an.ttype, an.q1, an.q2, an.q3, \
                    an.q4, an.q5 from answers an \
                    where an.id_test = (select max(id_test) from answers)"

    merge_html_page(sql_request, conn)

    for i in range(6, 9):

        sql_request = "select an.q" + str(i) + " from answers an \
                    where an.id_test = (select max(id_test) from answers)"

        merge_html_page(sql_request, conn)

    # create the API client instance 
    try: 
        with open('logs_to_pdf.txt', 'r') as f:
            for line in f:
                user, key = line.split()
            f.close()

        client = pdfcrowd.HtmlToPdfClient(user, key)
        client.convertFileToFile('temp.html', report)

    except pdfcrowd.Error as why:
        sys.stderr.write('Pdfcrowd Lib Error: {}\n'.format(why))
    
    conn.close()

    return render_template('index.html')

def merge_html_page(sql, conn, path='temp.html', path2='temp2.html'):

    df2 = sqlio.read_sql_query(sql, conn)
    df2.to_html(path2)

    with open(path2, 'r', encoding='utf-8') as t2:
        temp2_str = t2.read()
        t2.close()

    with open(path, 'a', encoding='utf-8') as t:
        t.write('<br>')
        t.write(temp2_str)
        t.close()

if __name__ == "__main__":
    app.run(debug=True)