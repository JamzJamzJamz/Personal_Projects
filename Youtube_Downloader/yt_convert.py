import ffmpeg
import youtube_dl


#url = input('Url of youtube video: ')
#title = input('Title of Video: ')

def convert(url,title):
    ydl_opt = {
        'format': 'bestaudio/best',
        'outtmpl': '{}.%(ext)s'.format(title),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    ydl = youtube_dl.YoutubeDL(ydl_opt)

    ydl.download([url])

    return '{} has been downloaded'.format(title)

#print('Video has been downloaded')