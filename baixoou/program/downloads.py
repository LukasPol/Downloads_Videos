from pytube import YouTube

def downloads(url, nome, format):
    try:
        yt = YouTube(url)

        if format == 'mp4':
            video = yt.streams.filter(res="720p").filter(subtype='mp4').first()
            if nome != None:
                video.download(filename=nome)
            else:
                video.download()
        else:
            video = yt.streams.filter(res="720p").filter(subtype='mp4').first()
            if nome != None:
                video.download(filename=nome)
            else:
                video.download()
    except:
        pass
        # print('ERRRO!!!')