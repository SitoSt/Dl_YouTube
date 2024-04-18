from pytube import YouTube

def Descargar_video(formato, res, url, path):
    try:
        yt = YouTube(url)
        print(f"Descargando video: {yt.title}")
        filename = ''

        if formato == 'progressive':
            video = yt.streams.filter(progressive=True, resolution=res).first()
            filename = video.default_filename.replace(' ', '-')
            video.download(output_path=path, filename=filename)

        elif formato == 'video':
            video = yt.streams.filter(only_video=True, resolution=res).first()
            filename = video.default_filename.replace(' ', '-')
            video.download(output_path=path, filename=filename)

        elif formato == 'audio':
            video = yt.streams.filter(only_audio=True, abr=res).first()
            filename = video.default_filename.replace(' ', '-')
            video.download(output_path=path, filename=filename)

        print(f"Video descargado con éxito", { 'filename':filename })
        return {'filename':filename, 'result_state':'Ok'}

    except Exception as e:
        print(f"no se pudo descargar el video: {e}")
        return {'filename': None , 'result_state': e }
