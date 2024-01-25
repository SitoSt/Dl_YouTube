from flask import Flask, render_template, request
from pytube import YouTube
from src.resolutions import Cap_resolutions
from src.download import Descargar_video

app = Flask(__name__)
url = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select', methods = ['POST'])
def Select():
    # 1º Cogemos la url del form
    global url
    url = request.form['Url']
    # 2º Accedemos al video y lo guardamos en la variable yt
    ####yt = YouTube(url)
    # 3º Guardamos todos los streams del video
    # streams = YouTube(url).streams
    # 4º Invocamos la función para ver las resoluciones del video
    resolutions = Cap_resolutions(url)
    
    return render_template('index.html', resolutions = resolutions)

@app.route('/download', methods = ['POST'])
def Download():

    res = request.form['Resolución']
    print(url) # El programa no guarda la url, habra que ver como conseguirlo
    print(res)
    Descargar_video(res, url, '')

    title = YouTube(url).title

    return render_template('index.html', title = title)
