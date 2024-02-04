from pytube import YouTube
#listado de todos los streams posibles

Resoluciones = {
    '144p': False,
    '240p': False,
    '360p': False,
    '480p': False,
    '720p': False,
    '1080p': False,
    '1440p': False,
    '2160p': False
}
Bibrates = {
    '48kbps': False, #mp4a.40.5
    '50kbps': False, #opus
    '70kbps': False, #opus
    '128kbps': False, #mp4a.40.2
    '160kbps': False #opus
}


def Cap_resolutions(url, formato):
    streams = YouTube(url).streams

    if formato == 'progresive':
        for res in Resoluciones:
            if streams.filter(progressive=True, resolution=res):
                Resoluciones[res] = True
    elif formato == 'video':
        for res in Resoluciones:
            if streams.filter(only_video=True, resolution=res):
                Resoluciones[res] = True
    elif formato == 'audio':
        for n in Bibrates:
            if streams.filter(only_audio=True, abr=n):
                Bibrates[n] = True


    if formato == 'progresive' or formato == 'video':
        print('Se han encontrado las siguientes Resoluciones:')
        for res in Resoluciones:
            if Resoluciones[res]:
                print(res)
        return Resoluciones
    elif formato == 'audio':
        print('Se han encontrado los siguientes bibrates:')
        for abr in Bibrates:
            if Bibrates[abr]:
                print(abr)
        return Bibrates

