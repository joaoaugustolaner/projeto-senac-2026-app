from playlist import Playlist

if __name__ == '__main__':

    playlist = Playlist('Rage')
    playlist.adicionar_musica('Know your enemy')
    assert len(playlist.musicas) == 1

    assert playlist.remover_musica('Rage Agains the Machine') \
         == 'Música não encontrada'
    
    playlist.remover_musica('Know your enemy')

    assert len(playlist.musicas) == 0