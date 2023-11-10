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

    pesquisa = "preferência kayblack"

    youtube_player.play(pesquisa)

