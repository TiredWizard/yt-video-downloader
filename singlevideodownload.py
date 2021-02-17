import os
import subprocess
import re
from pytube import YouTube


def download(link, path):
    YouTube(link).streams.first().download(output_path=path)


def download_audio_only(link, path):
    yt = YouTube(link)
    title = yt.title.replace("|", "")
    title = re.sub(r"\s+", "", title, flags=re.UNICODE)
    title = re.sub(r"\\", "", title, flags=re.UNICODE)
    title = re.sub(r":", "", title, flags=re.UNICODE)
    print(title)
    audio = yt.streams.get_audio_only()
    audio.download(output_path=path, filename=title)
    new_filename = path.replace("/", "\\") + '\\' + title + '.aac'
    default_filename = path.replace("/", "\\") + '\\' + title + '.mp4'
    ffmpeg = ('ffmpeg -i "{}" "{}"'.format(default_filename, new_filename))
    subprocess.run(ffmpeg, shell=True)
