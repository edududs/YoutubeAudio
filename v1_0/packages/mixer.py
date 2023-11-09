from pathlib import Path
import os
import sys
import pygame


class MixerPlay:
    BASE_ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))

    def __init__(self, file_name: str) -> None:
        self._file_name = file_name
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

    def load_path(self):
        try:
            _path = str(Path(self.BASE_ROOT, self._file_name))
            pygame.mixer.music.load(_path)
        except Exception as e:
            print(f"Não foi possível carregar o arquivo: {e}")

    def play(self):
        try:
            print(f"Dando play em {self._file_name}")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        except Exception as e:
            print(f"Não foi possível reproduzir o arquivo: {e}")
