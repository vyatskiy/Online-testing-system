from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/developer/', methods=['POST','GET'])
def developer():
    print ('I got clicked1!')
    return render_template('developer.html')

@app.route('/tester/', methods=['POST','GET'])
def tester():
    print ('I got clicked2!')
    return render_template('tester.html')

@app.route('/analitix/', methods=['POST','GET'])
def analite():
    print ('I got clicked3!')
    return render_template('analitix.html')

if __name__ == "__main__":
    app.run(debug=True)