from flask import Flask, render_template, request
from src.main import main


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Url', methods = ['POST'])
def Url():
    url = request.form['Url']
    video = main(url)
    return render_template('index.html', video = video)