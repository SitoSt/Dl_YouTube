from pytube import YouTube

def Descargar_video(res, url, formato, output_path):
    try:
        yt = YouTube(url)
        print(f"Descargando video: {yt.title}...")
        
        if formato == 'progresive':
            video = yt.streams.filter(progressive=True, resolution=res)
            print(video)
            video.first().download()
        elif formato == 'video':
            video = yt.streams.filter(only_video=True, resolution=res)
            video.first().download()
        elif formato == 'audio':
            video = yt.streams.filter(only_audio=True, abr=res)
            video.first().download()

        print(f"{yt.title} descargado exitosamente!!")
    except Exception as e:
        print(f"no se pudo descargar el video: {str(e)}")
