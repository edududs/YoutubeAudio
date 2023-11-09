from pytube import Search


class YoutubeSearch:
    def __init__(self, input_text=""):
        self._input_text = input_text
        self._url = ""
        self.video_id = ""
        self.video_title = ""
        self.query_set = []

    def search(self, multiple=False):
        search_results = []

        try:
            yt_search = Search(self.input_text)
            print(yt_search.completion_suggestions)
            search_results = yt_search.results
            if multiple and search_results is not None:
                for result in search_results:
                    id_title = result.title,result.video_id
                    self.query_set.append(id_title) 
                return self.query_set
            if search_results != [] and search_results is not None:
                self.video_title = search_results[0].title
                self.video_id = search_results[0].video_id
                
                print(f"Título do vídeo:{self.video_title}")
                print(f"Id do vídeo: {self.video_id}")
                self._set_url()

                return  self.video_id, self.video_title

        except Exception as e:
            print(f"Erro na pesquisa: {str(e)}")

    @property
    def input_text(self):
        return self._input_text

    @input_text.setter
    def input_text(self, value):
        self._input_text = value
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
    teste_musica = YoutubeSearch("Skrillex")
    lista = teste_musica.search(multiple=True)
    print(f"Video ID de {teste_musica.input_text}: {teste_musica.video_id}")
    print(f"Video Title de {teste_musica.input_text}: {teste_musica.video_title}")
    print(lista)