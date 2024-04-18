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
Vibrates = {
    '48kbps': False, #mp4a.40.5
    '50kbps': False, #opus
    '70kbps': False, #opus
    '128kbps': False, #mp4a.40.2
    '160kbps': False #opus
}

def Get_info(url):
    try:
        yt = YouTube(url)
        streams = yt.streams
        title = yt.title
        thumbnail_url = yt.thumbnail_url

        for res in Resoluciones:
            if streams.filter(only_video=True, resolution=res):
                Resoluciones[res] = True

        for n in Vibrates:
            if streams.filter(only_audio=True, abr=n):
                Vibrates[n] = True
        
        video_info = {
            'title': title,
            'thumbnail': thumbnail_url,
            'resolutions': Resoluciones,
            'vibrates': Vibrates
        }

        return video_info
    
    except Exception as e:
        print(f'No se ha podido acceder a los datos del video!! {e}')
        return {'err_msg': 'no se ha podido acceder al video'}

