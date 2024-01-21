from pytube import YouTube
import os

def descargar_video(url, output_path):
    try: 
        yt = YouTube(url)
        
        print(f"Descargando video: {yt.title}...")
        yt.streams.get_highest_resolution().download(output_path=output_path)
        print(f"{yt.title} descargado exitosamente!!")
    except Exception as e:
        print(f"no se pudo descargar el video: {str(e)}")

def main(url):
    project_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(project_directory, 'descargas') #Directorio de descargas dentro del directorio del proyecto

    print(f"El directorio : {project_directory}")

    video = YouTube(url).title

    descargar_video(url, output_path)
    return video