from flask import Flask, stream_template, request, send_from_directory
import os
import tempfile
import logging
from src.video_information import Get_info
from src.download import Descargar_video

app = Flask(__name__)
url = ''

tmpdir = tempfile.TemporaryDirectory()
path = os.path.abspath(tmpdir.name)

@app.route('/', methods = ['GET'])
def index():
    return stream_template('index.html')

@app.route('/select', methods = ['POST'])
def Select():
    global url
    url = request.form['Url']
    info = Get_info(url)
    return info

@app.route('/download', methods = ['POST'])
def Download():
    form = request.form
    descarga = Descargar_video(form['format'], form['res'], url, path)

    if descarga['result_state'] != 'Ok':
        print('no se ha podido descargar el video')
        return {'msg_err': 'no se ha podido descargar el video, revisa la respuesta del servidor para saver más'}

    return descarga

@app.route('/static/downloads/<filename>', methods = ['GET'])
def handleDlRequest(filename):
    return send_from_directory(path, filename)

@app.route('/static/favicon/<filename>')
def favicon(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/favicon'), filename)


if __name__ == '__main__' :
    app.run(debug=True, port=8080)
