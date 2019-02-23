import ffmpeg
import youtube_dl

url = input('Url of youtube video: ')
#title = input('Title of Video: ')


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