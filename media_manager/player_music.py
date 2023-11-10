from .utils import is_valid_url
from .youtube_manager import YoutubeDownloader, YoutubePlay, YoutubeSearch


class PlayerMusic:
    def __init__(self) -> None:
        self.youtube_search = YoutubeSearch()
        self.youtube_player = YoutubePlay()

    def search(self, query: str):
        video = self.youtube_search.search_one(query)
        if video is not None:
            return video

    def play(self, search):
        if is_valid_url(search):
            self.youtube_player.play(search)
        else:
            url_video = self.search(search)
            if url_video is not None:
                self.youtube_player.play(url_video["url"])


if __name__ == "__main__":

    inpuut = str(input("Search: "))
    yt_search = PlayerMusic()
    url = yt_search.search(inpuut)

    download = YoutubeDownloader()
    download.download_audio(url)
    print(url)
