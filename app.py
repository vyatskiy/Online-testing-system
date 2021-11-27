from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/developer/')
def developer():
    print ('I got clicked1!')
    return render_template('index.html')

@app.route('/tester/')
def tester():
    print ('I got clicked2!')
    return render_template('index.html')

@app.route('/analite/')
def analite():
    print ('I got clicked3!')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)