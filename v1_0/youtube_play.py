import os
import sys
from pathlib import Path

from .youtube_manager import YoutubeManager


class YoutubePlay:
    BASE_ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))

    # BASE_ROOT = Path(__file__).parent.parent
    def __init__(self, url) -> None:
        self.url = url
        self.ytm = YoutubeManager()

    def play(self):
        self.ytm.set_video_url(self.url)
        self.ytm.download_audio(convert_to_mp3=True)
        self.ytm.play()

    def __del__(self):
        try:
            file = Path(self.BASE_ROOT, self.ytm.audio_file_name_mp3)
            if os.path.exists(file):
                os.remove(file)
        except Exception as e:
            print(f"Error: {e}")
            


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=qV70vh3goD4"
    ytp = YoutubePlay(url)
    ytp.play()
