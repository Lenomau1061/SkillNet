from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("Index.html")

@app.route('/Config')
def Config():
    return render_template('Config.html')



@app.route('/Kevin_Keegan')
def Kevin_Keegan():
    return render_template('Kevin.html')





@app.route('/David_Golpe')
def David_Golpe():
    return render_template('David.html')

@app.route('/Elias_Gorondon')
def Elias_Gorondon():
    return render_template('Elias.html')







def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()
