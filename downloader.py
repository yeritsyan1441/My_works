from pytubefix import YouTube
from pytubefix.cli import on_progress


def downloader(url, format="mp3"):

    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Downloading... /{yt.title}/MP3 ")
    if format == "mp3":
        ys = yt.streams.get_audio_only()
        ys.download()
        print("*"*5)
        print(yt.title + " -> " + "Downloaded")
    else:
        ys = yt.streams.get_highest_resolution()
        ys.download()
