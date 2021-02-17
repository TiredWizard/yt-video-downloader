from pytube import Playlist
import singlevideodownload
import subprocess
import os
import re


def download(link, path):
    try:
        playlist = Playlist(link)
        for video in playlist.videos:
            video.streams.filter().first().download(output_path=path)
    except KeyError:
        singlevideodownload.download(link, path)


def download_audio_only(link, path):
    try:
        playlist = Playlist(link)
        for video in playlist.videos:
            title = video.title.replace("|", "")
            title = re.sub(r"\s+", "", title, flags=re.UNICODE)
            title = re.sub(r"\\", "", title, flags=re.UNICODE)
            title = re.sub(r":", "", title, flags=re.UNICODE)
            audio = video.streams.get_audio_only()
            audio.download(output_path=path, filename=title)
            new_filename = path.replace("/", "\\") + '\\' + title + '.aac'
            default_filename = path.replace("/", "\\") + '\\' + title + '.mp4'
            ffmpeg = ('ffmpeg -i "{}" "{}"'.format(default_filename, new_filename))
            subprocess.run(ffmpeg, shell=True)
    except KeyError:
        singlevideodownload.download_audio_only(link, path)
