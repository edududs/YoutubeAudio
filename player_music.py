from media_manager import YoutubePlay, YoutubeSearch


class PlayerMusic:
    def __init__(self) -> None:
        self.youtube_search = YoutubeSearch()
        self.youtube_player: YoutubePlay | None = None

    def search(self, query: str):
        self.youtube_search.input_text = query
        self.youtube_search.search()
        return self

    def play(self):
        self.youtube_player = YoutubePlay(self.youtube_search.url)
        self.youtube_player.play()
        return self


if __name__ == "__main__":
    inpuut = str(input("Search: "))
    yt_search = PlayerMusic()
    yt_search.search(inpuut)
    yt_search.play()
