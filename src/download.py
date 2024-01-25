from pytube import YouTube

def Descargar_video(res, url, output_path):
    try: 
        yt = YouTube(url)

        print(f"Descargando video: {yt.title}...")
        yt.streams.get_by_resolution(res).download()
        print(f"{yt.title} descargado exitosamente!!")
    except Exception as e:
        print(f"no se pudo descargar el video: {str(e)}")