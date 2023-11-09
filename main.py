from player_music import PlayerMusic

search_term = input("Digite o termo para tocar o áudio:")
player = PlayerMusic()
player.search(search_term).play()
