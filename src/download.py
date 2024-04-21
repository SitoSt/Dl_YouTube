from pytube import YouTube
from pytube.cli import on_progress

def Descargar_video(formato, res, url, path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Descargando video: {yt.title}")

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


