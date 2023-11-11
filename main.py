# from media_manager.player_music import PlayerMusic
import os
from pathlib import Path

from media_manager import *

os.chdir(Path(__file__).parent)


if __name__ == "__main__":
    youtube_player = PlayerMusic()
    youtube_downloader = YoutubeDownloader()
    youtube_search = YoutubeSearch()
    mixer = MixerPlay()
    play = YoutubePlay()

    pesquisa = "viva la vida"

    youtube_player.play(pesquisa)

