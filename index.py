from flask import Flask, stream_template, request
from pytube import YouTube
from src.resolutions import Cap_resolutions
from src.download import Descargar_video

app = Flask(__name__)

url = ''
formato = ''

@app.route('/')
def index():
    return stream_template('index.html')

@app.route('/select', methods = ['POST'])
def Select():
    # 1º Cogemos la url del form
    global url
    global formato
    global yt

    url = request.form['Url']
    formato = request.form['Formato']

    # Accedemos al video y lo guardamos en la variable yt
    yt = YouTube(url)
    title = yt.title

    # Invocamos la función para ver las resoluciones del video
    resolutions = Cap_resolutions(url, formato)

    return stream_template('index.html', url=url, formato=formato, title=title, resolutions=resolutions)


@app.route('/download', methods = ['POST'])
def Download():
    res = ''

    if formato == 'progresive':
        res = request.form['Progresive-res']
    elif formato == 'video':
        res = request.form['Video-res']
    elif formato == 'audio':
        res = request.form['Audio-res']
    else:
        print('ERROR: no hay formato para descargar')

    Descargar_video(res, url, formato, '')

    title = YouTube(url).title

    return stream_template('index.html', title = title, downloaded=True)
