from pathlib import Path
import os
import sys
import pygame


class MixerPlay:
    BASE_ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))

    def __init__(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

    def load_path(self, path: str):
        try:
            pygame.mixer.music.load(path)
        except Exception as e:
            print(f"Não foi possível carregar o arquivo: {e}")

    def play(self, path: str):
        try:
            print("Fazendo o load do arquivo")
            self.load_path(path)
            print(f"Dando play em {Path(path).name}")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        except Exception as e:
            print("Não foi possível reproduzir o arquivo.")
            raise e
