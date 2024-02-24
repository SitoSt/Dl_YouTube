from flask import Flask, stream_template, request
from pytube import YouTube
from src.video_information import Get_resolutions, Get_info
from src.download import Descargar_video

app = Flask(__name__)

url = ''
title = ''
thumbnail_url = ''

@app.route('/')
def index():
    return stream_template('index.html')

@app.route('/select', methods = ['POST'])
def Select():
    # 1º Cogemos la url del form
    global url
    global title
    global thumbnail_url

    url = request.form['Url']

    # Accedemos al video y lo guardamos en la variable yt
    yt = YouTube(url)
    
    # Invocamos las funciones para acceder al titulo, la miniatura y las resoluciones del video
    title, thumbnail_url = Get_info(url)
    Resolutions, Bibrates = Get_resolutions(url)

    print(thumbnail_url)

    return stream_template('index.html', title=title, thumbnail_url=thumbnail_url,  Resolutions=Resolutions, Bibrates=Bibrates)


@app.route('/download', methods = ['POST'])
def Download():
    formato = request.form['format_tracker']
    
    print(formato)

    if formato == 'progresive':
        res = request.form['progresive_res']
    elif formato == 'video':
        res = request.form['video_res']
    elif formato == 'audio':
        res = request.form['audio_res']
    else:
        print('ERROR: no hay formato para descargar')

    Descargar_video(res, url, formato, '')

    return stream_template('index.html', title = title, thumbnail_url=thumbnail_url, downloaded=True)
