from pytube import YouTube
from moviepy.editor import *
import os

def convert_yt_to_wav(song_list):
    for ytsong in song_list:
        
        YouTube(ytsong).streams.first().download()
        yt = YouTube(ytsong)
        song_title = yt.title
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

        song_audio = VideoFileClip(video)
        song_audio.audio.write_audiofile("C:/Users/rcroo/Music/from-youtube/" + str(song_title) + ".wav")

        print(str(song_title) + " uploaded!")

user_input = ""
songs = []

while (user_input != "done"):
    user_input = input("paste url: ")
    if user_input != "done":
        songs.append(user_input)
    else:
        pass

convert_yt_to_wav(songs)