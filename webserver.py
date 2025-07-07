from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("Index.html")

@app.route('/Config')
def Config():
    return render_template('Config.html')



@app.route('/Kevin Keegan')
def Kevin():
    return render_template('Kevin.html')





@app.route('/David golpe')
def David():
    return render_template('David.html')

@app.route('/Elias Gorondon')
def Elias():
    return render_template('Elias.html')







def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()
