from flask import Flask, stream_template, request
from pytube import YouTube
from src.video_information import Get_resolutions, Get_info
from src.download import Descargar_video

app = Flask(__name__)

url = ''
title = ''
thumbnail_url = ''
formato = ''
ready_to_dl = False

@app.route('/', methods = ['POST', 'GET'])
def index():
    global formato
    res=''
    if request.method == 'GET':
        return stream_template('index.html')
    else :
        try :
            formato = request.form['format_tracker']
            print('--El formato elegido es: ' + formato)
            res = request.form[f"{formato}_res"]
            print(formato)
        except Exception as e:
            print(f"Tio algo ha ido mal :(((( SUERTE<33 : {str(e)}")

        print('...  ...  ...  ...  ...  ...')
        ready_to_dl, state, filename = Descargar_video(res, url, formato)

        if state != 'Ok':
            print(state)

        print('')
        print('---------------penes-------------')
        print('')

        return stream_template('index.html', title=title, thumbnail_url=thumbnail_url, ready=ready_to_dl, filename=filename);


@app.route('/select', methods = ['POST'])
def Select():
    # 1º Cogemos la url del form
    global url
    global title
    global thumbnail_url

    url = request.form['Url']

    # Invocamos las funciones para acceder al titulo, la miniatura y las resoluciones del video
    title, thumbnail_url = Get_info(url)
    Resolutions, Vibrates = Get_resolutions(url)

    return stream_template('index.html', title=title, thumbnail_url=thumbnail_url,  Resolutions=Resolutions,
                            Vibrates=Vibrates, ready=ready_to_dl)


if __name__ == '__main__' :
    app.run(debug=True, port=8080)
