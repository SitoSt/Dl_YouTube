from flask import Flask, stream_template, request, send_from_directory, make_response
import os
import tempfile
from src.video_information import Get_info
from src.download import Descargar_video

app = Flask(__name__)
url = ''

tmpdir = tempfile.TemporaryDirectory()
path = os.path.abspath(tmpdir.name)


@app.route('/', methods = ['GET'])
def index():
    return stream_template('index.html')

@app.route('/get-video-info', methods = ['POST'])
def Get_video_info():
    global url

    print(f'Información de video solicitada')
    url = request.form.get('url')
    print(url)

    if url:
        print('esta es la url: %s' % url)
        info = Get_info(url)
        
        return info
    else:
        print(f'Petición no valida: no se puede acceder a la url del video')
        response = make_response('', 400)
        return response

@app.route('/download', methods = ['POST'])
def Download():
    form = request.form
    descarga = Descargar_video(form['format'], form['res'], url, path)

    if descarga['result_state'] != 'Ok':
        print('no se ha podido descargar el video')
        return {'msg_err': 'no se ha podido descargar el video, revisa la respuesta del servidor para saver más'}

    return descarga



@app.route('/downloads/<filename>', endpoint='handle_dl_req')
def handle_dl_req(filename):
    if  os.path.exists(f'{path}/' + filename):
        return send_from_directory(path, filename)
    else:
        print('no se ha encontrado la ruta de descargas')
        return {'err': 'no se ha encontrado la ruta de descargas'}

@app.route('/static/favicon/<filename>', endpoint='favicon')
def favicon(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/favicon'), filename)

@app.route('/sitemap.xml', endpoint='sitemap')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml')

@app.route('/robots.txt', endpoint='robots')
def robots():
    return send_from_directory(app.root_path, 'robots.txt')

@app.route('/ads.txt', endpoint='ads')
def ads():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ads.txt')
