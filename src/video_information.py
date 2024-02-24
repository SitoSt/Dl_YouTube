from pytube import YouTube

# ---- !!!                                          !!! ----
# ---- !!! Hay que intentar recoger de forma global !!! ----
# ---- !!! las variables necesarias como la url o   !!! ----
# ---- !!! el formato                               !!! ----
# ---- !!!                                          !!! ----

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

def Get_resolutions(url):
    streams = YouTube(url).streams

    for res in Resoluciones:
        if streams.filter(only_video=True, resolution=res):
            Resoluciones[res] = True

    for n in Bibrates:
        if streams.filter(only_audio=True, abr=n):
            Bibrates[n] = True
    
    return Resoluciones, Bibrates

def Get_info (url):

    yt = YouTube(url)
    title = yt.title
    thumbnail_url = yt.thumbnail_url

    return title, thumbnail_url
