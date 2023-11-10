import os
import sys
from pathlib import Path

from pytube import Search, YouTube

from .audio_editor import AudioEditor
from .mixer import MixerPlay
from .utils import is_valid_url


class YoutubeDownloader:
    def __init__(self):
        self.yt = None
        self.audio_file = ""
        self.audio_file_name = ""
        self.audio_file_name_mp3 = ""

    def download_audio(self, url: str, convert_to_mp3=True):
        if url == "":
            print("Defina primeiro o link do vídeo")
            return
        try:
            self.yt = YouTube(url)
            streams = self.yt.streams.filter(only_audio=True).first()
            if streams is not None:
                output_path = str(Path(__file__).parent.parent)
                self.audio_file = streams.download(output_path)
                self.audio_file_name = str(Path(self.audio_file).name)
                print(f"O áudio do vídeo foi baixado em: {self.audio_file}")
                if convert_to_mp3:
                    print("Convertendo o video com apenas o áudio em .mp3")
                    self.audio_file = self._convert_video_to_mp3()
                    return self.audio_file
                return self.audio_file
        except Exception as e:
            raise e

    def _convert_video_to_mp3(self):
        if self.audio_file_name.endswith(".mp4"):
            audio_file = AudioEditor(self.audio_file_name)
            self.audio_file_name_mp3 = self.audio_file_name.replace(".mp4", ".mp3")
            output_converted_audio = audio_file.convert_audio(self.audio_file_name_mp3)
            os.remove(self.audio_file)
            return output_converted_audio
        if self.audio_file_name != "":
            audio_file = AudioEditor(self.audio_file_name)
            output = audio_file.convert_audio()
            return output
        else:
            print("Defina o nome do arquivo de audio")


class YoutubePlay:
    BASE_ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))

    def __init__(self) -> None:
        self.youtube_downloader = YoutubeDownloader()

    def play(self, url):
        if is_valid_url(url):
            audio = self.youtube_downloader.download_audio(url)
            print(audio)
            if audio is not None and audio.endswith(".mp3"):
                mixer = MixerPlay()
                mixer.play(audio)
            print("Arquivo não é .mp3")
        print("Não é uma url valida")

    def __del__(self):
        try:
            file = Path(self.youtube_downloader.audio_file)
            if os.path.exists(file):
                os.remove(file)
        except Exception as e:
            print(f"Error: {e}")


class YoutubeSearch:
    def __init__(self):
        self._url = ""
        self.video_id = ""
        self.video_title = ""

    def search_one(self, input_text: str):
        search_results = []

        try:
            yt_search = Search(input_text)
            search_results = yt_search.results
            if search_results != [] and search_results is not None:
                self.video_title = search_results[0].title
                self.video_id = search_results[0].video_id

                print(f"Título do vídeo:{self.video_title}")
                print(f"Id do vídeo: {self.video_id}")
                self._set_url()
                video_info = {
                    "title": self.video_title,
                    "id": self.video_id,
                    "url": self.url,
                }

                return video_info
            print("Nenhum resultado encontrado")

        except Exception as e:
            print(f"Erro na pesquisa: {str(e)}")
            raise e

    def search_multiple(self, input_text: str):
        search_results = []
        videos = {}
        try:
            yt_search = Search(input_text)
            search_results = yt_search.results
            if search_results != [] and search_results is not None:
                for i, result in enumerate(search_results):
                    url = f"https://www.youtube.com/watch?v={result.video_id}"
                    video_info = {
                        f"Option{i}": {
                            "title": result.title,
                            "id": result.video_id,
                            "url": url,
                        }
                    }
                    videos.update(video_info)
                return videos

        except Exception as e:
            print(f"Erro na pesquisa: {str(e)}")
            raise e

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def _set_url(self):
        if self.video_id != "":
            self.url = f"https://www.youtube.com/watch?v={self.video_id}"


if __name__ == "__main__":
    YoutubePlay().play("https://www.youtube.com/watch?v=9bZkp7q19f0")
