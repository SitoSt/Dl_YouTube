from pytube import YouTube
import os
 #listado de todos los streams posibles 

Resoluciones = {
    '240p': False,
    '360p': False,
    '480p': False,
    '720p': False
}

def Cap_resolutions(url):
    streams = YouTube(url).streams

    for res in Resoluciones:
        if streams.filter(progressive=True, resolution=res):
            Resoluciones[res] = True

    print('Se han encontrado las siguientes Resoluciones:')

    for res in Resoluciones:
        if Resoluciones[res]:
            print(res)
    return Resoluciones
    
