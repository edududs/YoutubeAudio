from media_manager import *

yt_downloader = YoutubeDownloader()
yt_downloader.download_audio("https://www.youtube.com/watch?v=T3Y6RRSDm4o", convert_to_mp3=False)
