from v1_0 import YoutubePlay, YoutubeSearch

# url = "https://www.youtube.com/watch?v=6NiQB_qDZSQ"

# ytplay = YoutubePlay(url)
# ytplay.play()
class PlayerMusic:
    def __init__(self) -> None:
        self.yt_search = YoutubeSearch()
        self.yt_player: YoutubePlay | None = None
        
    def search(self, query: str):
        self.yt_search.input_text = query
        self.yt_search.search()
        return self

    def play(self):
        self.yt_player = YoutubePlay(self.yt_search.url)
        self.yt_player.play()
        return self
        
if __name__ == "__main__":
    inpuut = str(input("Search: "))
    yt_search = PlayerMusic()
    yt_search.search(inpuut)
    yt_search.play()
    