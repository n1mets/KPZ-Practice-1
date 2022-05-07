import pytube
import os
from pytube import YouTube
a = input("Введіть посилання")
try:
    yt_obj = YouTube('a')

    print(f'Video Title is {yt_obj.title}')
    print(f'Video Length is {yt_obj.length} seconds')
    print(f'Video Description is {yt_obj.description}')
    print(f'Video Rating is {yt_obj.rating}')
    print(f'Video Views Count is {yt_obj.views}')
    print(f'Video Author is {yt_obj.author}')

except Exception as e:
    print(e)
b = input("Введіть розширення відео")
url='a'
yt = pytube.YouTube(url)
stream=yt.streams
b = input("Введіть розширення відео")
video_480 = stream.filter(res="b").desc().first()
audio_best = stream.filter(adaptive=False, only_audio=True, abr="160kbps").desc().first()
adress=r'напишіть путь завантаження'
video_480.download(adress)
audio_best.download(adress)
thisvideo = str(adress)+'\\'+ str(yt.title)+".mp4"
thisFile = str(adress)+'\\'+ str(yt.title)+".webm"
 
ext = '.'+ os.path.realpath(thisFile).split('.')[-1:][0]
mp3file = thisFile.replace(ext,'.mp3')
os.rename(thisFile ,mp3file)
 
print(yt.title)