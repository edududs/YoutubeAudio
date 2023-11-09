import os
from pathlib import Path

from .audio_editor import AudioEditor
from .mixer import MixerPlay
from pytube import YouTube


class YoutubeManager:
    def __init__(self):
        self.url = ""
        self.yt = None
        self.audio_file = ""
        self.audio_file_name = ""
        self.audio_file_name_mp3 = ""

    def set_video_url(self, url):
        self.url = url
        print(f"URL: {self.url}")

    def download_audio(self, convert_to_mp3=False):
        if self.url == "":
            print("Defina primeiro o link do vídeo")
            return
        self.yt = YouTube(self.url)
        streams = self.yt.streams.filter(only_audio=True).first()
        if streams is not None:
            output_path = str(Path(__file__).parent.parent)
            self.audio_file = streams.download(output_path)
            self.audio_file_name = str(Path(self.audio_file).name)
            print(f"O áudio do vídeo foi baixado em: {self.audio_file}")
            if convert_to_mp3:
                print("Convertendo o video com apenas o áudio em .mp3")
                self._convert_video_to_mp3()

    def play(self):
        if self.audio_file_name != "":
            mixer = MixerPlay(self.audio_file_name_mp3)
            mixer.load_path()
            mixer.play()

    def _convert_video_to_mp3(self):
        if self.audio_file_name.endswith(".mp4"):
            audio_file = AudioEditor(self.audio_file_name)
            self.audio_file_name_mp3 = self.audio_file_name.replace(".mp4", ".mp3")
            audio_file.convert_audio(self.audio_file_name_mp3)
            os.remove(self.audio_file)
            return
        if self.audio_file_name != "":
            audio_file = AudioEditor(self.audio_file_name)
            audio_file.convert_audio()
        else:
            print("Defina o nome do arquivo de audio")

if __name__ == "__main__":
    yt_player = YoutubeManager()
    lapada_dela = "https://www.youtube.com/watch?v=qV70vh3goD4"
    yt_player.set_video_url(lapada_dela)
    yt_player.download_audio(convert_to_mp3=True)
    yt_player.play()
