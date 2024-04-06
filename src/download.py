from pytube import YouTube

def Descargar_video(res, url, formato):
    try:
        yt = YouTube(url)
        print(f"Descargando video: {yt.title}...")
        filename = ''

        if formato == 'progressive':
            video = yt.streams.filter(progressive=True, resolution=res).first()
            filename = video.default_filename.replace(' ', '-')
            video.download(output_path='static/downloads', filename=filename)
            print('filename......... ::::' + filename)

        elif formato == 'video':
            video = yt.streams.filter(only_video=True, resolution=res).first()
            # filename = video.default_filename.replace(' ', '-')
            video.download(output_path='static/downloads', filename=filename).on_complete()

        elif formato == 'audio':
            video = yt.streams.filter(only_audio=True, abr=res).first()
            # filename = video.default_filename.replace(' ', '-')
            video.download(output_path='static/downloads', filename=filename).on_complete()

        

        print(f"{yt.title} descargado exitosamente!!")
        return True, 'Ok', filename


    except Exception as e:
        print(f"no se pudo descargar el video: {str(e)}")
        return False, e, ''
