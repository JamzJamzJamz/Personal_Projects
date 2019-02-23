import youtube_dl
import ffmpeg

url = input('Url of youtube video: ')
#title = input('Title of Video: ')

#ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

ydl_opt = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192', 
    }]
}

ydl = youtube_dl.YoutubeDL(ydl_opt)

ydl.download([url])

print('Video has been downloaded')